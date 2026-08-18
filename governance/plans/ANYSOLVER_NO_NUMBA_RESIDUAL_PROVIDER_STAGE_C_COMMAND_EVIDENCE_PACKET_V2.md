# ANYsolver No-Numba Residual Provider Stage-C Command/Evidence Packet V2

## 1. Mechanical supersession and authority

This V2 preserves the rejected Stage-C packet as immutable evidence and replaces
only its distro/path identity, direct-call evidence transport, and missing host
state/lease gates.

- Preserved V1 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET.md`
- Preserved V1 SHA-256:
  `58B3DA22A0D18018E6762D55450A3BB6342947ACBB70D80FF02816956CA7E3E8`
- Accepted Provider V6 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN_V6.md`
- Accepted Provider V6 SHA-256:
  `C0BDA29EC0F68EF57A36F3F0CFF68236C41814E837532E4A9488AC12484985BD`
- ANYsolver source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- ANYsolver source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`

Every V1 rule not explicitly replaced below remains binding. The SHA-256 of
this V2 is an external launch parameter and is not embedded in this file.

This V2 is plan-only. It creates no executor, receipt, evidence root, process,
query, escalation request, lease, distro, import, archive, environment, or
provider artifact. Execution remains prohibited until the executor source,
interpreter identity, lease receipt, and exact launch envelope are independently
reviewed and accepted.

## 2. Correct distro and path identities

Qualification root `Q` remains:

`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28`

The exact builder distro and import directory that must be absent are:

- distro: `ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`
- import directory:
  `Q\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`

The exact final distro and import directory that must be absent are:

- distro: `ANYsolver-Ubuntu-24.04-82a9db28`
- import directory: `Q\wsl\ANYsolver-Ubuntu-24.04-82a9db28`

The provider archive is not a distro name or import-directory identity. It is a
separate pre/post path gate and must be absent:

`Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar`

The executor must also gate the archive's `.partial` sibling as absent. For all
three registered leaves, every existing ancestor from `Q` downward must be an
ordinary direct directory with no reparse-point attribute, mount point, junction,
symbolic link, alternate target, or case-colliding sibling. The absent leaves
must remain absent in every pre-check, inter-check, and final snapshot.

## 3. Future content-addressed host executor

### 3.1 Registered source and launch inputs

The only future Stage-C semantic/evidence owner is:

`C:\Github\ANYopenSoft\governance\tools\anysolver_no_numba_residual_stage_c_host_executor.py`

The source must be created later through `apply_patch`, encoded UTF-8 without
BOM/LF-only, AST/compile-only reviewed, and frozen by exact bytes and SHA-256.
It must remain absent until that separate authority. Any source change requires
a new hash and review; no in-place accepted-source update is allowed.

The registered interpreter candidate is:

`C:\Users\AudunArnesenNyhus\AppData\Local\Programs\Python\Python313\python.exe`

Before launch, an external read-only identity gate must independently accept the
interpreter's resolved direct path, non-reparse ancestry/file, bytes, SHA-256,
Authenticode identity, CPython implementation, and exact `3.13.9` version. The
interpreter identity becomes a literal launch input; this plan makes no new
observation or acceptance claim about it.

The eventual top-level argv has this exact shape, with each angle-bracket token
replaced once by an independently accepted literal before execution:

```text
["C:\\Users\\AudunArnesenNyhus\\AppData\\Local\\Programs\\Python\\Python313\\python.exe","-B","-I","C:\\Github\\ANYopenSoft\\governance\\tools\\anysolver_no_numba_residual_stage_c_host_executor.py","--packet","C:\\Github\\ANYopenSoft\\governance\\plans\\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V2.md","--packet-sha256","<ACCEPTED_V2_SHA256>","--executor-sha256","<ACCEPTED_EXECUTOR_SHA256>","--interpreter-sha256","<ACCEPTED_INTERPRETER_SHA256>","--boss-lease-receipt","<ACCEPTED_ABSOLUTE_LEASE_RECEIPT_PATH>","--boss-lease-sha256","<ACCEPTED_LEASE_RECEIPT_SHA256>","--qualification-root","C:\\Users\\AudunArnesenNyhus\\AppData\\Local\\ANYrelease\\qualification\\ANYsolver-no-numba-residual-82a9db28","--evidence-root","<FRESH_ABSOLUTE_STAGE_C_EVIDENCE_ROOT>"]
```

The launch uses `shell=False`, one visible top-level Python process, no
PowerShell child, no inline program, no shell parsing, no `cmd`, no batch file,
no encoded command, no launcher chain, no hidden window, no `Start-Process`, and
no Defender exception. The executor validates its own source, packet,
interpreter, and lease-receipt bytes/hashes before creating the evidence root or
starting a WSL query.

### 3.2 Five logical checks and exact child argv

The executor performs exactly five ordered logical checks. C01 uses only Python
standard-library hashing plus direct read-only Win32 APIs. It starts no child.
C02-C05 each use `subprocess.Popen` with `shell=False`, `stdin=DEVNULL`, binary
stdout/stderr capture, the accepted direct working directory, no window-hiding
flag, and exactly one of these immutable argv arrays:

| ID | Exact semantic operation or argv | Hard timeout |
|---|---|---:|
| C01 | Direct file/Win32 identity and signature validation of `C:\WINDOWS\system32\wsl.exe` | 30 s |
| C02 | `["C:\\WINDOWS\\system32\\wsl.exe","--version"]` | 30 s |
| C03 | `["C:\\WINDOWS\\system32\\wsl.exe","--status"]` | 45 s |
| C04 | `["C:\\WINDOWS\\system32\\wsl.exe","--list","--verbose"]` | 45 s |
| C05 | `["C:\\WINDOWS\\system32\\wsl.exe","--list","--quiet"]` | 45 s |

The C02-C05 argv are constants in the reviewed executor source. No environment,
CLI argument, receipt, or output may alter them. The executor computes and
records a canonical JSON argv hash for each row before launch. It uses absolute
paths and an explicitly recorded environment; it rejects Python/code injection
variables and records the retained environment key/value hash without exposing
credential values.

The shared command timeout is 195 seconds inside a 300-second Stage-C deadline.
Before each query the executor requires enough remaining time for that query and
the 60-second finalization reserve. It launches one child at a time and never
retries. On child timeout it may terminate and wait only for the exact owned
query child process; it must not issue `wsl --terminate`, `wsl --shutdown`,
service-control, distro, import, unregister, signal-broadcast, or cleanup
commands. Timeout and residual truth are terminal evidence.

## 4. C01 exact valid-Microsoft signature policy

C01 opens the literal direct file
`C:\WINDOWS\system32\wsl.exe`, rejects a reparse point or path redirection,
records file ID/volume serial/bytes, streams SHA-256, and records version-resource
fields through Win32 version APIs.

Signature acceptance requires all of the following, implemented through direct
`ctypes` bindings to documented Windows trust/certificate APIs without a child
process or network retrieval:

- `WinVerifyTrust` with `WINTRUST_ACTION_GENERIC_VERIFY_V2` returns zero;
- UI is disabled and URL retrieval is cache-only/offline;
- the verified subject is the exact opened file identity, not only a same-path
  replacement observed before or after verification;
- the leaf certificate has the code-signing EKU
  `1.3.6.1.5.5.7.3.3` and no disallowed critical extension;
- the leaf subject organization is exactly `Microsoft Corporation`;
- the leaf common name is exactly `Microsoft Windows` or
  `Microsoft Corporation`;
- the chain is valid at execution UTC under Windows Authenticode chain policy,
  terminates at a locally trusted self-signed root whose subject organization is
  exactly `Microsoft Corporation`, and has no policy error;
- test roots, untrusted roots, expired/not-yet-valid certificates, explicit
  distrust, bad usage, invalid basic constraints, and revoked certificates fail;
- cache-only revocation uncertainty is recorded explicitly and is not silently
  converted into a positive revocation assertion;
- leaf/issuer/root DER SHA-256, thumbprints, serials, subjects, issuers,
  validity, EKUs, chain flags, trust-provider return codes, catalog-versus-
  embedded source, and verification policy flags are recorded.

If offline Windows trust cannot establish this exact policy, C01 fails closed.
The executor must close trust state and certificate/store handles on every path.
It restats and revalidates file ID, volume, size, and SHA-256 after trust
verification; any time-of-check/time-of-use change is terminal.

## 5. Pre/post host-state snapshots

The executor records one durable preflight before C01, one inter-check snapshot
after every C01-C05 result, and one final snapshot before the aggregate report.
No query begins until its preceding snapshot is final.

### 5.1 Paths and reparse state

Every snapshot records, through `lstat` plus direct Win32 file-attribute/file-ID
APIs:

- packet, executor, interpreter, `wsl.exe`, qualification root, and evidence-root
  parent identities;
- builder and final import-directory absence;
- provider archive and archive-partial absence;
- exact ancestor component identity/type/reparse tag from drive root to every
  registered path;
- evidence-root ownership and all owned partial/final paths after its creation;
- case-normalized and ordinal path forms, volume serials, and file IDs.

Any registered import/archive leaf appearing, any ancestor changing identity,
or any unapproved reparse/mount/junction/symlink state stops before another WSL
query. Evidence-root files are the sole allowed filesystem additions.

### 5.2 OS, kernel, and architecture

Preflight and final snapshots use direct Win32 APIs and record:

- `RtlGetVersion` major/minor/build/service-pack values;
- `GetNativeSystemInfo` architecture, processor type, page size, allocation
  granularity, and processor count;
- `IsWow64Process2` process and native machine types;
- `C:\WINDOWS\system32\ntoskrnl.exe` direct path, reparse state, file ID,
  bytes, SHA-256, and version-resource identity;
- executor/interpreter process architecture and pointer width.

Pre/final OS, kernel, and architecture observations must be identical. Windows
CPython facts are host evidence only and never Ubuntu/CI-equivalence evidence.

### 5.3 Services and processes

Before C01, around each C02-C05 child, and at finalization the executor uses
read-only Service Control Manager and Toolhelp/process-query APIs to record:

- existence, state, PID, accepted controls, checkpoint, wait hint, start type,
  binary path, and service account for `WslService` and `LxssManager` when each
  name exists;
- all visible process PID/parent PID/session ID/start time/image path/file ID for
  `wsl.exe`, `wslservice.exe`, `wslhost.exe`, `wslrelay.exe`, `vmmem`, and
  `vmmemWSL`, plus access-denied rows;
- the executor and exact owned child lineage, start/wait/exit/timeout facts,
  handle closure, and post-wait residual state.

The executor never starts/stops/configures a service directly. If any read-only
`wsl.exe` query causes a stopped/absent-before service or related process to
become running/present, the exact first responsible check, transition, PID,
timestamps, and persistence through later snapshots are recorded as
`query_triggered_service_activation=true`. Such activation must never be
reported as unchanged host state. It is acceptable only when the external Boss
lease receipt explicitly permits observation of query-induced activation;
otherwise it is fail-closed. Regardless of policy, distro/import/archive
mutation remains forbidden.

## 6. External Boss lease binding and escalation

The executor cannot create or infer authority. Before evidence-root creation it
must validate an already durable external receipt with schema:

`anysolver.no_numba_residual.external_boss_stage_c_lease/1`

The receipt is outside executor ownership and is passed by absolute path plus
SHA-256. It must bind:

- Boss thread `019ff655-abd9-7eb1-b94e-d80252ff9215`;
- exact raw grant message hash and UTC;
- accepted V2 packet path/bytes/SHA-256;
- accepted executor path/bytes/SHA-256;
- accepted interpreter path/bytes/SHA-256/version;
- exact five logical checks/argv hashes/order/timeouts;
- evidence-root absolute path;
- under-five-minute, one-child, under-500-MB, no-network/no-GPU envelope;
- exclusive lease ID, grant/expiry state, and no competing ecosystem lease;
- whether query-triggered WSL service activation may be observed and accepted;
- exact sandbox/escalation authority for the single executor launch;
- no retry, fallback, cleanup, provider action, or Stage-M authority.

The future top-level executor call uses `login=false`. If sandbox service access
is known to be blocked, the one executor launch may use
`sandbox_permissions=require_escalated` only when the receipt says so. Exact
justification is:

`Allow this read-only, hash-pinned Stage-C WSL capability executor outside the sandbox; it may query WSL service state but cannot create, import, start, stop, terminate, or unregister a distribution.`

No prefix rule is requested. Escalation changes sandbox context only; packet,
executor, interpreter, argv, evidence root, timeout, and lease bytes remain
identical. There is no sandbox attempt followed by an escalated retry.

## 7. Executor-owned atomic evidence

The fresh evidence-root leaf is derived after V2 acceptance as:

`Q\provider-stage-c-<first-16-lowercase-hex-of-accepted-V2-SHA256>`

The executor validates the direct non-reparse parent and creates this leaf once,
failing if it exists. It is the sole owner of every Stage-C evidence path. The
external Boss lease receipt remains outside this root and is never modified.

Registered finals and their schemas are:

| Path under evidence root | Schema |
|---|---|
| `campaign_intent.json` | `anysolver.no_numba_residual.provider_stage_c_intent/2` |
| `snapshots/preflight.json` | `anysolver.no_numba_residual.provider_stage_c_host_snapshot/1` |
| `snapshots/post_C01.json` through `post_C05.json` | `anysolver.no_numba_residual.provider_stage_c_host_snapshot/1` |
| `snapshots/final.json` | `anysolver.no_numba_residual.provider_stage_c_host_snapshot/1` |
| `checks/C01/result.json` through `checks/C05/result.json` | `anysolver.no_numba_residual.provider_stage_c_check/2` |
| `checks/C02/process.json` through `checks/C05/process.json` | `anysolver.no_numba_residual.provider_stage_c_process/2` |
| `stage_c_report.json` | `anysolver.no_numba_residual.provider_stage_c_report/2` |
| `stage_c_failure.json` | `anysolver.no_numba_residual.provider_stage_c_failure/2` |

C01's direct-API process facts live in its check result and snapshots; it has no
fabricated child-process receipt. For C02-C05, raw streams are exact files:

- `checks/<ID>/stdout.bin`
- `checks/<ID>/stderr.bin`

Every final has a same-path `.partial`. The executor creates partials with
exclusive CreateNew/write-through ownership, records intent before launch,
captures child output directly into exclusive binary partial handles, waits,
flushes file buffers, closes handles, and promotes with a same-volume
`MoveFileExW` operation using write-through and without replace-existing
authority. JSON uses canonical UTF-8 without BOM, ordinal keys, compact
separators, integers for numeric fields, and one final LF. Each final records its
predecessors but no self-hash. External hashes are computed only after durable
close.

Every child process receipt records exact argv/hash, cwd, sanitized environment
hash, PID/parent/session, image/file ID, start/end UTC, exit/timeout, raw stream
paths/bytes/hashes, owned handle state, wait result, termination-if-timeout,
pre/post process snapshots, residuals, access-denied facts, peak memory when
available, and the external lease/packet/executor identities. A missing PID,
unobserved wait, contradictory residual, stream publication failure, or evidence
ownership failure is terminal.

The aggregate report binds all snapshot/check/process/raw-stream external
hashes, signature policy result, WSL `2.6.1.0`, WSL2 service/default version,
ordinal C04/C05 equality, exact builder/final name absence, exact import/archive
path gates, OS/kernel/architecture, service activation truth, resource state,
lease identity, and no forbidden mutation. Failure publication preserves every
partial/final and first-failure state. No evidence is cleaned, repaired, or
retried.

## 8. Freeze/review and stop boundary

Required order is:

1. Accept this V2 path/bytes/SHA-256.
2. Create only the registered executor source through `apply_patch` under a
   separate authority.
3. Independently review its source hash, AST/compile-only result, exact
   `shell=False` argv constants, Win32 trust/path/service/process APIs, atomic
   ownership, schemas, timeout, and no-mutation behavior.
4. Freeze and accept interpreter identity and an external Boss lease receipt.
5. Obtain a fresh explicit Stage-C execution grant bound to all exact hashes.
6. Execute the one host executor once and preserve first-failure truth.
7. Independently review evidence before any Stage-M proposal.

No query, interpreter probe, source creation, executor run, escalation request,
lease request, process, evidence-root creation, distro action, provider action,
acquisition, environment, import, build, export, validation, cleanup, Git/GitHub
action, source/test/workflow edit, publication, or Defender action is authorized
by creating this V2.
