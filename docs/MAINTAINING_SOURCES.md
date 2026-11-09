# Controlled public-source updates

This repo is self-contained. Users do not need source checkouts. Provenance locks
pin public upstream commits and the exact files approved for import; hashes refer
to Git blob bytes before local adaptations. Publication hashes describe the
current integrated files. Never copy a private tree and then blacklist content.

Maintainers can audit an existing public checkout with
`python scripts/check_upstream.py assistant --checkout PATH` or the `offline`
source selector. The command verifies the public origin and every allowlisted
blob at the pinned commit; it neither fetches nor copies files.

For a source update, compare the proposed public commit only for the recorded
files, review rights and version/evidence deltas, import individual approved
changes and retain local router/test-path adaptations. Update the relevant source
lock after review. Run privacy/reference checks, the reused tests and tool smoke.
Then record explicit publication approval with
`python scripts/publication_manifest.py --approve` and build the ZIP.

Do not create another maintained knowledge copy or silently overwrite adapted
skills. Private Core/CLI remains an optional local dependency, outside this
publication route. Source audits are development checks, not user runtime steps.
