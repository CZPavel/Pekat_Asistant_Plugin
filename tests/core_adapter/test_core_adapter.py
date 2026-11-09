"""Synthetic CLI tests; never require private Core or retain its output."""
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = (Path(__file__).resolve().parents[2] / "plugins" / "pekat-assistant" /
          "skills" / "pekat-core-local" / "scripts" / "core_adapter.py")
spec = importlib.util.spec_from_file_location("public_core_adapter", SCRIPT)
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


@pytest.fixture
def fake(tmp_path):
    """An actual child Python CLI shim, fed only synthetic responses."""
    shim = tmp_path / "fake_core.py"
    settings = tmp_path / "settings.json"
    calls = tmp_path / "calls.jsonl"
    settings.write_text(json.dumps({
        "identity": {"package": "pekat-assistant", "package_version": "0.3.0", "git_commit": None,
                     "source_root": "PRIVATE_PATH", "api_key": "PRIVATE_SECRET"},
        "capabilities": [{"capability_id": "SYNTHETIC-CAPABILITY", "state": "SYNTHETIC_STATE",
                          "version_scope": ["4.0.3"], "version_compatibility": "SYNTHETIC_MATCH",
                          "execution_eligible": True, "secret": "PRIVATE_SECRET"}],
        "plan": {"intent": "SYNTHETIC_INTENT", "mode": "SYNTHETIC_MODE", "supported": True,
                 "needs_model_interpretation": False, "missing_inputs": ["project"],
                 "context": {"password": "PRIVATE_SECRET"}},
    }), encoding="utf-8")
    shim.write_text('''import json, sys, time
from pathlib import Path
root = Path(__file__).parent
cfg = json.loads((root / "settings.json").read_text(encoding="utf-8"))
args = sys.argv[1:]
with (root / "calls.jsonl").open("a", encoding="utf-8") as stream:
    stream.write(json.dumps(args) + "\\n")
assert args[0] == "--report-dir"
assert Path(args[1]).parent == Path.cwd()
args = args[2:]
key = "identity" if args == ["build-identity"] else "capabilities" if args[:2] == ["knowledge", "capability"] else "plan"
if key != "identity":
    time.sleep(cfg.get("sleep", 0))
    if cfg.get("fail"): sys.exit(1)
    if cfg.get("invalid"): print("not json PRIVATE_SECRET"); sys.exit(0)
    if cfg.get("large"): print("x" * 2000001); sys.exit(0)
print(json.dumps(cfg[key]))
''', encoding="utf-8")
    return shim, settings, calls


def change(fake, **updates):
    settings = fake[1]
    cfg = json.loads(settings.read_text(encoding="utf-8"))
    cfg.update(updates)
    settings.write_text(json.dumps(cfg), encoding="utf-8")


def invoke(fake, operation="capabilities", **kwargs):
    if operation == "capabilities":
        kwargs.setdefault("query", "Detector")
    if operation == "plan":
        kwargs.setdefault("request", "Explain FLOW")
    if operation != "discover":
        kwargs.setdefault("version", "4.0.3")
    return adapter.run(operation, executable=str(fake[0]), **kwargs)


def test_discovery_and_projection(fake):
    result = invoke(fake, "discover")
    assert result["operations"] == ["discover", "capabilities", "plan"]
    assert result["execution_authorized"] is False
    assert "PRIVATE" not in json.dumps(result)


def test_capability_argv_and_projection(fake):
    query = 'Detector ; $(touch injected) & " --apply'
    result = invoke(fake, query=query)
    args = json.loads(fake[2].read_text(encoding="utf-8").splitlines()[-1])
    assert args[2:] == ["knowledge", "capability", query, "--version", "4.0.3", "--json"]
    assert result["capabilities"][0]["core_execution_eligible"] is True
    assert result["execution_authorized"] is False
    assert "PRIVATE" not in json.dumps(result)


def test_plan_is_compact_and_has_no_project_argument(fake):
    result = invoke(fake, "plan")
    args = json.loads(fake[2].read_text(encoding="utf-8").splitlines()[-1])
    assert args[2:] == ["host", "plan", "Explain FLOW", "--version", "4.0.3", "--json"]
    assert result["plan"]["missing_inputs"] == ["project"]
    assert "PRIVATE" not in json.dumps(result)


@pytest.mark.parametrize("operation, kwargs", [
    ("apply", {}), ("capabilities", {"query": "--help", "version": "4.0.3"}),
    ("capabilities", {"query": "abc\napply", "version": "4.0.3"}),
    ("plan", {"request": "a", "version": "4.0.3 --apply"}),
    ("plan", {"request": "a", "version": "4.0.3", "query": "extra"}),
    ("discover", {"query": "extra"}), ("discover", {"timeout": 0}),
    ("discover", {"timeout": float("nan")}),
])
def test_invalid_requests_never_launch(fake, operation, kwargs):
    with pytest.raises(adapter.AdapterError):
        adapter.run(operation, executable=str(fake[0]), **kwargs)
    assert not fake[2].exists()


def test_core_is_optional(tmp_path, monkeypatch):
    monkeypatch.delenv("PATH", raising=False)
    assert adapter.run("discover")["status"] == "unavailable"
    assert adapter.run("discover", executable=str(tmp_path / "missing.exe"))["core_required"] is False


@pytest.mark.parametrize("include_legitimate", [False, True])
def test_discovery_never_trusts_current_or_relative_path(tmp_path, monkeypatch, include_legitimate):
    current = tmp_path / "project"
    current.mkdir()
    relative = current / "bin"
    relative.mkdir()
    installed = tmp_path / "installed"
    installed.mkdir()
    name = "pekat.exe" if os.name == "nt" else "pekat"
    for directory in (current, relative, installed):
        placeholder = directory / name
        placeholder.write_text("not executable test content")
        placeholder.chmod(0o755)
    monkeypatch.chdir(current)
    entries = ["", ".", "bin", str(current), str(relative)]
    if include_legitimate:
        entries.append(str(installed))
    monkeypatch.setenv("PATH", os.pathsep.join(entries))
    expected = [str((installed / name).resolve())] if include_legitimate else None
    # Do not execute placeholders; inspect the exact resolved launch target.
    assert adapter._executable(None) == expected


def test_explicit_relative_executable_refused(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "pekat.exe").write_text("not executable test content")
    with pytest.raises(adapter.AdapterError, match="absolute_executable_required"):
        adapter.run("discover", executable="pekat.exe")


def test_batch_launcher_refused(tmp_path):
    launcher = tmp_path / "pekat.cmd"
    launcher.write_text("exit 0")
    with pytest.raises(adapter.AdapterError, match="unsupported_launcher"):
        adapter.run("discover", executable=str(launcher))


def test_unknown_version_discovery_only(fake):
    change(fake, identity={"package": "pekat-assistant", "package_version": "9.0.0", "git_commit": None})
    assert invoke(fake, "discover")["operations"] == ["discover"]
    with pytest.raises(adapter.AdapterError, match="unsupported_core_version"):
        invoke(fake)


@pytest.mark.parametrize("field, value", [
    ("execution_eligible", "true"), ("version_scope", "4.0.3"),
    ("version_compatibility", None), ("state", {"unexpected": "object"}),
])
def test_capability_schema_types(fake, field, value):
    cfg = json.loads(fake[1].read_text(encoding="utf-8"))
    cfg["capabilities"][0][field] = value
    change(fake, capabilities=cfg["capabilities"])
    with pytest.raises(adapter.AdapterError, match="incompatible_schema"):
        invoke(fake)


def test_plan_rejects_untyped_support(fake):
    change(fake, plan={"intent": "READ", "mode": "READ_PLAN", "supported": 1})
    with pytest.raises(adapter.AdapterError, match="incompatible_schema"):
        invoke(fake, "plan")


def test_empty_capabilities_are_valid(fake):
    change(fake, capabilities=[])
    assert invoke(fake)["capabilities"] == []


@pytest.mark.parametrize("updates, error", [
    ({"identity": {"package": "other"}}, "incompatible_identity"),
    ({"capabilities": {}}, "incompatible_schema"),
    ({"capabilities": [{"capability_id": "SECRET/path"}]}, "incompatible_schema"),
    ({"invalid": True}, "invalid_core_json"),
    ({"large": True}, "core_output_too_large"),
    ({"fail": True}, "core_command_failed"),
])
def test_child_failures_are_safe(fake, updates, error):
    change(fake, **updates)
    with pytest.raises(adapter.AdapterError, match=error) as exc:
        invoke(fake)
    assert "PRIVATE" not in str(exc.value)


def test_timeout(fake):
    change(fake, sleep=2)
    with pytest.raises(adapter.AdapterError, match="core_timeout"):
        invoke(fake, timeout=0.5)


def test_subprocess_boundary(fake, monkeypatch):
    real_run = adapter.subprocess.run
    def checked(args, **kwargs):
        assert isinstance(args, list)
        assert kwargs["shell"] is False
        assert kwargs["stdin"] == subprocess.DEVNULL
        assert 0 < kwargs["timeout"] <= 60
        return real_run(args, **kwargs)
    monkeypatch.setattr(adapter.subprocess, "run", checked)
    invoke(fake, "discover")


def test_cli_rejects_passthrough():
    result = subprocess.run([sys.executable, str(SCRIPT), "discover", "--apply"],
                            capture_output=True, text=True, timeout=5, check=False)
    assert result.returncode == 2
    assert "unrecognized arguments" in result.stderr
