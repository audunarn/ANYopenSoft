# ANYsolver No-Numba Residual Provider Capability, Acquisition, and Build Plan V6

## 1. Transport-only supersession

This V6 incorporates Provider V5 by exact identity and changes only PB22 host
transport and terminate ownership.

- Preserved Provider V5 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN_V5.md`
- Preserved Provider V5 SHA-256:
  `0579AE6C2936D99CC66FC1534CB640A7CDEDF770E37A352C08AF8F20B0FDD7ED`
- Governing Stage-P V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`

Provider V5 and all earlier plans remain immutable evidence. Every V5 provision
not explicitly replaced below remains binding. There is no science, provenance,
provider, wheel, semantic PB, timeout, deadline, resource, namespace, framing,
promotion, transport-security, or claim-boundary change.

This V6 is plan-only. No artifact, transport, process, claim, terminate, build,
export, action, or lease is created or executed.

## 2. PB22 host transport action

### 2.1 Identity and semantic ownership

A new contained host action wraps the exact PB22 `wsl.exe` invocation:

- Action ID: `PBT22-HOST-TRANSPORT`
- Ordinal position: after PB21 final and around the one PB22 semantic invocation;
  before `PBI22-23-RECEIVE`.
- Sole producer:
  `Q\provider-tools\provider_host_transport.py`, operation
  `invoke-and-capture-pb22`.
- Semantic child producer:
  distro-local `build_provider.py`, operation `sync-and-index`, remains the sole
  producer of PB22 semantic result/boundary/index.
- Host transport predecessor:
  SHA-256 of durable PB21 result.
- PB22 semantic predecessor:
  the same PB21 result hash, passed literally through the accepted command row.
- Hard timeout: PB22's accepted 180-second child timeout plus a frozen
  60-second host capture/finalization allowance, while still satisfying the
  shared deadline and 600-second reserve.

`provider_host_transport.py` cannot create or alter PB22 semantic JSON. It owns
only Windows invocation, containment, capture, framing validation, transcript/
process evidence, and its host transport result.

### 2.2 Exact invocation and containment

The transport producer launches exactly one accepted absolute `wsl.exe`
invocation with literal distribution, `--exec`, namespace wrapper, lane/build
Python, content-addressed `build_provider.py`, operation `sync-and-index`, PB21
predecessor hash, command-manifest hash, and distro-local output paths.

The transport process creates and self-assigns to the accepted Windows Job
Object, starts the accepted watchdog before self-assignment, and assigns the
single `wsl.exe` child tree to the Job. Inside the distro, PB22 remains confined
by V5's mount/PID/network/IPC/UTS namespaces, cgroup, PDEATHSIG, background
audits, and all-outcome process finalization.

No shell, host mount, second WSL command, semantic rewrite, retry, or alternate
producer is allowed.

### 2.3 Durable capture paths and schema

Host action root:

`H\host-transport\PBT22-HOST-TRANSPORT`

Registered paths:

- `intent.json.partial|json`;
- `transcript\stdout.bin`;
- `transcript\stderr.bin`;
- `transcript\index.json.partial|json`;
- `process\job_object.json.partial|json`;
- `process\start.json.partial|json`;
- `process\termination.json.partial|json`;
- `process\final.json.partial|json`;
- `watchdog\intent.json.partial|json`;
- `watchdog\transcript\stdout.bin` and `stderr.bin`;
- `watchdog\process.json.partial|json`;
- `watchdog\result.json.partial|json`;
- canonical captured frame `pb22.frame`;
- `result.json.partial|json`.

Result schema:

`anysolver.no_numba_residual.pb22_host_transport/1`

Before launch, intent and parent are durably flushed/fsynced. During launch,
stdout and stderr are captured as binary exclusive files. After child exit, the
producer flushes/fsyncs/closes both streams and parents before parsing stdout.

The stdout file must contain exactly one V5 canonical framed structured PB22
boundary payload and EOF. The producer validates framing, payload digest,
canonical JSON, PB22 result/boundary/index identities, semantic producer hash,
PB21 predecessor, command ordinal, distro identity, and zero trailing output.
It then durably publishes transcript/process/watchdog evidence and one transport
result. Every normal, diagnostic, launch-error, signal, timeout, exception, and
coordinator-loss outcome publishes all available truth and preserves partials.

The externally computed SHA-256 of durable
`H\host-transport\PBT22-HOST-TRANSPORT\result.json` is the sole transport result
hash.

## 3. Revised PBI22-23 receive action

`PBI22-23-RECEIVE` remains a distinct host action with the same producer, schema,
timeout, Job/watchdog containment, and final path from V5. Its inputs are narrowed
to exactly:

1. Durable `PBT22-HOST-TRANSPORT\result.json` and its external SHA-256.
2. Durable captured `PBT22-HOST-TRANSPORT\pb22.frame`.
3. The transport result's transcript/process/watchdog finals.

It does not consume live PB22 stdout, invoke WSL, read a distro path, or accept a
separate PB22 host receipt.

Its sole predecessor is the PBT22 host transport result hash. It revalidates the
captured frame and embedded PB22 result/boundary/index evidence, then publishes
the one V5 structured `PBI22-23-RECEIVE\result.json` final.

PB23's sole predecessor remains the SHA-256 of that PBI final. PB22 and PBT22
hashes are embedded evidence, not additional PB23 predecessor arguments.

The campaign order at this boundary is:

`PB21 -> PBT22-HOST-TRANSPORT[one PB22 semantic child] -> PBI22-23-RECEIVE -> PB23`.

## 4. Shared exclusive terminate claim

### 4.1 Single campaign primitive

All coordinator and watchdog paths for the exact builder distro share one durable
claim path:

`H\termination\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1\terminate_claim.json`

Claim schema:

`anysolver.no_numba_residual.provider_terminate_claim/1`

The claim is a fixed canonical structured JSON document created directly with
Windows `CreateFileW(..., CREATE_NEW, FILE_FLAG_WRITE_THROUGH)` semantics. It is
never created through a replaceable partial. The successful creator writes the
complete bounded document, calls `FlushFileBuffers`, closes, reopens, validates
canonical bytes/schema, and durably flushes the parent directory through the
accepted Windows directory-sync primitive before any terminate command.

Required fields include campaign/provider/distro IDs, operation/action ID,
claimant role (`coordinator` or `watchdog`), claimant PID/start identity and
producer hash, reason (`normal_stop`, `timeout`, or `coordinator_loss`), PB/
interstitial predecessor, UTC/monotonic time, deadline, exact terminate argv,
and one unique claim ID. It contains no self-hash.

The external SHA-256 of the closed claim is recorded in every subsequent
terminate/audit result.

### 4.2 Claim rule

Only the actor whose `CREATE_NEW` succeeds and whose claim is durably validated
may execute the one exact scoped:

`wsl.exe --terminate ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`.

If the claim path exists for any reason, every other coordinator/watchdog actor:

- must not terminate, shutdown, unregister, signal, replace, delete, truncate,
  repair, or reclaim;
- validates and records the existing bytes if readable;
- audits/waits for process/distro state within its frozen timeout;
- publishes an audit-only or infrastructure-failure result;
- stops without a second terminate.

An empty, partial, malformed, unreadable, unflushed, foreign, or mismatched claim
still blocks every other actor from terminate authority. It is preserved as
first-failure evidence and makes state unproven.

The claim is never released, deleted, renamed, or reused during the campaign.
There can be at most one successful terminate claimant and at most one terminate
invocation for the builder distro.

### 4.3 Claimant result paths

Under the claim directory:

- `claimant_intent.json.partial|json`;
- `terminate_transcript\stdout.bin` and `stderr.bin`;
- `terminate_transcript\index.json.partial|json`;
- `terminate_process\start.json.partial|json`;
- `terminate_process\final.json.partial|json`;
- `distro_state.json.partial|json`;
- `claimant_result.json.partial|json`.

Schemas:

- `anysolver.no_numba_residual.provider_terminate_claimant_result/1`;
- existing transcript/process/distro-state schemas from V5.

The successful claimant records exact claim hash, one terminate command,
wait/exit, scoped running-state audits, Windows Job/process residuals, and
stopped/unproven result. Non-claimants record the existing claim identity and
their audit-only wait/state result under their own action watchdog paths; they do
not write claimant paths.

## 5. PB23 normal stop and watchdog behavior

PB23 normal coordinator attempts the shared claim with reason `normal_stop`.
Only successful durable claim ownership permits its sole terminate command.

The watchdog may attempt a claim for timeout/coordinator loss only when no claim
exists. If coordinator already owns any claim, the watchdog is audit/wait-only,
even if durable normal-stop proof is not yet complete. It cannot issue a second
terminate to repair missing proof.

After the successful claimant proves stopped state, PB23 publishes V5's durable
`normal_stop.json`. Once that proof is valid, every watchdog remains audit-only
as already accepted. Contradictory running state is infrastructure failure, not
new terminate authority.

The same shared claim rule applies to PB03/PB23 import/export timeout and every
host interstitial/transport coordinator-loss path that V5 allowed to terminate.
An earlier claim means the campaign is terminal and no later provider build step
is eligible.

## 6. Ordinal, deadline, and producer integration

`PBT22-HOST-TRANSPORT` has one ordinal and one predecessor/result. It participates
in the existing absolute 90-minute deadline and 600-second reserve. Before its
launch:

`remaining_seconds >= 240 + 600`.

The 240 seconds comprise the PB22 semantic timeout and host finalization
allowance; no hidden extension is permitted. `PBI22-23-RECEIVE` retains its
120-second timeout and same reserve gate.

Future artifact/command manifests bind exact producer/interpreter hashes for
`provider_host_transport.py`, coordinator, watchdog, PB22 `build_provider.py`,
Job Object implementation, claim primitive, paths, schemas, and argv. Any
producer/hash/operation/predecessor mismatch is terminal.

## 7. Unchanged boundaries

V5's canonical framing, PBI03-04 action, semantic PB22 output, PBI22-23 schema,
single PB23 predecessor, host-owned stop/export, PB24 validation/atomic
promotion, T-to-R-to-I sequencing, signed provenance, provider/wheel/science
scope, namespaces, process evidence, resources, Defender-safe transport, and
Ubuntu-reproduction claim remain unchanged.

No action or lease is authorized. The new host transport, claim primitive,
schemas, paths, producers, and command rows remain future independently reviewed
artifacts.
