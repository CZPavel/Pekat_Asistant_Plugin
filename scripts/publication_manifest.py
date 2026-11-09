"""Record explicit review approval; CI checks hashes without approving new files."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "provenance/publication-manifest.json"
EXCLUDED = {".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "dist", "work"}


def reviewed_files(root: Path = ROOT) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED for part in relative.parts):
            continue
        attributes = os.lstat(path)
        if stat.S_ISLNK(attributes.st_mode) or getattr(attributes, "st_file_attributes", 0) & 1024:
            raise ValueError("Linked publication path: " + relative.as_posix())
        if path.is_file() and relative.as_posix() != MANIFEST:
            result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def check(root: Path = ROOT) -> list[str]:
    try:
        expected = json.loads((root / MANIFEST).read_text(encoding="utf-8"))["files"]
        current = reviewed_files(root)
        return ["publication approval drift: " + name for name in sorted(set(expected) | set(current))
                if current.get(name) != expected.get(name)]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return ["publication manifest: " + str(exc)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approve", action="store_true", help="Record explicitly reviewed files, never run automatically in CI")
    args = parser.parse_args()
    if args.approve:
        path = ROOT / MANIFEST
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"schema": "pekat-publication/1", "files": reviewed_files()}, indent=2) + "\n", encoding="utf-8")
        print("Recorded reviewed public files")
    else:
        failures = check()
        if failures:
            raise SystemExit("\n".join(failures))
        print("PASS: explicit publication approvals")
