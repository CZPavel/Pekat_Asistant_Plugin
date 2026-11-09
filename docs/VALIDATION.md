# Validation and remaining acceptance

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

Local installation and new-session model/tool smoke are recorded separately after
the package is published and installed. A marketplace registration alone is not
installation evidence. Official Directory submission, Free-account availability,
the original account's GPT migration and hardware acceptance remain unverified.
