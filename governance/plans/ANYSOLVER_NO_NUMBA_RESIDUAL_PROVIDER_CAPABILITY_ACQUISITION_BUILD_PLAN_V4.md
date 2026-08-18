# ANYsolver No-Numba Residual Provider Capability, Acquisition, and Build Plan V4

## 1. Mechanical supersession

This V4 incorporates Provider V3 by exact identity and changes only the four
sequencing contracts directed by review.

- Preserved Provider V3 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN_V3.md`
- Preserved Provider V3 SHA-256:
  `5337C626FEC170B6A4CD639D9119A03C8CCEBDE8400F8E9C8D0DFF48F390F88B`
- Governing Stage-P V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`

Provider V3 and all earlier plans remain immutable evidence. Every V3 provision
not explicitly superseded below remains binding. There is no science, signed
provenance, provider architecture, wheel route, PB count/order, child timeout,
absolute deadline, reserve, resource, transport, or result-claim change.

This is plan-only. No artifact, manifest, receipt, producer, distro, namespace,
process, Job Object, watchdog, acquisition, build, export, action, or lease is
created or executed.

## 2. Exact pre-I receipt sequence

Every action before Layer I is an ordinal operation with exactly one
content-addressed producer, one authority class, one hard timeout, one unique
receipt family, and one predecessor final hash. No operation may be skipped,
reordered, replayed, retried, or merged with another operation.

### 2.1 Registered pre-I producers

- `Q\provider-tools\freeze_provider_trust_inputs.py`
- `Q\provider-tools\acquire_provider_inputs.py`
- `Q\provider-tools\validate_verifier_bootstrap.py`
- `Q\provider-tools\verify_canonical_signature.py`
- `Q\provider-tools\validate_provider_inputs.py`
- `Q\provider-tools\verify_actions_python_attestation.py`
- `Q\provider-tools\create_anysolver_source_archive.py`
- `Q\provider-tools\freeze_verified_build_inputs.py`

Each future producer path, bytes, SHA-256, interpreter, AST/compile-only result,
argv schema, read/write roots, descendant policy, and process contract must be
accepted before its authority stage. A producer receives the predecessor hash as
a literal argument and records it in intent and result.

### 2.2 Authority classes

- `META`: primary-source metadata only; network read; no payload acquisition.
- `ACQUIRE`: one expected payload acquisition; network read; no execution of
  acquired bytes.
- `VERIFY`: offline static/signature/archive/attestation validation only.
- `SOURCE`: exact local Git-object archive and source receipt only.
- `INDEX`: offline immutable Layer-I freeze only.

Each authority is separately reviewed. No authority class implies another.

### 2.3 Fixed bootstrap ordinals

| Ordinal | ID | Producer | Authority | Timeout | Required final |
| ---: | --- | --- | --- | ---: | --- |
| 1 | `PREI-T01` | `freeze_provider_trust_inputs.py` | META | 300 s | Layer-T final |
| 2 | `PREI-R01-VERIFIER-ACQUIRE` | `acquire_provider_inputs.py` | ACQUIRE | 300 s | verifier acquisition success |
| 3 | `PREI-R02-KEYRING-ACQUIRE` | `acquire_provider_inputs.py` | ACQUIRE | 300 s | keyring acquisition success |
| 4 | `PREI-R03-VERIFIER-BOOTSTRAP` | `validate_verifier_bootstrap.py` | VERIFY | 300 s | verifier-bootstrap receipt |
| 5 | `PREI-R04-ROOTFS-SIGNED-METADATA` | `acquire_provider_inputs.py` | ACQUIRE | 300 s | checksum/signature acquisitions |
| 6 | `PREI-R05-ROOTFS-SIGNATURE` | `verify_canonical_signature.py` | VERIFY | 180 s | Canonical rootfs signature receipt |
| 7 | `PREI-R06-ROOTFS-ACQUIRE` | `acquire_provider_inputs.py` | ACQUIRE | 900 s | rootfs acquisition success |
| 8 | `PREI-R07-ROOTFS-VALIDATE` | `validate_provider_inputs.py` | VERIFY | 600 s | rootfs archive validation receipt |

Ordinal 1 binds an externally accepted governing-plan-envelope hash. Every later
fixed ordinal binds the immediately preceding final result hash.

### 2.4 Deterministic Layer-T row ordinals

After fixed ordinal 8, each Layer-T expected row is expanded into exact receipt
commands before any execution. Layer T freezes `row_ordinal`, `artifact_id`,
action IDs, producer hash, authority, timeout, predecessor ID, expected paths,
and schemas. Rows are sorted by these immutable groups and then ASCII artifact
ID:

1. Ubuntu `InRelease` acquisition, signature verification, Packages-index
   acquisition/validation, and each `.deb` acquisition/validation.
2. `actions/python-versions` release metadata, digest/attestation verification,
   archive acquisition, and archive validation for 3.11.15, 3.12.13, 3.13.14.
3. PyPI, sibling, build-stack, lane-lock, and wheel metadata/acquisition/
   validation rows.

Exact row-action bindings:

| Row action | Producer | Authority | Timeout |
| --- | --- | --- | ---: |
| primary metadata freeze | `freeze_provider_trust_inputs.py` | META | 300 s |
| payload acquisition | `acquire_provider_inputs.py` | ACQUIRE | Layer-T exact value, at most 1,800 s |
| Canonical signature | `verify_canonical_signature.py` | VERIFY | 180 s |
| archive/package/wheel validation | `validate_provider_inputs.py` | VERIFY | Layer-T exact value, at most 600 s |
| actions digest/attestation | `verify_actions_python_attestation.py` | VERIFY | 300 s |

Every expanded action gets one monotonically increasing `pre_i_ordinal`. Its
predecessor is exactly the immediately previous accepted result hash, including
between row groups. Layer T contains the complete expanded ledger before the
first acquisition and cannot be amended in place.

### 2.5 Source and index tail

After the final expanded Layer-T row:

| ID | Producer | Authority | Timeout | Predecessor/final |
| --- | --- | --- | ---: | --- |
| `PREI-SOURCE` | `create_anysolver_source_archive.py` | SOURCE | 300 s | previous row result -> exact source receipt |
| `PREI-INDEX` | `freeze_verified_build_inputs.py` | INDEX | 300 s | source receipt result -> Layer-I final |

`PREI-INDEX` validates every expected ordinal, predecessor hash, receipt schema,
producer hash, authority, timeout, success/preserved-failure state, input path,
and signed chain. Any missing, duplicate, out-of-order, mismatched, or failed
required receipt blocks Layer I.

### 2.6 Unique pre-I evidence

For pre-I action ID `X`:

- `Q\provider-pre-i\X\intent.json.partial|json`;
- `Q\provider-pre-i\X\transcript\stdout.bin` and `stderr.bin`;
- `Q\provider-pre-i\X\transcript\index.json.partial|json`;
- `Q\provider-pre-i\X\process\start.json.partial|json`;
- `Q\provider-pre-i\X\process\termination.json.partial|json`;
- `Q\provider-pre-i\X\process\final.json.partial|json`;
- `Q\provider-pre-i\X\result.json.partial|json`;
- action-specific immutable acquisition/signature/archive/source/index receipt
  partial/final paths from V3.

Every outcome uses V3 all-outcome finalization. Only a final, policy-matching,
zero-residual result can become the next predecessor. Failure is preserved and
stops the sequence.

## 3. PB03 to PB04 durable boundary

PB03 remains the host coordinator import operation. It produces on the host:

- `H\host-commands\PB03\result.json`;
- `H\host-commands\PB03\result.json.sha256` as a separate externally computed
  fixed 64-hex receipt, schema
  `anysolver.no_numba_residual.boundary_hash_receipt/1`;
- full Job Object/watchdog/process/import state from V3.

After PB03 finalization, the exact accepted PB03 result SHA-256 is passed as a
literal argument to the first distro-local boundary producer already embedded in
the seed:

`/opt/provider-tools/import_boundary_receipt.py`

The host coordinator streams the exact PB03 result bytes over the direct
`wsl.exe --exec` child's stdin. No shell, host mount, relative path, encoding, or
reconstruction is allowed. The boundary producer:

1. Requires the literal expected byte count and SHA-256.
2. Reads exactly that many bytes and rejects trailing data.
3. Verifies SHA-256 and schema.
4. Writes/fsyncs/atomically publishes
   `L/boundaries/PB03.host_result.json`.
5. Writes/fsyncs/atomically publishes
   `L/boundaries/PB03_to_PB04.json`, schema
   `anysolver.no_numba_residual.pb_boundary_handoff/1`, binding PB03 hash,
   provider/distro/import identities, local path/hash, producer hash, and UTC.
6. Fsyncs both parent directories.
7. Emits only the canonical handoff SHA-256 line to stdout.

The host records the child transcript/process result and ordinally compares the
emitted hash to its own hash of the durably received handoff bytes returned over
stdout as a separately framed payload. PB04 launches only after independent
acceptance of this host/distro agreement. PB04's predecessor is the exact local
`PB03_to_PB04.json` hash, and PB04 revalidates the embedded PB03 result hash
before any isolation/build action.

Any transport, framing, hash, schema, fsync, process, or agreement failure
preserves both sides and blocks PB04. There is no replay.

## 4. PB22 to PB23 durable boundary

PB22 is renamed semantically from `sync-stop-and-index` to
`sync-and-index`. It cannot and does not stop WSL.

PB22 completes all distro-local sync, background/process/network/mount audits,
environment/build reports, and `L/distro_evidence_index.json`. It then publishes:

- `L/commands/PB22/result.json`;
- `L/boundaries/PB22_to_PB23.json`, schema
  `anysolver.no_numba_residual.pb_boundary_handoff/1`, binding PB22 result hash,
  distro evidence-index hash, provider output hash ledger, sync results, zero
  task-process/background proof, producer hash, and UTC.

After both files and parents are fsynced, PB22 emits one strictly framed boundary
payload and SHA-256 over stdout. The host coordinator captures exact bytes in its
exclusive PB22 transcript, validates framing/hash/schema, and durably publishes:

- `H\boundaries\PB22_to_PB23.json`;
- `H\boundaries\PB22_to_PB23.host_receipt.json`, schema
  `anysolver.no_numba_residual.pb_boundary_host_receipt/1`, binding captured
  bytes/hash, `wsl.exe` exit, transcript/process hashes, distro identity, and UTC.

PB23's predecessor is the host receipt hash plus the embedded PB22 boundary hash.
After export, PB24 must locate the original distro-local PB22 boundary/result in
the archive and prove byte/hash equality with the host copies. A mismatch
invalidates the export and provider.

## 5. PB23 host-owned normal stop and export

PB23 remains produced by `provider_host_coordinator.py` with
`provider_host_watchdog.py` as its sole safety descendant. It begins only after
the PB22 host boundary receipt is final and accepted.

PB23's exact normal transition is:

1. Revalidate PB22 host receipt, builder name/import path, Job Object/watchdog,
   deadline/reserve, and no unexpected Windows/task process.
2. Invoke one read-only in-distro final status command under the accepted
   namespace/audit contract; require PB22 index/hash, zero task child/background,
   and no mutable write after PB22.
3. Exit that status command and wait/reap it.
4. Invoke exactly
   `wsl.exe --terminate ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`
   under the PB23 Job Object/watchdog contract.
5. Wait for terminate exit.
6. Repeatedly inspect only the exact scoped running-state command within the
   frozen PB23 child timeout, without relaunching termination.
7. Require the exact builder absent from `wsl --list --running` and prove no
   owned Windows `wsl.exe`, distro, namespace, task, or background process
   remains.
8. Durably publish `PB23.normal_stop.json`, schema
   `anysolver.no_numba_residual.provider_normal_stop/1`, with command/process/
   watchdog/wait/stopped/residual proof.
9. Only after stopped proof, invoke one exact `wsl.exe --export` to the fresh
   registered provider-builder export partial.
10. Wait/reap export, close/fsync the partial, record bytes/hash, and publish
    PB23 result. PB23 never renames the partial to final.

Normal stop is host-owned and watchdog-covered. PB22 never calls terminate,
shutdown, unregister, or stop. On timeout/coordinator loss, V3's watchdog uses
the same single scoped terminate rule and residual proof. It never calls
`--shutdown`, unregisters, targets another distro, retries terminate, or cleans
state.

If stopped state, export completion, partial durability, or zero residual cannot
be proven, PB23 fails and preserves the partial/distro/evidence.

## 6. PB24 validation and atomic promotion

PB24's sole producer remains `validate_provider_export.py`. It alone owns
validation and promotion of the PB23 export partial.

PB24 must:

1. Require PB23 final, normal-stop receipt, watchdog final, PB22 host receipt,
   export partial, and no pre-existing export final.
2. Recompute export partial bytes/SHA-256 and compare to PB23.
3. Perform complete safe tar/member validation and provider identity checks.
4. Locate and validate distro-local PB22 result, PB22 boundary, evidence index,
   all indexed receipts/reports/output hashes, and exact equality with durable
   host boundary copies.
5. Extract only registered handoff evidence through the V3 safe exclusive
   mechanism and verify every extracted hash.
6. Validate provider rootfs, lane environments, package/ELF closure, wheel,
   environment reports, no host mounts/routes/credentials, and output claim
   boundary.
7. Flush and fsync the export partial and its parent directory.
8. Durably publish a pre-promotion validation receipt, schema
   `anysolver.no_numba_residual.provider_export_validation/1`.
9. Atomically rename the same-volume export partial to the exact final provider
   archive path using one no-overwrite promotion.
10. Fsync the final file and parent directory.
11. Recompute final bytes/SHA-256 and require equality to the validated partial.
12. Durably publish a promotion receipt, schema
    `anysolver.no_numba_residual.provider_export_promotion/1`, linking PB22,
    PB23, validation, old partial identity, final identity, fsync/rename results,
    producer hash, process audit, and UTC.
13. Publish PB24 result only after all preceding finals are durable.

PB24 never modifies archive bytes. Any validation, extraction, fsync, rename,
rehash, handoff, or evidence mismatch fails closed. The partial/final and all
receipts remain preserved as truthful state; no retry or cleanup occurs.

PB25 consumes only the PB24 final archive and promotion receipt to create the
unchanged provider capability/index bundle. PB25 has no export-validation or
promotion authority.

## 7. Producer bindings added by V4

The following additional future artifacts are registered and must be
content-addressed before use:

- `Q\provider-tools\import_boundary_receipt.py`, producer only for the PB03 to
  PB04 distro-local handoff;
- existing `provider_host_coordinator.py`, producer for host boundary receipts,
  PB23 normal stop/export, and no other PB ordinal;
- existing `build_provider.py` operation `sync-and-index`, producer for PB22 and
  its distro-local boundary;
- existing `validate_provider_export.py`, sole PB24 validator/promoter.

Their paths/hashes, literal argv, stdin/stdout framing, schemas, descendants,
read/write roots, Job Object/namespace behavior, timeouts, and all-outcome
evidence are frozen in Layer I and the PB command manifest before execution.

## 8. Unchanged boundaries

Pre-I actions and PB01-PB25 retain the accepted absolute 90-minute provider-build
deadline where applicable, exact child timeouts, 600-second reserve, ordinal
first-failure behavior, namespaces, process/background audits, Windows Job
Object/watchdog containment, signed provenance, sole in-builder ANYsolver wheel
route, resource limits, Defender-safe transport, and Ubuntu-reproduction claim.

No action or lease is authorized. All manifests, producers, receipts, boundary
transports, builder/provider artifacts, and command packets remain future
independently reviewed prerequisites.
