# FLOW interpretation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Explain actual execution and branches rather than module inventory. Image raster, native results and custom state have different branch behavior. Historical Gate and native-tool evidence covered narrow subsets.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.

## User-guided functional design

Evidence: general design advice and a synthetic illustration. This public pack has no candidate validator, runtime integration or writer. Patterns are recommendations, not mandatory module templates.

Start with the user goal and functional hierarchy: whole object, regions, checks, dependencies and local/final outcomes. Preserve an explicitly supplied hierarchy where practical. If none is given, propose understandable groups and proceed when sufficient facts are known; clarification is not a compulsory approval gate. Explain departures using concrete dependencies, shared localization/inference, image transforms, copying cost, latency, uncertain joins or a more suitable native operation.

Reason from goal to functional groups, dependencies, image domains, native/Code operations, useful branches, results and final image. Keep observed execution topology separate from every recommended alternative. Module inventory does not establish execution order.

## Native-first alternatives and shared inference

Compare sequential, branched and hierarchical alternatives. Prefer suitable native operations when they simplify design, preserving requested or necessary Code. Conditional Gate may replace simple custom decisions only after exact-version semantics and equivalence are established. Parallelism may reduce auxiliary Code for image handling or native-result forwarding; branch count is not an optimization target.

Keep shared inference as one producer where input domain and requirements permit. Different preprocessing may justify a separate image branch without repeating shared inference. Explain rejected alternatives and tradeoffs: synchronization, Context ownership after joining, large-image copies, latency, module count and technician readability. Do not invent an empty branch as proof that the original image survives.

## Image, result and visualization lineage

Describe separately:

- Original capture, each transformed/preprocessed raster and coordinate mapping.
- Raster consumed by every check and the expected transfer at every join.
- Native result provenance, local decisions and the final result collector/report.
- Custom Context ownership, validity and freshness, separate from native results.
- Final raster, native overlays and custom annotation rendering, including mapping to original coordinates.

Merging decisions does not prove image merging or overlay transfer. A structurally consistent design proves neither runtime acceptance, model quality nor writer authority. Missing exact-version join/image/Context/overlay behavior remains an explicit open gap. Recommend the smallest separately authorized per-frame experiment that distinguishes competing behaviors; this advice does not execute it.

## Synthetic example

A fictional fixture has an upper symbol group and a lower fastener group. Preserve those user-facing groups, localize once and propose one shared object inference. One check consumes native results; another needs a contrast-adjusted raster. Discuss a separate preprocessing branch without automatically duplicating inference. Attribute each result to its producer and raster. Collect OK/NOK/UNKNOWN decisions explicitly.

For visualization in original coordinates, name the original capture as the intended final raster, record every transform and map annotations back before rendering. Whether raster and native overlays survive a particular join remains unverified until tested on the exact version. A sequential alternative may be simpler when branching adds copies or uncertain joins. Explain the choice; no project is changed.

## Current bounded support — 2026-10-23

Exact 4.0.3 C1 accepts editing an existing BRIGHTNESS_CONTRAST item: brightness integer -255..255 and finite contrast 0.01..4, preserving siblings. This is distinct from PREPROCESS CUT and Contrast equalisation. Arbitrary filter creation/chains remain outside this subset.

Conditional Gate accepted variants are Boolean EQUAL, finite numeric GlobalData comparisons, nested AND/OR Context/Result groups, and D1 Rectangle COUNT with strict integer operands and Any/Every/Together selectors. The historical float COUNT failure does not exclude that integer subset. Other Rectangle properties and explicit classes remain excluded. This package supplies advisory knowledge, not execution authority.
