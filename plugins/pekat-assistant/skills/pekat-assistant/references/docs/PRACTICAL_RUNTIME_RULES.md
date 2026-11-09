# Practical PEKAT runtime rules

Status: sanitized public engineering conclusions.
Primary historical runtime scope: PEKAT VISION 4.0.3 unless a narrower note says otherwise.
These rules do not expose or authorize private transport mechanisms.

## FLOW topology and lifecycle

A project registry and the executed FLOW are different representations. Explain recursive execution topology first. A module that exists in project storage may be inactive, retained history, recoverable state or otherwise outside active execution. Do not classify it as active merely because it exists, and do not recommend deletion from inventory alone.

A static project representation is suitable for explanation and comparison, but it is not a writer contract.

## Image, native results and custom state

Treat these as separate layers:

1. image raster/pixels;
2. PEKAT-native detections, measurements, heatmaps or result objects;
3. custom Context and shared process state.

An image operation can change pixels without erasing all native result semantics. Conversely, removing or replacing result structures is not the same as editing the image.

In parallel FLOWs, an unchanged branch can preserve an earlier raster while other branches produce native results. Do not assume that all branch outputs merge identically.

## Branch exit

Historical runtime evidence shows branch-local exit behavior. Therefore do not explain an exit flag as universally terminating the entire FLOW unless exact-version topology and runtime evidence establish that wider behavior.

## GlobalData and persistent state

GlobalData is shared process-lifetime state and resets when the relevant project server restarts. It is not durable database history.

Every shared value used for production decisions should have a producer, owner, item/product identity where relevant, freshness or timestamp semantics, reset behavior and invalid/stale handling.

A valid value from a previous item must not silently decide the next item.

Historical PEKAT Code can also use persistent Python/module state. Presence of persistent state is not automatically a defect. Treat it first as a dependency that needs ownership and reset analysis.

## Detector versus Classifier

Detector answers object/location questions. Classifier answers class/state questions about an inspected input. Do not treat a Classifier candidate list as detected object instances.

Historical PEKAT observations show that candidate class lists can contain more than the eventual winner. Therefore routing must identify the winner according to the exact family/version contract; testing whether a label appears anywhere in the candidate list is unsafe.

## Annotation representations

Keep these distinct: Smart Mask or segmentation suggestion, accepted segmentation mask, bounding box, persisted Detector rectangle and OCR region/partition information.

Conversion between representations is a deliberate operation with geometry/raster assumptions. A suggestion is not persistence.

## Training and model lifecycle

Training start acknowledgement, progress and terminal UI text are separate from durable artifact creation.

A defensible training conclusion should establish as much as the family supports: run/model identity, terminal state, artifact presence, active model binding/selection and relevant dataset/annotation provenance.

Do not generalize one family's lifecycle to Detector, Classifier, OCR, Anomaly and Supervised interchangeably.

## PTool, Form and Python

A Form control key, displayed default, serialized value and runtime value are separate concepts. Validate types and actual execution values.

Portable PTool/package artifacts do not automatically include external Python packages, ABI compatibility, model weights or device dependencies.

## REST, outputs and communication

Separate process/project reachability, provider/source readiness, image transport, inference, result semantics and outbound delivery.

A successful connection or HTTP response does not prove that the intended image was evaluated by the intended model.

Distributed/shared-state integrations need identity, freshness, timeout, duplicate and restart semantics.

## Version boundary

Version similarity is evidence for investigation, not writer authority.

A behavior observed on 4.0.1 may inform a 4.0.3 hypothesis. It does not prove a 4.0.3 writer or runtime contract. Future PEKAT versions should be treated as fresh version intake until bounded evidence exists.

## Current capability and knowledge boundaries — 2026-10-23

Use the [current decision-guide addendum](../knowledge/assistant/DECISION_GUIDE_403.md) for ID-specific Detector edits, Brightness/Contrast, OCR authoring and accepted Gate variants. Dated negative observations remain historical evidence. Supersession applies only to the matching exact-version contract and evidence scope; retain do_not_repeat and disclose cycles/conflicts. Workflow-first intent selection remains read-only and cannot authorize execution. Public main, released artifacts and hosted GPT knowledge are separate states; local generation does not update a hosted assistant.
