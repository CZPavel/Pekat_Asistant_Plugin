# Validation and remaining acceptance

## Verified 2026-11-09

- Public repository, default branch `main`, including anonymous GitHub access.
- Portable manifest checked against the published Agent Plugins JSON Schema;
  all three skills checked by the official skill validator.
- 143 tests passed locally and in GitHub CI on Python 3.11 and 3.13: 104 reused
  offline tests, 32 adapter tests and seven package/benchmark checks.
- Real bundled CLI smoke: synthetic log analysis, compatibility lookup and
  generation of a form-bearing PEKAT 4.0.3 PTool. No live import/evaluation.
- Optional adapter exercised against an already installed trusted Core 0.3.0:
  discovery, compact capability lookup and a non-executing plan. No project was
  supplied. Default executable lookup excludes current/relative PATH locations;
  this boundary has a regression test.
- Codex CLI 0.160.0 added the GitHub marketplace and installed plugin 0.3.0.
  `plugin list` reported `installed=true`, `enabled=true`; all 93 installed
  package files matched the reviewed source bytes.
- A **new local Codex desktop chat** discovered `pekat-assistant:pekat-assistant`
  and `pekat-assistant:pekat-vision` from the installed package. It explicitly
  used those skills, ran the installed log analyzer on one synthetic timeout
  line, and validated exit 0 / JSON / one ERROR / no unparsed lines. It also
  used the Context/GlobalData reference to explain stale-value handling.
  Automatic skill selection for arbitrary future requests was not evaluated.
- Deterministic standalone ZIP includes manifest, all three skills, tools,
  references, requirements, Apache license and MIT notice.

Status: **REPOSITORY_CREATED / PLUGIN_BUILT / PUBLIC_VALIDATED /
LOCAL_INSTALLED / TOOL_ACCEPTANCE_VERIFIED** for the bounded cases above.
**GPT_MIGRATION: PARTIAL** — actual owner-account configuration and Actions
remain unavailable. The retained nine response fixtures are still expectations;
their pending suite status does not negate the installation/single-chat smoke.

The public package is checked by its publication manifest, privacy/reference/
syntax gates, reused offline-tool tests, optional-adapter tests, real synthetic
analysis/generation, and deterministic standalone ZIP build. These checks do not
establish PEKAT runtime behavior, camera/sensor timing, physical accuracy or
production quality.

The upstream public skill's 104 offline tests are retained with only fixture/root
paths adapted. The independently authored Core adapter has positive and negative
tests for its fixed operations, unavailable/incompatible Core, argument rejection,
output schema, timeout and output-size handling. No private Core source or data
is bundled. Live local adapter smoke is separate from fake-child unit evidence.

`python scripts/smoke_tools.py` runs the actual bundled log analyzer and library
compatibility lookup against synthetic inputs without Core or network. The
generator suite creates and validates version-specific module artifacts without
loading them into PEKAT. The public response fixtures are expectations, not proof
of model response quality.

The installation and new-session smoke above are separate from static package
tests. A marketplace registration alone is not installation evidence.
Official Directory submission, Free-account availability,
the original account's GPT migration and hardware acceptance remain unverified.
