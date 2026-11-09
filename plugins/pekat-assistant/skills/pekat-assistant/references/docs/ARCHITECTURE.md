# Architecture

Human documentation, topic-oriented knowledge and a Codex skill share the same advisory boundaries. Custom GPT guidance uses curated public knowledge. Packaging produces standalone views and adds no control capability.

The skill follows intent → exact version/model → relevant topic → evidence-qualified advice. Device-specific facts belong to reviewed specialist sources; PEKAT reasoning maps valid, fresh information into an inspection design.

Historical upstream analysis and accepted changes used separate interfaces. This preview publishes concepts, not those parsers, controllers or contracts. See [Evidence model](EVIDENCE_MODEL.md).

## Control architecture concept

```text
User / chat / agent
       |
PEKAT Assistant knowledge + capability routing
       |
Typed Core + safe transaction boundary
       |
Supported, exact-version PEKAT interfaces
       |
PEKAT VISION
```

The public preview supplies the knowledge and routing layer. The lower control
layers describe an engineering architecture; they are not included dependencies.
A typed operation constrains target identity, parameters, preconditions and
expected readback. Knowledge that an operation exists is separate from permission
and a supported executable implementation for that exact version.

For an independently supplied and authorized control implementation, use
inspect → plan → bounded action → durable readback → verify, with restoration
of temporary state where supported. A transaction cannot guarantee crash recovery
or physical safety merely because its normal path was tested. Human approval and
site policy remain an explicit boundary for target, side effects and deployment.

A future official PEKAT MCP could be a transport/adapter over this same typed
boundary. It is a possible future integration, not a current dependency or a
claim that an official MCP is available. Chat, voice or a different transport
must preserve the same capability and policy boundaries.

Version scope: architecture concept; historical runtime conclusions exact 4.0.3.
Evidence level: curated engineering synthesis, not a new runtime verification.
Known limitations: no public controller, generic writer or crash-recovery engine.
