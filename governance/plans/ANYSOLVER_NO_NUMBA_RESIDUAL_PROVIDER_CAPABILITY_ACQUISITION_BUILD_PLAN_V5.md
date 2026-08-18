# ANYsolver No-Numba Residual Provider Capability, Acquisition, and Build Plan V5

## 1. Transport-only supersession

This V5 incorporates Provider V4 by exact identity and changes only interstitial
transport sequencing.

- Preserved Provider V4 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN_V4.md`
- Preserved Provider V4 SHA-256:
  `FA20FA71DA3D0956F06515229F4EE8576FC044E13E662F885560A96F3BC05048`
- Governing Stage-P V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`

Provider V4 and all earlier plans remain immutable evidence. Every V4 provision
not explicitly replaced below remains binding. There is no change to science,
signed provenance, trust/acquisition/index sequencing, provider architecture,
wheel route, PB01-PB25 order, PB child timeouts, absolute deadline/reserve,
resource limits, namespaces, Job Object containment, transport security, or
Ubuntu-reproduction claim.

This V5 is plan-only. No artifact, receipt, process, interstitial action, import,
build, stop, export, validation, or lease is created or executed.

## 2. One canonical framed payload contract

Every host/distro boundary uses exactly one binary framing protocol. No producer
may emit an unframed hash, a second payload representation, or trailing text.

Frame bytes are:

1. ASCII magic exactly `ANYSOLVER-PB-HANDOFF/1\n`.
2. ASCII decimal payload length with no sign, whitespace, or leading zero except
   the single value `0`, followed by `\n`.
3. Exactly that many payload bytes.
4. One byte `\n`.
5. ASCII `SHA256 ` followed by exactly 64 lowercase hexadecimal characters and
   `\n`.
6. EOF, with no trailing byte.

Payload bytes are one canonical structured JSON receipt encoded UTF-8 without
BOM using:

- object keys sorted ordinally;
- separators exactly `,` and `:` with no insignificant whitespace;
- ASCII escaping enabled;
- integers only for numeric fields;
- no float, NaN, Infinity, duplicate key, or Unicode-normalization ambiguity;
- one schema field and no embedded self-hash.

The frame digest is SHA-256 of payload bytes only. The digest trailer is framing
integrity, not a second receipt. A consumer validates magic, canonical length,
payload limit, exact read, newline, digest syntax/value, EOF, JSON canonical
re-encoding equality, schema, and semantic fields before trusting the payload.

The structured JSON final is the sole receipt. Its file SHA-256, computed
externally after durable publication, is the sole predecessor hash. V4's raw
`.sha256` receipt path is retired and must not be created.

## 3. Interstitial action I03-04

### 3.1 Identity and order

- Action ID: `PBI03-04-HANDOFF`
- Ordinal position: after PB03 final, before PB04 intent.
- Sole host producer:
  `Q\provider-tools\provider_host_coordinator.py`, operation
  `pb03-pb04-handoff`.
- Sole distro producer:
  `/opt/provider-tools/import_boundary_receipt.py`, an exact registered safety
  descendant of the host producer.
- Predecessor: SHA-256 of durable PB03 `result.json` structured final.
- Hard timeout: 120 seconds.
- Successor: PB04.

This action is not part of PB03 or PB04 and cannot be hidden in either result.

### 3.2 Containment

The dedicated host coordinator process creates and self-assigns to the accepted
Windows Job Object. It starts the accepted watchdog before self-assignment and
launches exactly one `wsl.exe --exec` child in that Job. The distro boundary
producer executes under the accepted network/mount/PID/IPC/UTS namespace,
PDEATHSIG, cgroup, base/background, and all-outcome process-audit contracts.

Timeout/coordinator loss uses the already accepted scoped watchdog containment.
No other distro, process, retry, shell, mount, or transport is allowed.

### 3.3 Paths and schema

Host paths:

- `H\interstitial\PBI03-04-HANDOFF\intent.json.partial|json`;
- transcript/process/Job/watchdog paths under that action root using V4 schemas;
- received acknowledgment frame:
  `H\interstitial\PBI03-04-HANDOFF\ack.frame`;
- sole structured final:
  `H\interstitial\PBI03-04-HANDOFF\result.json.partial|json`.

Distro paths:

- `L/boundaries/PBI03-04-HANDOFF/input.frame`;
- `L/boundaries/PBI03-04-HANDOFF/PB03.result.json`;
- `L/boundaries/PBI03-04-HANDOFF/ack.json.partial|json`.

Final schema:

`anysolver.no_numba_residual.interstitial_pb03_pb04/1`

The final binds action/ordinal, PB03 result path/bytes/hash/schema, exact distro
and import identity, local copied PB03 bytes/hash/path, acknowledgment
payload/frame hashes, host/distro producer hashes, namespace/Job/watchdog/
process/transcript finals, fsync/parent-fsync results, UTC, and success state.

### 3.4 Protocol

The host sends PB03 result bytes to the distro as the canonical frame over the
single child's stdin. The distro validates, durably publishes the exact PB03
structured bytes and acknowledgment, then emits exactly one canonical frame
whose payload is the structured acknowledgment. The host validates the frame,
durably publishes the sole interstitial result, and computes its external file
hash.

PB04 receives one literal predecessor argument: the SHA-256 of the final
`PBI03-04-HANDOFF\result.json`. Its intent binds only that predecessor. PB04 also
validates the distro-local acknowledgment and embedded PB03 hash, but no second
hash is a predecessor.

Any framing, schema, hash, path, fsync, containment, process, or semantic mismatch
stops before PB04. No replay occurs.

## 4. Interstitial action I22-23

### 4.1 Identity and order

- Action ID: `PBI22-23-RECEIVE`
- Ordinal position: after PB22 final, before PB23 intent.
- Sole producer:
  `Q\provider-tools\provider_host_coordinator.py`, operation
  `pb22-pb23-receive`.
- Predecessor: SHA-256 of the PB22 structured result carried and verified in the
  received frame.
- Hard timeout: 120 seconds.
- Successor: PB23.

PB22 remains produced solely by distro-local `build_provider.py` operation
`sync-and-index`. PB22 does not produce a host receipt and is not assigned the
host coordinator.

### 4.2 Containment

PB22's payload/descendants remain inside the accepted Linux namespace/cgroup and
all-outcome audit. After PB22 durably publishes its result, boundary payload, and
evidence index, it emits exactly one canonical frame on its already registered
stdout and exits.

The distinct host receive action runs in its own accepted Windows Job Object with
the accepted watchdog. It launches no new distro build payload. It consumes only
the already closed PB22 stdout transcript/frame and performs local validation/
publication. Its process, Job, watchdog, transcript, exception, and residual
state are durably recorded for every outcome.

### 4.3 Paths and schema

Distro source paths:

- `L/commands/PB22/result.json`;
- `L/boundaries/PB22_to_PB23.json`;
- `L/distro_evidence_index.json`.

Host paths:

- `H\interstitial\PBI22-23-RECEIVE\intent.json.partial|json`;
- `H\interstitial\PBI22-23-RECEIVE\input.frame`;
- transcript/process/Job/watchdog paths under that action root;
- sole structured final:
  `H\interstitial\PBI22-23-RECEIVE\result.json.partial|json`.

Final schema:

`anysolver.no_numba_residual.interstitial_pb22_pb23/1`

The PB22 frame payload is one structured boundary receipt containing PB22 result
bytes/hash/schema, distro evidence-index bytes/hash, output ledger, sync state,
zero task/background proof, namespace/process finals, producer identity, and UTC.
The host final binds the validated frame/payload, PB22 predecessor, closed
transcript/process facts, exact distro identity, producer/Job/watchdog identity,
and publication durability.

### 4.4 Single PB23 predecessor

PB23's sole predecessor is the externally computed SHA-256 of durable
`H\interstitial\PBI22-23-RECEIVE\result.json`.

PB23 intent contains exactly that one predecessor hash. PB22 result/boundary/
index hashes remain embedded evidence within the structured host receipt, not
additional predecessor arguments. PB24 later verifies embedded distro bytes from
the export archive exactly as V4 requires.

Any frame, transcript, PB22 result, schema, index, process, Job/watchdog,
durability, or producer mismatch blocks PB23 without a second receive action.

## 5. PB23 normal-stop and watchdog non-duplication

PB23 retains V4's host-owned normal stop before export. The coordinator durably
publishes these ordered state records:

1. `normal_stop_intent.json` before the sole scoped terminate call.
2. `normal_stop_command.json` after terminate command wait/exit.
3. `normal_stop.json` only after exact builder absent-from-running-list proof,
   zero owned process/residual proof, and all file/parent fsyncs.

`normal_stop.json` schema remains
`anysolver.no_numba_residual.provider_normal_stop/1` and includes the sole
terminate command identity and a boolean `normal_stop_proven=true` only when all
required proof is final.

The watchdog rules are:

- Before a valid durable `normal_stop.json` exists, timeout or coordinator loss
  follows V4's scoped recovery logic, first auditing whether the normal terminate
  was started/completed and never blindly duplicating a completed command.
- Once a valid durable `normal_stop.json` with `normal_stop_proven=true` exists,
  the watchdog is audit-only. It must not invoke `wsl --terminate`, `--shutdown`,
  unregister, or any signal/cleanup action.
- In audit-only mode it verifies the normal-stop receipt hash/schema, builder
  stopped state, Job/process residuals, export operation identity if started,
  and publishes a no-action watchdog result.
- Any post-proof running/residual contradiction is infrastructure failure, but it
  does not authorize a second terminate.

PB23 may begin export only after the valid durable normal-stop proof. PB24's
validation/promotion ownership remains unchanged.

## 6. Interstitial ordinal and deadline integration

The provider campaign order is now:

`PB01, PB02, PB03, PBI03-04-HANDOFF, PB04 ... PB22, PBI22-23-RECEIVE, PB23, PB24, PB25`.

The two interstitial actions participate in the same absolute 90-minute deadline
and 600-second reserve. Before either action or successor launch:

`remaining_seconds >= action_timeout_seconds + 600`.

Each interstitial final becomes the sole next predecessor as defined above.
Their resource use remains inside the accepted combined envelope. First failure
stops; no retry, replay, fallback framing, or alternate receipt exists.

## 7. Unchanged boundaries

V4's T-to-R-to-I authority, verifier bootstrap, signed Canonical and
`actions/python-versions` provenance, local distro evidence/export handoff,
content-addressed PB producers, namespace/background audits, sole ANYsolver wheel
route, PB24 validation/atomic promotion, Defender-safe transport, resources,
preservation, and Ubuntu-reproduction claim remain unchanged.

No action or lease is authorized. Both interstitial producers, schemas, frames,
paths, command rows, and hashes remain future independently reviewed artifacts.
