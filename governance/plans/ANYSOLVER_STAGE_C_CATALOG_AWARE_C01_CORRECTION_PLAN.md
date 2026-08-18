# ANYsolver Stage-C Catalog-Aware C01 Correction Plan

## 1. Objective and authority boundary

This plan corrects only the Stage-C C01 Authenticode classification gap exposed
by the immutable first attempt. Windows reports the held System32 `wsl.exe` as a
valid catalog-signed Microsoft binary, while the accepted executor checks only
an embedded signature with `WINTRUST_FILE_INFO` and `WTD_CHOICE_FILE`.

This document is plan-only. It authorizes no source edit, interpreter import,
test, WinTrust or catalog API call, WSL query, process, Job Object, evidence-root
creation, escalation, PERF action, cleanup, retry, provider action, Git action,
or publication. Later work requires independent acceptance of this exact file
identity and a separate bounded edit authority.

## 2. Immutable first-failure evidence

The following V4 attempt is preserved byte-for-byte and is never retried,
overwritten, repaired, renamed, moved, or cleaned:

- Evidence root: `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-dc0e416339ccf5bb`
- Packet: `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V4.md`
- Packet SHA-256: `DC0E416339CCF5BB66F7EADA6C571FAEEE636129C6902D73683AEEBCBA65DA0E`
- Executor SHA-256: `9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D`
- Interpreter receipt SHA-256: `B32BBC98F529061436835A82BAB4E149568F1B743D66AEB3C457240606DF36E1`
- Authority receipt SHA-256: `2C4871AA98E55A1BA5819CAC7934E9A1D52768A6E3A3CDD9B670D187E2DDAAD9`
- PERF-state receipt SHA-256: `3E68DF734C0279D2DAB94523A4523A3FBB88804961EB96D658181EB105B141F1`
- `campaign_intent.json`: 2,696 bytes, SHA-256 `89384045394733BD010E1BE5B1EE4D3706C0B946C9080E1C2FC2293075D95B60`
- `snapshots/preflight.json`: 16,218 bytes, SHA-256 `F2A810CBFF4A1901F643CAEA8BC8E88724ACFB5669FFA14E1EEF7FCE1F8B141F`
- `stage_c_failure.json`: 15,475 bytes, SHA-256 `D58E8106A46C46C250B41396A49DC3D2F612528081A59CCA8CBC25DFD8ECACEA`

The failure is classified exactly as C01 fail-closed after 43 ms:
`WinVerifyTrust` returned signed status `-2146762496`, unsigned
`0x800B0100` (`TRUST_E_NOSIGNATURE`), for held
`C:\WINDOWS\system32\wsl.exe` SHA-256 ending `8126`. C02-C05 did not run.
No WSL child, provider, network, or PERF action occurred, and no evidence
partial exists. Independent read-only evidence classifies the same binary as
`Valid` with `SignatureType=Catalog`.

## 3. Exact correction ownership

Prospective owned paths are limited to:

- `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V5.md`
- `C:\Github\ANYopenSoft\governance\tools\anysolver_no_numba_residual_stage_c_host_executor.py`
- One later registered focused catalog-contract test file, whose exact path must
  be added by an accepted edit amendment before creation.

No ANYsolver package source, test, workflow, dependency metadata, accepted V1-V4
packet, prior receipt, or prior evidence-root path is owned.

## 4. Catalog-aware C01 trust contract

### 4.1 Embedded verification remains first

C01 continues to call `WinVerifyTrust` first with
`WINTRUST_FILE_INFO`, `WTD_CHOICE_FILE`, the held direct file handle, no UI, and
the existing accepted Microsoft chain/publisher/critical-extension policy.

- Embedded success returns `signature_mode=embedded`; no catalog lookup occurs.
- Only exact `TRUST_E_NOSIGNATURE` may enter catalog lookup.
- Every other embedded result remains the primary typed failure. It must never
  be reclassified, hidden, or repaired by catalog lookup.
- Every `WTD_STATEACTION_VERIFY` has exactly one matching
  `WTD_STATEACTION_CLOSE`, with raw signed/unsigned status and close result
  recorded.

### 4.2 Local catalog discovery and hashing

The correction binds direct `wintrust.dll` APIs with reviewed ctypes prototypes
and structures matching the installed Windows SDK:

- `CryptCATAdminAcquireContext2`
- `CryptCATAdminCalcHashFromFileHandle2`
- `CryptCATAdminEnumCatalogFromHash`
- `CryptCATCatalogInfoFromContext`
- `CryptCATAdminReleaseCatalogContext`
- `CryptCATAdminReleaseContext`
- `WINTRUST_CATALOG_INFO`
- `CATALOG_INFO`
- `WTD_CHOICE_CATALOG`

`CryptCATAdminAcquireContext2` is mandatory and requests exactly local SHA-256
catalog hashing. There is no legacy API fallback, shell, PowerShell, child
process, package install, online lookup, or mutation of the catalog database.
Unsupported API/structure/algorithm behavior fails before accepting trust.

The campaign-held `wsl.exe` handle remains open with read sharing only, denying
write/delete sharing from before C01 through all later child creation. Catalog
hashing uses that same file object. The executor saves its file position, resets
to zero, performs the two-call size/hash protocol, and restores/reset-verifies
the position on every outcome. A catalog member hash is not conflated with the
raw file SHA-256; both identities are recorded separately.

The catalog member tag is the exact uppercase hexadecimal catalog-member hash.
Enumeration must return locally registered matching catalogs. Each candidate's
context, canonical path, direct file identity, bytes, SHA-256, and API results
are captured. Candidate contexts remain valid through verification and are
released exactly once on every path. Catalog-admin context release is also
exactly once.

### 4.3 Catalog WinVerifyTrust

For each candidate, C01 builds `WINTRUST_CATALOG_INFO` with exact reviewed
field sizes and pointer lifetimes:

- candidate catalog path;
- uppercase member tag;
- member path `C:\WINDOWS\system32\wsl.exe`;
- the campaign-held member handle;
- calculated catalog hash bytes and length;
- the matching catalog/admin contexts required by the Windows API contract.

`WinVerifyTrust` uses `WTD_CHOICE_CATALOG`, no UI, and
`WTD_CACHE_ONLY_URL_RETRIEVAL`. Network-backed retrieval is forbidden even when
local verification cannot complete. The existing provider-state signer-chain
extraction and Microsoft policy apply unchanged to catalog success. A zero trust
status without a complete accepted chain is not success.

All candidates are recorded. Deterministic result ordering uses normalized
catalog path, volume/file ID, and SHA-256 with ordinal comparison. If multiple
candidates satisfy the same accepted policy, the selected evidence identity is
the ordinal-lowest candidate; all successful and failed candidate statuses
remain in the receipt. No candidate means typed `NO_LOCAL_CATALOG`; candidates
without one accepted local chain mean typed `CATALOG_TRUST_REJECTED`.

## 5. C01 evidence and regressions

The C01 result retains its existing schema and adds one canonical `trust`
object. The object records:

- held member path/raw SHA/file ID before and after;
- embedded attempt status and close accounting;
- fallback eligibility and exact reason;
- catalog admin algorithm/context acquisition and release;
- calculated member-hash bytes, length, and member tag;
- ordered candidate catalog identities and per-candidate trust/close results;
- selected signature mode, catalog identity, signer chain, and policy result;
- all opened/closed handles, ctypes structure sizes/offsets, last-error values,
  and `network_allowed=false`.

Failure publication must survive catalog enumeration, trust, signer extraction,
or cleanup errors while preserving the first error and every partial/final
already owned. Catalog support does not alter C02-C05, Job containment, timeout,
memory, host-delta, receipt, or cleanup behavior.

The later focused test amendment must prove at least these exact cases:

- embedded valid: succeeds without catalog API use;
- embedded `TRUST_E_NOSIGNATURE`: enters catalog verification once;
- embedded non-`TRUST_E_NOSIGNATURE`: fails without catalog lookup;
- no local matching catalog: typed fail-closed result;
- one valid local catalog: catalog mode and accepted Microsoft chain;
- mixed invalid/valid candidates: deterministic accepted selection with all
  attempts preserved;
- multiple valid candidates: ordinal deterministic selection;
- hash sizing/hash/catalog enumeration/trust/close/release failure paths;
- cache-only/no-network flag and no child-process contract;
- held member identity/position stability and write/delete-share denial;
- embedded and catalog signer-policy parity;
- unchanged C02-C05 argv, Job, timeout, memory, and evidence-root contracts.

No test may substitute `Get-AuthenticodeSignature` for production truth. Any
live-System32 observation is supplemental; deterministic API-adapter fixtures
remain the oracle for branch/error/cleanup behavior.

## 6. Superseding packet and fresh-root lifecycle

After this plan is accepted, a separately authorized edit creates V5 as a
content-addressed child of accepted V4. V5 changes only:

- the immutable first-failure ledger above;
- the catalog-aware C01 contract;
- the new executor identity;
- the corrected one-shot lifecycle below.

The executor then pins the exact V5 path/hash and its new source hash. V5's
accepted SHA-256 derives a new root exactly as:

`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-<first-16-lowercase-V5-SHA256>`

The derived leaf must be absent and non-reparse immediately before launch. It
must differ ordinally from the preserved V4 leaf. The V4 leaf is checked
read-only against the three exact final hashes above at corrected-attempt
preflight and final accounting; no old path is opened for write.

The corrected campaign is not a retry of V4. It is one new content-addressed
attempt with a new packet, executor, authority, PERF-state, and evidence root.
Before launch it requires:

- independently accepted V5 and corrected executor bytes/hashes;
- an independently accepted interpreter identity receipt bound to the current
  direct interpreter file; immutable prior facts may be reused only through an
  explicit acceptance ledger;
- a fresh short execution-authority receipt binding V5, corrected executor,
  interpreter receipt, exact new root, C01 catalog behavior, C02-C05 argv,
  under-five-minute/one-child/under-500-MB/no-network/no-GPU envelope, service
  activation policy, escalation mode, first-failure, and no retry/cleanup;
- a distinct fresh PERF-state receipt proving no competing exclusive lease;
- one explicit one-shot execution grant after all receipts are hashed and
  accepted.

Any failure preserves the new root and stops. There is no automatic retry,
repair, overwrite, cleanup, fallback to PowerShell trust, provider continuation,
or reuse of the V4 root.

## 7. Review, evidence, and stop order

The required order is exact:

1. Independently accept this plan path, bytes, and SHA-256.
2. Register the exact focused test path and source-edit allowlist amendment.
3. Create V5 and correct only the executor/catalog test under apply-patch-only
   authority.
4. Run AST/compile and the accepted focused deterministic contract tests only
   under separate authority; no WSL query is part of that gate.
5. Freeze V5, executor, test, and immutable V4 evidence identities and obtain
   independent source review.
6. Obtain and accept fresh interpreter/authority/PERF-state receipts and the
   exact fresh root.
7. Request and receive one explicit Stage-C execution grant.
8. Execute once, preserve first-failure truth, and independently review all
   evidence before any provider Stage M/P or cleanup proposal.

No action after step 1 is authorized by this plan's creation. The old evidence,
all prior packets, all receipts, and all failure artifacts remain immutable.

## 8. Authoritative V2 supersession

This section supersedes every conflicting statement above. The rejected
11,627-byte plan identity remains immutable review evidence at SHA-256
`ECD8517F18272E53D2E6DE6A5FCF8ABC8E16407AB73A6B94CD1CB3A29BFA320D`.
Its embedded-first fallback rule and fresh-root/no-replay lifecycle remain
unchanged. No source edit, test, API call, WSL action, evidence-root creation,
lease, or execution is authorized by this supersession.

### 8.1 Bound diagnosis and complete V4 inventory

The held member is canonical path `C:\WINDOWS\system32\wsl.exe`, raw SHA-256
`E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126`.
The accepted diagnosis is narrow: the executor's embedded-only
`WTD_CHOICE_FILE` attempt correctly returned `TRUST_E_NOSIGNATURE`, while an
independent read-only Windows result classified that exact file identity as
`Valid` and `SignatureType=Catalog`. This is not authority to trust shell
output, skip WinTrust, or accept a different file. It requires a held-file,
local-catalog `WTD_CHOICE_CATALOG` path with the existing provider and Microsoft
policy checks.

The complete recursive V4 evidence inventory is frozen below. Every directory
has only the `Directory` attribute, every file has only the `Archive` attribute,
no item is a link or reparse point, and no `.partial` exists.

| Relative path | Kind | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `.` | directory | - | - |
| `checks` | directory | - | - |
| `checks/C01` | directory | - | - |
| `checks/C02` | directory | - | - |
| `checks/C03` | directory | - | - |
| `checks/C04` | directory | - | - |
| `checks/C05` | directory | - | - |
| `snapshots` | directory | - | - |
| `campaign_intent.json` | file | 2,696 | `89384045394733BD010E1BE5B1EE4D3706C0B946C9080E1C2FC2293075D95B60` |
| `snapshots/preflight.json` | file | 16,218 | `F2A810CBFF4A1901F643CAEA8BC8E88724ACFB5669FFA14E1EEF7FCE1F8B141F` |
| `stage_c_failure.json` | file | 15,475 | `D58E8106A46C46C250B41396A49DC3D2F612528081A59CCA8CBC25DFD8ECACEA` |

The V4 root and every listed item remain immutable. The corrected attempt uses
a new absent content-addressed root and never retries, repairs, overwrites,
renames, moves, or cleans V4 evidence.

### 8.2 Exact catalog API and flags

The later executor correction binds reviewed ctypes signatures and makes only
these catalog calls. Every reserved or flags argument is exactly zero:

- `CryptCATAdminAcquireContext2(&hCatAdmin, NULL, L"SHA256", NULL, 0)`;
- `CryptCATAdminCalcHashFromFileHandle2(hCatAdmin, heldMemberHandle, &cbHash, NULL, 0)`, followed by the exact-sized-buffer call with final argument `0`;
- first `CryptCATAdminEnumCatalogFromHash(hCatAdmin, hash, cbHash, 0, NULL)`;
- continuation `CryptCATAdminEnumCatalogFromHash(hCatAdmin, hash, cbHash, 0, &previous)`;
- `CryptCATCatalogInfoFromContext(hCatInfo, &catalogInfo, 0)`;
- `CryptCATAdminReleaseCatalogContext(hCatAdmin, ownedHCatInfo, 0)` only for a context still owned locally;
- `CryptCATAdminReleaseContext(hCatAdmin, 0)` exactly once after successful acquisition.

There is no legacy catalog API, alternate algorithm, online catalog retrieval,
catalog database mutation, shell, PowerShell, child process, or package action.
The catalog member tag is the exact uppercase hexadecimal member hash. Member
hashing uses the already held direct `wsl.exe` file object, saves its position,
seeks to zero, performs the two-call protocol, and restores and verifies the
position on every outcome. Raw file SHA-256 and catalog member hash remain
separate typed identities.

### 8.3 `HCATINFO` ownership and enumeration result

Enumeration is an explicit consuming ownership state machine:

1. A non-null enum return is the sole locally owned `HCATINFO`.
2. To continue, the owned value is moved to `previous`, local ownership is
   cleared before the call, and `&previous` is passed.
3. The continuation call consumes or replaces that previous context. The caller
   never releases the previous value after passing it.
4. A newly returned non-null context becomes the sole owned context.
5. `CryptCATAdminReleaseCatalogContext(..., 0)` is called only if enumeration
   stops early while a context remains locally owned. It is never called twice
   for one context.

Immediately before every enum call, last error is set to `ERROR_SUCCESS`. A
null return is a clean end only when captured last error is `ERROR_SUCCESS`,
`ERROR_NOT_FOUND` (`1168`), or unsigned `CRYPT_E_NOT_FOUND` (`0x80092004`). Any
other value, including `ERROR_SERVICE_NOT_ACTIVE`, is a typed enumeration
error. Every call records input ownership, return value, captured last error,
and resulting ownership.

`HCATINFO` is never cast to, stored as, or passed as `PCCTL_CONTEXT`. It is used
only by the enum, catalog-info, and release APIs. In
`WINTRUST_CATALOG_INFO`, `pcCatalogContext` is exactly `NULL` and `hCatAdmin` is
the acquired `HCATADMIN`; catalog path and member fields define the trust
subject.

### 8.4 Held catalog identity and WinTrust state lifecycle

Each enumerated catalog path is canonicalized and opened through the accepted
direct-file helper with `GENERIC_READ`, `FILE_SHARE_READ` only,
`OPEN_EXISTING`, and reparse rejection. Its handle is held from before the
candidate intent and hash through candidate WinTrust, provider extraction,
conditional state close, and post-check identity. Pre/post canonical path,
volume/file ID, bytes, and SHA-256 must agree. Read-only sharing permits the
provider to read the catalog while denial of write/delete sharing prevents
replacement.

Embedded and catalog attempts use this exact state contract:

1. Publish the applicable durable intent before `WTD_STATEACTION_VERIFY`.
2. Record raw signed and unsigned WinTrust status.
3. If `hWVTStateData` is non-null, extract provider data and all available
   signer-chain or failure-chain evidence before close.
4. If and only if a state handle exists, perform exactly one
   `WTD_STATEACTION_CLOSE`, record its status, and clear local state ownership.
5. A close failure blocks fallback, candidate selection, or acceptance.

Embedded fallback is considered only for exact `TRUST_E_NOSIGNATURE` and only
after provider extraction plus conditional close. Embedded success is accepted
only after provider extraction, Microsoft policy evaluation, and close. Every
catalog candidate likewise completes provider extraction and conditional close
before deterministic selection. No WinTrust state may remain open when the next
candidate or phase begins.

### 8.5 Durable C01 receipts

The corrected fresh root owns these exact CreateNew, same-volume,
write-through/flush, atomic-no-replace partial/final pairs:

- `checks/C01/trust_intent.json.partial` -> `checks/C01/trust_intent.json`;
- `checks/C01/embedded_attempt.json.partial` -> `checks/C01/embedded_attempt.json`;
- `checks/C01/catalog_enumeration.json.partial` -> `checks/C01/catalog_enumeration.json`;
- `checks/C01/catalog_candidates/<zero-padded-ordinal>-<lowercase-catalog-sha256>/candidate_intent.json.partial` -> `candidate_intent.json`;
- the same directory's `candidate_result.json.partial` -> `candidate_result.json`, or `candidate_failure.json.partial` -> `candidate_failure.json`;
- `checks/C01/trust_failure.json.partial` -> `checks/C01/trust_failure.json`;
- existing success path `checks/C01/result.json.partial` -> `checks/C01/result.json`.

`trust_intent.json` is durable before the first embedded trust call and binds
member identity, accepted identity ledger, packet, flags, API contract,
deadline, and expected receipt paths. Candidate intent is durable after the
catalog's held direct identity is established but before candidate trust.
Embedded, enumeration, and candidate receipts record raw calls, statuses,
last-error values, ownership transitions, provider extraction, conditional
close, and pre/post identity.

Every C01 exception or typed rejection attempts `trust_failure.json` without
replacing any final. It preserves the primary phase/error and records secondary
publication, provider, close, release, or snapshot errors without masking the
primary failure. Owned partials and finals are never deleted or overwritten.
Thus every C01 path has durable intent and either a final success result or an
all-outcome failure receipt.

### 8.6 Exact diff and symbol boundary

The later edit amendment may alter only these executor symbol groups:

- catalog constants, ctypes structures, prototypes, and last-error helpers;
- `_authenticode_identity`, only to share provider/state handling;
- new `_wintrust_attempt`, `_close_wintrust_state`, `_catalog_member_hash`,
  `_catalog_candidates`, and `_verify_catalog_candidate` helpers;
- `_c01_held_identity_impl`, only to integrate embedded-first catalog fallback;
- C01 receipt path/schema constants and C01 atomic publication helpers;
- packet/executor/external-ledger argument parsing and acyclic identity checks;
- C01 failure/result fields required to bind the new receipts.

No semantic diff is permitted in `CHECKS`, C02-C05 argv/timeouts,
`_run_contained_wsl`, any Job/process creation or termination symbol, timeout or
memory enforcement, host snapshots/deltas, service-activation accounting, or
the C02-C05 execution loop. Existing interpreter/authority/PERF validation may
only add external-ledger fields; all prior validation semantics remain exact.
The one later registered focused test is the only other source path.

Independent review must compare the accepted and corrected executor by exact
diff hunk and symbol, reject every hunk outside this allowlist, and prove the
C02-C05 command, containment, evidence, timeout, and resource contracts are
unchanged.

### 8.7 Acyclic external identity ledger

The old Section 6 language saying that V5 and the executor pin one another is
withdrawn. Neither V5 nor the executor embeds its own final SHA-256. The
executor does not embed V5's final SHA-256, and V5 does not embed the executor's
final SHA-256.

After this plan, V5, the corrected executor, the focused test, and the V4
inventory manifest are each frozen and independently accepted, a separate
artifact may be created at:

`C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_STAGE_C_CATALOG_C01_ACCEPTED_IDENTITY_LEDGER.json`

Its schema is exactly
`anysolver.no_numba_residual.stage_c_catalog_c01_identity_ledger/1`. It records
canonical path, bytes, and SHA-256 for this plan, V5, executor, focused test,
immutable V4 recursive-inventory manifest, and accepted interpreter receipt. It
also records its own canonical path, schema, creation UTC, and acceptance scope,
but never its own hash.

The ledger's final SHA-256 is an external accepted launch parameter. Fresh
execution-authority and PERF-state receipts bind that hash. Launch supplies
ledger path/hash, packet path/hash, executor path/hash, and fresh root. The
executor validates the external ledger and every listed identity before root
creation. The fresh root leaf is derived from the externally supplied,
ledger-verified V5 SHA-256. This graph has no packet or executor self-hash
cycle.

### 8.8 Superseding lifecycle and stop boundary

The authoritative order is:

1. Independently accept this superseding plan identity.
2. Register the exact focused test path and apply-patch-only edit amendment.
3. Freeze V5, executor, test, and immutable V4 inventory manifest.
4. Run only separately authorized AST/compile and deterministic catalog adapter
   tests; no WSL query belongs to that gate.
5. Obtain exact-diff/symbol review and create/accept the external identity
   ledger.
6. Obtain fresh interpreter, execution-authority, and PERF-state receipts bound
   to the ledger and exact absent fresh root.
7. Request one explicit Stage-C execution grant, then execute at most once.

No step after item 1 is authorized now. The original root remains immutable,
the failed attempt is never replayed, and PERF remains free. There is no edit,
test, API, WSL, evidence-root, cleanup, retry, provider, publication, or lease
authority from this plan-only supersession.

## 9. Authoritative V3 evidence-graph closure

This section supersedes only conflicting evidence-identity, receipt-chain,
candidate-ordering, hash-size, and symbol-boundary language above. It does not
change the accepted catalog API, context ownership, conditional WinTrust close,
anti-replacement, C02-C05 preservation, fresh-root, or no-action contracts.

### 9.1 Catalog diagnosis status

The independent `Valid` / `SignatureType=Catalog` observation has no durable
receipt bound to the failed attempt. It is therefore explicitly demoted to
`evidence_limited_unreceipted` diagnostic context. It is not an accepted input
to the identity ledger, not a trust fact, not a source-test oracle, and not
authority to accept catalog fallback. The only authoritative V4 runtime fact is
the immutable C01 failure receipt for the exact held member identity and exact
embedded `TRUST_E_NOSIGNATURE` result.

Deterministic adapter tests must establish the catalog branch contract before
source acceptance. A future direct Windows catalog observation may be promoted
only through a separately accepted receipt path/hash and plan amendment; this
plan neither requires nor authorizes that observation.

### 9.2 Immutable V4 recursive manifest

The exact prospective manifest path is:

`C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_STAGE_C_V4_IMMUTABLE_EVIDENCE_MANIFEST_D58E8106.json`

Its schema is exactly
`anysolver.no_numba_residual.stage_c_v4_immutable_evidence_manifest/1`. Its sole
producer is a separately authorized apply-patch publication from the accepted
Section 8.1 table; producer identity is the accepted plan path/SHA plus literal
producer label `governance_apply_patch_from_accepted_plan/1`. It is canonical
UTF-8 without BOM, sorted-key compact JSON with one final LF, CreateNew, and is
never generated by reading or writing the V4 root at correction runtime. Its
payload contains:

- schema, producer label, producer plan path/SHA, creation UTC, and canonical
  immutable V4 root;
- every directory and file in Section 8.1, with slash-normalized relative path,
  exact kind, exact attribute names, `is_reparse=false`, and `is_link=false`;
- exact file bytes/SHA-256 and null bytes/hash for directories;
- exact entry count `11`, directory count `8`, file count `3`, and
  `partials=[]`;
- exact packet, executor, interpreter, authority, PERF-state, held-member, and
  three V4 final identities already frozen by this plan.

Before any corrected-root creation, and again on every corrected campaign
outcome before top-level publication completes, the executor recursively walks
the V4 root without following links. It includes the root as `.`, emits every
descendant once, normalizes relative separators to `/`, sorts paths by ordinal
UTF-8 bytes, and computes the same manifest fields. The generated canonical
inventory must be exactly equal entry-for-entry to the accepted manifest:
paths, counts, kinds, attributes, reparse/link booleans, bytes, hashes, and
empty partial list. Missing, extra, duplicate, unreadable, reparse, changed, or
unexpected entries fail closed. The check never opens V4 for write.

The preflight and final inventory canonical bytes and SHA-256 are recorded in
the corrected campaign's top-level intent and terminal receipt. On exceptional
exit, final inventory is nested-protected: a snapshot failure is recorded as a
secondary error and cannot mask the primary failure. The external accepted
identity ledger lists the manifest path/bytes/SHA. No corrected execution is
eligible until that manifest has been created and independently accepted.

### 9.3 Canonical receipt envelope and schemas

Every corrected C01 final receipt uses canonical UTF-8 without BOM, sorted-key
compact JSON with one final LF. Each has these exact top-level fields:

- `schema`: one exact schema string listed below;
- `attempt_id`: the lowercase first 16 hex digits of accepted V5 SHA-256;
- `receipt_id`: stable kind plus zero-padded ordinal where applicable;
- `receipt_kind`, `phase`, `created_utc`, and integer `sequence`;
- `producer`: accepted executor canonical path/bytes/SHA-256;
- `authority`: identity-ledger, V5 packet, interpreter, execution-authority,
  PERF-state, and V4-manifest paths/SHA-256 values;
- `predecessor`: either null only for campaign intent, or exact canonical path,
  schema, bytes, and SHA-256 of the immediately preceding durable final;
- `outcome`: exact enum `intent`, `success`, `failure`, or `typed_rejection`;
- `payload`: kind-specific values without omitted required keys;
- `primary_error`: null or typed phase/code/message object;
- `secondary_errors`: ordered array, empty when none.

The exact C01 and terminal schemas are:

| Receipt | Schema |
| --- | --- |
| campaign intent | `anysolver.no_numba_residual.stage_c.campaign_intent/2` |
| C01 trust intent | `anysolver.no_numba_residual.stage_c.c01.trust_intent/1` |
| embedded attempt | `anysolver.no_numba_residual.stage_c.c01.embedded_attempt/1` |
| catalog enumeration | `anysolver.no_numba_residual.stage_c.c01.catalog_enumeration/1` |
| candidate intent | `anysolver.no_numba_residual.stage_c.c01.candidate_intent/1` |
| candidate result | `anysolver.no_numba_residual.stage_c.c01.candidate_result/1` |
| candidate failure | `anysolver.no_numba_residual.stage_c.c01.candidate_failure/1` |
| C01 success | `anysolver.no_numba_residual.stage_c.c01.result/1` |
| C01 failure | `anysolver.no_numba_residual.stage_c.c01.failure/1` |
| top-level success | `anysolver.no_numba_residual.stage_c.result/2` |
| top-level failure | `anysolver.no_numba_residual.stage_c.failure/2` |

The predecessor chain is exact:

1. Campaign intent has `predecessor=null` and is durable before C01.
2. Trust intent points to campaign intent.
3. Embedded attempt points to trust intent.
4. On fallback, catalog enumeration points to embedded attempt.
5. The first candidate intent points to catalog enumeration. Each candidate
   result/failure points to its intent. Each next candidate intent points to the
   prior candidate result/failure.
6. C01 success/failure points to the last applicable embedded, enumeration, or
   candidate final. An embedded non-fallback failure therefore points directly
   to embedded attempt; no-candidate or enumeration failure points to catalog
   enumeration.
7. Top-level success/failure contains `predecessor` pointing to the C01
   success/failure receipt and a `c01_receipt_chain` array listing every C01
   final path/schema/bytes/SHA in sequence order. Existing C02-C05 result data
   remains in its existing payload and is not rewritten into this chain.

Before publishing a successor, the executor closes and reopens the predecessor
final by direct path, verifies non-reparse identity, hashes exact final bytes,
and records that identity. A final receipt never contains its own hash. The
next receipt or top-level terminal receipt supplies it. If intent publication
itself fails, top-level failure points to the last durable campaign intent and
records the intended C01 path plus partial identity in `secondary_errors`. If a
later C01 receipt cannot be promoted, top-level failure points to the last
durable final and records the unpromoted partial without treating it as a
predecessor. No broken or missing predecessor can produce success.

### 9.4 Exact SHA-256 member-hash outcomes

For `CryptCATAdminCalcHashFromFileHandle2`, the sizing call starts with
`cbHash=0`, `pbHash=NULL`, and flags `0`. It must return true and set
`cbHash==32`. Any false return or any other size is typed
`CATALOG_HASH_SIZE_FAILED`; there is no resize or retry.

The fill call allocates exactly 32 zero-initialized bytes, resets `cbHash=32`,
passes flags `0`, and must return true with final `cbHash==32`. False return,
size mutation, short fill, or overrun is typed `CATALOG_HASH_FILL_FAILED`; no
partial hash is accepted. The result is exactly 32 bytes and the member tag is
exactly 64 uppercase ASCII hexadecimal characters. Both calls record boolean
return, requested/final size, raw last error, file position before/after, and
buffer bytes only on complete success.

### 9.5 Candidate materialization, duplicates, sort, and ordinal

Enumeration is completed before any candidate WinTrust call. Every enum result
is first materialized into a raw descriptor containing source enumeration
ordinal, catalog-info path, canonical held path, volume serial, 128-bit file ID,
bytes, lowercase SHA-256, attributes/reparse state, and all API statuses. A
descriptor failure makes enumeration a typed failure; no already materialized
candidate is trusted after incomplete enumeration.

Physical identity key is `(volume_serial, file_id_128)`. Full descriptor key is
`(normalized_path, volume_serial, file_id_128, bytes, sha256)`, where
`normalized_path` is the canonical DOS path with `\\?\` removed and separators
normalized to `\`. Duplicate handling is exact:

- repeated full descriptor keys collapse to one physical candidate while all
  source enumeration ordinals are retained in ascending order;
- multiple paths for one physical identity collapse to one candidate with all
  aliases retained; its display path is the ordinal-lowest path;
- one normalized path resolving to different physical identities or content is
  typed `CATALOG_IDENTITY_CONFLICT` and fails before trust;
- duplicate source ordinals, an empty path, or a descriptor whose held identity
  changes is typed `CATALOG_MATERIALIZATION_INVALID`.

Unique candidates sort with Windows `CompareStringOrdinal(..., TRUE)` on
normalized path. Ties use unsigned numeric volume serial, ordinal byte order of
the 16 file-ID bytes, numeric bytes, lowercase SHA-256 ASCII, then
`CompareStringOrdinal(..., FALSE)` on display path. After this complete stable
sort, candidates receive contiguous zero-based ordinals formatted as four
decimal digits (`0000`, `0001`, ...). Candidate receipt directories use that
ordinal and hash exactly. All candidates are attempted in that order; there is
no early acceptance. The accepted candidate is the lowest ordinal with complete
trust, provider, Microsoft policy, close, and stable-identity success. Every
candidate outcome remains in the C01 chain.

### 9.6 Terminal propagation symbol allowance

Section 8.6 is extended only by these exact new symbols:

- `_canonical_receipt_bytes`;
- `_published_receipt_identity`;
- `_publish_c01_receipt`;
- `_C01ReceiptChain`;
- `_append_c01_receipt`;
- `_c01_chain_snapshot`;
- `_attach_c01_chain_to_terminal_payload`.

Exact call-site hunks are also allowed in the C01 branch and the existing two
top-level atomic terminal-publication call sites, solely to pass the chain head,
ordered chain identities, V4 pre/post inventory identities, and predecessor
object into success or failure. Existing atomic writer semantics may be called
but not weakened. No other terminal, C02-C05, process, Job, timeout, memory,
snapshot, service, command, or cleanup symbol is owned.

This closes plan mechanics only. No source/test/API/WSL/evidence-root/Git/
cleanup/PERF action is authorized, the old root remains immutable, and PERF
remains free.

## 10. Authoritative V4 global-DAG correction

This section supersedes only Section 9.3's global predecessor ordering, its
top-level terminal predecessor rule, the corresponding symbol allowance, and
Section 9.5's same-file-ID alias rule. All other accepted Sections 8 and 9
contracts remain exact.

### 10.1 Actual global receipt order

There are two related but distinct views:

- `global_receipt_chain` is the authoritative chronological chain of every
  durable campaign receipt in the accepted executor order;
- `c01_receipt_chain` is the exact contiguous C01 subset, retained separately
  in top-level success/failure for C01 audit and never substituted for the
  global predecessor.

The global order is exact:

1. `campaign_intent.json` is first and has null predecessor.
2. The existing durable preflight receipt `snapshots/preflight.json` follows
   campaign intent and becomes global head before C01.
3. C01 trust intent points to the preflight receipt, not campaign intent.
4. Embedded, enumeration, candidate, and C01 terminal receipts follow the
   exact internal order in Section 9.3. C01 success or failure becomes global
   head when atomically published.
5. After C01 success, every accepted existing post-C01 receipt, each C02-C05
   result/failure receipt in actual execution order, and every accepted final
   snapshot/receipt is appended to the global chain. Each points to the actual
   current global head immediately before its publication; after its final is
   reopened and hashed, it becomes the new head. Check payloads, argv, schema,
   behavior, containment, timeout, and resource semantics remain unchanged.
6. If an exception path publishes an existing durable exception/check/final-
   snapshot receipt, that receipt is appended and becomes the global head. If
   its publication fails, the head remains the last successfully published
   final and the publication failure is retained as a secondary error.
7. Top-level success or failure points to the actual global head at terminal
   publication. It never forces its predecessor back to the C01 terminal.

Top-level success/failure contains both `global_receipt_chain` and
`c01_receipt_chain`. Each is an ordered array of canonical path, schema, bytes,
SHA-256, sequence, and predecessor identity. The C01 array must equal the
contiguous C01 slice of the global array exactly. The top-level predecessor
must equal the final entry of `global_receipt_chain`. Empty, skipped,
duplicated, reordered, or divergent entries fail closed.

On C01 failure there are no post-C01 check receipts; the C01 failure is normally
the global head unless a later durable exception/final-snapshot receipt was
published. On success, C02-C05/final receipts advance the head. This preserves
the accepted executor's actual chronology and crash evidence.

### 10.2 Compatible check schemas and explicitly owned terminal schemas

Existing preflight, post-C01, C02-C05, exception, and final-snapshot receipt
schema strings and payloads remain compatible and are not version-bumped by
this correction. Their existing atomic publication call sites are owned only
to receive the prior global head, register the published final identity, and
advance the in-memory/durable global chain; no check-specific payload or
behavior may change.

The changed top-level schema constants are explicitly owned and exact:

- `_STAGE_C_RESULT_SCHEMA_V2 = "anysolver.no_numba_residual.stage_c.result/2"`;
- `_STAGE_C_FAILURE_SCHEMA_V2 = "anysolver.no_numba_residual.stage_c.failure/2"`.

The additional exact owned symbols are:

- `_GlobalReceiptChain`;
- `_append_global_receipt`;
- `_global_chain_snapshot`;
- `_bind_global_predecessor`;
- `_STAGE_C_RESULT_SCHEMA_V2`;
- `_STAGE_C_FAILURE_SCHEMA_V2`.

Allowed call-site hunks are limited to the existing campaign-intent/preflight
handoff, C01 entry/exit, each existing post-C01/C02-C05/final or exception
receipt publication, and the two top-level terminal publications. They may
only propagate/hash the global head and attach the two chain arrays. C02-C05
production/check symbols remain outside ownership. Independent exact-diff
review must reject any other schema constant, publication site, or behavior
change.

### 10.3 Corrected alias conflict rule

Aliases sharing one `(volume_serial, file_id_128)` collapse only if `bytes` and
SHA-256 are also exactly equal. They retain every source path and enumeration
ordinal, with the ordinal-lowest normalized path as display path. If any alias
for the same physical identity differs in bytes or SHA-256, materialization
fails before trust with typed `CATALOG_IDENTITY_CONFLICT`. There is no collapse,
selection, retry, or acceptance in that case. The existing rule for one
normalized path resolving to differing physical/content identities remains the
same typed conflict.

This is a plan-only chronology correction. No source/test/API/WSL/evidence/
Git/cleanup/PERF action is authorized; V4 remains immutable and PERF free.

## 11. Authoritative V5 final mechanical closure

This section supersedes only the campaign-intent constant ownership,
`_run_contained_wsl` receipt propagation boundary, and empty-chain rules above.
No process, Job, receipt payload, science, command, timeout, resource, or C02-C05
behavior changes.

### 11.1 Campaign-intent schema ownership

The changed campaign-intent schema constant is explicitly owned:

`_STAGE_C_CAMPAIGN_INTENT_SCHEMA_V2 = "anysolver.no_numba_residual.stage_c.campaign_intent/2"`

Its constant definition and the one existing campaign-intent payload/publication
call site are allowed exact-diff hunks. The payload change is limited to the
accepted identity-ledger/V4-manifest authority fields and global-chain seed.
No other campaign initialization, path, freshness, deadline, or publication
semantics may change.

### 11.2 Internal Job/process receipt propagation

`_run_contained_wsl` remains behaviorally frozen but its signature and existing
internal durable-receipt publication sites are explicitly owned for chain
propagation only. Its signature adds exactly one keyword-only parameter:

`receipt_chain: _GlobalReceiptChain`

Its existing return type and every other parameter remain unchanged. At entry,
the supplied chain head is the exact durable receipt preceding the contained
call. Immediately after each existing internal Job/process intent, start,
process, transcript, result, failure, timeout, termination, wait, residual, or
all-outcome receipt is atomically promoted, the function reopens and hashes that
final and calls `_append_global_receipt` once. The first such receipt points to
the supplied head; each later receipt points to the prior internal final. The
actual last durable internal receipt is therefore the global head before normal
return or exception propagation.

No new internal receipt is invented, no existing receipt schema or payload is
changed, and no reverse reconstruction is used. If an internal publication
fails before promotion, it is not appended; the chain remains at the actual
last durable final and the publication error follows existing failure handling.
If `_run_contained_wsl` fails before any internal durable final, the supplied
head remains unchanged. The allowed hunks are only the keyword-only signature,
the existing caller's exact argument, and one append call directly after each
existing successful atomic promotion. Process creation, creation-time Job
assignment, handles, waits, termination, timeout, memory, snapshots, residual
proof, stdout/stderr, command argv, and exceptions remain outside ownership.

Independent review must enumerate the accepted function's internal atomic
promotion sites and prove a one-to-one append after every site, no append before
promotion, no skipped durable final, no duplicate append, and no other hunk in
the function.

### 11.3 Truthful empty-chain cases

Top-level success requires nonempty `global_receipt_chain` and nonempty
`c01_receipt_chain`. Their terminal identities and subset relationship must pass
Section 10 exactly; an empty success chain is impossible and fail-closed.

Top-level failure permits `global_receipt_chain=[]` and `predecessor=null` only
when failure occurred before `campaign_intent.json` became a durable final. That
failure must record `pre_durable_failure=true`, the intended campaign-intent
path, primary phase/error, and any owned partial identity. No placeholder or
synthetic predecessor is allowed.

Top-level failure permits `c01_receipt_chain=[]` only when failure occurred
before C01 `trust_intent.json` became a durable final, including campaign-intent
or preflight failure. The global chain may still be nonempty and its predecessor
must be its actual last durable entry. Once trust intent is durable, every
terminal failure must carry a nonempty C01 chain beginning with that intent and
ending at the actual last durable C01 final. No null, placeholder, skipped, or
fabricated chain entry is allowed.

This completes plan mechanics only. No source/test/API/WSL/evidence/Git/
cleanup/PERF action is authorized; V4 remains immutable and PERF remains free.

## 12. Authoritative V6 post-promotion registration failure

This section supersedes only Section 11.2's handling of a failure inside
`_append_global_receipt` after an atomic promotion has already succeeded. It
chooses the required fail-stop, out-of-band evidence-limited branch; it does not
claim that the prior global head still describes all durable finals.

### 12.1 Dedicated fatal state

If reopen, direct-path identity, bytes, SHA-256, schema, predecessor, sequence,
or chain validation fails after a receipt final was atomically promoted,
`_append_global_receipt` raises exactly `_ReceiptRegistrationLost`. The object
retains in memory:

- promoted canonical path and receipt kind/sequence;
- expected canonical bytes count/SHA-256 computed before promotion;
- prior global head path/schema/bytes/SHA-256;
- atomic promotion completion UTC;
- failing registration phase, exception type/message, and any safely available
  direct-file identity;
- `durable_final_exists=true`, `registered_in_global_chain=false`, and
  `evidence_status=evidence_limited`.

The promoted final is never deleted, replaced, renamed, rewritten, or treated
as absent. The prior head remains the last registered entry but is not reported
as the latest durable receipt.

### 12.2 No in-root successor or terminal publication

`_ReceiptRegistrationLost` bypasses every ordinary exception/check/final-
snapshot/top-level success/top-level failure publisher. After it is raised,
there is no further durable write or promotion anywhere under the corrected
evidence root. In particular, no successor, exception receipt,
`stage_c_result.json`, or `stage_c_failure.json` may be created. This prevents a
false predecessor claim and preserves the unregistered promoted final exactly.

The host emits one bounded canonical JSON diagnostic to the already captured
stderr stream and exits nonzero after containment. That stream is transport
evidence only; it is never represented as an in-root receipt. The separately
accepted execution authority must bind an external transcript/process-result
identity before launch. Boss review records the nonzero exit, stderr object,
promoted path, and residual-process truth as an out-of-band
`evidence_limited_registration_loss`; any repair or chain recovery requires a
new content-addressed plan and may not occur in the failed campaign.

### 12.3 Required process containment before exit

At every point where an internal Job/process receipt can be promoted, all task
children are already creation-time members of the accepted non-inheritable
kill-on-close Job Object and the host retains the Job and process handles. No
uncontained task child is permitted. On `_ReceiptRegistrationLost`:

1. no new child or durable receipt is created;
2. any active contained Job is terminated through the existing exactly-once
   termination path, then retained process handles are waited/reaped and zero
   live Job PID is required;
3. if Job termination is nonterminal, the accepted retained-handle direct
   termination/wait/reap path runs exactly once;
4. containment outcomes are emitted only in the bounded stderr diagnostic and
   observed by the external process transcript; no in-root cleanup or receipt
   is attempted;
5. the host exits nonzero. A containment failure remains terminal and
   evidence-limited; it never authorizes another publication or retry.

For host-only C01 phases before a WSL child exists, the same branch proves no
task child was launched and exits nonzero without creating one.

### 12.4 Exact symbol and catch-site allowance

The exact additional owned symbols are:

- `_ReceiptRegistrationLost`;
- `_registration_loss_diagnostic`;
- `_abort_after_receipt_registration_loss`.

Allowed hunks are limited to the raise site in `_append_global_receipt`, the
outermost catch placed before every generic terminal-publication catch, and
calls to existing exactly-once containment primitives. The catch must never
fall through to ordinary terminal publication. Independent review must prove
that a simulated post-promotion registration failure leaves exactly the
promoted final plus preexisting evidence, creates no later in-root final,
terminates/reaps every contained child, exits nonzero, and preserves the prior
primary registration error.

This is the sole all-outcome exception to durable in-root terminal publication.
It is fail-stop rather than a fabricated chain. No source/test/API/WSL/evidence/
Git/cleanup/PERF action is authorized now; V4 remains immutable and PERF free.

## 13. Authoritative V7 nested bypass and external capture

This section supersedes only Section 12's catch reachability, absolute-write
wording, diagnostic framing, and external evidence contract. Its fail-stop and
no-recovery decision remains exact.

### 13.1 Branch before every publishing catch

Every `except BaseException` or `except Exception` on a path that can catch
`_ReceiptRegistrationLost` before the outer boundary receives a dedicated
`except _ReceiptRegistrationLost` branch immediately before the publishing
catch. This includes every prospective C01 publisher and every nested publisher
inside `_run_contained_wsl`. The dedicated branch never invokes an ordinary
failure, exception, snapshot, result, or terminal publisher.

Containment runs at the innermost scope that still owns the relevant Job and
process handles:

- a C01/host-only scope attaches immutable outcome `no_child_created` and
  rethrows;
- `_run_contained_wsl` terminates/waits/reaps through its existing exactly-once
  primitives while its handles remain valid, then attaches the immutable local
  outcome and rethrows;
- every outer dedicated branch sees the attached outcome, performs no second
  containment action, and rethrows until the outermost boundary emits the sole
  stderr diagnostic and exits nonzero.

`_RegistrationLossContainmentOutcome` is an exact frozen value object with
`owner_scope`, `started_utc`, `completed_utc`, Job identity, process PID,
pre/post live-PID arrays, ordered actions/results, terminal/zero-PID booleans,
and ordered containment errors. `_ReceiptRegistrationLost` is immutable;
`with_containment_outcome(outcome)` returns a new immutable exception retaining
the original traceback/cause and all registration-loss fields. It rejects a
second attachment. The outermost branch requires exactly one attached outcome
and never repeats containment.

Independent exact-diff review enumerates every broad publishing catch in the
accepted executor plus prospective C01 helpers and proves the dedicated branch
precedes it. A missing, reordered, publishing, swallowing, or double-
containment branch fails review.

### 13.2 Host publication prohibition and truthful child partials

After registration loss, the host creates no successor path, writes no new host
evidence payload, and performs no host promotion, rename, finalization, or
top-level publication under the corrected evidence root. It does not modify or
delete any existing final or partial.

An already running contained child may continue writing only through raw
stdout/stderr/transcript partial handles that were opened before the loss, until
the local owning scope terminates and reaps it. Those bytes are truthful but
unregistered. The host never promotes, renames, finalizes, truncates, deletes,
or interprets those partials afterward. They remain preserved as
`evidence_limited` raw partials. No new child, handle, or evidence file may be
created. This child-write allowance replaces Section 12's broader phrase "no
further durable write" without permitting any host successor or finalization.

### 13.3 Exact stderr diagnostic frame

The outermost branch emits at most one diagnostic frame. Its schema is exactly
`anysolver.no_numba_residual.stage_c.registration_loss_stderr/1`. It is
sorted-key compact JSON encoded as UTF-8 without BOM or CR, followed by exactly
one LF. `ensure_ascii=true` is required. The complete frame, including LF, is
at most `16,384` bytes and is written by one direct unbuffered stderr write; no
logger prefix, second frame, retry, or stdout duplicate is permitted.

The untruncated payload has exact keys: `schema`, `attempt_id`, `event`,
`created_utc`, `promoted_receipt`, `prior_global_head`, `registration_error`,
`containment_outcome`, `host_successor_publication_prohibited=true`,
`raw_partials_may_have_advanced`, `evidence_status="evidence_limited"`, and
`truncated=false`. Receipt/head identities contain canonical path, schema,
sequence, expected bytes, and expected SHA-256. Error contains phase, exception
type/message, and ordered secondary errors.

If canonical full framing would exceed `16,384` bytes, the host emits one valid
replacement frame under the same schema with `truncated=true`, the same fixed
identity/containment booleans, `full_frame_bytes`, `full_frame_sha256`, and
`omitted_fields` as an ordinal-sorted array. Variable messages and action detail
are omitted rather than byte-sliced. The replacement frame must itself be at
most `16,384` bytes; otherwise no frame is written and the external producer
records `diagnostic_frame_unavailable`. A short/failed stderr write is never
retried and is recorded from actual captured bytes after exit.

### 13.4 Prebound external capture contract

Before any future corrected execution, the accepted V5 SHA prefix derives a
fresh sibling transport root exactly:

`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-<first-16-lowercase-V5-SHA256>-transport`

The execution-authority receipt must bind that absent, non-reparse root and one
independently accepted external producer with schema
`anysolver.no_numba_residual.stage_c.external_capture_producer/1`, canonical
producer path/bytes/SHA-256, exact executor argv, and these CreateNew paths:

- `executor.stdout.bin.partial` -> `executor.stdout.bin`;
- `executor.stderr.bin.partial` -> `executor.stderr.bin`;
- `executor.process_result.json.partial` -> `executor.process_result.json`.

The external producer is outside the executor/evidence root and never imports
the executor. It creates raw stdout/stderr capture handles before process
launch, passes only those exact handles, records PID/start UTC, waits for the
host, proves terminal exit and residual task-process state, flushes the raw
captures, then atomically promotes them without replacement. Only after both
raw finals exist does it publish canonical UTF-8/sorted-key/one-LF process
result schema
`anysolver.no_numba_residual.stage_c.external_process_result/1`.

The process result contains producer/executor/packet/ledger/authority/PERF
identities; argv; PID; start/end UTC; exit code; timeout; process-tree and
residual proof; stdout/stderr canonical paths, bytes, and SHA-256; exact count
and byte range of valid registration-loss frames; parsed frame or parse error;
expected promoted path; and `evidence_status`. Registration loss requires a
nonzero host exit and exactly one valid frame unless the actual stderr write was
short/failed, in which case raw stderr identity plus
`diagnostic_frame_unavailable` remains truthful evidence-limited failure.

Producer failure preserves owned partials and publishes no process-result
final. No actor retries, repairs, overwrites, cleans, or promotes on its behalf.
The producer source and external paths require separate content-addressed review
and authority; they are not authorized or created by this plan.

### 13.5 Additional exact symbol allowance

The exact additional owned symbols are:

- `_RegistrationLossContainmentOutcome`;
- `_ReceiptRegistrationLost.with_containment_outcome`;
- `_registration_loss_stderr_frame`.

Also owned are only the dedicated pre-publisher catch branches described in
Section 13.1 and the outermost single unbuffered stderr write. All ordinary
publisher bodies and containment primitives remain unchanged.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 19. Authoritative V13 pre-Job routing and non-overriding finalizer

This section supersedes only Section 18's reachability of ordinary prelaunch
publication and the timing of terminal/fatal emission relative to
`_release_campaign_wsl_hold()`. The 0/1/2-final lanes, fatal bypasses, exit
codes, external classification, and no-action boundary remain exact.

### 19.1 Fatal-bypass-first envelope for the two pre-Job writes

Exactly two accepted writes precede `_run_contained_wsl`'s current ordinary
catch: `job_intent` and `creation_attributes_intent`. They are wrapped together
in one narrow enclosing boundary that ends before any Job/process creation or
later run logic. Catch order is exact:

1. `except _ReceiptRegistrationLost`: attach the reserved-run immutable
   `no_child_created` outcome if none is attached, then rethrow; do not invoke
   the ordinary publisher.
2. `except _ContainmentProofLost`: rethrow unchanged; this type is not converted
   to ordinary failure.
3. `except BaseException as error`: create/retain the reserved-run
   `no_child_created` proof and route exactly once to the existing ordered
   two-final ordinary failure publisher.

The ordinary catch is eligible only when the failing `_atomic_json` reports
`promoted=false`. If promotion succeeded and later chain registration failed,
the first fatal branch owns it. The envelope cannot catch errors raised by the
two-final publisher itself, so publisher failure cannot recursively invoke the
publisher. A frozen one-shot guard records `ordinary_publisher_invoked=true`
before entry and rejects a second call.

### 19.2 Structured pre-Job failure transport

The exact frozen transport object is `_PreJobOrdinaryFailureContext`. It has:

- reserved `run_id`, run-material SHA-256, and failing site exactly
  `job_intent` or `creation_attributes_intent`;
- actual prior global-head path/schema/sequence/bytes/SHA-256, or null only when
  truthfully no durable head exists;
- target final path, owned partial path/bytes/SHA-256 when safely readable, and
  `promoted=false`;
- primary phase, exception type, full-message SHA-256, and ordered secondary
  errors;
- immutable `no_child_created` proof identity;
- `ordinary_publisher_invoked` and UTC.

It is passed keyword-only as `prejob_failure` to the existing two-final
ordinary publisher. It may supply the primary failure and actual chain head but
does not add or alter either internal failure-final payload. It is retained in
host state for the pending top-level failure payload under exact field
`ordinary_prejob_failure`. That top-level field is explicitly owned; no other
receipt payload is changed. If final 1 or final 2 fails before promotion, the
context is immutably extended with the actual 0/1-final result and preserved
partial identity before top-level failure construction.

The exact additional owned symbols are:

- `_PreJobOrdinaryFailureContext`;
- `_route_prejob_ordinary_failure_once`.

Allowed hunks are limited to the enclosing three-branch boundary, one-shot
route, keyword-only publisher argument, and the pending top-level failure field.

### 19.3 Finalizer cannot replace selected outcome

`main()` maintains immutable pending campaign outcome containing selected exit
class/code, pending top-level payload when applicable, pending fatal diagnostic
when applicable, and primary error. No top-level terminal or fatal stderr frame
is emitted before the WSL-hold finalizer has completed.

Its `finally` executes `_release_campaign_wsl_hold()` inside a nested
non-publishing `try/except BaseException`. The call produces frozen
`_CampaignWslHoldReleaseOutcome` with attempted/success booleans, start/end UTC,
pre/post hold identity/state, and on failure phase/type/code/full-message
SHA-256. The finalizer catch never raises, returns, changes selected code,
replaces primary error, invokes containment, or writes evidence.

After `finally`:

- pending success/ordinary failure adds exact
  `campaign_wsl_hold_release_outcome` to its sole top-level `/2` payload and
  then performs the existing one atomic terminal publication/validation;
- pending registration loss or containment-proof loss adds the outcome to its
  sole fatal diagnostic frame and then performs the existing single stderr
  write;
- no second fatal frame, top-level terminal, exception receipt, or finalizer
  publication is created.

If hold release failed, the selected numeric code remains exactly `0`, `1`,
`86`, or `87`. For `0`/`1`, independent top-level validation requires
`campaign_wsl_hold_release_outcome.success=true` for qualification; false yields
external classification `campaign_wsl_hold_release_failed`, evidence-limited,
despite the preserved selected code. For `86`/`87`, the mandatory fatal frame
contains the failed outcome and external classification remains the selected
fatal type. Thus finalizer truth is recorded without overriding or obscuring
the primary outcome.

If later top-level terminal registration itself is lost, the existing
registration-loss transition may select exit `86`; that is a new terminal
evidence failure, not finalizer override. No finalizer is run twice.

### 19.4 Exact finalizer ownership

The exact additional owned symbols are:

- `_PendingStageCOutcome`;
- `_CampaignWslHoldReleaseOutcome`;
- `_capture_campaign_wsl_hold_release`.

Allowed call-site hunks are limited to deferring the existing sole terminal or
fatal emission, nesting the existing finalizer call, attaching its frozen
outcome, and emitting once afterward. `_release_campaign_wsl_hold()` itself,
its hold semantics, all process/Job logic, and C01-C05 behavior remain
unchanged.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 18. Authoritative V12 pre-promotion failure and exit classification

This section supersedes only Section 17's ordinary prelaunch/failure-final
coverage and external nonzero-exit classification. Existing post-promotion
registration-loss prefixes, terminal reopening, chain-only metadata, numeric
precedence, C05/inter-run lanes, and distinct fatal schemas remain exact.

### 18.1 Ordinary prelaunch failure after run reservation

After the caller has reserved a valid run ID but before child creation, an
ordinary prelaunch failure uses the immutable `no_child_created` proof bound to
that run ID. It enters the existing ordinary internal failure publisher, which
has the two real ordered final sites already labeled
`internal-failure-final-1` and `internal-failure-final-2`. No process or Job is
created and no contained action is inferred.

The atomic JSON helper distinguishes failure before final promotion from
failure after promotion. `_AtomicJsonPrePromotionFailure` records target path,
owned partial path/identity when present, phase, primary exception, and
`promoted=false`. The partial is preserved and is never a receipt or chain
consumer. Only a successfully promoted and subsequently registered final is a
consumer.

The exhaustive ordinary prelaunch/failure-publication outcomes are:

| Outcome | Actual registered failure finals | Global head for later top-level failure |
| --- | --- | --- |
| final-1 `_atomic_json` fails before promotion | none | predecessor that existed before the failure publisher |
| final-1 registers; final-2 `_atomic_json` fails before promotion | `internal-failure-final-1` | final 1 |
| both `_atomic_json` calls promote and both append successfully | `internal-failure-final-1`, `internal-failure-final-2` | final 2 |

Each lane may then publish the deterministic top-level failure outside the
global chain. Its payload records the actual head, exact absent/preserved
partial identities, and ordinary publication error. The corresponding proof
consumer sequence is respectively:

- `[top-level-failure-published]`;
- `[internal-failure-final-1, top-level-failure-published]`;
- `[internal-failure-final-1, internal-failure-final-2, top-level-failure-published]`.

There is no missing-final placeholder and no synthetic outer failure result or
snapshot.

These pre-promotion paths are distinct from `_ReceiptRegistrationLost`:

- if final 1 is atomically promoted but its append fails, registered prefix is
  `[]` and promoted-unregistered identity is final 1;
- if final 1 registered and final 2 is promoted but its append fails, prefix is
  `[internal-failure-final-1]` and promoted-unregistered identity is final 2.

Those two cases retain Section 17's fatal no-successor behavior and never enter
ordinary top-level failure publication.

### 18.2 Exact process exit codes

The host's exact exit constants are explicitly owned:

- `_EXIT_STAGE_C_SUCCESS = 0`;
- `_EXIT_STAGE_C_ORDINARY_FAILURE = 1`;
- `_EXIT_STAGE_C_REGISTRATION_LOSS = 86`;
- `_EXIT_STAGE_C_CONTAINMENT_PROOF_LOSS = 87`.

The outermost registration-loss branch emits or attempts its one frame and then
returns exactly `86`. The containment-proof-loss branch returns exactly `87`.
Frame write success, short write, write failure, truncation, or frame parseability
never changes the fatal exit code. Ordinary handled failure returns `1`; success
returns `0`. Any other exit code is unclassified infrastructure/process truth
and is never coerced to ordinary failure.

The final `__main__` boundary passes this small nonnegative integer to the
process exit unchanged. No nested broad catch may intercept or rewrite a fatal
classification after the outermost branch selects it.

### 18.3 External classification matrix

The external producer classifies only by exact exit code plus independent file
and raw-stream evidence:

| Exit | Required classification |
| ---: | --- |
| `0` | require independently valid `stage_c_result.json`; otherwise `success_terminal_validation_failed` |
| `1` | ordinary failure only if `stage_c_failure.json` independently validates; absent/invalid final is `ordinary_failure_terminal_unavailable`, evidence-limited |
| `86` | registration loss regardless of frame availability; never ordinary |
| `87` | containment-proof loss regardless of frame availability; never ordinary |
| any other | `unclassified_nonzero_exit`, evidence-limited |

For exit `86`, a valid registration-loss frame strengthens classification. A
short, invalid, missing, or unavailable frame yields
`registration_loss_frame_unavailable` while retaining exit code, raw stderr
bytes/SHA, actual durable root inventory, and process truth. For exit `87`, the
analogous classification is `containment_proof_loss_frame_unavailable`.

A valid fatal frame whose schema disagrees with exit `86`/`87`, or a fatal frame
on exit `0`/`1`, is `fatal_exit_frame_mismatch`; evidence remains limited and no
ordinary/success qualification is made. Fatal exits require no ordinary
`stage_c_failure.json`. If a fatal frame or root inventory identifies a top-
level final as promoted but unregistered, that file is preserved and reported
only as the fatal promoted receipt, never reopened as an ordinary terminal.

The external process result records `exit_classification`, exact exit code,
expected/observed fatal schema, frame availability/parse result, deterministic
terminal-file inventory, and the independent terminal validation object. It may
not infer ordinary failure solely from a nonzero exit or missing fatal frame.

### 18.4 Exact additional ownership

The exact additional owned symbols are:

- `_AtomicJsonPrePromotionFailure`;
- `_EXIT_STAGE_C_SUCCESS`;
- `_EXIT_STAGE_C_ORDINARY_FAILURE`;
- `_EXIT_STAGE_C_REGISTRATION_LOSS`;
- `_EXIT_STAGE_C_CONTAINMENT_PROOF_LOSS`.

Allowed hunks are limited to annotating the atomic helper's pre-promotion
failure, the ordinary two-final branch accounting, outer fatal return values,
and final process-exit forwarding. Atomic promotion semantics, existing final
paths/payloads, process containment, and every C02-C05 behavior remain outside
ownership.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 17. Authoritative V11 exhaustive lanes and external terminal validation

This section supersedes only Section 16's non-exhaustive lane table, its claim
about externally observing an in-memory mark, its receipt-payload allowance,
and its physical-order sentence. Numeric precedence alone is authoritative:
the highest numbered section controls only its named conflicts. No claim about
the physical placement of Section 15 relative to Section 14 is retained.

### 17.1 Existing receipt roles and registration-loss prefixes

Consumer IDs are chain-metadata labels for existing atomic publication sites;
they do not create files. The ordinary internal failure branch has exactly two
existing durable failure-final promotion sites, identified without inventing an
outer result or snapshot:

- `run:<run_id>:internal-failure-final-1`: the first existing atomic final in
  `_run_contained_wsl`'s ordinary process/Job failure publisher;
- `run:<run_id>:internal-failure-final-2`: the second existing atomic final in
  that same publisher, after final 1.

Independent source review must map those two labels one-to-one to the two
accepted source promotion sites and their actual paths. The labels never imply
a third internal final.

Registration-loss prefixes for that branch are exact:

| Loss point | Registered consumer prefix | Promoted but unregistered |
| --- | --- | --- |
| final 1 append | `[]` | `internal-failure-final-1` |
| final 2 append | `[internal-failure-final-1]` | `internal-failure-final-2` |
| later top-level failure validation | `[internal-failure-final-1, internal-failure-final-2]` | deterministic top-level failure final |

At registration loss, `observed_consumer_ids` is exactly the applicable prefix,
`attempted_consumer_id` identifies the promoted unregistered final, and no
remaining lane consumer is attempted.

### 17.2 Exhaustive outer/campaign branch table

The exact existing outer chain labels are:

- `run:<run_id>:outer-result`, only after the existing outer result final;
- `run:<run_id>:post-check-snapshot`, only after the existing post-check
  snapshot final;
- `run:<run_id>:campaign-final-snapshot`, only after the existing C05 campaign
  final-snapshot final.

Top-level publication labels are post-publication marks, not chain entries:
`run:<run_id>:top-level-success-published` and
`run:<run_id>:top-level-failure-published`.

The exhaustive lanes are:

| Actual branch | Existing chain consumers in order | Post-publication terminal mark |
| --- | --- | --- |
| internal process/Job failure | `internal-failure-final-1`, `internal-failure-final-2` | `top-level-failure-published` |
| semantic failure after contained return, before outer result promotion | none beyond the already registered contained-run prefix | `top-level-failure-published` |
| other pre-result failure after contained return | none beyond the already registered contained-run prefix | `top-level-failure-published` |
| outer result promoted, then post-check snapshot fails before promotion | `outer-result` | `top-level-failure-published` |
| C02-C04 success followed by next-run reservation | `outer-result`, `post-check-snapshot` | none |
| C02-C04 inter-run failure after prior post-check registration but before next-run reservation | no new run consumer; prior run remains complete | campaign-scoped `top-level-failure-published` with no proof re-consumption |
| C05 failure after result/post-check but before campaign final-snapshot promotion | `outer-result`, `post-check-snapshot` | `top-level-failure-published` |
| C05 failure after campaign final-snapshot promotion during later validation | `outer-result`, `post-check-snapshot`, `campaign-final-snapshot` | `top-level-failure-published` |
| C05 success | `outer-result`, `post-check-snapshot`, `campaign-final-snapshot` | `top-level-success-published` |

The "already registered contained-run prefix" is the exact normal-terminal
internal prefix established by the three accepted post-close promotions and is
not restated as a new outer receipt. A C02-C04 inter-run failure occurs when no
new run has been reserved; it uses the actual prior global head, creates no run
consumer, and may not reopen or re-consume the completed prior proof. Its
terminal payload records an exact campaign-scoped failure phase instead.

For every lane, registration loss may occur at any existing chain promotion.
The observed consumer list is exactly the successfully registered prefix, and
the attempted consumer is the one promoted final that failed registration.
There is no synthetic failure-result, failure-snapshot, or missing-site label.

### 17.3 Acyclic deterministic terminal reopen contract

The in-memory `_TopLevelPublicationMark` remains a host-local proof-retention
mechanism only. It is never claimed as externally observable, never serialized,
and never referenced by the external producer.

After host exit and process-tree terminal proof, the external producer derives
the only eligible deterministic top-level final path:

- host exit `0`: `<corrected-root>\stage_c_result.json` with exact schema
  `anysolver.no_numba_residual.stage_c.result/2`;
- ordinary nonzero exit without either fatal stderr schema:
  `<corrected-root>\stage_c_failure.json` with exact schema
  `anysolver.no_numba_residual.stage_c.failure/2`;
- registration-loss or containment-proof-loss fatal frame: neither top-level
  final is eligible, except that a top-level final named as the frame's promoted
  unregistered receipt is preserved and classified exactly as such.

The producer opens the eligible final read-only with reparse rejection and no
write/delete sharing, records canonical path and direct file identity, reads
exact bytes once, computes bytes/SHA-256, parses strict canonical JSON, and
validates schema, attempt/authority identities, outcome versus exit code,
predecessor, global/C01 chain arrays, V4 pre/final inventory identities, and
that no opposite terminal final exists. It repeats direct file identity after
read and requires stability before acceptance.

The external process-result schema remains
`anysolver.no_numba_residual.stage_c.external_process_result/1` and records
`top_level_final_validation` with path, schema, bytes, SHA-256, file identity,
validation booleans/errors, and terminal-fatal classification. It contains no
publication-mark field. Reopen, identity, parse, schema, chain, opposite-file,
or outcome mismatch sets `evidence_status="terminal_validation_failed"`; it
preserves captures/root and makes no success/failure qualification claim. No
retry, repair, or replacement follows.

### 17.4 Run and consumer metadata location

Run/consumer metadata does not alter existing internal, outer-result,
post-check, campaign-final, or failure receipt payloads or schema strings. The
Section 16.3 allowance for adding `run_id`,
`run_identity_material_sha256`, or `consumer_receipt_id` to those payloads is
withdrawn.

Metadata lives only in `_GlobalReceiptChain` nodes and the top-level serialized
chain arrays. Each chain node uses schema
`anysolver.no_numba_residual.stage_c.global_receipt_chain_node/1` and contains
receipt canonical path/schema/bytes/SHA-256, predecessor identity, sequence,
and optional `run_context` with run ID, run-material SHA-256, consumer ID, and
terminal-proof identity. Existing receipt bytes remain unchanged.

Owned hunks are limited to passing this metadata as separate arguments to
`_append_global_receipt`, storing it in `_GlobalReceiptChain`, serializing chain
nodes in the two top-level payload builders, and external validation of those
nodes. The exact `_run_contained_wsl` keyword-only signature from Section 16.3
remains owned, but no existing receipt builder/payload is owned for run or
consumer fields.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 16. Authoritative V10 branch-accurate consumers and fatal states

Numeric precedence is explicit: where wording conflicts, Section 16 supersedes
Section 15, which supersedes Section 14, and so on in descending section order.
Section 15 is physically after Section 14 and remains authoritative except for
the exact branch table, terminal-chain rule, signature/payload boundary, and
containment-proof-loss handling replaced here.

### 16.1 Actual branch consumer sets

No outer failure result or outer failure snapshot is invented. A consumer ID is
marked only after the corresponding accepted existing final was actually
promoted and registered, or after a top-level terminal was atomically published
and validated under Section 16.2.

The exact IDs are:

- `run:<run_id>:contained-failure`, only for the existing internal
  process/Job failure final published by `_run_contained_wsl`;
- `run:<run_id>:outer-result`, only for an existing successful outer check
  result final;
- `run:<run_id>:post-check-snapshot`, only for an existing post-check snapshot
  final after an outer result;
- `run:<run_id>:campaign-final`, only for the existing C05 successful campaign
  final;
- `run:<run_id>:top-level-success-published` or
  `run:<run_id>:top-level-failure-published`, only as the acyclic
  post-publication mark in Section 16.2.

The exact lane table replaces Section 15.2:

| Actual lane | Required ordered consumers | Count |
| --- | --- | ---: |
| internal process/Job failure | `contained-failure`, `top-level-failure-published` | 2 |
| semantic failure after contained return but before outer result | `top-level-failure-published` | 1 |
| other pre-result failure after contained return | `top-level-failure-published` | 1 |
| outer result promoted, then post-check snapshot fails before promotion | `outer-result`, `top-level-failure-published` | 2 |
| C02-C04 success | `outer-result`, `post-check-snapshot` | 2 |
| C05 success | `outer-result`, `post-check-snapshot`, `campaign-final`, `top-level-success-published` | 4 |

An internal failure lane has no outer result or post-check snapshot consumer. A
semantic or pre-result failure has neither. A result-then-snapshot failure has
the outer result but not a snapshot consumer. The top-level failure payload
records the actual global head and failure phase; it does not synthesize the
missing receipts.

Lane selection occurs at the first branch-discriminating event and is immutable
thereafter. Before that event the proof carries the exact finite allowed-lane
set; marking a consumer eliminates incompatible lanes. If failure chooses a
lane, the expected sequence becomes exact before terminal publication. Any
receipt inconsistent with the selected lane fails closed. Proof retention lasts
through the post-publication terminal mark when that lane includes one.

### 16.2 Top-level terminals remain outside their contained chain

`stage_c_result.json` and `stage_c_failure.json` are never entries in
`global_receipt_chain` or `c01_receipt_chain`. Their payloads contain immutable
snapshots of those chains ending at the actual latest pre-terminal durable
receipt, and their `predecessor` equals that chain head. This removes terminal
self-membership and every hash cycle.

After a top-level terminal is atomically promoted, the host reopens and
validates its exact path/schema/bytes/SHA-256. It then creates only an in-memory
immutable `_TopLevelPublicationMark` with terminal kind, terminal identity,
contained global-head identity, run ID, UTC, and matching success/failure
consumer ID. The mark is not a receipt, is never added to either serialized
chain, and causes no successor publication. It may consume the retained proof
only after terminal validation succeeds.

The external process-result receipt durably records the terminal identity and
post-publication mark fields after host exit. If terminal reopen/hash/validation
fails after promotion, Section 13 registration-loss fail-stop applies with the
terminal as `promoted_receipt`; no mark is created and the proof remains
retained. Thus publication evidence is acyclic and truthful.

### 16.3 Explicit signature and payload supersession

Section 11.2's statement that `_run_contained_wsl` gains exactly one keyword-
only parameter is superseded. The exact added keyword-only parameters are:

`receipt_chain: _GlobalReceiptChain, run_id: str, run_identity_material: Mapping[str, object]`

The existing return type remains unchanged. Section 11.2's absolute no-payload-
change sentence is also superseded only to allow exact fields `run_id`,
`run_identity_material_sha256`, and `consumer_receipt_id` in existing internal
receipt envelopes. No existing payload value, process data, schema, argv,
timeout, Job, or resource semantics may otherwise change.

The exact additional owned symbol is `_TopLevelPublicationMark`; allowed hunks
are its creation after terminal validation and proof consumption using the
matching post-publication consumer ID.

### 16.4 Distinct containment-proof-loss fatal state

Failure to prove ordinary containment terminality is not receipt-registration
loss. If ordinary failure handling cannot establish terminal process state,
zero Job PID, or required retained-handle close truth before failure-receipt
promotion, it raises immutable `_ContainmentProofLost`. No ordinary failure
receipt is promoted, no `_ReceiptRegistrationLost` is constructed, and no
registration-loss schema is reused.

The outer fatal frame schema is exactly
`anysolver.no_numba_residual.stage_c.containment_proof_loss_stderr/1`. It uses
the same canonical UTF-8/no-BOM/one-LF/16,384-byte single-write and external
capture rules as Section 13, but has these mandatory keys:

- `schema`, `attempt_id`, `run_id`, `event="containment_proof_loss"`,
  `created_utc`, and `truncated`;
- `latest_durable_global_head`: null only before the first durable receipt,
  otherwise exact path/schema/sequence/bytes/SHA-256;
- `promoted_receipt`: null when no unregistered promotion occurred, otherwise
  its exact identity and `registered_in_global_chain` truth;
- `original_failure`: phase, exception type, and full-message SHA-256;
- `containment_attempt`: owner scope, Job identity, PID, process-creation
  identity, ordered actions, terminal state, zero-PID state, handle state, and
  ordered errors with phase/type/code/message SHA-256;
- fixed booleans `registration_loss=false`,
  `containment_proof_complete=false`,
  `host_successor_publication_prohibited=true`,
  `containment_repeated=false`, and truthful
  `raw_partials_may_have_advanced`;
- `evidence_status="evidence_limited"`.

The truncated replacement must retain every listed key; only variable detail
outside them may be omitted. All nested publishing catches receive a prior
`_ContainmentProofLost` bypass just like registration loss. Because the local
scope has already exhausted the accepted exactly-once containment attempt, no
outer scope repeats it. The host publishes no in-root successor/terminal and
exits nonzero after the one distinct frame. The external process result records
which of the two mutually exclusive fatal schemas was observed.

The exact additional owned symbols are:

- `_ContainmentProofLost`;
- `_containment_proof_loss_stderr_frame`;
- `_abort_after_containment_proof_loss`.

Independent review must prove every ordinary containment failure reaches this
distinct schema, retains the actual durable head/promoted state, bypasses all
publishers, and cannot be mislabeled as registration loss.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 15. Authoritative V9 run identity and proof lifetime

This section supersedes only Section 14's run-ID assumption, proof-consumer
lifetime, ordinary contained-failure proof, and truncated-frame process
identity. All accepted process and evidence behavior remains exact.

### 15.1 Collision-checked run ID shared by caller and callee

The caller creates and reserves a run identity before the first prelaunch
promotion. Canonical material is sorted-key compact UTF-8 JSON without BOM or
LF under schema
`anysolver.no_numba_residual.stage_c.contained_run_identity_material/1`, with
exact keys:

- full accepted V5 SHA-256, full campaign-intent SHA-256, and `attempt_id`;
- `check_id` exactly one of `C02`, `C03`, `C04`, `C05`;
- zero-based global contained invocation ordinal;
- exact current predecessor receipt SHA-256;
- canonical argv SHA-256 and canonical environment-manifest SHA-256.

`run_id` is the lowercase 64-hex SHA-256 of those exact material bytes. New
helper `_derive_contained_run_id(material)` is the sole derivation. The caller
registers `(run_id, material_bytes, material_sha256)` in
`_GlobalReceiptChain.reserve_contained_run`; duplicate material, duplicate
ordinal/check pair, reuse of a run ID, or one digest mapped to differing material
fails typed `CONTAINED_RUN_ID_COLLISION` before promotion or child creation.

The caller passes keyword-only `run_id` and the exact material to
`_run_contained_wsl`. The callee independently canonicalizes the received
material with the same helper, requires exact run-ID equality, and requires the
existing reservation before its first promotion. Every internal receipt,
terminal proof, outer consumer, and diagnostic carries that run ID. Caller and
callee may not generate separate IDs or infer one from PID/time.

### 15.2 Exact proof consumers and counts

Every retained proof owns an immutable expected-consumer set selected from
these exact receipt IDs:

- `run:<run_id>:check-terminal`;
- `run:<run_id>:post-check`;
- `run:<run_id>:campaign-final`;
- `run:<run_id>:top-level-success`;
- `run:<run_id>:top-level-failure`.

The exact branch table is:

| Lane | Required consumers | Count |
| --- | --- | ---: |
| C02-C04 success followed by another check | `check-terminal`, `post-check` | 2 |
| C02-C04 ordinary/typed failure | `check-terminal`, `post-check`, `top-level-failure` | 3 |
| C05 success | `check-terminal`, `post-check`, `campaign-final`, `top-level-success` | 4 |
| C05 ordinary/typed failure | `check-terminal`, `post-check`, `top-level-failure` | 3 |

`check-terminal` means exactly the existing outer result-or-failure receipt for
that check; `post-check` means its accepted post-check/failure snapshot receipt.
The two forms are mutually exclusive at one receipt ID and cannot double-count.
The lane is frozen when the contained outcome is known and before the first
outer consumer promotion. A thrown ordinary exception uses the failure lane.

`mark_contained_proof_consumed` requires the exact expected receipt ID, exact
run ID, and newly registered global-chain receipt identity. It rejects unknown,
duplicate, out-of-order, or cross-run consumers. A proof is complete only when
its observed ordered consumer IDs equal the lane's expected set exactly.

For C02-C04 success, the next run may reserve only after the prior proof's two
consumers are complete. A failure proof remains retained through the actual
top-level failure append. C05 proof remains retained through campaign-final and
top-level success, or through top-level failure on its failure lane. A proof is
never discarded merely because handles closed, `_run_contained_wsl` returned,
or a later snapshot began. Registration loss at any required consumer obtains
that exact still-retained proof. No proof is superseded early, consumed twice,
replaced with another run's proof, or replaced by `no_child_created`.

If top-level terminal registration itself is lost, the proof remains retained
in memory for the Section 13 external diagnostic and process result. The failed
campaign performs no proof cleanup or successor publication.

### 15.3 Ordinary failure already-contained proof

Every ordinary `_run_contained_wsl` failure path that created or may have
created a child performs the accepted exactly-once containment/wait/reap while
Job/process handles remain owned. Before any ordinary failure-receipt promotion,
it creates immutable `_ContainedProcessTerminalProof` bound to the reserved
run ID with reason `ordinary_failure_already_contained`, exact original primary
exception identity, containment actions/errors, terminal process exit, and
zero-Job-PID proof. It is finalized after existing handle close and retained in
the global chain before the failure lane is selected.

Ordinary failure-receipt publication is permitted only when that proof has
`terminal=true`, `zero_pid=true`, and `handles_closed=true`. Registration loss
on the failure receipt attaches the proof as
`owner_scope="run_contained_wsl_ordinary_failure_already_contained"` and may not
terminate/wait/reap again. If containment cannot prove terminal/zero PID, no
ordinary failure receipt is promoted; the campaign enters the existing
out-of-band fail-stop with the incomplete containment truth.

A failure proven before child creation uses the reserved run ID and exact
`no_child_created` proof. Once any creation call may have succeeded, a
`no_child_created` substitution is forbidden even if PID extraction later
fails.

### 15.4 Mandatory process identities in truncated frames

In addition to Section 14.4, every truncated frame contains these mandatory
keys:

- `run_id`: the exact reserved 64-hex contained run ID; for a pure host-only C01
  loss where no contained run is applicable, the key is present with null and
  `child_created=false`;
- `job_identity`: exact Job name/identity, configured limits SHA-256, and
  creation-time assignment receipt SHA-256, or null only when child creation
  never began;
- `pid`: exact integer child PID, or null only under the same no-creation rule;
- `process_creation_identity`: canonical image path, volume/file ID, raw
  SHA-256, canonical argv SHA-256, and creation UTC, or null only under the same
  no-creation rule.

If child creation may have succeeded but any mandatory identity is unavailable,
the key remains present with a typed `unknown_after_creation_attempt` object and
the corresponding containment error hash; it is never represented as
`no_child_created`. These identities, null/unknown reasons, and hashes may not
be omitted by truncation. Worst-case frame preflight includes their maximum
registered path/field sizes.

### 15.5 Exact additional ownership

The exact additional owned symbols are:

- `_derive_contained_run_id`;
- `_GlobalReceiptChain.reserve_contained_run`;
- `_ContainedProcessTerminalProof.expected_consumer_ids`;
- `_ContainedProcessTerminalProof.observed_consumer_ids`.

Allowed call-site hunks are limited to caller reservation, callee independent
validation, lane freezing, exact consumer marking, and ordinary-failure proof
creation before existing failure publishers. Independent review must prove the
run material/ID is identical on both sides, consumer counts match the table,
and no proof can be superseded before its lane is complete.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.

## 14. Authoritative V8 contained-run state closure

This section supersedes only Section 13's `_run_contained_wsl` catch placement,
post-close outcome retention, later outer-append outcome selection, and
truncated-frame required keys. All other nested-bypass and external-capture
contracts remain exact.

### 14.1 Enclosing bypass for the two pre-catch promotions

The accepted `_run_contained_wsl` has two atomic receipt promotions before its
current broad publishing catch and before child creation. The entire function
body receives one enclosing `except _ReceiptRegistrationLost` boundary outside
those two sites and every existing inner boundary. Before either promotion,
state is exactly `child_lifecycle="not_created"`, with no Job, process, PID, or
child handle.

If either pre-catch append raises registration loss, the enclosing branch
attaches immutable `_RegistrationLossContainmentOutcome` with
`owner_scope="run_contained_wsl_prelaunch"`, `terminal=true`, `zero_pid=true`,
`child_created=false`, empty PID/action/error arrays, and reason
`no_child_created`; it then rethrows. It performs no containment call and no
publication. If a registration-loss exception reaching the enclosing boundary
already has an outcome from an inner scope, the boundary only rethrows and may
not attach or act again.

### 14.2 Frozen normal-terminal proof before handle close

For a created child, `_run_contained_wsl` constructs exactly one immutable
`_ContainedProcessTerminalProof` after terminal wait/reap and zero-Job-PID proof
but before closing the retained process and Job handles. Exact fields are:

- `run_id`, `owner_scope="run_contained_wsl"`, Job identity, PID, and process
  creation identity;
- wait result, process exit code, terminal UTC, ordered termination actions,
  and ordered errors;
- pre/post Job PID arrays, `terminal=true`, `zero_pid=true`, and
  `handles_verified_before_close=true`;
- handle-close completion UTC and `handles_closed=true`, set by creating a new
  final frozen proof after the existing close sequence succeeds.

The three accepted normal-terminal receipt promotions that occur after handle
close each run with that final proof retained in local scope. A registration
loss at any of those sites attaches
`_RegistrationLossContainmentOutcome.from_terminal_proof(proof)` with
`owner_scope="run_contained_wsl_already_terminal"`, reason
`already_terminal_reaped`, and exact terminal/zero-PID values; it performs no
termination or wait again and rethrows. A proof with false terminal, false
zero-PID, unclosed handles, mismatched run ID, or errors inconsistent with the
accepted outcome fails closed before the first post-close promotion.

### 14.3 Retained proof for later outer appends

The existing return value and return type of `_run_contained_wsl` remain
unchanged. Instead, `_GlobalReceiptChain` retains the final
`_ContainedProcessTerminalProof` keyed by exact `run_id`. The new exact methods
are:

- `retain_contained_terminal_proof(proof)`;
- `require_contained_terminal_proof(run_id)`;
- `mark_contained_proof_consumed(run_id, receipt_identity)`.

Retention occurs after the proof is final and before normal return. The caller
passes the exact run ID to every corresponding outer result and snapshot append.
If registration loss occurs there, the dedicated branch obtains the matching
proof, attaches the same immutable `already_terminal_reaped` outcome, and
rethrows without containment repetition. A missing, stale, mismatched, already-
superseded, or nonterminal proof is itself fail-closed and cannot be replaced by
`no_child_created`.

The proof remains available through all required outer result/snapshot
promotions for that run. Each successful promotion records its receipt identity
against the proof. It may be superseded by the next run only after every
accepted required outer promotion for the prior run is registered in the global
chain. No C02-C05 result value or process behavior changes.

### 14.4 Mandatory truncated diagnostic content

The truncated replacement frame from Section 13.3 must always contain these
keys and values; only additional variable detail may be omitted:

- `schema`, `attempt_id`, `event`, `created_utc`, `truncated=true`,
  `full_frame_bytes`, `full_frame_sha256`, and ordinal `omitted_fields`;
- `promoted_receipt`: canonical path, kind, sequence, expected bytes, and
  expected SHA-256;
- `prior_global_head`: null only when truthfully absent, otherwise canonical
  path, schema, sequence, bytes, and SHA-256;
- `registration_error`: primary phase, exception type, and SHA-256 of the full
  UTF-8 error message;
- `containment_outcome`: owner scope, reason, `child_created`, `terminal`,
  `zero_pid`, `handles_closed`, and an ordered error array whose entries retain
  error phase/type/code plus SHA-256 of each full UTF-8 message;
- fixed booleans `durable_final_exists=true`,
  `registered_in_global_chain=false`,
  `host_successor_publication_prohibited=true`,
  `containment_repeated=false`, and truthful
  `raw_partials_may_have_advanced`;
- `evidence_status="evidence_limited"`.

Paths, hashes, fixed enums, booleans, numeric identities, and containment errors
are mandatory and may never be moved into `omitted_fields`. Before execution,
the external producer validates that a worst-case mandatory frame using the
prebound path limits fits within `16,384` bytes. Failure blocks launch. Runtime
truncation therefore always emits a valid mandatory frame within the cap unless
the single OS stderr write itself is short/fails; that transport result remains
captured exactly as Section 13.4 requires.

### 14.5 Exact additional ownership

The exact additional owned symbols are:

- `_ContainedProcessTerminalProof`;
- `_RegistrationLossContainmentOutcome.from_terminal_proof`;
- `_GlobalReceiptChain.retain_contained_terminal_proof`;
- `_GlobalReceiptChain.require_contained_terminal_proof`;
- `_GlobalReceiptChain.mark_contained_proof_consumed`.

Allowed call-site hunks are only the enclosing prelaunch bypass, proof creation
immediately before/after existing handle close, the three accepted post-close
promotion bypasses, proof retention before return, and corresponding outer
result/snapshot bypasses. Independent review must map those exact sites and
prove no process, receipt payload, C02-C05 value, timeout, resource, or
containment primitive changed.

No source/test/API/WSL/evidence/Git/cleanup/PERF action is authorized. V4 stays
immutable and PERF remains free.
