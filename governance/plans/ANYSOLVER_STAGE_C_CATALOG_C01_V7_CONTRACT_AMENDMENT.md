# ANYsolver Stage-C Catalog C01 V7 Contract Amendment

## 1. Purpose, authority boundary, and frozen predecessors

This is a plan-only amendment to accepted catalog correction plan
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_AWARE_C01_CORRECTION_PLAN.md`,
SHA-256 `D5FBB6527192026CA6923751B16E96731786AAFE1CC9C37CEBCE8820C49EE88E`.
It repairs contract defects found during static review without executing Stage C
or changing the accepted scientific/provider scope.

The following artifacts are immutable rejected/review evidence and MUST NOT be
overwritten, deleted, renamed, repaired, imported, or executed:

- V5 packet `69F1ACD2B4549148FEEC1DD39B9AD619CF845D2D90B0B68EF4A97A350866A61B`;
- V5 executor `F27BCA7B8910CDC200E672A1391079C2A62100BA4709360C3B1AFC8856965B6C`;
- V5 focused test `6224E0B5274A561C85E990EDFF5FB8F9C60B94F5158F3129C130B9E0A2284620`;
- V6 packet `BCFFE9CF6CFB2CAD42354E4DE4B0A937B77C5986A8B83F4CBDEFC52F57509E0A`;
- V6 executor `F47F63D6CD8658D80C207F110E7926FA9EF3CA39D0F853E42009EAF8EA825125`;
- V6 focused test `6468E2F223EE8AD800FF0C7DA6BAF035A1F47C21BA1F67F295C8E5764BD79A4A`;
- immutable V4 evidence root
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-dc0e416339ccf5bb`.

No execution, import, WinTrust/catalog API, WSL query, evidence-root creation,
PERF action, Git action, cleanup, network/provider action, package build, tag,
release, or publication is authorized by this amendment.

## 2. Exact future successor paths and CreateNew rule

Only after independent acceptance of this amendment may one correction phase
create these three absent successor paths:

1. `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V7.md`
2. `C:\Github\ANYopenSoft\governance\tools\anysolver_no_numba_residual_stage_c_host_executor_v7.py`
3. `C:\Github\ANYopenSoft\governance\tests\test_anysolver_stage_c_catalog_c01_contract_v3.py`

Each target must be absent before creation. The executor successor is derived
from exact frozen V6 executor bytes and corrected at the new path; its internal
`EXECUTOR_PATH`, packet path, and focused-test path bind the three V7 successors.
The V6 canonical executor/test paths remain byte-exact. No fourth source,
packet, fixture, manifest, ledger, or evidence path is owned by the correction.

## 3. Accepted graph contracts remain `/1`

V7 MUST restore and retain, without schema expansion:

- manifest schema
  `anysolver.no_numba_residual.stage_c_v4_immutable_evidence_manifest/1`;
- identity-ledger schema
  `anysolver.no_numba_residual.stage_c_catalog_c01_identity_ledger/1`;
- the accepted V5 manifest top-level fields and nine identity-row labels/order;
- ledger labels/order `correction_plan`, `packet_v5`, `executor_v5`,
  `focused_catalog_test`, `v4_manifest`, `interpreter_receipt`.

Those ledger labels are frozen compatibility labels. For a separately accepted
V7 launch ledger, their paths/hashes bind the accepted V7 successor packet,
executor, and focused test while the labels remain unchanged. No `/2`, V6/V7
row-label migration, top-level manifest field, or implicit document migration
is permitted by this task. Any future schema migration requires its own plan.

Required manifest and ledger are currently absent. Source and tests MUST fail
closed on absence. This amendment does not create them.

## 4. Exact historical identity bindings without schema expansion

The existing manifest `/1` `identity_rows` array is label-specific. Freeze these
exact canonical JSON pointers and zero-based positions:

- `v4_executor`: `/identity_rows/1`;
- `v4_held_member`: `/identity_rows/5`.

The selected row must have exactly `row_id`, `path`, `bytes`, `sha256`; its
`row_id` must equal the pointer label. `v4_executor` must equal accepted hash
`9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D`.
`v4_held_member` must use canonical path
`C:\WINDOWS\system32\wsl.exe`; its bytes/hash are supplied only by the accepted
content-addressed manifest and ledger. These two historical targets are not
live-reopened because the executor and OS member can legitimately have changed.
All other identity rows are direct-file reopened and rehashed.

The validator MUST NOT recursively search arbitrary receipt payloads. It checks
the exact row pointer, label, canonical path, bytes/hash shape, accepted manifest
hash, and external accepted ledger hash. Duplicate labels, paths, bytes/hash
identities, pointer displacement, or a held-member path other than the frozen
System32 path fails closed. Exact 11 entries, 8 directories, 3 files, empty
partials, and the accepted canonical recursive snapshot digest remain mandatory
under `/1`; V7 may not add snapshot fields absent from the accepted schema.

## 5. C01 receipt state machine and exact order

C01 uses one durable chronology owner: `_GlobalReceiptChain`. The prior
independent local C01 `head`, `sequence`, and committed-chain state are removed.
A C01 context may hold only immutable authority, directory, raw event buffer,
and a list of globally committed C01 node identities derived from the global
chain. `_v5_c01_emit` promotes/reopens one artifact and asks the global owner to
register it. On success it derives the C01 view from the committed global node;
there is no second local head commit. On failure, global durable head and the
promoted-but-unregistered identity remain truthful and no ordinary successor is
allowed.

Exact C01 ordering is:

1. trust intent;
2. one embedded VERIFY/CLOSE attempt;
3. either embedded failure/success, or classified `TRUST_E_NOSIGNATURE` then
   catalog fallback intent and hash/enumeration evidence;
4. for each deterministically ordered catalog candidate: candidate intent,
   one VERIFY/CLOSE attempt, signer policy, candidate held-handle close, then
   candidate result/failure before the next candidate intent;
5. catalog-context release outcome;
6. trust success or trust failure.

Candidate intent/result pairs may not be batched as all intents then all results.
A result is impossible before its candidate handle close. Catalog-context
release is its own classified raw event and final trust success/failure carries
that proof; it is not retroactively copied into already promoted candidate
results.

Every raw event has one fixed `/1` schema already authorized by the accepted
plan, explicit `outcome` in `intent|success|classified_non_success|failure`, raw
API call data, primary error, ordered secondary errors, and ownership proof.
No new C01 schema version is introduced. Receipt failure classification uses
explicit outcome, not suffix or mere key presence.

## 6. WinTrust, hash, enumeration, and close truth

Each WinTrust attempt records both signed `LONG` (`status_signed`) and unsigned
32-bit (`status_u32`, uppercase hex) VERIFY/CLOSE values. Decisions compare the
unsigned value; raw signed values are never discarded. Exactly one embedded
VERIFY occurs. Provider extraction and chain validation happen before embedded
success publication. VERIFY remains primary if CLOSE also fails; CLOSE is
ordered secondary and always fail-closed.

Catalog hash records exact 32-byte size/fill calls, flags, last errors, member
hash, saved offset, restore call, post-restore offset, and equality. Restore or
post-restore query failure is a composite fatal hash outcome even when sizing or
fill already failed; neither primary nor restore evidence may be lost.

Enumeration records each call's input previous context, returned context,
last-error, ownership transfer, descriptor extraction, and release. A previous
HCATINFO is consumed exactly once by the next enumeration call and is never
double-released. Clean end is distinguished from API failure. Acquire/release
context outcomes are explicit. Every opened candidate and admin/catalog context
has exactly one all-outcome close/release proof. Rollback and close errors are
ordered secondary evidence and stop acceptance.

Raw-event buffering is transactional: a copied prefix is deleted only after
artifact promotion, held direct-file reopen, global-node promotion/reopen, and
single-owner chain commit. Pre-promotion or registration loss retains the full
buffer in mandatory fatal truth.

## 7. Contained-run lanes, publication, and immutable fatal exits

`run_id` is the lowercase 64-hex SHA-256 of LF-free canonical material using the
accepted V7 packet SHA as its version field. Consumer binding and
`attempted_consumer_id` are resolved before artifact reopen and retained through
all registration-loss branches.

Pre-Job ordinary publication has exact durable prefixes:

- 0 finals: neither process nor Job failure final exists;
- 1 final: process failure exists; Job failure does not;
- 2 finals: process then Job failure both exist.

The final count is derived from reopened promoted finals and their committed
global consumer nodes, never a mutable caller integer. A partial is not a final.
A promoted artifact with failed global registration is exit 86, not an ordinary
0/1/2 lane.

Postprocess failure admits only an exact observed prefix: internal terminal
receipts, optional result, optional post-check snapshot, and only for C05 an
optional campaign-final snapshot. C05 success requires final snapshot followed
by one top-level success mark. Top-level terminal files remain outside the global
chain; their publication marks atomically commit attempted consumer, terminal
identity, observed consumers, receipts, and finalized state.

Exit 86 and 87 are immutable. Full, reduced, and ASCII fallback fatal frames
must each contain the same mandatory fields: schema, fatal kind, exit code,
attempt ID, run ID, attempted consumer, promoted/prior/durable identities,
primary phase/type/message hash, containment owner/terminal/zero-PID/errors,
Job identity, PID, process-creation identity, source artifact, pre-Job evidence,
consumer manifest, retained C01 raw events, and fixed false
`stage_c_failure_published`, `success_report_published`,
`host_successor_promotion_allowed`, `retry_allowed`, `cleanup_allowed`.
Fallback sanitization may truncate variable detail but may not null a retained
mandatory identity. Finalizer/watchdog/stderr errors never replace 86/87.

## 8. Focused deterministic static contract

The V3 test remains AST-only and may not import/execute the executor. It must use
deterministic fixture AST/source snippets and structural assertions, not broad
substring presence. Exact required cases:

1. `/1` manifest and ledger constants, fields, labels, and V5 compatibility
   labels remain exact; `/2`, `packet_v6`, and `executor_v6` are rejected.
2. Manifest row fixture has exact 11/8/3 counts and pointers
   `/identity_rows/1` and `/identity_rows/5`; held-member label/path displacement
   fails.
3. C01 AST proves one global owner and no local committed head/sequence.
4. Candidate call order is intent, VERIFY/CLOSE, handle close, result, repeated;
   result emission outside that per-candidate block fails the test.
5. Signed and unsigned WinTrust statuses, composite hash restore, enumeration
   previous-context ownership, context release, and raw close outcomes are
   structurally asserted.
6. Raw buffer deletion is after global node reopen/commit, never before.
7. Deterministic 0/1/2 fixtures derive count from actual reopened final/node
   pairs and reject partials, missing nodes, invented finals, and reordering.
8. Registration-loss fixtures cover failure before binding, artifact reopen,
   node promotion, node reopen, and top-level mark while retaining exact run and
   attempted consumer where applicable.
9. Full/reduced/fallback fatal AST dictionaries each independently contain all
   mandatory keys; union-of-dictionaries assertions are prohibited.
10. Source and test AST parse and in-memory compile without executor import.

The required manifest and ledger are absent; tests freeze fail-closed path and
schema behavior with deterministic synthetic documents only. They do not create
governance/evidence artifacts or inspect the immutable V4 root.

## 9. Ordered correction and review gates

After independent amendment acceptance only:

1. CreateNew the three V7 successor paths from the exact V6 source basis.
2. Modify only those three successors.
3. Run only AST parse and in-memory compile for V7 source/test; do not execute
   tests or import the executor.
4. Freeze bytes, LF/CR/BOM, and SHA-256 once.
5. Submit one consolidated static review covering C01 ordering/ownership,
   global DAG, lanes/fatal truth, `/1` graph compatibility, and test strength.

Any patch conflict, path pre-existence, schema drift, missing mandatory field,
or inability to prove exact control flow stops without retry or fallback.
Source acceptance grants no Stage-C execution. A later launch still requires
separately accepted manifest, ledger, interpreter identity, execution authority,
PERF-state receipt, absent fresh root, and explicit one-shot authority.

## 10. Acceptance criteria

The amendment closes only when independent review verifies:

- all V5/V6 and V4 artifacts remain immutable;
- the three V7 paths are absent before correction;
- `/1` manifest/ledger and V5 graph labels are unchanged;
- exact manifest pointers bind executor and held member;
- one global chronology owner eliminates contradictory heads;
- C01 intent/result, signed status, hash restore, enumeration, and close truth
  satisfy the exact state machine;
- 0/1/2, C05, registration-loss, containment, and fatal fields are exhaustive;
- deterministic AST fixtures exercise failure paths rather than checking only
  textual presence;
- no prohibited action occurred.

## 11. Normative V7 correction and precedence

This section supersedes only conflicting clauses of accepted plan D5 for the
V7 successor paths, raw-event representation, identity order, consumer lanes,
fatal frames, and focused-test gate. Every other D5 requirement remains binding.
This section also supersedes conflicting text earlier in this amendment.

### 11.1 Canonical C01 envelopes and raw events

Every durable C01 receipt retains exactly these canonical envelope fields:
`schema`, `attempt_id`, `receipt_id`, `receipt_kind`, `phase`, `created_utc`,
`sequence`, `producer`, `authority`, `predecessor`, `outcome`, `payload`,
`primary_error`, `secondary_errors`. `attempt_id` is the first 16 lowercase
hexadecimal characters of the accepted V7 packet SHA-256 and is mandatory on
every durable C01 receipt. Envelope `outcome` is exactly one of `intent`,
`success`, `failure`, or `typed_rejection`.

Every nested raw event retains schema
`anysolver.no_numba_residual.stage_c.c01_raw_event/1` and exactly these fields:
`schema`, `event_id`, `event_kind`, `phase`, `created_utc`, `outcome`,
`api_calls`, `ownership`, `primary_error`, `secondary_errors`. Raw-event
`outcome` is exactly one of `intent`, `success`, `classified_non_success`, or
`failure`. Raw events are buffered payload objects only. They are never
standalone files or global-chain nodes.

The durable C01 schema/outcome mapping is exact:

- trust intent uses `anysolver.no_numba_residual.stage_c.c01.trust_intent/1`
  with `intent`;
- embedded attempt uses
  `anysolver.no_numba_residual.stage_c.c01.embedded_attempt/1` with `success`,
  `typed_rejection` only for exact clean `TRUST_E_NOSIGNATURE`, and `failure`
  otherwise;
- catalog enumeration uses
  `anysolver.no_numba_residual.stage_c.c01.catalog_enumeration/1` with
  `typed_rejection` only for clean zero-descriptor exhaustion, `success` when
  one or more candidates materialize, and `failure` otherwise. If all
  materialized candidates are later rejected, candidate-failure receipts plus
  terminal `c01.failure/1` with `typed_rejection` represent that outcome;
- candidate intent uses
  `anysolver.no_numba_residual.stage_c.c01.candidate_intent/1` with `intent`;
- accepted candidate uses
  `anysolver.no_numba_residual.stage_c.c01.candidate_result/1` with `success`;
- cleanly rejected candidate uses
  `anysolver.no_numba_residual.stage_c.c01.candidate_failure/1` with
  `typed_rejection`;
- candidate API, identity, VERIFY, CLOSE, or held-handle failure uses
  `anysolver.no_numba_residual.stage_c.c01.candidate_failure/1` with `failure`;
- final trust success uses `anysolver.no_numba_residual.stage_c.c01.result/1`
  with `success`;
- final trust failure uses `anysolver.no_numba_residual.stage_c.c01.failure/1`
  with `typed_rejection` exactly when no candidate is accepted, every
  trust-decision rejection is a clean `typed_rejection`, and every operational
  hash, enumeration, materialization, VERIFY-CLOSE, held-handle, and
  catalog-context cleanup outcome succeeds. Any operational error makes the
  terminal outcome `failure`.

Raw `classified_non_success` maps to durable `typed_rejection`. `non_success`
is forbidden. Failed embedded, enumeration, and candidate receipts retain their
dedicated schemas. `c01.failure/1` is reserved for the terminal trust-failure
receipt. Catalog fallback, hash, and enumeration raw events are carried by the
catalog-enumeration payload. Catalog-context release is a raw event carried by
final `c01.result/1` or `c01.failure/1`. No extra path or schema version is
created.

The phrase "reject `/2`" applies only to manifest, ledger, and raw-event
schemas. Campaign intent and top-level `stage_c.result` and `stage_c.failure`
retain their accepted `/2` schemas.

### 11.2 Fatal and top-level publication fields

Full, reduced, and ASCII fallback fatal forms each independently contain every
one of these non-omittable keys:

`schema`, `event`, `created_utc`, `truncated`, `fatal_kind`, `exit_code`,
`attempt_id`, `run_id`, `attempted_consumer_id`, `promoted_receipt`,
`prior_global_head`, `durable_head`, `durable_final_exists`,
`registered_in_global_chain`, `registration_loss`,
`containment_proof_complete`, `primary_error`, `secondary_errors`,
`containment_outcome`, `job_identity`, `pid`, `process_creation_identity`,
`source_artifact`, `ordinary_prejob_failure`, `run_consumer_manifest`,
`global_receipt_chain`, `c01_pending_raw_events`,
`campaign_wsl_hold_release_outcome`, `stage_c_failure_published`,
`success_report_published`, `host_successor_publication_prohibited`,
`host_successor_promotion_allowed`, `containment_repeated`,
`raw_partials_may_have_advanced`, `evidence_status`, `retry_allowed`,
`cleanup_allowed`.

The fixed values are:

- `stage_c_failure_published=false`;
- `success_report_published=false`;
- `host_successor_publication_prohibited=true`;
- `host_successor_promotion_allowed=false`;
- `containment_repeated=false`;
- `evidence_status="evidence_limited"`;
- `retry_allowed=false`;
- `cleanup_allowed=false`.

Schema `registration_loss_stderr/1` has `event=registration_loss`,
`exit_code=86`, `registration_loss=true`, and
`containment_proof_complete=true`. Exit 86 also fixes
`promoted_receipt!=null`, `durable_final_exists=true`,
`registered_in_global_chain=false`, and `durable_head=prior_global_head`.
Schema `containment_proof_loss_stderr/1` has `event=containment_proof_loss`,
`exit_code=87`, `registration_loss=false`, and
`containment_proof_complete=false`. Exit 87 records
`durable_final_exists` truthfully from an independently identified promoted
final and records `registered_in_global_chain` truthfully; it never fabricates
a promoted receipt.

`containment_outcome` contains exactly `owner_scope`, `reason`,
`child_created`, `terminal`, `zero_pid`, `handles_closed`, ordered `actions`,
and ordered `errors`. `campaign_wsl_hold_release_outcome` contains exactly
`attempted`, `success`, `start_utc`, `end_utc`, `pre_hold_state`,
`post_hold_state`, and `error`, where `error` is null or exactly `phase`, `type`,
`code`, `message_sha256`.

When `truncated=true`, `full_frame_bytes`, `full_frame_sha256`, and ordinal
`omitted_fields` are mandatory. Mandatory identities may not be truncated or
null. `run_id` may be null only for a pure host/C01 failure before any contained
run reservation. A reserved pre-Job/no-child lane retains its non-null run ID;
only Job, PID, and process identity may be null there. Once creation may have
succeeded, unavailable identity is a typed `unknown_after_creation_attempt`
object.

`run_id` and `attempted_consumer_id` bind before artifact promotion. If a final
exists, attempted consumer cannot be discovered later or be null. Observed
consumers, head, and sequence mutate only in one staged commit after artifact
and node reopen validation.

The immutable top-level mark contains exactly `terminal_kind`,
`terminal_identity`, `contained_global_head`, `run_id`, `consumer_id`,
`created_utc`, `committed=true`. It remains outside both serialized chains.
Terminal reopen or registration failure after promotion is exit 86. Missing,
mismatched, or unattachable terminal proof is exit 87. Neither may become
ordinary exit 1.

### 11.3 Exact proof-consumer sequences

Operational Job/process receipts remain global receipts but are not arbitrary
proof-consumer prefixes. Only these labels participate:

`internal-failure-final-1`, `internal-failure-final-2`, `outer-result`,
`post-check-snapshot`, `campaign-final-snapshot`,
`top-level-success-published`, `top-level-failure-published`.

Every full consumer ID is `run:<run_id>:<label>`. Top-level labels are
post-publication marks, not chain nodes. Exact sequences are:

- zero failure finals: `[top-level-failure-published]`;
- one failure final:
  `[internal-failure-final-1, top-level-failure-published]`;
- two failure finals: `[internal-failure-final-1,
  internal-failure-final-2, top-level-failure-published]`;
- C02-C04 success: `[outer-result, post-check-snapshot]`;
- C02-C04 failure before result, after a contained run returned without any
  internal failure-final consumer: `[top-level-failure-published]`;
- C02-C04 result followed by pre-promotion snapshot failure:
  `[outer-result, top-level-failure-published]`;
- inter-run failure after completed C02-C04 and before the next run reservation
  consumes no prior proof again. It publishes a validated campaign-scoped
  top-level mark outside both chains with `run_id=null`,
  `consumer_id="campaign:top-level-failure-published"`, and the actual global
  head;
- C05 pre-result failure, after a contained run returned without any internal
  failure-final consumer: `[top-level-failure-published]`;
- C05 result-before-post-check failure:
  `[outer-result, top-level-failure-published]`;
- C05 after post-check and before campaign-final:
  `[outer-result, post-check-snapshot, top-level-failure-published]`;
- C05 after campaign-final during later validation:
  `[outer-result, post-check-snapshot, campaign-final-snapshot,
  top-level-failure-published]`;
- C05 success: `[outer-result, post-check-snapshot,
  campaign-final-snapshot, top-level-success-published]`.

Registration-loss prefixes are exact: final-1 loss has observed `[]` and
attempted final-1; final-2 loss has observed `[final-1]` and attempted final-2;
outer, post, final, or top loss has the exact preceding observed prefix and the
exact next attempted ID. A missing receipt is never synthesized and a partial
is never counted as a final.

### 11.4 Acyclic identity DAG and historical anchors

The exact identity order is:

accepted D5, accepted amended-V7 hash, V5/V6 rejected hashes, and immutable V4
receipts -> CreateNew V7 packet -> CreateNew V7 executor and test -> V4
manifest `/1` and interpreter receipt -> identity ledger `/1` after every
listed input is frozen -> independent ledger-hash acceptance -> short authority
and PERF-state receipts -> one-shot launch into the absent packet-hash-derived
root.

The V7 packet embeds D5 path/SHA, amended-V7 path/SHA, V6 packet/executor/test
predecessor hashes, and successor paths. It embeds neither its own hash nor
future executor/test hashes. Executor and test may bind the already frozen
packet path/SHA and amendment hash; neither embeds its own hash nor the other's
future hash.

The ledger is created last. It records its own path but never its own hash.
Compatibility row order remains `correction_plan`, `packet_v5`, `executor_v5`,
`focused_catalog_test`, `v4_manifest`, `interpreter_receipt`.
`packet_v5`/`executor_v5` bind V7 artifacts. `correction_plan` remains D5; the
V7 packet transitively binds this amendment.

Manifest `/1` fields are exactly `schema`, `producer_label`,
`producer_plan_path`, `producer_plan_sha256`, `created_utc`, `immutable_root`,
`entries`, `entries_sha256`, `entry_count`, `directory_count`, `file_count`,
`partials`, `identity_rows`. Each entry has exactly `relative_path`, `kind`,
`attributes`, `is_reparse`, `is_link`, `bytes`, `sha256`.

Ledger `/1` fields are exactly `schema`, `ledger_path`, `created_utc`,
`acceptance_scope`, `identity_rows`. Each identity row is exactly `row_id`,
`path`, `bytes`, `sha256`.

Historical pointers remain `/identity_rows/1` for `v4_executor` and
`/identity_rows/5` for `v4_held_member`. Both cross-check exact JSON pointers
in hash-pinned immutable receipts. The four required literal pointers are
`campaign_intent.json#/executor`, `stage_c_failure.json#/executor`,
`campaign_intent.json#/campaign_held_wsl_identity`, and
`stage_c_failure.json#/campaign_held_wsl_identity`. Both receipt copies must
agree with their manifest row and the frozen byte count and SHA-256.
The executor identity is exactly 143,022 bytes and SHA-256
`9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D`.
The `campaign_held_wsl_identity` is canonical
`C:\WINDOWS\system32\wsl.exe`, exactly 278,528 bytes and SHA-256
`E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126`.
Validation uses exact JSON-pointer parsing of the hash-pinned receipts, never
live reopening or recursive search.

### 11.5 Focused gate and unchanged stop boundary

The no-action boundary remains unchanged. After V7 packet/executor/test freeze,
the later gate requires one separately authorized isolated execution of the
focused AST-only test. The test may parse executor source and AST but may not
import or execute the executor or invoke API, WSL, network, evidence-root, or
cache actions. AST parse/compile alone is freeze evidence, not assertion
evidence.

The later fixture gate withdraws any fixture described as "registration loss
before binding". Failure before binding or promotion is an ordinary
pre-promotion failure. Every post-promotion registration-loss fixture begins
with an already bound run and consumer. Each full, reduced, and ASCII fallback
fixture independently asserts all mandatory keys and fixed values, the run-ID
nullability rule, exit-86 durable truth, and that terminal-proof attach or
mismatch failure produces exit 87.

Only this amended plan identity is submitted now. V7 packet, executor, and test
remain absent until explicit acceptance.
