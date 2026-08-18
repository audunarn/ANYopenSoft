# ANYsolver No-Numba Residual Provider Stage-C Command/Evidence Packet V4

## 1. Mechanical supersession

This V4 incorporates Stage-C V3 by exact identity and changes only the WSL-child
creation-time Job membership and standard-handle inheritance contract required
by review.

- Preserved V3 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V3.md`
- Preserved V3 SHA-256:
  `E0DF5E99D86A32C169378949F39EE8DC4AEEEA5BB0C96A5186914DF117A79034`
- Accepted Provider V6 SHA-256:
  `C0BDA29EC0F68EF57A36F3F0CFF68236C41814E837532E4A9488AC12484985BD`
- ANYsolver source commit/tree:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e` /
  `00b2b20691e73a05589b797b32352f1c760a2451`

Every V3 provision not explicitly replaced below remains binding. V1-V3 remain
immutable rejected-plan evidence. The SHA-256 of this V4 is an external accepted
launch parameter and is not embedded in this file.

This V4 is plan-only. It creates no executor, interpreter probe, process, Job
Object, receipt, evidence root, WSL query, escalation request, execution
authority, PERF lease, distro action, or provider action.

## 2. Creation-time Job membership replaces post-create assignment

V3 Section 3.2 steps 5-10 are replaced in full by this section. The executor
must never call `AssignProcessToJobObject` for C02-C05. There is no fallback to
post-create assignment, ordinary `Popen`, breakaway, an intermediate supervisor,
or an uncontained suspended process.

For each C02-C05 child, the executor performs this exact order:

1. Durably publish the check intent and Job intent before creating any process
   or thread handle.
2. Create one unnamed Job Object. The Job handle has
   `HANDLE_FLAG_INHERIT` cleared and is never included in the inherited-handle
   list.
3. Apply and read back `JOBOBJECT_EXTENDED_LIMIT_INFORMATION` with exactly
   `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`, `JOB_OBJECT_LIMIT_ACTIVE_PROCESS`, and
   `ActiveProcessLimit=1`. Breakaway and silent-breakaway flags are absent.
4. Create exclusive stdout/stderr partial-file handles and one read-only NUL
   stdin handle using security attributes that initially make exactly these
   three standard-I/O handles inheritable. Require `GetHandleInformation` to
   report `HANDLE_FLAG_INHERIT` on all three.
5. Require every other executor-created handle relevant to the launch,
   including Job, packet, executor, interpreter, receipt, snapshot, intent,
   attribute-list storage, process-audit, and directory handles, to have
   `HANDLE_FLAG_INHERIT` clear.
6. Initialize one `STARTUPINFOEXW` attribute list with capacity exactly two.
   Both size-probe and initialized-list API results/errors are recorded.
7. Add `PROC_THREAD_ATTRIBUTE_HANDLE_LIST` containing exactly the three handles
   in this ordinal order: stdin, stdout, stderr. No duplicate, pseudo-handle,
   Job handle, or additional handle is permitted.
8. Add `PROC_THREAD_ATTRIBUTE_JOB_LIST` containing exactly the single configured
   Job handle. The Job handle must have assignment/query/terminate rights needed
   by the frozen executor contract but remains non-inheritable.
9. Read back or otherwise validate all locally owned attribute-list inputs,
   counts, byte sizes, pointer lifetimes, handle identities, and inheritance
   flags before process creation. Publish a durable
   `creation_attributes_ready` receipt before calling `CreateProcessW`.
10. Set `STARTUPINFOW.dwFlags` to include `STARTF_USESTDHANDLES` and set
    `hStdInput`, `hStdOutput`, and `hStdError` to exactly the same three handles
    in the handle-list attribute. No other STARTF flag may redirect or hide the
    process.
11. Call `CreateProcessW` once with exact application path
    `C:\WINDOWS\system32\wsl.exe`, an executor-owned mutable command-line buffer
    reconstructed only from the registered argv, `bInheritHandles=TRUE`, exact
    recorded environment/cwd, the populated `STARTUPINFOEXW`, and flags
    `CREATE_SUSPENDED | EXTENDED_STARTUPINFO_PRESENT |
    CREATE_UNICODE_ENVIRONMENT | CREATE_NEW_PROCESS_GROUP`. Do not use
    `CREATE_BREAKAWAY_FROM_JOB`, `CREATE_NO_WINDOW`, a shell, or any second
    creation call.
12. Require `CreateProcessW` success to mean the returned child is already a
    member of the single configured Job by construction. While its primary
    thread remains suspended, validate returned PID/TID, image path/file ID,
    exact command identity, Job active-process count, and Job PID list. Require
    the Job to contain exactly that one suspended child PID.
13. Immediately clear `HANDLE_FLAG_INHERIT` on the three parent-side standard
    handles after successful creation, record the read-back state, and retain
    only the parent handles needed for stream flush/accounting. The child's
    inherited standard handles remain those selected by the explicit handle
    list.
14. Publish the durable assigned-at-creation/before-resume receipt, including
    Job membership, attribute-list identity, exact stdio inheritance, all API
    return/error values, process/thread identity, and suspended state.
15. Resume exactly the primary thread once. The semantic timeout starts only
    after `ResumeThread` succeeds with the expected previous suspend count.

`PROC_THREAD_ATTRIBUTE_JOB_LIST` is mandatory. If the host, interpreter, Win32
API surface, nested-Job policy, or current process containment does not support
it, the executor fails before `CreateProcessW`. Unsupported attributes,
`UpdateProcThreadAttribute` failure, Job incompatibility, or inability to prove
creation-time membership cannot be repaired by post-create assignment.

Because Job membership is supplied to `CreateProcessW`, these are the only
possible outcomes of the creation call:

- it fails and creates no child; or
- it succeeds with the child already assigned to the kill-on-close Job before
  any child instruction can execute.

If the executor is lost during or immediately after a successful creation call,
its non-inheritable Job handle closes and Windows terminates the already assigned
child. There is no created-but-unassigned interval.

## 3. Exact attribute and handle constraints

The reviewed executor source must define and validate the documented
`PROC_THREAD_ATTRIBUTE_HANDLE_LIST` and `PROC_THREAD_ATTRIBUTE_JOB_LIST`
constants through the Windows attribute-value construction rules appropriate to
the interpreter's pointer width. Hard-coded numeric values must be accompanied
by compile/source comments and tests in the later source review; runtime values
must be recorded in the creation receipt.

Attribute storage, handle arrays, mutable command-line storage, environment
block, security-attribute structures, and `STARTUPINFOEXW` must remain alive and
unmodified through `CreateProcessW` return. The executor calls
`DeleteProcThreadAttributeList` exactly once on every path after no further use
is possible and records that accounting. Attribute-list memory is never
inherited by the child.

Before each creation attempt the executor records the inheritance state of all
handles it created for that check. Exactly stdin/stdout/stderr may have
`HANDLE_FLAG_INHERIT` set. The Job handle is non-inheritable even though its
value is supplied in `PROC_THREAD_ATTRIBUTE_JOB_LIST`. The explicit handle-list
attribute and `STARTF_USESTDHANDLES` must agree byte-for-byte on those three
handles.

If standard-handle creation, inheritance validation, attribute-list creation,
Job-list update, handle-list update, STARTUPINFO configuration, or durable
precreation publication fails, `CreateProcessW` is not called. Open handles are
closed with all outcomes recorded; partials remain preserved.

## 4. Updated evidence paths and schemas

V3's all-outcome Job/process paths and schemas remain binding. Each C02-C05 check
also owns these paths:

- `checks/<ID>/creation_attributes_intent.json.partial|json`
- `checks/<ID>/creation_attributes_ready.json.partial|json`
- `checks/<ID>/assigned_at_creation_before_resume.json.partial|json`
- `checks/<ID>/creation_attributes_final.json.partial|json`

Their schema is:

`anysolver.no_numba_residual.provider_stage_c_creation_attributes/1`

The finals bind:

- V4, executor, interpreter, execution-authority, PERF-state, campaign, and
  check identities;
- exact HANDLE_LIST/JOB_LIST attribute constants, list capacity, allocation
  size, pointer width, storage lifetime, API calls/return values/last errors,
  and deletion accounting;
- Job handle identity/rights/inheritance/limits and the one-element Job list;
- stdin/stdout/stderr path or NUL identity, handle values, security attributes,
  pre/post inheritance flags, the exact three-element handle list, and
  `STARTF_USESTDHANDLES` fields;
- exact application/argv/cwd/environment/creation flags and mutable-buffer hash;
- returned PID/TID/image, suspended state, creation-time Job PID list/count,
  assignment proof, resume result, and first-failure state;
- every opened/closed handle and every preserved partial/final path.

The aggregate report cannot succeed unless all four WSL child checks have a
durable `creation_attributes_ready` final, an
`assigned_at_creation_before_resume` final, exact three-handle inheritance
proof, creation-time one-Job/one-PID proof, single-resume proof, normal terminal
Job/process receipt, raw stream finals, zero residuals, and matching semantic
result.

On abrupt executor loss, durable intent/ready/assigned receipts and partials are
preserved to the point reached. Kill-on-close supplies containment, but missing
post-crash finals remain terminal evidence-limited failure requiring separately
authorized audit. No retry, repair, overwrite, cleanup, or inferred success is
allowed.

## 5. Unchanged authority and resource boundary

V3's real interpreter path, CPython identity gate, exact five logical checks and
argv, 195-second child budget, 300-second Stage-C deadline, one-child/under-500
MB/no-network/no-GPU envelope, Microsoft signature policy, path/import/archive
gates, OS/kernel/architecture snapshots, service/process activation truth,
atomic evidence ownership, short read-only execution-authority receipt, distinct
PERF-lease-state receipt, escalation metadata, first-failure behavior, and
no-provider-action boundary are unchanged.

The short read-only execution authority remains distinct from an exclusive PERF
lease. This V4 neither requests nor creates either one.

Required order remains V4 acceptance, separately authorized executor-source
creation, independent source/interpreter/containment review, fresh execution
authority plus PERF-state binding, then one separately granted execution. No
executor/source creation, interpreter query, WSL query, process, Job Object,
receipt, evidence root, escalation request, execution authority, PERF lease,
distro/provider action, acquisition, import, build, export, validation, cleanup,
Git/GitHub action, source/test/workflow edit, publication, or Defender action is
authorized by creating this V4.
