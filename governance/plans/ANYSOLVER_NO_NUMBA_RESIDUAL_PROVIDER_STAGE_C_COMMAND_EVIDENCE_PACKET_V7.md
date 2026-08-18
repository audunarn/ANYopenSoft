# ANYsolver No-Numba Residual Provider Stage-C Command/Evidence Packet V7

## 1. Authority and immutable predecessors

This source-review-only packet implements accepted correction plan
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_AWARE_C01_CORRECTION_PLAN.md`,
SHA-256 `D5FBB6527192026CA6923751B16E96731786AAFE1CC9C37CEBCE8820C49EE88E`,
as amended by
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_C01_V7_CONTRACT_AMENDMENT.md`,
SHA-256 `90D911524C5158B8994810F6A906B4600D2F333CA38CDD1A764405B80A76BFFA`.

Immutable rejected predecessors remain evidence only: V5 packet
`69F1ACD2B4549148FEEC1DD39B9AD619CF845D2D90B0B68EF4A97A350866A61B`,
executor `F27BCA7B8910CDC200E672A1391079C2A62100BA4709360C3B1AFC8856965B6C`,
and focused test `6224E0B5274A561C85E990EDFF5FB8F9C60B94F5158F3129C130B9E0A2284620`;
V6 packet `BCFFE9CF6CFB2CAD42354E4DE4B0A937B77C5986A8B83F4CBDEFC52F57509E0A`,
executor `F47F63D6CD8658D80C207F110E7926FA9EF3CA39D0F853E42009EAF8EA825125`,
and focused test `6468E2F223EE8AD800FF0C7DA6BAF035A1F47C21BA1F67F295C8E5764BD79A4A`.

The V7 successors are this packet,
`C:\Github\ANYopenSoft\governance\tools\anysolver_no_numba_residual_stage_c_host_executor_v7.py`,
and
`C:\Github\ANYopenSoft\governance\tests\test_anysolver_stage_c_catalog_c01_contract_v3.py`.
This packet embeds neither its own future accepted hash nor either future
executor/test hash; those identities are frozen externally after all three
files exist.

This packet grants no Stage-C execution, WSL or WinTrust/catalog API call,
evidence-root creation, PERF use, Git action, cleanup, provider/network action,
package build, release, or publication.

## 2. Packet-derived identity and absent fresh root

The independently accepted V7 packet SHA-256 supplies `attempt_id` as its first
16 lowercase hexadecimal characters and supplies the compatibility
`v5_sha256` field in LF-free contained-run identity material. A future root is
exactly
`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-<attempt_id>`.
It is not created here and must be absent before separately accepted one-shot
execution.

The acyclic launch order is: accepted D5 plus this accepted V7 amendment plus
V5/V6 rejected identities plus immutable V4 receipts; this CreateNew packet;
the CreateNew V7 executor and focused test; manifest `/1` and interpreter
receipt; ledger `/1` after every input is frozen; independent ledger-hash
acceptance; short authority and PERF-state receipts; then one-shot launch. The
ledger records its own path but never its own hash.

## 3. Exact `/1` compatibility graph

The required manifest schema is
`anysolver.no_numba_residual.stage_c_v4_immutable_evidence_manifest/1`; its exact
fields are `schema`, `producer_label`, `producer_plan_path`,
`producer_plan_sha256`, `created_utc`, `immutable_root`, `entries`,
`entries_sha256`, `entry_count`, `directory_count`, `file_count`, `partials`,
and `identity_rows`. Entry fields are exactly `relative_path`, `kind`,
`attributes`, `is_reparse`, `is_link`, `bytes`, and `sha256`. Counts are
exactly 11/8/3 and partials are empty.

The required ledger schema is
`anysolver.no_numba_residual.stage_c_catalog_c01_identity_ledger/1`; exact
fields are `schema`, `ledger_path`, `created_utc`, `acceptance_scope`, and
`identity_rows`. Each row is exactly `row_id`, `path`, `bytes`, and `sha256`.
Compatibility row order remains `correction_plan`, `packet_v5`, `executor_v5`,
`focused_catalog_test`, `v4_manifest`, `interpreter_receipt`; the V5 labels bind
the V7 successors. `/2` is rejected only for manifest, ledger, and raw events.
Campaign intent and top-level result/failure remain accepted `/2` schemas.

Manifest pointers `/identity_rows/1` (`v4_executor`) and `/identity_rows/5`
(`v4_held_member`) cross-check `campaign_intent.json#/executor`,
`stage_c_failure.json#/executor`,
`campaign_intent.json#/campaign_held_wsl_identity`, and
`stage_c_failure.json#/campaign_held_wsl_identity`. Frozen identities are
executor 143,022 bytes/SHA-256
`9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D` and
held `C:\WINDOWS\system32\wsl.exe` 278,528 bytes/SHA-256
`E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126`.
Historical rows are parsed from hash-pinned receipts, not live reopened; all
other rows are direct-file reopened and rehashed.

## 4. Canonical C01 chronology

`_GlobalReceiptChain` is the sole chronology owner. Durable C01 receipts have
exactly `schema`, `attempt_id`, `receipt_id`, `receipt_kind`, `phase`,
`created_utc`, `sequence`, `producer`, `authority`, `predecessor`, `outcome`,
`payload`, `primary_error`, and `secondary_errors`; outcomes are
`intent|success|failure|typed_rejection`.

Nested raw events use
`anysolver.no_numba_residual.stage_c.c01_raw_event/1` and exactly `schema`,
`event_id`, `event_kind`, `phase`, `created_utc`, `outcome`, `api_calls`,
`ownership`, `primary_error`, and `secondary_errors`; outcomes are
`intent|success|classified_non_success|failure`. They are buffered payload
objects only. Raw `classified_non_success` maps to durable `typed_rejection`.

Durable schemas remain trust intent, embedded attempt, catalog enumeration,
candidate intent, candidate result/failure, and terminal result/failure `/1`.
Failed embedded/enumeration receipts retain their dedicated schemas. Candidate
intent, one VERIFY/CLOSE, signer decision, candidate-handle close, and candidate
result/failure complete before the next intent. Enumeration is
`typed_rejection` only for clean zero-descriptor exhaustion, `success` when
candidates materialize, and `failure` for operational errors. Terminal failure
is `typed_rejection` exactly when no candidate is accepted, every trust-decision
rejection is clean, and every operational/cleanup outcome succeeds; any
operational error yields `failure`.

Signed and unsigned WinTrust status, exact 32-byte hash sizing/fill and position
restore, previous-context enumeration ownership, deterministic candidate order,
FILE_ID_INFO alias conflict, and all cleanup outcomes are mandatory. A buffered
prefix is removed only after artifact and global-node reopen plus one staged
global-chain commit.

## 5. Consumer lanes and fatal truth

Operational process/Job receipts remain global receipts but are not arbitrary
proof consumers. Participating labels are only `internal-failure-final-1`,
`internal-failure-final-2`, `outer-result`, `post-check-snapshot`,
`campaign-final-snapshot`, `top-level-success-published`, and
`top-level-failure-published`, each using the exact accepted lane sequences.
Top-level marks are outside both serialized chains. Inter-run failure uses null
run ID, `campaign:top-level-failure-published`, and the actual global head
without prior-proof re-consumption.

Full, reduced, and ASCII fallback fatal forms independently retain every
mandatory field/fixed value. Exit 86 requires a real promoted final,
`durable_final_exists=true`, no global registration, and unchanged durable/prior
head. Exit 87 records independently known durable/registration truth without
fabricating a promoted receipt. Missing or unattachable terminal proof is 87,
never ordinary failure. Reserved pre-Job/no-child lanes retain a non-null run
ID.

## 6. Static gate and stop boundary

Only AST parse and in-memory compile of the V7 executor and focused test are
authorized during freeze. The separately gated focused test may parse executor
source/AST but may never import/execute it or invoke API, WSL, network,
evidence-root, or cache actions. Deterministic fixtures and control-flow
assertions cover `/1` compatibility, exact historical pointers, one chronology
owner, candidate order/cleanup, raw-buffer commit order, exact 0/1/2 and
C02-C05 lanes, fatal 86/87 full/reduced/fallback truth, and terminal-proof
attachment. Pre-binding failure is ordinary pre-promotion failure; every
registration-loss fixture begins after run/consumer binding.

The required manifest, ledger, receipts, and fresh root remain absent. No test
execution, executor import, Stage C, WinTrust/catalog call, WSL action,
evidence creation, PERF action, Git action, cleanup, provider/network action,
build, release, or publication is authorized pending independent static review.
