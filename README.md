# PEKAT Assistant

The v0.3.0 functional baseline was publicly validated and locally installed. A fresh local Codex
chat used the installed skills and an actual bundled tool; see the scoped
[acceptance evidence](docs/VALIDATION.md). GPT account migration remains partial.

Version 0.3.1 includes the original icon from the companion PEKAT Assistant desktop application. Update the installed plugin to refresh its branding.

A standalone public plugin for PEKAT VISION engineering: detailed version-aware
knowledge, inspection/FLOW design, bundled offline project/log/dataset/model
analysis, and Code/PTool/PModule generation. Optional local Core lookup is a thin
adapter to an existing installation; the plugin includes no private Core.

## Install in Codex

```powershell
codex plugin marketplace add CZPavel/Pekat_Asistant_Plugin --ref main
codex plugin add pekat-assistant@pekat-assistant-public
codex plugin list --marketplace pekat-assistant-public --json
```

Start a **new chat/session** after installation. The installed package, rather
than this checkout, supplies its skills. Python 3.11+ and the packages listed in
`requirements.txt` are needed for executable offline workflows. Knowledge-only
questions need no running PEKAT or private Core. A host still needs file/skill
access. Other plugin hosts require their own supported installation workflow.

For tool development or direct CLI use:

```powershell
git clone https://github.com/CZPavel/Pekat_Asistant_Plugin.git
cd Pekat_Asistant_Plugin
python -m pip install -r requirements-dev.txt
python scripts/validate_public.py
python -m pytest -q
python scripts/smoke_tools.py
python scripts/build_release.py --output dist
```

See [installation and updates](docs/INSTALLATION.md), [capability map](docs/CAPABILITIES.md),
[scenarios](docs/SCENARIOS.md), [versions](docs/VERSION_SUPPORT.md),
[hardware/integration](docs/INTEGRATIONS.md), and [host tools](docs/HOST_TOOLS.md).

## Included skills and tools

- `pekat-assistant`: technical knowledge, whole-inspection design and routing.
- `pekat-vision`: bundled public offline analyzers, compatibility checks, Form
  normalization and module generator. See its
  [tool catalog](plugins/pekat-assistant/skills/pekat-vision/references/bundled-tools-catalog.md).
- `pekat-core-local`: optional installed-Core discovery, capability lookup and
  offline planning. No generic forwarding or live writer.

Ask: “Explain this FLOW and trace image/result/Context separately”, “Analyze this
sanitized log”, or “Generate a parameterized 4.0.3 PTool from this specification”.
The host must actually expose Python/files/terminal for tool execution. Included
network demos require a separate explicit target and authorization.

The package preserves 3.18.x general guidance and separate 3.19.3, 4.0.1 and 4.0.3
evidence. Generated artifacts require exact-target validation before use in PEKAT.
No camera, sensor, PLC or running inspection was exercised for this release.

## Distribution and migration

This GitHub marketplace is a repository distribution route, separate from the
official Plugin Directory. No directory submission is performed. No promise of
availability on every plan, region or host is implied. See the
[Custom GPT migration plan](docs/GPT_MIGRATION.md), [roadmap](docs/ROADMAP.md),
[validation record](docs/VALIDATION.md), and [licenses](THIRD_PARTY_NOTICES.md).
