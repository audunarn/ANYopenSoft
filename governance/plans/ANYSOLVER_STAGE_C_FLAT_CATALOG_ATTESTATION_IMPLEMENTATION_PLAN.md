# ANYsolver Stage-C Flat Catalog Attestation Implementation Plan

Date: 2026-08-14 (Europe/Oslo)

Status: **PLAN-ONLY; INDEPENDENT ACCEPTANCE REQUIRED BEFORE FILE CREATION,
IMPLEMENTATION, FIXTURES, TESTS, API/WSL USE, OR EVIDENCE.**

Registered path:
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_FLAT_CATALOG_ATTESTATION_IMPLEMENTATION_PLAN.md`

Authority:

- accepted scope-reduction plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_ATTESTATION_SCOPE_REDUCTION_PLAN.md`;
- SHA-256:
  `FCD071559C10AF0827E185A84F8042AD8915A16C5100C29F0A0209D76268CE9D`.

### Immutable V4 and D5 inputs

The simplified implementation is bound to these exact historical inputs. They
are read-only acceptance anchors, never live implementation files:

- V4 packet
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V4.md`,
  SHA-256 `DC0E416339CCF5BB66F7EADA6C571FAEEE636129C6902D73683AEEBCBA65DA0E`;
- accepted V4 executor identity: 143,022 bytes, SHA-256
  `9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D`;
- D5 correction plan
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_AWARE_C01_CORRECTION_PLAN.md`,
  SHA-256 `D5FBB6527192026CA6923751B16E96731786AAFE1CC9C37CEBCE8820C49EE88E`;
- interpreter receipt SHA-256
  `B32BBC98F529061436835A82BAB4E149568F1B743D66AEB3C457240606DF36E1`;
- execution-authority receipt SHA-256
  `2C4871AA98E55A1BA5819CAC7934E9A1D52768A6E3A3CDD9B670D187E2DDAAD9`;
- PERF-state receipt SHA-256
  `3E68DF734C0279D2DAB94523A4523A3FBB88804961EB96D658181EB105B141F1`;
- immutable V4 campaign intent: 2,696 bytes, SHA-256
  `89384045394733BD010E1BE5B1EE4D3706C0B946C9080E1C2FC2293075D95B60`;
- immutable V4 preflight: 16,218 bytes, SHA-256
  `F2A810CBFF4A1901F643CAEA8BC8E88724ACFB5669FFA14E1EEF7FCE1F8B141F`;
- immutable V4 failure: 15,475 bytes, SHA-256
  `D58E8106A46C46C250B41396A49DC3D2F612528081A59CCA8CBC25DFD8ECACEA`;
- solver source commit/tree
  `82a9db28d67507c82ef15c631f582a0c3bf6740e` /
  `00b2b20691e73a05589b797b32352f1c760a2451`.

The held executable identity is exactly canonical
`C:\WINDOWS\system32\wsl.exe`, 278,528 bytes, SHA-256
`E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126`.
The accepted V4 campaign intent and failure receipt copies must agree on that
identity. No current OS path is used to replace these historical anchors.

## 1. Objective and owned future paths

Implement only the simplified Stage-C replacement: one small catalog-aware C01
attestor, accepted contained V4 C02-C05 behavior, one atomic receipt per check,
one flat terminal manifest, and behavioral fixtures.

After this plan is independently accepted, the implementation slice may create
and own only these fresh paths:

1. source:
   `C:\Github\ANYopenSoft\governance\tools\anysolver_stage_c_flat_catalog_attestation.py`;
2. focused behavioral test:
   `C:\Github\ANYopenSoft\governance\tests\test_anysolver_stage_c_flat_catalog_attestation.py`;
3. deterministic fixture directory:
   `C:\Github\ANYopenSoft\governance\tests\fixtures\anysolver_stage_c_flat_catalog_attestation_v1`.

The fixture directory may contain only small canonical JSON API/OS boundary
observations created by this task. It may not contain binaries, private models,
V4-V7 evidence, captured host paths, or live API output.

No existing source, test, plan, packet, receipt, manifest, ledger, or evidence
file is an implementation path. Existing files remain byte-identical.

## 2. Architecture boundary

The source is one transparent Python module with four bounded layers:

1. pure canonical-JSON, identity, and atomic-promotion helpers;
2. a narrow injectable Windows trust boundary for held-file, WinVerifyTrust,
   CryptCATAdmin, catalog enumeration, and handle cleanup operations;
3. the C01 attestation state machine using that boundary; and
4. a flat campaign coordinator that invokes C01 and the accepted C02-C05
   contained-check interface, then writes independent check receipts and one
   terminal manifest.

Production C01 uses real Windows calls only in a separately authorized host
campaign. Focused tests inject deterministic fakes and must not import or call
WinTrust, CryptCATAdmin, WSL, network, or immutable evidence.

C02-C05 preserve the accepted V4 behavioral contract for creation-time process
containment, timeout, resource limits, stream capture, terminal wait, and zero
residual process proof. The new source must implement that behavior directly
and minimally; it must not import, execute, rewrite, or copy V7. V4 remains an
immutable behavioral reference, not a runtime dependency or mutable input.

## 3. C01 contract

C01 holds the target executable against replacement and records canonical path,
size, SHA-256, file identity, and final handle-close truth. It performs exactly:

1. one embedded WinVerifyTrust attempt;
2. embedded acceptance only after the frozen Microsoft signer policy passes;
3. catalog fallback only for exact `TRUST_E_NOSIGNATURE`;
4. SHA-256 catalog-hash acquisition with position restoration evidence;
5. ordinal catalog enumeration and deterministic candidate ordering;
6. one VERIFY/CLOSE and identity-before/after check per candidate; and
7. catalog-context and held-handle cleanup with all errors retained.

Outcomes are exactly `success`, `typed_rejection`, or `failure`. Clean exhaustive
no-acceptance is `typed_rejection`. Malformed provider data, API failure,
identity drift, VERIFY/CLOSE failure, or cleanup failure is `failure`. All
enumerated candidates are attempted; one operational failure makes the final
outcome failure even if another candidate verifies.

### Exact Microsoft signer policy

Embedded and catalog success apply the same predicate. WinTrust uses generic
verify V2, no UI, whole-chain revocation, and provider flags exactly
`0x00000080 | 0x00001000 | 0x00002000` (chain-exclude-root, cache-only URL
retrieval, and MD2/MD4 disable). Acceptance requires:

- provider and signer present; at least two certificates; signer error zero;
- `pChainContext` trust evidence present; chain trust error zero; every
  certificate provider error zero;
- leaf organization exactly `Microsoft Corporation`;
- leaf common name exactly `Microsoft Windows` or `Microsoft Corporation`;
- leaf EKUs contain code signing `1.3.6.1.5.5.7.3.3`;
- leaf critical extensions are a subset of exactly `2.5.29.14`, `2.5.29.15`,
  `2.5.29.19`, `2.5.29.32`, `2.5.29.35`, and `2.5.29.37`;
- leaf is not test, revoked, or provider-error and is within its UTC validity;
- root organization exactly `Microsoft Corporation`, with trusted-root and
  self-signed true and test-certificate false; and
- every VERIFY state has exactly one successful CLOSE before acceptance.

Any absent/malformed field or failed predicate is operational failure. The only
clean embedded fallback remains exact `TRUST_E_NOSIGNATURE`.

## 3.1 Frozen C02-C05 behavior

The literal contained-check table is:

| Check | Exact argv | Semantic timeout |
| --- | --- | --- |
| C02 | `["C:\\WINDOWS\\system32\\wsl.exe","--version"]` | 30 seconds |
| C03 | `["C:\\WINDOWS\\system32\\wsl.exe","--status"]` | 45 seconds |
| C04 | `["C:\\WINDOWS\\system32\\wsl.exe","--list","--verbose"]` | 45 seconds |
| C05 | `["C:\\WINDOWS\\system32\\wsl.exe","--list","--quiet"]` | 45 seconds |

The campaign deadline is 300 seconds with a 60-second finalization reserve.
Each check exits zero, reaches terminal contained state, and leaves zero Job
PIDs. C01 acquires the held `wsl.exe` handle before trust inspection and retains
the same file object through every C02-C05 creation. Each suspended child image
path, file ID, bytes, and SHA-256 must equal that held identity before its sole
resume. The handle continues to deny write/delete sharing until all checks and
the final host snapshot complete.

C02 decodes bounded output into unique ordered `label: value` records and
requires the `WSL version` value exactly `2.6.1.0`. C03 decodes bounded nonempty
status output into unique ordered `label: value` records; it invents no default
distribution value, while the immediate post-C03 host snapshot must prove a
functioning WSL service in running state.

C04 parses one verbose table with header fields `NAME`, `STATE`, `VERSION`,
unique nonempty distro names, nonempty state, and integer version. C05 parses
one unique nonempty distro name per nonempty line. Their ordinal name arrays
must be exactly equal. Both must exclude
`ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1` and
`ANYsolver-Ubuntu-24.04-82a9db28`.

### Host-state and provider-absence gates

Snapshots occur before C01, after C01, after each C02-C05, and finally. Every
snapshot records OS/kernel/architecture, registered service/process inventory,
the held executable identity, and these absent provider leaves:

- builder import directory
  `Q\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`;
- final import directory
  `Q\wsl\ANYsolver-Ubuntu-24.04-82a9db28`;
- provider archive and `.partial` sibling
  `Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar`.

All ancestors are direct non-reparse directories. The leaves remain absent at
every snapshot. OS and registered path identities remain exact. Service/process
changes are accepted only when the frozen authority permits query-triggered
activation and the transition is attributable to the immediately preceding
query; every other delta fails. No distro import, registration, termination,
unregistration, provider build, archive creation, or network action is allowed.

## 4. Independent check receipts

Each C01-C05 check owns one final path derived from its fixed check ID under a
fresh future campaign root. Every receipt uses schema
`anysolver.stage_c.flat_check_receipt/1` and exact top-level fields:

`schema`, `campaign_id`, `check_id`, `created_utc`, `input_identity`, `outcome`,
`observation`, `process`, `resource`, `cleanup`, `primary_error`,
`secondary_errors`.

The receipt is written to a sibling `.partial`, flushed, atomically promoted,
reopened, byte/hash validated, and then treated as immutable. A pre-existing
partial or final is fatal before the check. Failure before promotion leaves no
final; an owned partial remains truthful preserved evidence. Reopen failure
does not trigger another receipt or fatal frame.

C01 `observation` contains ordered embedded, hash, enumeration, candidate, and
cleanup events plus selected attestation. C02-C05 `process` and `resource`
contain the accepted contained-run terminal facts. No receipt points to another
receipt, global head, consumer, terminal mark, or mutable chain state.

## 5. Flat terminal manifest

After all required checks stop, the coordinator writes exactly one manifest
with schema `anysolver.stage_c.flat_terminal_manifest/1` and fields:

`schema`, `campaign_id`, `created_utc`, `immutable_inputs`, `ordered_checks`,
`check_receipts`, `overall_outcome`, `primary_error`, `secondary_errors`,
`retry_allowed`, `cleanup_allowed`.

`ordered_checks` is exactly `C01,C02,C03,C04,C05`. Each `check_receipts` row is
exactly `check_id,path,bytes,sha256,outcome` or a truthful absence row with
`path/bytes/sha256=null`. The coordinator reopens every listed final and checks
canonical bytes, hash, schema, campaign, check ID, and outcome before manifest
promotion. Overall success requires five validated success receipts. Any typed
rejection, failure, missing receipt, or validation error makes overall failure.

The manifest uses the same sibling-partial atomic lifecycle. Promotion/reopen
failure is returned to the direct caller through exit status and bounded
stderr; no successor publication, registration-loss frame, containment-loss
frame, reduced frame, or emergency frame exists.

## 6. Behavioral fixture and focused-test matrix

The focused test must exercise public behavior through injected fakes:

- embedded success; exact no-signature fallback; non-fallback failure;
- zero, one, repeated, duplicate-alias, malformed, rejected, and operationally
  failing catalog candidates;
- returned-context rows, deterministic ordering, identity drift, VERIFY/CLOSE,
  held-handle cleanup, catalog release, and all-candidate traversal;
- check-receipt success, pre-promotion failure, reopen failure, preserved
  partial, and stale-path refusal;
- C02-C05 contained success/failure/timeout/resource/residual observations;
- manifest five-success, typed rejection, operational failure, missing receipt,
  mismatched hash, and stale-final refusal.

Matching fixtures also freeze:

- every positive and negative Microsoft signer-policy predicate above;
- the exact four argv/timeouts and held-image identity continuity;
- C02 version `2.6.1.0`, C03 ordered status parsing and running-service proof;
- C04 verbose parsing, C05 quiet parsing, exact ordinal equality, duplicate/name
  mismatch, malformed header/state/version, and provider-name rejection; and
- pre/inter/final snapshots with allowed query activation, forbidden unrelated
  service/process delta, changed OS/path identity, reparse ancestor, and each
  provider leaf present.

Assertions use parsed values and observable calls/results. AST parse/compile may
be reported separately but source spelling, substring presence, mutation of
source text, or fabricated key unions cannot qualify behavior.

## 7. Implementation and review sequence

1. Independently accept this plan and verify all three future paths are absent.
2. Create only the source, focused test, and registered fixture files.
3. Perform AST parse/compile only and submit frozen identities for static review.
4. After static acceptance, request separate authority for one focused
   behavioral test run using only injected fakes.
5. Correct at most one bounded implementation defect round; recurrence triggers
   simplify/defer/abandon review.
6. Only after source and behavioral acceptance, register a fresh campaign packet,
   absent evidence root, host identities, resource envelope, and PERF request.

No real WinTrust/catalog call or WSL process is part of implementation or the
focused behavioral gate.

## 8. Retained exclusions and current stop gate

Excluded without exception:

- global receipt DAG, mutable head, consumer-state machine, proof prefixes,
  terminal marks, fatal ladder, reduced/emergency frames, and source-spelling
  AST gates;
- V7 repair, V8, reuse of V7 source/tests/schemas/paths, or mutation of V4-V7;
- imports from retired executors or reliance on ambient evidence/worktrees;
- network, package acquisition, build, publication, Git mutation, cleanup,
  Defender exception, performance, or broad tests.

Current authority ends with creation and hashing of this Markdown plan. It does
not authorize any future owned path, fixture, implementation, test, API, WSL,
evidence-root, PERF, Git, or cleanup action.
