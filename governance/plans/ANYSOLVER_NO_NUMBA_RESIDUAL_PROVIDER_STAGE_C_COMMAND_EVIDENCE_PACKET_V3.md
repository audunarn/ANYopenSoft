# ANYsolver No-Numba Residual Provider Stage-C Command/Evidence Packet V3

## 1. Mechanical supersession

This V3 incorporates Stage-C V2 by exact identity and changes only the accepted
interpreter binding, atomic WSL-child containment, and execution-authority/PERF
lease distinction required by review.

- Preserved V2 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V2.md`
- Preserved V2 SHA-256:
  `2E955342DB55F1608FE899FCC7CB22994DAA7292885F61D1216D630FD1486B58`
- Accepted Provider V6 SHA-256:
  `C0BDA29EC0F68EF57A36F3F0CFF68236C41814E837532E4A9488AC12484985BD`
- ANYsolver source commit/tree:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e` /
  `00b2b20691e73a05589b797b32352f1c760a2451`

Every V2 provision not explicitly replaced below remains binding. V1 and V2
remain immutable rejected-plan evidence. The SHA-256 of this V3 is an external
accepted launch parameter and is not embedded in this file.

This V3 is plan-only. No executor, interpreter probe, query, process, Job Object,
receipt, evidence root, escalation request, execution authority, PERF lease,
distro action, or provider action is created or executed.

## 2. Correct interpreter binding

Every V2 reference to the absent path
`C:\Users\AudunArnesenNyhus\AppData\Local\Programs\Python\Python313\python.exe`
is retired and must not appear in a launch, receipt, or accepted identity.

The independently present interpreter path is exactly:

`C:\Python\Python313\python.exe`

The identity contract is CPython `3.13.9`, Windows AMD64, direct ordinary file,
direct non-reparse ancestry, and no Store/App-Execution-Alias indirection. Before
executor-source acceptance or execution, a separately accepted read-only
identity receipt must freeze its resolved path, volume/file ID, bytes, SHA-256,
PE machine, file/product version, CPython implementation/version/ABI, and valid
Authenticode chain. That receipt's path and SHA-256 are external launch inputs.
No interpreter observation is made by this plan.

The future top-level argv shape replaces V2's argv in full:

```text
["C:\\Python\\Python313\\python.exe","-B","-I","C:\\Github\\ANYopenSoft\\governance\\tools\\anysolver_no_numba_residual_stage_c_host_executor.py","--packet","C:\\Github\\ANYopenSoft\\governance\\plans\\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V3.md","--packet-sha256","<ACCEPTED_V3_SHA256>","--executor-sha256","<ACCEPTED_EXECUTOR_SHA256>","--interpreter-receipt","<ACCEPTED_ABSOLUTE_INTERPRETER_RECEIPT_PATH>","--interpreter-receipt-sha256","<ACCEPTED_INTERPRETER_RECEIPT_SHA256>","--execution-authority-receipt","<ACCEPTED_ABSOLUTE_EXECUTION_AUTHORITY_PATH>","--execution-authority-sha256","<ACCEPTED_EXECUTION_AUTHORITY_SHA256>","--perf-lease-state-receipt","<ACCEPTED_ABSOLUTE_PERF_LEASE_STATE_PATH>","--perf-lease-state-sha256","<ACCEPTED_PERF_LEASE_STATE_SHA256>","--qualification-root","C:\\Users\\AudunArnesenNyhus\\AppData\\Local\\ANYrelease\\qualification\\ANYsolver-no-numba-residual-82a9db28","--evidence-root","<FRESH_ABSOLUTE_STAGE_C_EVIDENCE_ROOT>"]
```

The executor validates the direct interpreter file against the accepted receipt
before creating evidence or invoking Win32 trust/WSL operations. Any mismatch is
pre-execution failure.

## 3. Atomic-at-creation WSL child containment

### 3.1 No ordinary Popen launch

V2's ordinary `subprocess.Popen` launch contract for C02-C05 is withdrawn.
Python `subprocess` may be used only for constants/data helpers that never start
a process; it may not create the WSL query child.

The reviewed executor must bind direct `ctypes` Win32 calls and implement one
contained launch primitive for each exact V2 C02-C05 argv. It must not use
PowerShell, `cmd`, a batch file, shell parsing, WMI process creation,
`ShellExecute`, `Start-Process`, a hidden-window launcher, or an intermediate
supervisor.

### 3.2 Ordered containment before first instruction

For each C02-C05 child, the executor performs this exact order:

1. Durably publish the check intent and job intent before any process handle is
   created.
2. Create an unnamed Job Object with a NULL security descriptor and a
   non-inheritable handle; verify `HANDLE_FLAG_INHERIT` is clear.
3. Apply `JOBOBJECT_EXTENDED_LIMIT_INFORMATION` with
   `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`, `JOB_OBJECT_LIMIT_ACTIVE_PROCESS`, and
   `ActiveProcessLimit=1`. Do not set breakaway, silent-breakaway, or
   preserve-job-time flags.
4. Query the Job Object and require the read-back limit flags/active limit equal
   the requested values before child creation.
5. Create exclusive raw stdout/stderr partial files and one read-only NUL stdin
   handle. Use `STARTUPINFOEXW` plus `PROC_THREAD_ATTRIBUTE_HANDLE_LIST` so only
   those three explicit standard-I/O handles are inherited. The Job Object,
   executor files, receipts, packet, interpreter, and all unrelated handles are
   non-inheritable.
6. Call `CreateProcessW` directly with exact executable
   `C:\WINDOWS\system32\wsl.exe`, an executor-owned mutable command-line buffer
   reconstructed only from the registered argv, `bInheritHandles=TRUE`, exact
   recorded environment/cwd, and flags `CREATE_SUSPENDED |
   EXTENDED_STARTUPINFO_PRESENT | CREATE_UNICODE_ENVIRONMENT |
   CREATE_NEW_PROCESS_GROUP`. Do not use `CREATE_BREAKAWAY_FROM_JOB`,
   `CREATE_NO_WINDOW`, or a shell.
7. While the primary thread is still suspended, validate the returned process
   image/file ID and exact command identity, then call
   `AssignProcessToJobObject` and require success.
8. Query the Job Object and require exactly the suspended child PID is assigned,
   with active-process count one and no other PID.
9. Durably publish the assigned-before-resume receipt, including all Job/process
   IDs, limits, argv, stream handles, and API return/error values.
10. Resume exactly the primary thread once. Only after successful `ResumeThread`
    may the semantic timeout begin.

If any step before resume fails, the executor must never resume the child. It
terminates the exact suspended process if one exists, waits/reaps it, closes the
Job Object only after wait, publishes failure evidence, and stops. A nested-job
or assignment restriction is an infrastructure failure, not authority to use
breakaway or ordinary `Popen`.

Atomicity means no WSL child instruction executes before successful Job Object
assignment. The non-inheritable Job Object handle remains open only in the
executor. If the executor exits, crashes, is terminated, or loses all handles,
Windows kill-on-close terminates every assigned child. No child can retain or
inherit the Job handle.

### 3.3 Normal, timeout, exception, and crash outcomes

On normal completion the executor waits for the process handle, records exit,
queries final Job accounting and assigned-process state, flushes/closes raw
streams, closes thread/process handles, verifies zero active Job processes,
then closes the Job handle. It publishes process/job finals before the semantic
check result.

On semantic timeout the executor calls `TerminateJobObject` exactly once with a
registered timeout exit code, waits/reaps, records all return/error/accounting
facts, verifies zero active processes, then closes the Job handle. It never calls
`wsl --terminate`, `wsl --shutdown`, service control, unregister, import, or
general process cleanup.

On handled Python/Win32 exception the executor preserves the original exception,
uses the same owned-Job termination/wait path only when an assigned child is
still active, and publishes exception/job/process evidence before stopping.

An abrupt executor crash can prevent a final JSON receipt, but cannot leave the
assigned WSL child alive after the executor's Job handle closes. The durable
intent, assigned-before-resume receipt, raw stream partials, process/job
partials, shell-command transport exit, and absent final become the truthful
crash evidence. Such a campaign is terminal and requires separately authorized
read-only recovery/audit; it is never accepted, retried, repaired, or cleaned.
No plan claims an impossible post-crash executor-written residual final.

## 4. Job/process evidence ownership

V2's executor-owned evidence table remains binding and gains these per-check
paths for C02-C05:

- `checks/<ID>/job_intent.json.partial|json`
- `checks/<ID>/job_configured.json.partial|json`
- `checks/<ID>/assigned_before_resume.json.partial|json`
- `checks/<ID>/job_process.json.partial|json`
- `checks/<ID>/job_process_failure.json.partial|json`
- `checks/<ID>/stdout.bin.partial|bin`
- `checks/<ID>/stderr.bin.partial|bin`

The Job receipt schema is:

`anysolver.no_numba_residual.provider_stage_c_job_process/1`

Every all-outcome job/process receipt records:

- V3 packet, executor, interpreter, authority, PERF-state, campaign, and check
  identities;
- exact argv/canonical hash, executable direct path/file ID, cwd, environment
  hash, ordinal, and timeout;
- Job handle inheritance state, configured/read-back limits, Job accounting,
  completion-port state if used, active PID list/count, and every Job API
  return/last-error value;
- process/thread PIDs and handles, creation flags, inherited-handle allowlist,
  suspended-state proof, assignment proof, resume count/result, start/exit UTC,
  timeout/exception state, exit code, wait result, and handle-close results;
- stdout/stderr paths, bytes, hashes, flush/promotion results, and whether each
  remains partial;
- pre/post service/process/path snapshot hashes, owned-child residual result,
  peak Job/process memory, and first-failure truth;
- normal, timeout, pre-resume failure, handled exception, or abrupt-crash
  classification without converting missing finals into success.

Finals use V2's exclusive CreateNew/write-through partial creation and
same-volume no-replace promotion. Every partial is preserved on every failure.
No runner, watchdog, later check, or recovery process may delete or overwrite a
partial.

The aggregate Stage-C report cannot be successful unless C02-C05 each has a
durable assigned-before-resume receipt, normal-exit job/process final, raw stream
finals, zero active Job process proof, closed-handle proof, and matching semantic
result. A timeout, exception, pre-resume failure, abrupt crash, missing final, or
residual contradiction is terminal failure.

## 5. Read-only execution authority versus PERF lease

V2's single `external_boss_stage_c_lease` concept is withdrawn. Stage-C has two
distinct external governance inputs and neither may substitute for the other.

### 5.1 Short read-only execution authority

The mandatory one-shot execution receipt schema is:

`anysolver.no_numba_residual.external_boss_stage_c_execution_authority/1`

It is issued by Boss thread `019ff655-abd9-7eb1-b94e-d80252ff9215`, remains
outside executor ownership, and binds exact V3/executor/interpreter identities,
the five logical checks and Job containment, evidence root, escalation mode,
under-five-minute deadline, one-child/under-500-MB/no-network/no-GPU envelope,
service-activation policy, first-failure/no-retry rule, grant UTC/expiry, and
raw grant-message hash. This is command authority only. It is not a PERF lease,
does not reserve ecosystem performance resources, and does not authorize any
benchmark, build, test, profiler, import, provider stage, or continuation.

### 5.2 Exclusive PERF lease state

A separate read-only governance-state receipt uses schema:

`anysolver.no_numba_residual.ecosystem_perf_lease_state/1`

It binds Boss thread, observation UTC, active holder/state, and raw status-message
hash. Stage-C may launch only when this receipt proves no competing exclusive
PERF lease is active, unless Boss explicitly issues a distinct exclusive PERF
lease for Stage-C. If a distinct PERF lease is issued, its receipt and identity
are additional inputs; it never replaces the execution-authority receipt.

The executor records `execution_authority_kind=short_read_only` and
`exclusive_perf_lease_consumed=false` for the ordinary Stage-C path. It must not
say `PERF LEASE GRANTED`, `lease held`, or `lease released` unless a separate
actual PERF lease receipt exists. Any authority/PERF-state ambiguity fails
before evidence-root creation.

The future escalation justification remains exactly:

`Allow this read-only, hash-pinned Stage-C WSL capability executor outside the sandbox; it may query WSL service state but cannot create, import, start, stop, terminate, or unregister a distribution.`

Escalation is bound by the short execution authority, uses no prefix rule, and
changes no command bytes. It does not imply or acquire a PERF lease.

## 6. Updated review and stop order

Required order is:

1. Accept this V3 path/bytes/SHA-256.
2. Create only the registered executor source through a separate `apply_patch`
   authority.
3. Independently review source hash, AST/compile-only result, real interpreter
   binding, direct Win32 signature/state APIs, exact C02-C05 argv, suspended
   CreateProcess/Job assignment/resume order, kill-on-close behavior, evidence
   ownership, and crash semantics.
4. Independently freeze the real interpreter identity receipt.
5. Obtain a fresh short read-only execution-authority receipt and a distinct
   current PERF-lease-state receipt; obtain a separate PERF lease only if Boss
   expressly requires one.
6. Execute the one accepted host executor once under its exact authority.
7. Preserve first-failure truth and independently review all evidence before any
   Stage-M proposal.

No executor/source creation, interpreter query, WSL query, Job Object, process,
receipt, evidence root, execution authority, escalation request, PERF lease,
distro action, provider action, acquisition, import, build, export, validation,
cleanup, Git/GitHub action, source/test/workflow edit, publication, or Defender
action is authorized by creating this V3.
