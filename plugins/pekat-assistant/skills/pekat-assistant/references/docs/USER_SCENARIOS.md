# User scenarios

These statuses describe the historical upstream requirements catalog, not tools included in this preview. The public pack can advise from supplied evidence; it cannot execute these workflows.

- `AVAILABLE_NOW`: a verified narrow upstream capability existed.
- `PARTIALLY_AVAILABLE`: useful pieces existed, with explicit end-to-end gaps.
- `PLANNED`: a product goal without a completed workflow.
- `FUTURE_VISION`: depended on later interfaces, hardware, history or multimodal development.

| ID | Goal | Historical upstream status |
|---|---|---|
| US-02 | Understand a new inspection problem | PARTIALLY_AVAILABLE |
| US-03 | Explain an existing PEKAT project | PARTIALLY_AVAILABLE |
| US-04 | Safely modify FLOW | PARTIALLY_AVAILABLE |
| US-05 | Capture a bounded image set | AVAILABLE_NOW |
| US-06 | Dataset audit before training | PARTIALLY_AVAILABLE |
| US-07 | Select useful images | PLANNED |
| US-08 | Bootstrap Detector | PARTIALLY_AVAILABLE |
| US-09 | Teach by pointing | FUTURE_VISION |
| US-10 | Teach OK/NOK state | PLANNED |
| US-11 | Correct target conversationally | FUTURE_VISION |
| US-12 | Smart Mask proposal | PARTIALLY_AVAILABLE |
| US-13 | Automatic Annotations review | PLANNED |
| US-14 | Compare model iterations | PARTIALLY_AVAILABLE |
| US-15 | Champion/challenger deployment | PARTIALLY_AVAILABLE |
| US-16 | Preprocessing experiment | PARTIALLY_AVAILABLE |
| US-17 | Training campaign | PARTIALLY_AVAILABLE |
| US-18 | Stop iterating | FUTURE_VISION |
| US-19 | External multimodal OCR annotation | PARTIALLY_AVAILABLE |
| US-20 | OCR error mining | PARTIALLY_AVAILABLE |
| US-21 | Diagnose gradual degradation | FUTURE_VISION |
| US-22 | Shared confidence loss | FUTURE_VISION |
| US-23 | Explain unexpected NOK | PARTIALLY_AVAILABLE |
| US-24 | Manual production feedback | PLANNED |
| US-25 | Retrospective defect search | FUTURE_VISION |
| US-26 | Production sampling | FUTURE_VISION |
| US-27 | Voice tag data | PARTIALLY_AVAILABLE |
| US-28 | Voice review dataset | FUTURE_VISION |
| US-29 | Voice FLOW change | PARTIALLY_AVAILABLE |
| US-30 | Operator next-step guidance | PLANNED |
| US-31 | Multi-step assembly | PLANNED |
| US-32 | Distributed vision process | PARTIALLY_AVAILABLE |
| US-33 | Multi-camera aggregate result | FUTURE_VISION |
| US-34 | External sensor Gate | PLANNED |
| US-35 | TCP measurement plus camera | PLANNED |
| US-36 | Preserve clean image and native results | PARTIALLY_AVAILABLE |
| US-37 | Selective NOK/borderline collection | PARTIALLY_AVAILABLE |
| US-38 | Whole system health | FUTURE_VISION |
| US-39 | Compare one camera | FUTURE_VISION |
| US-40 | Bounded camera optimization | FUTURE_VISION |
| US-41 | Embedded Python compatibility | PARTIALLY_AVAILABLE |
| US-42 | Closed-loop vision lifecycle | FUTURE_VISION |
| US-43 | Safe refusal | AVAILABLE_NOW |
| US-44 | Exact-version boundary | AVAILABLE_NOW |

Full output reconstruction, arbitrary rewiring, automatic annotation review, comparative deployment, reconnect/freshness orchestration, voice/visual grounding and durable multi-camera history remain incomplete goals. Narrow atomic evidence does not establish a complete scenario. See [Capabilities](CAPABILITIES.md).

## Representative advisory workflows

| Scenario | Sanitized prerequisite | Useful public output | Remaining boundary |
|---|---|---|---|
| US-03 Explain a project | Exact version and supplied FLOW/Code/result description | Execution and decision map with unknowns | Supplied inventory alone does not reconstruct all outputs or persistent state |
| US-05 Capture images | Selected ready project and camera; capture policy | Checklist for a bounded image set and identity/readback | Historical 4.0.3 capture evidence does not provide a public capture tool |
| US-08 Bootstrap Detector | Reviewed seed labels and original image basis | Seed/geometry/training/artifact checklist | Full automatic review, retraining and comparison loop remains partial |
| US-12 Smart Mask proposal | Target and reviewed proposal geometry | Explain suggestion versus accepted annotation | Suggestion is not a persisted annotation or an accuracy guarantee |
| US-23 Explain unexpected NOK | Matched image, evaluated results and acceptance rule | Evidence-based hypothesis and smallest discriminating check | A screenshot or static module list cannot establish the full decision path |
| US-34 External sensor Gate | Exact device data, units, identity and freshness rules | PEKAT integration design with invalid/stale handling | Complete sensor-to-Gate execution is planned, not provided |
| US-41 Python compatibility | Exact embedded build, ABI and candidate package | Compatibility assessment and bounded import-test proposal | Arbitrary package installation is not automated |

Version scope: source catalog snapshot with narrow historical 4.0.3 evidence.
Evidence level: reconciled requirements and curated capability conclusions.
Known limitations: catalog statuses are historical upstream statuses; this public
preview provides advice rather than executing those workflows.

## Short Czech and English intents

Use the [decision guide](../knowledge/assistant/DECISION_GUIDE_403.md) for ten practical intents, preflight/readback questions and unsupported variants. Workflow names describe separately authorized upstream implementations; this edition provides advice only.
