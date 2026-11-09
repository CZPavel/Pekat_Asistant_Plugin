"""Exercise bundled tools with synthetic data, without Core, PEKAT or network."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins/pekat-assistant/skills/pekat-vision/scripts"


def run_smoke() -> dict:
    with tempfile.TemporaryDirectory(prefix="pekat-plugin-smoke-") as temp:
        work = Path(temp)
        log = work / "synthetic.txt"
        log.write_text("SERVER - 2026-01-01 12:00:00,000 - runtime.camera - ERROR - Synthetic acquisition timeout\n", encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPTS / "analyze_pekat_log.py"), str(log), "--json"],
                                capture_output=True, text=True, check=True, timeout=20)
        report = json.loads(result.stdout)
        if "timeout" not in result.stdout.casefold():
            raise AssertionError("Synthetic timeout not identified")
        compatibility = subprocess.run([sys.executable, str(SCRIPTS / "check_pekat_library_compat.py"),
                                        "--pekat-version", "4.0.3", "--package", "numpy", "--json"],
                                       capture_output=True, text=True, check=True, timeout=20)
        json.loads(compatibility.stdout)
        specification = work / "module-spec.json"
        specification.write_text(json.dumps({"target_version": "4.0.3", "label": "Synthetic check",
                                             "source_code": "def main(context, form):\n    context['synthetic_check'] = form.get('enabled', False)\n",
                                             "form": [{"type": "checkbox", "formKey": "enabled", "label": "Enabled", "defaultValue": True}],
                                             "form_values": {"enabled": True}}), encoding="utf-8")
        artifact = work / "synthetic.ptool"
        subprocess.run([sys.executable, str(SCRIPTS / "generate_code_module.py"), str(specification),
                        "--output", str(artifact)], capture_output=True, text=True, check=True, timeout=20)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        if payload["version"] != "4.0.3":
            raise AssertionError("Wrong generated target version")
        return {"log_analyzer": "PASS", "compatibility_lookup": "PASS", "ptool_generation": "PASS", "network": "NOT_USED",
                "core": "NOT_REQUIRED", "report_fields": sorted(report)}


if __name__ == "__main__":
    print(json.dumps(run_smoke(), indent=2))
