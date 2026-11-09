# Installation and updates

Use the repository marketplace from the README. `marketplace add` only registers
a source; `plugin add` installs it. Check `plugin list --json` for installation
and enablement, then open a new session and confirm that the namespaced skills
and their installed paths are actually available.

Codex CLI 0.160.0 exposes these commands. On a host without `plugin add`, use its
documented Plugins Directory workflow; do not emulate installation by silently
copying skills into global directories. A package and a source registration alone
are not acceptance evidence.

Install Python dependencies into the environment that will execute scripts:
`python -m pip install -r requirements.txt` from a checkout, or the corresponding
requirements file included at the installed plugin root. No PEKAT installation
is needed for ordinary knowledge, module generation or supplied-file analysis.

To update, use `codex plugin marketplace upgrade pekat-assistant-public`, then
repeat `codex plugin add pekat-assistant@pekat-assistant-public` and verify the
installed version. Start a new session and repeat a representative tool test.
If the host offers a separate refresh/update UI, use its supported mechanism.

The plugin runs local tools, so its portable OpenAI metadata declares
`requires_local_executor`. This does not grant file, network or device rights.
File access, Python, terminal, MCP and Computer Use depend on the host. No MCP
server is bundled; there is no MCP startup or authorization requirement.

The ZIP has `plugin.json`, licenses, requirements and `skills/` at its root.
It is self-contained and contains neither Git history nor runtime/customer data.
Other users need only this repo or the ZIP, not the original source repositories.
