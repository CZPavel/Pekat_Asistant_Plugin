# Image, Context, Result and Output — practical PEKAT VISION guidance

Public technical note, 2026-11-09. Evidence scope: **bounded PEKAT VISION 4.0.3 observations** and the explicitly stated comparison with 4.0.1; no assertion that every 4.x version or project behaves identically. This page is knowledge for user review, not an automation interface.

## Distinguish four independently meaningful things

1. **Image raster:** the actual pixels available at the current step, which may have been cropped, rescaled, masked or otherwise processed.
2. **Native recognition and measurement results:** rectangles, classes, OCR, heatmaps, lines and measurements returned by the relevant tools.
3. **Custom Context/shared values:** information passed between operations or held beyond a single evaluation; it may not have the same lifetime or merge behavior as image data.
4. **Visualization and persisted output:** what appears as an overlay in the UI, or what is actually saved to disk. Displaying a result and saving it are distinct outcomes.

A rectangle visible over an image is not proof that the rectangle has been drawn into the image pixels. A visually correct preview is not proof of successful file delivery.

## Frame identity, filenames and stale values

For the observed Folder-source recipe, the input filename is available as a filename-only value in Context. Its presence must be checked for the current input, not borrowed from a previous evaluation.

Shared GlobalData values may survive multiple evaluations but reset with project-server restart. Initialize each evaluation's result quality/validity before producers execute, and associate results with a current frame identity. When a producer fails or a branch is skipped, publish **UNKNOWN/INVALID** rather than silently reusing the previous positive result.

For multi-branch FLOW, avoid assuming that merging image pixels also automatically merges or replaces custom values and native results with equivalent rules. Assess each output channel separately.

## Coordinate systems and transformations

Always state the coordinate basis of a result: full original image, current module image, cropped region, scaled image or unknown. A result can have plausible numbers but still refer to the wrong image basis.

For one previously tested **axis-aligned application recipe** with crop origin (ox, oy), crop scale s and independent original-space scale (sx, sy):

- X = (ox + x × s) × sx
- Y = (oy + y × s) × sy
- W = w × s × sx
- H = h × s × sy

This equation is a scoped numerical mapping, **not** a general PEKAT rule for rotated rectangles, every Unifier mode, percentage-based coordinates, heatmaps or camera calibration. Check landmarks and image size against the actual current transform.

A non-destructive annotation conversion should preserve the original detections and associate any derived representation with its source frame and transformation. New geometry does not automatically establish improved physical accuracy.

## Image Saver and delivery correctness

A bounded 4.0.3 configuration/evaluation test established that an active local Saver needs an eligible execution path and an appropriate production-mode state. Observed selection was: **ALL** accepts True/False/None; **OK** accepts True; **NG** accepts False. These are observations for the tested path, not a universal guarantee across modes and versions.

Treat the following as separate checks:

- the relevant output module is reached and enabled;
- the intended image/overlay and filename basis is selected;
- the configured destination belongs to the intended producer;
- the file has actually appeared and can be opened;
- any accompanying JSON/meta evidence belongs to **the same current frame**, not a previously written image.

For tests, use a unique frame or request marker and check a fresh image plus matching metadata. Separate image and metadata writes are not inherently an atomic pair. A file with a plausible name can still belong to an earlier frame.

**Retention warning:** On the bounded tested configuration, automatic retention could delete **entire old date directories**, including unrelated nested content. Do not enable automatic deletion on a shared/customer directory without first isolating its root and testing the exact settings. Configuration rollback cannot restore files already deleted by a completed cleanup.

## Safe result policy

For a composite inspection, retain a confirmed NOK even if another required check is UNKNOWN. Confirm overall OK only when all required checks are OK, expected instances are covered and observations refer to the current item/frame. Otherwise emit REVIEW/UNKNOWN, while keeping communication and acquisition errors separately visible.

## Suggested acceptance checks

1. Reprocess two distinct, identifiable frames sequentially; verify that labels, images and result metadata do not cross over.
2. Test missing or skipped producers; verify no previous positive value leaks into the next result.
3. Use a visible landmark to verify crop/scale output coordinates.
4. Compare visible overlays with the saved raster; do not presume they are the same.
5. Verify the real delivery path with a unique marker, not only the configured Saver state.
6. If cleanup is used, test it exclusively in an isolated disposable directory.

This note does not claim production concurrency, camera metrological accuracy, rotated-geometry compatibility, general hardware acceptance or a publicly distributed Image Saver controller.

See [practical runtime rules](PRACTICAL_RUNTIME_RULES.md), [capabilities](CAPABILITIES.md) and [public usage guide](PUBLIC_CAPABILITY_GUIDE.md).
