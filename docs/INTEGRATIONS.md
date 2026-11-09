# Industrial integration

Start with the packaged public bridge for the domain and its source references. Confirm exact product, firmware, PEKAT version, topology and operating mode. Distinguish a successful transport response from valid, current inspection data. Document timeouts, quality, units, source identity and recovery. Existing integrations do not imply a writer in this plugin.

## Basler

Identify exact camera model, area versus line scan, GigE/5GigE/USB transport, sensor mode, triggering and, for line scan, encoder geometry. Resolve pylon and pypylon versions and OS compatibility. GenICam node availability, range, access and dependencies are model/firmware specific: inspect the actual node map and model documentation instead of assuming any feature. Size exposure, transfer, bandwidth and buffering for the actual cycle. Public specialist: [Basler cameras](https://github.com/CZPavel/codex-skill-basler-cameras). Consult current official camera and SDK documentation for the selected model.

## IFM and IO-Link

Identify master and port, sensor model and firmware, IODD identity/revision and master firmware. Decode the IODD-defined PDIn/PDOut bit order, signedness, scale, unit and reserved/invalid states. Keep ISDU parameters separate from cyclic process data and distinguish sensor status, master quality and connection status. Validate decoding using known physical values and timestamps. Public specialist: [IFM IO-Link](https://github.com/CZPavel/codex-skill-ifm-io-link). Consult the exact IODD and official master and sensor documentation.

## KEYENCE

Identify LJ-X8000, LJ-X8000A or LJ-S8000 controller and compatible head, firmware, selected program and interface. Treat command response, profile data and scalar measurement as different contracts. For gap/flush specify coordinate convention, units, sign, calibration, datum, validity and freshness; verify the actual controller program and reference samples. Program selection does not create a measurement program. Do not transfer commands or performance across families. Public specialist: [KEYENCE LJ-X/LJ-S](https://github.com/CZPavel/keyence-ljx-s-skill). Consult exact official controller/head manuals.

Configuration writes, acquisition, motion and output changes require an appropriate verified operation and authorized target. No physical acceptance is asserted here.
