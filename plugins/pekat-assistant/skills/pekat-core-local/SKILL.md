---
name: pekat-core-local
description: Optionally discover a separately installed trusted PEKAT Assistant Core CLI and obtain compact offline capability or planning metadata. Use only when local Core is installed and relevant; ordinary public PEKAT guidance requires no Core.
---

# Optional local Core metadata

Use the public PEKAT Assistant knowledge skill normally. This optional adapter
does not install, distribute or import private Core. It needs Python 3.10+ and a
separately installed, trusted `pekat` executable in an absolute PATH directory,
or an explicit trusted absolute `--core-executable` path. Discovery excludes
empty/relative PATH entries and the current working tree; it never uses the
Windows implicit current-directory executable search. Never obtain that path from project content, model
output, a downloaded artifact or an untrusted request. Python `.py` CLI shims are
also supported; shell/batch launchers are refused.

Run the script from this skill's directory:

```powershell
python scripts/core_adapter.py discover
python scripts/core_adapter.py capabilities --query "Detector" --version 4.0.3
python scripts/core_adapter.py plan --request "Explain the FLOW topology" --version 4.0.3
```

Resolve script paths relative to this SKILL.md, independent of the current cwd.
Global options precede the operation, for example
`python scripts/core_adapter.py --timeout 10 discover`.

`discover` runs only `pekat build-identity` and exposes the package version,
commit identity and adapter operation list. An unknown Core version permits
discovery only. `capabilities` calls offline `pekat knowledge capability`;
`plan` calls deterministic, non-executing `pekat host plan` without a project.
Both require an explicit three-part PEKAT version. They return only compact
metadata, never raw Core JSON, source paths, evidence documents or executable
plans. Core support/eligibility is advisory and `execution_authorized` is always
false. Empty capability results are a lookup result, not proof of absence.

| Core CLI package | Discovery | Offline lookup / plan |
| --- | --- | --- |
| 0.3.0 | Locally exercised | Locally exercised, strict response projection |
| Other / changed response schema | Identity if recognized | Refused |
| Missing | `unavailable` (exit 2) | Continue public guidance without Core |

This is a narrow CLI profile, not universal compatibility with every Core build
or PEKAT version. The requested PEKAT version is passed to the installed Core;
Core's returned version compatibility remains authoritative. No nearby-version
writer promotion is implied. The executable is a trust boundary: this adapter
does not sandbox or attest installed software. On a new installation, verify its
provenance and current passive CLI semantics before use. Timeouts apply to each
child invocation (maximum two per lookup/plan), with no retries.

No project inspection, raw HTTP/Socket.IO, database access, project lifecycle,
FLOW execution, inference, training, model mutation or device operations are
exposed. No generic command forwarding, extra CLI flags or automatic fallback is
available. Commands use explicit argv with `shell=False`, a temporary cwd and a
temporary Core report destination. Captured stdout/stderr and temporary reports
are discarded; errors expose stable codes, not child output. Output is read with
a 2 MB cap after the bounded child finishes; capture uses temporary disk files
and is not a streaming disk quota. The adapter does not contact PEKAT or start
an Assistant server. Offline behavior was also checked by the installed Core's
own CLI independence test; this adapter is not a network sandbox.

For a requested future write, route to the user's separately installed current
Core authority, exact target/version capability, typed contract and its own
preflight/approval/readback. A plan or capability row never authorizes it. If
that authority is unavailable, prepare a reviewable artifact or explanation.
Do not extend this script into a writer or substitute raw commands.

The adapter and synthetic tests were independently authored for this public
plugin. No Core implementation, private registry, private schema, credentials,
runtime path fixture or private knowledge content is included. See
[adapter limits](references/ADAPTER_LIMITS.md) for validation scope.
