# OCR annotation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Separate region geometry, transcription and character partition. Historical upstream changes concerned an existing region; new-region authoring and external transcription service policy remained gaps. Require human review and appropriate privacy handling.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.

## Current bounded support — 2026-10-23

The historical existing-region-only observation above is superseded within the exact 4.0.3 C1/C2 authoring subset: region creation/deletion, normalized geometry, length-changing transcription, initial N-character partition and separator editing. Preserve whole-string rectangle → transcription → split-to-characters → boundary adjustment. Require fresh preimage, sibling preservation and readback. E1.1 center-preserving rotation at fixed geometry does not prove arbitrary interactive drag. External transcription privacy and service policy remain separate. No public writer is included.
