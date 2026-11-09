# Host tools and execution

| Surface | Availability and evidence |
|---|---|
| This skill and its references | Advisory instructions and public evidence; no execution by themselves. |
| Bundled `pekat-vision` | Offline tooling described by its own skill. Requires the host to expose its files and any needed execution environment. Check actual inputs and results. |
| Optional external PEKAT Assistant Core | Separately installed and versioned; the bundled `pekat-core-local` adapter is scoped to identity, offline capability lookup and deterministic planning, without a project or live writer. Discover the Core identity and documented capabilities. The plugin does not supply or guarantee Core. A capability listing is not authority or successful preflight. |
| Host file, terminal or Python tools | Available only if exposed and permitted in the actual session. Scope operations to user-provided/authorized files and inspect effects. |
| Host MCP | Only servers and operations actually exposed by the host. The knowledge pack does not create a PEKAT MCP server. |
| Host Computer Use | Only when provided by the host. Inspect the current UI, target, side effects and authorization; navigation itself may trigger evaluation. |

Do not claim a tool call, live project state, controller connection or hardware test without observation. A failed or unavailable path should leave a useful analysis or draft and a precise gap. After an unknown operation outcome inspect state before retrying.
