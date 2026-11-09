# Scenarios

| Request | Route | Evidence and result |
|---|---|---|
| Design inspection | Vision design and FLOW authoring | Define part, defects, illumination, timing, acceptance and native/ML alternatives; specify unknowns. |
| Explain an existing project | Project analysis and bundled offline skill when available | Separate active topology from registered modules, input evidence and inferred behavior. |
| Code, PTool, Form | Context/GlobalData and PTool references | Draft readable artifacts with state, side effects and exact-version assumptions; do not infer a writer from storage. |
| Detector, Classifier or OCR | Model families and annotation references | Keep annotation artifacts and family semantics separate; prove saved model and selection before claiming success. |
| Troubleshoot | Troubleshooting and log references | Use symptoms, exact environment and discriminating observations; distinguish startup, acquisition and inference. |
| Integrate camera, IO-Link or profiler | [Integration guide](INTEGRATIONS.md) and exact vendor documentation | Specify transport, scaling, validity, freshness and failure behavior; test actual device separately. |
| Live project operation | Discovered external Core or actual host facilities | Only operations supported by the discovered tool and authorized scope; verify target, preflight, effects and readback. |

All scenarios depend on actual available inputs, host capabilities and exact product version. A reference does not itself execute a workflow.
