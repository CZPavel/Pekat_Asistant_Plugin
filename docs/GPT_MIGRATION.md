# GPT migration

This package supplies portable skill instructions and curated public reference files. It does not access a user's GPT configuration, instructions, actions, knowledge files, credentials or publishing settings. Existing GPT account configuration is unavailable here: migration remains partial until the owner inspects and transfers applicable settings and verifies them in the destination.

Compare purpose and scope, public knowledge coverage, instructions, actions and authentication separately. Reconcile each action with an actually available host tool and exact operation contract; do not reproduce credentials or assume an Action or MCP server exists. Review rights and remove private content before publishing. Test representative prompts, supplied artifacts and intended host access in a fresh session. Record unresolved differences; installation alone does not establish equivalence.

| Original component | New route | Remaining account step |
|---|---|---|
| Published instructions | Main `pekat-assistant` skill | Compare actual published text; finish intended published edits before migration |
| Knowledge files | 44 curated references plus detailed technical offline-skill references | Inventory actual account files and verify rights/version/supersession |
| Code/module examples | Bundled generator, schema, templates and tests | Compare outputs with familiar requests; test actual target import separately |
| Action definitions | Compatible existing host app/contract or open integration gap | Export/review actual definitions; do not migrate credentials into GitHub |
| Starters and older scenarios | Bundled acceptance fixtures and 48-question golden suite | Run familiar prompts and a harder case, inspecting real answers and tool use |
| Model selection and sharing | Destination host/account settings | Review explicitly; no assumed setting or audience transfer |

Use the creator account's available **Migrate to plugin** workflow, based on the
latest published configuration. Review the migrated skill/files before replacing
them. The original becomes read-only after migration. Prior conversations remain
in their history; they are not transferred as plugin context. Custom Actions
need separate replacements and existing users are not automatically granted
plugin access. Confirm recipient installation and use before announcing parity.

Check the [official migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)
and the account's notice. [Plugin availability](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
depends on account/plan, region, surface and workspace. This local-execution
package has not been accepted into the official directory, and universal Free
availability is not established. GitHub installation is a different route.
