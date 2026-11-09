import json
import sys
import zipfile
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_public import sensitive_issues, validate, link_issues
from publication_manifest import check
from build_release import build
from smoke_tools import run_smoke


def test_public_package():
    assert validate(ROOT) == []


def test_sensitive_data_rejected():
    assert sensitive_issues("gh" + "p_" + "x" * 36)
    assert sensitive_issues("https://" + "192.168." + "7.3")
    assert sensitive_issues("C:" + chr(92) + "Users" + chr(92) + "private-person")
    assert not sensitive_issues("TensorRT 10.13.0.35")
    assert sensitive_issues("api_" + "key = " + "sensitive-value")


def test_unreviewed_new_file_rejected(tmp_path):
    (tmp_path / "provenance").mkdir()
    (tmp_path / "provenance/publication-manifest.json").write_text(json.dumps({"files": {}}))
    (tmp_path / "unexpected.md").write_text("new content")
    assert check(tmp_path) == ["publication approval drift: unexpected.md"]


def test_link_outside_package_rejected():
    assert link_issues(ROOT, ROOT / "README.md", "[outside](../unreviewed.md)")


def test_standalone_zip_layout_and_determinism(tmp_path):
    archive = build(tmp_path)
    first = archive.read_bytes()
    assert build(tmp_path).read_bytes() == first
    with zipfile.ZipFile(archive) as package:
        names = set(package.namelist())
        assert {"plugin.json", "LICENSE", "THIRD_PARTY_NOTICES.md", "requirements.txt"} <= names
        assert "skills/pekat-vision/scripts/generate_code_module.py" in names
        assert "skills/pekat-core-local/SKILL.md" in names
        assert not any(name.startswith(".git/") for name in names)


def test_real_offline_smoke():
    assert run_smoke()["log_analyzer"] == "PASS"


def test_reused_benchmark_routes_and_expectations():
    plugin = ROOT / "plugins/pekat-assistant"
    fixtures = yaml.safe_load((plugin / "acceptance-fixtures.yaml").read_text())
    benchmark = yaml.safe_load((ROOT / "benchmarks/assistant_behavior_v0_2.yaml").read_text())
    identifiers = {case["id"] for case in benchmark["cases"]}
    assert len(fixtures["cases"]) == 9
    for case in fixtures["cases"]:
        assert case["prompt"] and case["expected"]
        assert case["benchmark"] in identifiers
        assert (plugin / "skills/pekat-assistant" / case["reference"]).is_file()
