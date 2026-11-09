# Adapter validation and limits

The public adapter owns its small output schema. It reads only selected CLI
metadata fields, rejects wrong types, and discards unknown fields. It does not
reproduce Core's models, parameter schemas, registry or implementation.

Supported operations are discovery, offline capability metadata lookup and
deterministic non-executing planning. There is no project argument. Every lookup
and plan first rechecks installed package identity; missing Core is an optional
integration state. Unknown package versions fail closed beyond discovery.

The local acceptance check used a user-installed Core CLI package 0.3.0 on
Windows, with discovery plus one explicit-version capability lookup and one
planning request. It established subprocess invocation and output compatibility
for that installation. It did not test a PEKAT project, inference, model quality,
GUI, physical hardware, production behavior or another computer. A package
version alone is not an attestation of binary contents or every build's effects.

Synthetic executable tests cover explicit argument boundaries, shell metacharacters,
leading-option rejection, operation allowlisting, version/timeout validation,
missing executable, incompatible identity/schema, unknown version, child failure,
timeout, oversized/invalid JSON output and omission of private/credential fields.
Discovery regression tests place malicious executable placeholders in cwd and
relative PATH directories, check resolution with a legitimate installed PATH
entry, and check unavailable behavior without one. Explicit executable paths
must be absolute; automatic lookup excludes the current working tree.

Intentional parity gaps with separately installed private Core include full
knowledge lookup, project analysis/comparison, typed workflows and parameter
schemas, all live readers, every writer and all device routes. Those features
are neither bundled nor emulated. Use public static guidance without Core, or
the separately installed authority for its supported work.
