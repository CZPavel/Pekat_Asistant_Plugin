# PEKAT 4.0.3 decision guide — October update

This advisory card separates current bounded support (2026-10-23) from the historical 2026-10-09 checkpoint. The older table below preserves historical gaps, not current blanket prohibitions. It distributes no runtime controller. Current official PEKAT 4.x documentation, exact-4.0.3 observations and offline recipes are separate evidence classes; none grants execution authority.

## Current bounded support and routing — 2026-10-23

The historical table below preserves the 2026-10-09 checkpoint. Later exact 4.0.3 accepted subsets qualify its historical gaps: [ID-specific Detector edits](DETECTOR_ANNOTATION_403.md), [Brightness/Contrast and Gate variants](FLOW_AUTHORING.md), and [OCR region authoring](OCR_ANNOTATION.md). Brightness/Contrast is distinct from Contrast equalisation; a crop never substitutes for either.

| Current exact-4.0.3 subset | Accepted boundary in the separately authorized Assistant |
|---|---|
| Detector ID-specific edit | Existing rectangle ID: relabel/move/resize/stored-anchor rotate/delete; fresh preimage and sibling preservation. Last-object deletion is PRESENT_EMPTY, not ABSENT. Image-wide Clear is a different operation. |
| Brightness/Contrast | Edit an existing BRIGHTNESS_CONTRAST item: brightness integer -255..255, finite contrast 0.01..4. Filter creation/chains and Contrast equalisation are outside this subset; PREPROCESS CUT is different. |
| OCR authoring | Region creation/deletion, geometry, transcription, character partition and separator editing. Arbitrary interactive drag remains unaccepted. |
| Conditional Gate | Boolean EQUAL, finite numeric GlobalData comparisons, nested AND/OR Context/Result groups, strict integer Rectangle COUNT Any/Every/Together; other Rectangle properties and explicit classes remain excluded. |

These are bounded upstream accepted contracts. This public package contains no runtime controller or writer and grants no execution authority.

Prefer an existing closed workflow matching the requested outcome. Intent recognition is read-only and grants no writer authority. Confirm exact version, capability state, parameter schema, preflight and explicit authorization in the separately installed controller. Negated, ambiguous, unknown or unsupported requests must remain classified gaps; never substitute a similar destructive action.

Knowledge lookup must prefer applicable current evidence over explicitly superseded evidence while retaining history and do_not_repeat. Follow multi-step supersession only within matching version/contract/evidence scope. Cycles, conflicting relations or unclear scope require an explicit unresolved result rather than an inferred promotion. A newer date alone is insufficient.

## Choose the function before the tool

Interpret short Czech or English requests by the object, intended result and variant, even when word order or accents differ. Prefer an existing closed workflow in an separately installed authorized controller. This package can explain its preconditions and checks; it cannot execute it. Confirm exact version, required arguments, project state, side effects, preflight and readback before proposing execution.

## Historical checkpoint — 2026-10-09

The following table records the earlier checkpoint only. Its Detector delete/relabel and Contrast gap statements are qualified by the current bounded support above; use that current section for accepted exact-4.0.3 subsets.

| Request / intent | Advisory route | Boundary and useful check |
|---|---|---|
| Smaž jen tento detekovaný obdélník / delete one rectangle | Detector annotation editor | Generic delete-by-ID/relabel writer remains a contract gap. Image-wide clear is a different operation; never substitute it. |
| Ulož snímek s heatmapou / save with heatmap | Image Saver overlay/heatmap settings | Documentation describes this option; no public writer. Verify the saved raster, not just preview appearance. |
| Ulož originální snímek bez heatmapy / save original | Acquisition image and Image Saver | Original, current raster and overlay-free output can differ after crop/scale. Require explicit image provenance. |
| Kamera je vypnutá, proč nejde FLOW? / camera off | Camera acquisition preconditions | Live Stream OFF can coexist with service OPEN. Explain the state mismatch; do not bypass the FLOW guard. |
| Přidej filtr pro zvýšení kontrastu / add contrast | Preprocess GUI | Sixteen GUI choices were observed; upstream writer is CUT-only. Contrast writer is a gap. |
| Vyřízni oblast podle součástky / crop detected part | Unifier or explicit crop recipe | Accepted upstream one-object contract is narrow. Rotation/multi-anchor behavior remains unverified. |
| Neukládej snímek pod předchozím názvem / avoid stale name | Context freshness and Image Saver | Carry current frame identity with results; reject missing/stale identity. JPEG/JSON atomic pairing remains unproven. |
| Spusť analýzu jednoho snímku přes API / analyze one image | Closed single-image analysis workflow | Prefer that workflow over improvised calls where a verified controller exists. Validate response identity and inspection outcome separately from transport success. |
| Přidej vstupní hodnotu do Operator View / Operator input | Closed Operator Input workflow | Identify name, type, default and ownership; compare configured and runtime values. Public pack offers guidance only. |
| Vyhodnoť vítěznou třídu / Classifier winner | Classifier decision semantics | Use the winning class and threshold; label presence in a candidate list is insufficient. |

## State and image evidence

Context describes the evaluated frame; GlobalData is shared process-lifetime state. Restart resets process-lifetime state and does not make it durable. Initialize/reset frame-local collectors, attach current frame identity and reject missing or stale inputs. Two sequential upstream evaluations had internally consistent identities; this does not establish concurrent correctness or atomic output persistence.

Image pixels, native overlays/results and custom Context are independent channels. A final raster can have no native overlay while custom results still describe the original image. A heatmap preview is not proof that a saved raster includes heatmap pixels. Check each requested channel explicitly.

An offline axis-aligned crop/scale fixture verified bbox restoration and raster bounds within one pixel. Store crop origin and independent x/y scale with the result. This does not validate rotation, perspective, native Unifier/Parallelism transforms, percentage annotations or physical metrology.

## Product, upstream and public support

Current official 4.x prose describes broader Unifier and Detector GUI behavior than the narrow accepted upstream 4.0.3 writer contracts. Preserve the one-object Unifier limit and annotation editor versus generic writer distinction. Preprocess GUI/schema observation proves discoverability, not every filter's runtime behavior.

A completed, saved, selected Detector model was observed upstream. No independent test dataset was available for that observation. Training completion, artifact presence, selection and generalization are four separate claims. Request independent representative validation before judging production quality.

Image Saver documentation describes all/OK/NG filtering, Context JSON, overlay/heatmap, Local/FTP and naming options. Sequential identity checks support a bounded freshness conclusion only. Pair image and JSON by explicit identity and account for partial writes; concurrency, crash recovery and atomic pairing remain open gaps.

No new native writer capability was promoted by the October mapping. The public edition contains this explanation, references and offline validation tooling; it contains no controller, private Core, raw evidence or hardware operation. Deterministic private routing tests are not a live small-model evaluation. SMALL_MODEL_LIVE_EVAL_NOT_RUN applies unless a separately recorded model run establishes otherwise.
