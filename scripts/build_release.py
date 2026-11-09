"""Build a deterministic standalone plugin ZIP from explicitly reviewed files."""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

from publication_manifest import ROOT, reviewed_files
from validate_public import validate


def build(output: Path, root: Path = ROOT) -> Path:
    issues = validate(root)
    if issues:
        raise ValueError("\n".join(issues))
    plugin = root / "plugins/pekat-assistant"
    version = json.loads((plugin / "plugin.json").read_text())["version"]
    output.mkdir(parents=True, exist_ok=True)
    target = output / f"pekat-assistant-{version}.zip"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in reviewed_files(root):
            path = root / name
            if path.is_relative_to(plugin):
                item = zipfile.ZipInfo(path.relative_to(plugin).as_posix(), (1980, 1, 1, 0, 0, 0))
                item.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(item, path.read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (output / "SHA256SUMS.txt").write_text(f"{digest}  {target.name}\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    print(build(parser.parse_args().output))
