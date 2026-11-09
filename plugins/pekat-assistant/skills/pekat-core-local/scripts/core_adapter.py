"""Optional local CLI adapter. Independently authored; no Core package is bundled.

The selected executable is trusted installed software, not untrusted request data.
Only the command shapes below can be issued. Returned metadata is advisory.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PROFILE_VERSIONS = frozenset({"0.3.0"})
OPERATIONS = ("discover", "capabilities", "plan")
MAX_OUTPUT_BYTES = 2_000_000


class AdapterError(Exception):
    """A public error code, intentionally excluding child output and local paths."""


def _text(value: object, name: str, limit: int = 2000) -> str:
    if (not isinstance(value, str) or not value.strip() or len(value) > limit
            or value.startswith("-") or any(ord(c) < 32 for c in value)):
        raise AdapterError("invalid_" + name)
    return value


def _identifier(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_.-]{1,120}", value):
        raise AdapterError("incompatible_schema")
    return value


def _boolean(value: object) -> bool:
    if type(value) is not bool:
        raise AdapterError("incompatible_schema")
    return value


def _identifiers(value: object) -> list[str]:
    if not isinstance(value, list) or len(value) > 100:
        raise AdapterError("incompatible_schema")
    return [_identifier(item) for item in value]


def _installed_path_executable() -> str | None:
    # shutil.which on Windows/Python 3.11 implicitly prepends cwd, even with
    # an explicit PATH. Never use it here: project contents are not installers.
    current = Path.cwd().resolve()
    for entry in os.environ.get("PATH", "").split(os.pathsep):
        directory = Path(entry)
        if not entry or not directory.is_absolute():
            continue
        directory = directory.resolve()
        if directory == current:
            continue
        candidate = (directory / ("pekat.exe" if os.name == "nt" else "pekat")).resolve()
        if candidate.is_relative_to(current):
            continue
        if candidate.is_file() and (os.name == "nt" or os.access(candidate, os.X_OK)):
            return str(candidate)
    return None


def _executable(configured: str | None) -> list[str] | None:
    # A configured absolute path is operator configuration, never request data.
    if configured is not None and not Path(configured).is_absolute():
        raise AdapterError("absolute_executable_required")
    resolved = str(Path(configured).resolve()) if configured else _installed_path_executable()
    if not resolved or not Path(resolved).is_file():
        return None
    suffix = Path(resolved).suffix.lower()
    if suffix in {".bat", ".cmd", ".ps1"}:
        raise AdapterError("unsupported_launcher")
    if os.name == "nt" and suffix not in {".exe", ".py"}:
        raise AdapterError("unsupported_launcher")
    # Explicit Python CLI shims support local packaging and cross-platform tests.
    return [sys.executable, "-I", resolved] if suffix == ".py" else [resolved]


def _invoke(executable: list[str], args: list[str], timeout: float) -> object:
    # Disk-backed capture bounds Python memory; timeout bounds the child lifetime.
    # No caller project is used as cwd and no Core report is retained here.
    with (
        tempfile.TemporaryDirectory(prefix="pekat-public-adapter-") as directory,
        tempfile.TemporaryFile() as output,
        tempfile.TemporaryFile() as errors,
    ):
        try:
            result = subprocess.run(
                [*executable, "--report-dir", str(Path(directory) / "reports"), *args],
                shell=False, cwd=directory, stdin=subprocess.DEVNULL,
                stdout=output, stderr=errors, timeout=timeout, check=False,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )
        except subprocess.TimeoutExpired:
            raise AdapterError("core_timeout") from None
        except OSError:
            raise AdapterError("core_launch_failed") from None
        if result.returncode != 0:
            raise AdapterError("core_command_failed")
        if output.tell() > MAX_OUTPUT_BYTES or errors.tell() > MAX_OUTPUT_BYTES:
            raise AdapterError("core_output_too_large")
        output.seek(0)
        try:
            return json.loads(output.read(MAX_OUTPUT_BYTES).decode("utf-8-sig"))
        except (UnicodeError, ValueError, RecursionError):
            raise AdapterError("invalid_core_json") from None


def _identity(raw: object) -> dict:
    if not isinstance(raw, dict) or raw.get("package") != "pekat-assistant":
        raise AdapterError("incompatible_identity")
    version = _identifier(raw.get("package_version"))
    commit = raw.get("git_commit")
    if commit is not None and (not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40,64}", commit)):
        raise AdapterError("incompatible_identity")
    # Deliberately omit source_root, paths, raw catalogs and all unknown fields.
    return {"package": "pekat-assistant", "package_version": version, "git_commit": commit,
            "profile_supported": version in PROFILE_VERSIONS}


def run(operation: str, *, executable: str | None = None, query: str | None = None,
        request: str | None = None, version: str | None = None, timeout: float = 20) -> dict:
    """Execute one typed passive operation; no generic command/argv entry point."""
    if operation not in OPERATIONS:
        raise AdapterError("unsupported_operation")
    if type(timeout) not in (int, float) or not 0.1 <= timeout <= 60:
        raise AdapterError("invalid_timeout")
    if operation == "discover":
        if query is not None or request is not None or version is not None:
            raise AdapterError("unexpected_argument")
    else:
        version = _text(version, "version", 32)
        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
            raise AdapterError("invalid_version")
        if operation == "capabilities":
            query = _text(query, "query")
            if request is not None:
                raise AdapterError("unexpected_argument")
        else:
            request = _text(request, "request")
            if query is not None:
                raise AdapterError("unexpected_argument")
    command = _executable(executable)
    if command is None:
        return {"status": "unavailable", "operation": operation, "core_required": False}
    identity = _identity(_invoke(command, ["build-identity"], timeout))
    common = {"status": "ok", "operation": operation, "identity": identity,
              "execution_authorized": False}
    if operation == "discover":
        return {**common, "operations": list(OPERATIONS) if identity["profile_supported"] else ["discover"]}
    if not identity["profile_supported"]:
        raise AdapterError("unsupported_core_version")
    if operation == "capabilities":
        raw = _invoke(command, ["knowledge", "capability", query, "--version", version, "--json"], timeout)
        if not isinstance(raw, list) or len(raw) > 1000:
            raise AdapterError("incompatible_schema")
        records = []
        for item in raw:
            if not isinstance(item, dict):
                raise AdapterError("incompatible_schema")
            records.append({"id": _identifier(item.get("capability_id")),
                            "state": _identifier(item.get("state")),
                            "versions": _identifiers(item.get("version_scope")),
                            "compatibility": _identifier(item.get("version_compatibility")),
                            "core_execution_eligible": _boolean(item.get("execution_eligible"))})
        return {**common, "requested_version": version, "capabilities": records}
    raw = _invoke(command, ["host", "plan", request, "--version", version, "--json"], timeout)
    if not isinstance(raw, dict):
        raise AdapterError("incompatible_schema")
    return {**common, "requested_version": version, "plan": {
        "intent": _identifier(raw.get("intent")), "mode": _identifier(raw.get("mode")),
        "supported": _boolean(raw.get("supported")),
        "needs_model_interpretation": _boolean(raw.get("needs_model_interpretation")),
        "missing_inputs": _identifiers(raw.get("missing_inputs")),
    }}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--core-executable", help="Trusted installed executable or Python CLI shim path")
    parser.add_argument("--timeout", type=float, default=20)
    commands = parser.add_subparsers(dest="operation", required=True)
    commands.add_parser("discover", allow_abbrev=False)
    lookup = commands.add_parser("capabilities", allow_abbrev=False)
    lookup.add_argument("--query", required=True)
    lookup.add_argument("--version", required=True)
    plan = commands.add_parser("plan", allow_abbrev=False)
    plan.add_argument("--request", required=True)
    plan.add_argument("--version", required=True)
    args = parser.parse_args()
    try:
        result = run(args.operation, executable=args.core_executable, timeout=args.timeout,
                     query=getattr(args, "query", None), request=getattr(args, "request", None),
                     version=getattr(args, "version", None))
    except AdapterError as error:
        print(json.dumps({"status": "error", "code": str(error)}))
        return 1
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["status"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
