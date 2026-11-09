from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = REPO_ROOT / "plugins" / "pekat-assistant" / "skills" / "pekat-vision"
sys.path.insert(0, str(SKILL_ROOT / "scripts"))
