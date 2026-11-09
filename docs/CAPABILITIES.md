# Capabilities and boundaries

The PEKAT Assistant skill provides source-grounded advice on inspection design, FLOW, Code, PTool/Form, datasets, ML, diagnostics and integration. Its 44 curated references live once under `plugins/pekat-assistant/skills/pekat-assistant/references/`. They describe bounded evidence, not an executable contract.

The separately bundled `pekat-vision` skill contains its documented offline tools. Discover the skill and host execution facilities, inspect inputs and run only within authorized scope. Offline observations concern supplied artifacts, not live execution. A separately installed PEKAT Assistant Core is optional and has its own versioned contract and authorization. It is not provided by these references. Host tools are independent capabilities; see [host tools](HOST_TOOLS.md).

No live PEKAT execution, physical camera or sensor, host installation or current runtime acceptance is established by the knowledge pack. Consult each reference for exact evidence and limitations.

| Operation | Delivered route | Inputs / output / verification |
|---|---|---|
| Inspection/FLOW design, optics, light, ML selection | Bundled main skill and 44 references | User objective, exact version and relevant evidence → justified design and validation plan; advisory |
| Project/FLOW, source, dataset/model, training-history analysis | Bundled `pekat-vision` scripts | Explicit supplied files; 4.0.3-specific tools enforce their scope → static reports; restricted parser and synthetic regression tests |
| Log diagnosis | Bundled log analyzer | Supplied sanitized text/project → incident/session summary; actual CLI smoke |
| Code/PTool/PModule generation | Bundled generator and Form normalization | JSON ModuleSpec, exact 3.19.3/4.0.1/4.0.3 target → requested artifact; syntax/schema/round-trip checks; no live import |
| Compatibility and dependencies | Bundled compatibility lookup | Version, package or wheel name → historical evidence/tag assessment; not package installation |
| Files | Host plus explicit-output tools | Read user-supplied artifacts/write requested reports; host scope applies; no unrestricted filesystem service |
| Core identity, capability metadata and non-executing plan | Optional `pekat-core-local` adapter | Trusted installed Core 0.3.0; typed arguments → compact validated JSON; unavailable Core is handled |
| GUI inspection and supported parameter configuration | Host Computer Use plus specialist/current target contract | Only actually exposed host tools; effects, target and result require verification; not bundled GUI automation |
| Basler/pylon/GenICam, IFM IO-Link, KEYENCE profiles/GAP-FLUSH | Packaged specialist bridges and host-provided specialist skills | Exact device/firmware/IODD/SDK context; no bundled hardware transport or new device writer |
| Network examples | Existing explicit-target demos | Opt-in examples; runtime-changing commands require authorization; excluded from offline execution |
| Live project/device writers, arbitrary Core command forwarding | Not implemented | Continue with a reviewable artifact or existing separately authorized exact contract |
| MCP server | Not bundled | Host MCP may be used if actually exposed; no invented PEKAT MCP |

Model families, native GUI functions, private capabilities and publicly shipped
tools remain separate availability claims. Tool contracts and flags are in the
bundled tool catalog and the Core adapter skill. No API key is needed for these
offline tools.
