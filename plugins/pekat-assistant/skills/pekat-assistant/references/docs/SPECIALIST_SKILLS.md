# Specialist skills

Specialist sources are optional; no hardware skill or transport is bundled. Use a separately reviewed specialist or exact official documentation for device facts.

| Domain | Required identity | Boundary |
|---|---|---|
| Basler | Model, interface, pylon/pypylon version | Camera features differ from PEKAT provider state |
| IFM / IO-Link | Master, port, device, firmware, IODD revision | Preserve scaling, validity, quality and freshness |
| KEYENCE | Controller family, head, operating mode | LJ-X8000, LJ-X8000A and LJ-S8000 remain distinct |
| MX-G2000 | Platform identity and PEKAT version | Host/service state differs from FLOW |

A reference does not authorize triggering, reset, program changes, firmware, process-data writes or persistent settings. See [bridge topics](../knowledge/INDEX.md).

Reviewed optional public sources:

- [Basler](https://github.com/CZPavel/codex-skill-basler-cameras), snapshot `6ccc9c09845effb5d746041696e556fee7f6b64a`.
- [IFM IO-Link](https://github.com/CZPavel/codex-skill-ifm-io-link), snapshot `4bb94a1910cf71207953c39825acd52b875d21de`.
- [KEYENCE LJ-X/LJ-S](https://github.com/CZPavel/keyence-ljx-s-skill), snapshot `b5c39334479f93109cf2c7283f36e97294dac210`.

Each source has its own MIT license and independent scope. Review upstream changes before replacing these snapshots. The historical legacy PEKAT skill is not the default route.
