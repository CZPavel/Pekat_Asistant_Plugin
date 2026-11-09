# Detector, Classifier and OCR

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Detector answers where objects are and their classes. Classifier answers the inspected input's class/state; a winner is not an object-instance list. OCR answers text within supported region/partition semantics. Preserve these meanings rather than using one generic threshold. Record image, family/module, class/transcription, geometry and raster basis. Smart Mask proposals and accepted boxes are not the same representation. Model comparison needs a stable validation basis, variant coverage and relevant miss/false-reject objectives.

Object geometry, classification and recognition require separate annotation and training semantics. Smart Mask suggestion is not persistence; a bounding box is not a segmentation mask.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.
