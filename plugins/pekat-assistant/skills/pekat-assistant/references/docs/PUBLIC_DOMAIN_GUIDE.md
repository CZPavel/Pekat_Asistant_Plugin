# Practical domain guide

This guide maps user tasks to usable advice. All domain cards below are `PUBLIC_KNOWLEDGE`; native PEKAT functions require the user's own installation and version check. The public Assistant does not include a PEKAT connector or project/device writer. Historical bounded private capabilities are `PRIVATE_VERIFIED_NOT_DISTRIBUTED`, not executable public tools. See the [seven availability classes](PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification).

Inputs mean sanitized material the user supplies voluntarily and has permission to share. A path, screenshot or module name alone does not supply the underlying project, data or runtime state. Start from the relevant card and linked topic; do not require a full project export for a small question.

## Inspection design and acquisition

### Inspection concept and vision-method selection

**Purpose/scenario:** detect a missing component or surface defect with measurable miss and false-reject objectives. **Inputs:** representative OK/NG images, defect size, material, pose variation, field of view, motion, cycle time and acceptance criteria.

**Native functions:** candidate preprocessing, geometry, Detector, Classifier, anomaly, supervised surface inspection and OCR; availability and fit require the exact version. **Assistant role:** compare native/classical/ML alternatives, propose optics/light/acquisition and the smallest discriminating trial. **Automation/limits:** a design or illustrative script is reviewable advice; image visibility, physical repeatability, accuracy and cycle time need independent trials. Start with [inspection design](../knowledge/assistant/VISION_DESIGN.md).

### Camera acquisition and triggering

**Purpose/scenario:** acquire one correctly exposed frame per inspected part. **Inputs:** exact camera/interface, lens, exposure, trigger source, motion, image format and ownership of acquisition.

**Native functions:** configured source, capture/live processing and image selection where supported. **Assistant role:** distinguish camera configuration, live feature values, stream state, processing state and saved images; route exact Basler facts to the specialist. **Automation/limits:** no public acquisition controller; no inferred physical frame freshness from a matching filename or HTTP response. One physical camera owner at a time. See [acquisition](../knowledge/assistant/CAMERA_ACQUISITION.md) and [Basler bridge](../knowledge/bridges/BASLER_PEKAT_BRIDGE.md).

## FLOW, code and image meaning

### FLOW, Parallelism and Conditional Gate

**Purpose/scenario:** explain why a detected object still produces NOK, or group checks by component. **Inputs:** version, active topology, module types/settings, intended dependencies and representative results.

**Native functions:** sequential FLOW, Parallelism, Conditional Gate and preprocessing in the installed version. **Assistant role:** trace execution, preserve the user's functional hierarchy, compare sequential/branched alternatives and identify shared inference. **Automation/limits:** proposals do not author live FLOW; module inventory is not execution order, branch exit is not a universal stop, and joining decisions does not prove image/overlay merging. See [FLOW interpretation](../knowledge/assistant/FLOW_AUTHORING.md).

### Code, Context and GlobalData

**Purpose/scenario:** calculate a custom measurement or diagnose a value left over from a previous frame. **Inputs:** source snippet, version, expected frame identity, input/output schema, reset rules and side effects.

**Native functions:** Code execution and its supported Context/shared-state mechanisms. **Assistant role:** declare producer, frame ownership, missing-input behavior, units, coordinates and lifetime; draft or review code. **Automation/limits:** generated code has not run in embedded PEKAT Python; process-lifetime state is not durable storage or evidence of current-frame validity. File, network and hardware effects require separate scope. See [Context/shared state](../knowledge/assistant/CONTEXT_CODE_GLOBALDATA.md).

### Form, PTool and PModule

**Purpose/scenario:** expose technician parameters for a reusable computation. **Inputs:** exact artifact/version, entry point, stable parameter keys, values/defaults, units/ranges, dependencies and example input/output.

**Native functions:** supported Form controls and native import/export for the actual artifact family. **Assistant role:** prepare readable code and a module card stating purpose, FLOW placement, reads, writes, effects and validation status. **Automation/limits:** no public live import/metadata writer; defaults are not proven execution values, and a narrow package round trip does not prove dependency portability. See [PTool/Form](../knowledge/assistant/PTOOL_PMODULE_FORM.md).

### Embedded Python and external models

**Purpose/scenario:** determine whether an external algorithm or pretrained model can run in Code/PTool. **Inputs:** PEKAT build, observed Python/package profile, CPU/GPU, model/license/weights, preprocessing and resource budget.

**Native functions:** embedded Python/Code in the installed runtime; installed dependencies must be established independently. **Assistant role:** propose a CPU reference, explicit dependency checks and bounded evaluation. **Automation/limits:** package presence, import, model construction and real inference are different evidence levels. A tested machine is not a clean installation, and one external-model example does not establish arbitrary-model compatibility. See [runtime profile](../knowledge/assistant/RUNTIME_PYTHON_ML.md) and [external-model example](../knowledge/assistant/EXTERNAL_TORCHVISION_PTOOL_403.md).

### Image, annotations, native Result and Output

**Purpose/scenario:** deliver the right image and result when a branch crops or changes its raster. **Inputs:** source image, transformations, producer/frame identity, result/context artifact, intended overlay basis and destination ownership.

**Native functions:** image display, native results/overlays, local Image Saver and output modules as individually supported. **Assistant role:** trace raster, geometry, native result and custom state separately; define freshness and complete-delivery checks. **Automation/limits:** no public saver/output writer; equal image dimensions do not prove alignment, configuration/ACK does not prove file delivery, and sequential evidence does not prove concurrency. Retention can delete foreign files in owned date folders. See [image/output guide](IMAGE_CONTEXT_OUTPUT_GUIDE.md).

## Dataset, annotation and model lifecycle

### Detector and annotation

**Purpose/scenario:** locate/count parts and review missing or incorrect boxes. **Inputs:** representative images, class definitions, box geometry/basis, module/model identity and independent validation examples.

**Native functions:** Detector labeling, training, inference and supported Smart Mask assistance. **Assistant role:** distinguish object instances from image-level class predictions, review dataset coverage and draft labeling/QA rules. **Automation/limits:** Smart Mask computation is not persisted annotation; a box is not a segmentation mask. No generic public annotation/model-delete writer is shipped. See [Detector annotation](../knowledge/assistant/DETECTOR_ANNOTATION_403.md).

### Classifier and result interpretation

**Purpose/scenario:** distinguish a correctly assembled input from an incorrect variant. **Inputs:** input domain/source, allowed classes, labels, selected model, predictions/confidence and validation split.

**Native functions:** family-specific labeling/training, class inference and available statistics. **Assistant role:** reason about winner versus other candidates, source/domain consistency, ambiguity and validation leakage. **Automation/limits:** candidate presence does not prove the winning class; current settings do not retroactively redefine a trained model, and TRAIN-inclusive statistics are not independent quality. See [Detector/Classifier/OCR](../knowledge/assistant/DETECTOR_CLASSIFIER_OCR.md).

### Anomaly learning and supervised surface inspection

**Purpose/scenario:** detect an unusual surface or localize a known defect. **Inputs:** representative normal variation, module-specific OK/NG labels or masks, defect definitions, pixel basis and held-out evaluation set.

**Native functions:** anomaly and supervised surface workflows as separate model families. **Assistant role:** choose a family, review label/mask quality and propose threshold/coverage experiments. **Automation/limits:** tags, OK/NG labels and pixel masks are distinct; unlabeled does not mean confirmed normal. No shared generic annotation/training writer or inferred cross-family progress scale. See [anomaly](../knowledge/assistant/ANOMALY_UNSUPERVISED.md) and [supervised masks](../knowledge/assistant/SUPERVISED_MASK_LIFECYCLE.md).

### OCR and text annotation

**Purpose/scenario:** read a marking and compare it with an expected identifier. **Inputs:** image/region, transcription policy, charset/format, orientation, model/version and accepted error criteria.

**Native functions:** supported OCR regions/partitions, annotation, recognition and training. **Assistant role:** separate annotation text, recognized text, confidence and application-level format validation. **Automation/limits:** no public OCR writer; region geometry and transcription have their own contracts. Correct format alone does not prove the text is correct or belongs to the current frame. See [OCR annotation](../knowledge/assistant/OCR_ANNOTATION.md).

### Training history, model selection and portability

**Purpose/scenario:** decide whether a trained model is usable or move data to another project. **Inputs:** family/version, dataset/splits, training terminal state, saved artifact, selected model identity, metrics and source/target export formats.

**Native functions:** family-specific training/status/selection, Image Library transfer, supported Detector COCO and native model-package transfer. **Assistant role:** distinguish command acknowledgement, terminal state, saved weights, selection and independent quality; plan an explicit transfer check. **Automation/limits:** progress 100 or a completed record does not alone prove saved usable weights. Export families are not interchangeable and clean import does not prove equal inference. See [training history](../knowledge/assistant/TRAINING_HISTORY_DIAGNOSTICS.md) and [portability](../knowledge/assistant/DATA_MODEL_PORTABILITY.md).

## Project understanding and operation

### Project explanation, comparison and modernization

**Purpose/scenario:** understand a supplied project, identify a change between versions, or replace custom logic with a native feature. **Inputs:** sanitized snapshots/diagrams, exact builds, active topology, code/settings, known good behavior and intended delta.

**Native functions:** project management and installed native alternatives; the comparison itself is an advisory/offline task. **Assistant role:** separate active modules from recoverable history, match by meaning rather than only IDs, preserve working logic and identify the smallest regression check. **Automation/limits:** this repository includes no project parser/controller; name the separate public offline skill when recommending its scripts. Static similarity proves neither runtime equivalence, timing nor equal OK/NOK behavior. See [project analysis](../knowledge/assistant/PROJECT_ANALYSIS.md), [semantic diff](../knowledge/assistant/SEMANTIC_PROJECT_DIFF.md) and [modernization](../knowledge/assistant/MODERNIZATION_ADVISOR.md).

### Logs, startup and troubleshooting

**Purpose/scenario:** diagnose apparent hangs, initial evaluation or missing results. **Inputs:** version, source/mode, timestamps, sanitized logs/stderr, readiness/model state, last successful action and repeatable symptom.

**Native functions:** project lifecycle/status and runtime logging in the installed version. **Assistant role:** rank hypotheses and propose one low-risk discriminating check; distinguish startup, server-ready, model-ready and actual processing. **Automation/limits:** a restart can trigger evaluation/effects; a native success result can coexist with a Code traceback. Do not classify every initial frame as faulty or call an execution-bearing reader a passive check. See [troubleshooting](../knowledge/assistant/TROUBLESHOOTING.md) and [log diagnosis](../knowledge/assistant/LOG_DIAGNOSTICS.md).

### Projects, Operator and statistics

**Purpose/scenario:** present inspection state to an operator and explain summary counts. **Inputs:** intended operator workflow, layout, data origin/reset rules, project lifecycle and recovery requirements.

**Native functions:** available Operator layout/input, kiosk and statistics facilities; each requires version-specific evidence. **Assistant role:** propose understandable status/UNKNOWN/error handling and distinguish a display from an operator state machine. **Automation/limits:** retained Operator runtime evidence was Input-only; kiosk recovery remained manual. No public UI automation or complete statistics writer is included. See [Operator/statistics](../knowledge/assistant/PROJECTS_OPERATOR_STATISTICS.md).

## Communication and industrial integration

### REST, official SDK, HTTP Output and Cross-PEKAT

**Purpose/scenario:** request inspection externally or forward a result to another system. **Inputs:** exact version/interface documentation, input/result schema, request/frame identity, timeouts, acknowledgement semantics and destination ownership.

**Native functions:** documented REST/SDK interfaces, HTTP Output and supported cross-project mechanisms have separate scopes. **Assistant role:** draft a bounded integration contract, distinguish request acceptance from processing/delivery, and define stale/duplicate/timeout behavior. **Automation/limits:** no public live client/controller is bundled; an SDK release does not establish a generic writer. Happy-path state transfer proves neither reconnect behavior nor atomic image/JSON delivery. See [REST/SDK](../knowledge/assistant/REST_SDK_CROSS_PEKAT.md), [HTTP Output](../knowledge/assistant/HTTP_OUTPUT_403.md) and [Cross-PEKAT](../knowledge/assistant/CROSS_PEKAT_403.md).

### Basler, IFM IO-Link, KEYENCE LJ-X/LJ-S and MX-G2000

**Purpose/scenario:** combine a camera, distance sensor or line profile with vision, or deploy onto an embedded platform. **Inputs:** exact model/family/firmware, interface, units/quality, timing, device ownership, coordinate calibration and PEKAT build.

**Native functions:** only those independently established for the named PEKAT source/transport and exact device. **Assistant role:** route vendor facts to the matching specialist and own PEKAT-side timestamp/frame/measurement composition. **Automation/limits:** specialist knowledge is an independent dependency, not a device writer; LJ-X/LJ-S families are not interchangeable, an installed SDK is not acquisition proof, and platform compatibility is not an industrial acceptance test. See the [hardware bridges](../knowledge/INDEX.md).

## How to finish a useful advisory task

Return a concrete explanation, code draft, inspection design, comparison or integration contract; list the inputs still missing only when they affect its use. Name the exact version and evidence level. State which artifact/tool is actually shipped and the smallest remaining offline, runtime or physical check. Unsupported execution does not block useful preparation. Public publication utilities are `PUBLIC_EXECUTABLE`; new live connectors, new writers and a public Windows installer remain separately reviewed work, not features implied by these cards.
