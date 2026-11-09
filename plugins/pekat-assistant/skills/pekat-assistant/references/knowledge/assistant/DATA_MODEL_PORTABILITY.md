# Data and model portability

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Keep original source, Image Library, native exported raster and model-package identities separate. Names can route files without proving original identity. Check dimensions and coordinate basis: upstream exported Detector rasters could differ from corresponding library rasters despite equal dimensions. Do not infer the transformation or rebuild labels against a guessed basis. Inventory tags, splits, labels, annotations and bindings individually. Clean-target transfer does not establish safe merge/reimport, partial-failure rollback or cross-version compatibility.

Image export, Detector COCO transfer and model-package transfer are separate contracts. Check archive structure, raster basis, class mapping and geometry. Names do not prove original identity; similar ZIPs are not interchangeable.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.
