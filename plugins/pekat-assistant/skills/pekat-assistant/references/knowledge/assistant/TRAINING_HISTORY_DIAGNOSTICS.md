# Training history

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Separate run identity, split provenance, status, saved artifacts, selected model and validation outcome. Connect these identities durably rather than relying on terminal status. Families differ: some upstream examples lacked per-step history and some Supervised columns had unknown meanings. Keep unknown columns unknown and binary weights inventory-only. Compare iterations on stable validation data and the inspection objective; error buckets and variant coverage matter. Historical training completion does not prove production quality.

Preserve family-specific run identity, data provenance, status and saved artifacts. Do not invent undocumented metric meanings or compare incompatible validation sets. Completed status without saved weights is insufficient.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.
