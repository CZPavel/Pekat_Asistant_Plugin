"""Public package gates adapted from the existing public PEKAT publication checks."""
from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote

import yaml

from publication_manifest import ROOT, reviewed_files, check

PLUGIN = ROOT / "plugins/pekat-assistant"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PUBLIC_REPOS = {"Pekat_Asistant_Plugin", "PEKAT-Assistant", "codex-skill-pekat-vision",
                "codex-skill-basler-cameras", "codex-skill-ifm-io-link", "keyence-ljx-s-skill"}
PRIVATE_IP = re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b")


def sensitive_issues(text: str) -> list[str]:
    # Preserve the upstream public skill's documented package-version exception.
    text = text.replace("10.13.0.35", "<TensorRT-version>")
    patterns = {
        "private endpoint": PRIVATE_IP,
        "personal local path": re.compile(r"(?i)[A-Z]:[\\/](?:Users|Documents and Settings)[\\/][^\s\"<>]+"),
        "private key": re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"),
        "token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b|\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
        "credential URL": re.compile(r"https?://[^/\s]+:[^/\s]+@"),
        "credential assignment": re.compile(r'''(?i)(?:password|passwd|api[_-]?key|(?:auth|access)[_-]?token|(?:client[_-]?)?secret)["']?[ \t]*[=:][ \t]*(?:"[^"\r\n]{8,}"|'[^'\r\n]{8,}'|[^\s"';,]{8,})'''),
        "private source repository": re.compile(r"PEKAT-Assistant-3" + r"\.0"),
    }
    return [name for name, pattern in patterns.items() if pattern.search(text)]


def link_issues(root: Path, path: Path, text: str) -> list[str]:
    issues = []
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = target.split(' "', 1)[0].strip("<>")
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:|#", target):
            continue
        resolved = (path.parent / unquote(target.split("#", 1)[0])).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            issues.append("broken/outside link: " + target)
    return issues


def validate(root: Path = ROOT, approvals: bool = True) -> list[str]:
    issues = check(root) if approvals else []
    plugin = root / "plugins/pekat-assistant"
    required = ["plugin.json", "LICENSE", "requirements.txt", "THIRD_PARTY_NOTICES.md"]
    issues.extend("missing plugin file: " + name for name in required if not (plugin / name).is_file())
    try:
        manifest = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
        if manifest.get("$schema") != SCHEMA or manifest.get("name") != "pekat-assistant":
            issues.append("invalid portable plugin identity")
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", manifest.get("version", "")):
            issues.append("invalid plugin version")
        meta = manifest["extensions"]["com.openai"]
        for field in ("logo", "composerIcon"):
            asset_ref = meta["interface"].get(field, "")
            if not isinstance(asset_ref, str) or not asset_ref.startswith("./assets/") or not (plugin / asset_ref).is_file():
                issues.append("missing or invalid branding asset: " + field)
        if meta["interface"]["displayName"] != "PEKAT Assistant" or meta["requires_local_executor"] is not True:
            issues.append("invalid host metadata")
        catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        entry, = catalog["plugins"]
        if entry["name"] != manifest["name"] or entry["source"] != {"source": "local", "path": "./plugins/pekat-assistant"}:
            issues.append("marketplace plugin path/identity mismatch")
        if catalog["name"] != "pekat-assistant-public":
            issues.append("invalid marketplace identity")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        issues.append("invalid package metadata: " + str(exc))

    try:
        paths = reviewed_files(root)
    except (OSError, ValueError) as exc:
        return issues + [str(exc)]
    for name in paths:
        path = root / name
        if name == "plugins/pekat-assistant/assets/app-icon.png":
            icon_bytes = path.read_bytes()
            if (
                len(icon_bytes) < 32 or len(icon_bytes) > 5 * 1024 * 1024
                or not icon_bytes.startswith(bytes.fromhex("89504e470d0a1a0a"))
                or icon_bytes[12:16] != b"IHDR"
            ):
                issues.append(name + ": invalid PNG branding asset")
            else:
                width = int.from_bytes(icon_bytes[16:20], "big")
                height = int.from_bytes(icon_bytes[20:24], "big")
                if width != height or not 48 <= width <= 4096:
                    issues.append(name + ": branding asset must be square and 48-4096 px")
            continue
        if path.suffix.lower() in {".db", ".sqlite", ".sqlite3", ".log", ".pem", ".key", ".exe", ".dll"} or path.name.startswith(".env"):
            issues.append(name + ": forbidden private/runtime file family")
        try:
            text = path.read_text(encoding="utf-8-sig")
            if "\0" in text:
                issues.append(name + ": binary content")
            # Exact existing synthetic redaction fixtures; all other signals and
            # every other file are scanned unchanged. Never exempt a whole test.
            scan_text = text
            if name == "tests/core_adapter/test_core_adapter.py":
                scan_text = scan_text.replace("PRIVATE_SECRET", "FIXTURE")
            elif name == "tests/offline/test_pekat_log_analyzer.py":
                scan_text = scan_text.replace("secret" + "=synthetic", "synthetic-redaction-fixture")
            issues.extend(name + ": " + item for item in sensitive_issues(scan_text))
            if path.suffix in {".json", ".ptool", ".pmodule"}:
                json.loads(text)
            elif path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(text)
            elif path.suffix == ".py":
                ast.parse(text)
            if path.suffix == ".md":
                boundary = plugin if path.is_relative_to(plugin) else root
                issues.extend(name + ": " + item for item in link_issues(boundary, path, text))
            if path.name == "SKILL.md":
                front = yaml.safe_load(text.split("---", 2)[1])
                if front.get("name") != path.parent.name or not front.get("description"):
                    issues.append(name + ": skill frontmatter mismatch")
        except (OSError, ValueError, SyntaxError, UnicodeError, IndexError, yaml.YAMLError) as exc:
            issues.append(name + ": " + str(exc))
    return sorted(set(issues))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before-approval", action="store_true", help="Review new files; does not approve them")
    parser.add_argument("--schema", type=Path, help="Also validate against a downloaded official JSON Schema")
    args = parser.parse_args()
    failures = validate(approvals=not args.before_approval)
    if args.schema:
        import jsonschema
        jsonschema.validate(json.loads((PLUGIN / "plugin.json").read_text()), json.loads(args.schema.read_text()))
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: public privacy, references, syntax, plugin and marketplace checks")
