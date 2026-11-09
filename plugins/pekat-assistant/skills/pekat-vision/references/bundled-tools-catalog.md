# Bundled tools catalog

Run from any working directory with Python 3, using the full path to the selected script. `$S` below means the path to this skill's `scripts` directory. The files and references are bundled; no source checkout is needed. See each script's `--help` and the linked references for full input constraints and evidence boundaries. JSON output is a static analysis report, not execution by PEKAT Core. Generated files require manual, isolated PEKAT import and validation. The separate bundled `pekat-core-local` skill offers optional local Core discovery/lookup; these offline tools do not require it.

## Offline CLI

| Command | Input, output, scope |
|---|---|
| `python "$S/generate_code_module.py" SPEC --output PATH` | UTF-8 JSON ModuleSpec to `.pmodule` or `.ptool` (extension derived from target version); prints resulting path. Supports 3.19.3, 4.0.1 and the narrowly documented 4.0.3 subset; see `module-format.md` and schema. Writes the requested output. |
| `python "$S/analyze_flow_database.py" INPUT [--output PATH]` | Project/database directory or ZIP; JSON to stdout or file. Restricted offline parsing; see `flow-database-projects.md`. |
| `python "$S/analyze_source_state_403.py" PROJECT` | Stored source state for exactly 4.0.3; JSON to stdout; `source-state-pekat403.md`. |
| `python "$S/inspect_dataset_model.py" PROJECT [--output PATH]` | Read-only inventory for exactly 4.0.3; JSON to stdout or outside-project file; `dataset-model-inspection.md`. |
| `python "$S/analyze_training_history.py" PROJECT --family {detector,classifier,supervised,anomaly,unsupervised,ocr} [--model-id ID] [--output PATH]` | Stored model/training data for exactly 4.0.3; JSON to stdout or outside-project file; `training-history-diagnostics.md`. |
| `python "$S/pekat_project_diagnostics.py" PROJECT [--flow] [--json]` | Filesystem project diagnostics; optional offline FLOW analysis; text or JSON stdout. `--runtime` additionally probes process/port and `--probe-http` sends HTTP; these are not offline operations. See `project-diagnostics.md`. |
| `python "$S/analyze_pekat_log.py" TARGET [--json] [--max-families N] [--severity LEVEL]... [--component TEXT] [--incident-family TEXT] [--since TIME] [--until TIME] [--last-session]` | Existing log or project target; filtered text or JSON stdout; `log-troubleshooting.md`. |
| `python "$S/check_pekat_library_compat.py" --pekat-version VERSION [--package NAME] [--wheel FILENAME] [--json]` | Looks up bundled compatibility evidence and wheel tags, text or JSON stdout. Evidence is version-specific and historical, not a live runtime check; `code-library-installation.md`. |
| `python "$S/runtime_fingerprint.py"` | Read-only filesystem discovery of default Windows 3.19.3 and 4.0.1 installations, JSON stdout; does not execute PEKAT. Library `fingerprint_installation(path, version)` can inspect an explicit directory. |

## Python helpers and examples

`form_normalization.py` implements version-specific Form normalization used by the generator; `code_module_template.py` and `add_libs_to_sys_path.py` are PEKAT Code examples, not standalone CLIs. `industrial_io_guard.py` provides bit extraction and a guarded write helper; never invoke its write path without explicit authorization and a verified target. These examples do not establish hardware or PEKAT runtime behavior.

**NETWORK_DEMO:** `rest_api_client_demo.py` and `projects_manager_tcp_demo.py` are importable examples, not offline tools or standalone CLI commands. They may send network requests; Projects Manager `start`, `stop`, and `switch` mutate runtime state. Use only for an explicit user target and authorization; never automatically execute based on a prompt or as part of offline analysis. They are retained from upstream for continuity and were not exercised against a live endpoint.

See `version-context.md` before transferring behavior across releases. In particular, the 4.0.3 references describe bounded evidence, not general portability or production acceptance.
