"""Audit an explicit public-source allowlist without copying or updating files."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(source: str, checkout: Path) -> int:
    filename = "knowledge.json" if source == "assistant" else "offline-tools.json"
    lock = json.loads((ROOT / "provenance" / filename).read_text(encoding="utf-8"))
    expected = lock.get("repository", lock.get("source_repository"))
    commit = lock.get("commit", lock.get("source_commit"))
    origin = subprocess.check_output(["git", "-C", str(checkout), "remote", "get-url", "origin"], text=True).strip()
    if origin.removesuffix(".git") != expected:
        raise ValueError("Checkout is not the explicitly approved public upstream")
    for record in lock["files"]:
        path = record.get("source", record.get("source_path"))
        data = subprocess.check_output(["git", "-C", str(checkout), "show", f"{commit}:{path}"])
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError("Upstream source hash mismatch: " + path)
    return len(lock["files"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", choices=["assistant", "offline"])
    parser.add_argument("--checkout", type=Path, required=True)
    args = parser.parse_args()
    print("PASS: public upstream Git blobs", check(args.source, args.checkout))
