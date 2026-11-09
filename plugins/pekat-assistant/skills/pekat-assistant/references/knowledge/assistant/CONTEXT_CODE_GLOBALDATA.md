# Context and shared state

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Code performs custom computation while Context carries an evaluation's data. GlobalData resets at project-server restart; it is neither durable storage nor an automatic parallel merge. Specify branch-owned keys, item identity, writers, readers, reset and stale-value rules. A previous item's valid value must not silently decide the next item. Native results, raster pixels and custom metadata need separate review. Historical 4.0.3 persistent Python state can be a legitimate cache; shared readers/writers establish a dependency, not an automatic collision.

Separate per-evaluation state from process-lifetime shared state and durable history. Restart-sensitive state needs explicit reset and ownership. Persistent Python state is not automatically defective; matching names do not prove a collision.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.
