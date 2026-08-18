# ANYsolver No-Numba Residual Provider Stage-C Command/Evidence Packet

## 1. Authority and identity boundary

This packet is plan-only. It freezes the five registered read-only WSL
capability checks required before provider acquisition or construction. It does
not execute a command, create a capability receipt, request a lease, create or
import a distribution, acquire an artifact, or mutate host state.

Authoritative inputs are:

- ANYsolver source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- ANYsolver source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`
- Stage-P prerequisites V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`
- Provider V6 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN_V6.md`
- Provider V6 SHA-256:
  `C0BDA29EC0F68EF57A36F3F0CFF68236C41814E837532E4A9488AC12484985BD`

The SHA-256 of this packet is an external accepted launch parameter. The packet
does not contain its own hash. Any later Stage-C intent and report must bind the
accepted packet path, byte count, and external SHA-256 exactly.

## 2. Frozen names and roots

Qualification root `Q` is:

`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28`

Stage-C evidence root `C` is:

`Q\provider-stage-c-C0BDA29E`

The names that must be absent from both WSL enumeration forms are:

- `ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`
- `ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1`

The corresponding import directories that must be absent are:

- `Q\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`
- `Q\wsl\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1`

This packet does not create `C` or inspect those paths. A later authority must
require every existing ancestor to be a direct, non-reparse directory and every
owned Stage-C target to be absent before creation. No receipt may overwrite,
repair, reuse, or delete another path.

## 3. Transport and shared execution envelope

The future Stage-C run consists of exactly five ordered `shell_command` calls,
one process at a time. Every call uses `login=false`, the exact command field in
Section 4, and the exact working directory `C:\Github\ANYopenSoft`.

The fixed outer PowerShell host supplied by `shell_command` is transport only.
For C01 it evaluates the one short, transparent, read-only identity expression
shown below without starting a child shell. C02-C05 each contain only one call
operator followed by the absolute `wsl.exe` path and literal arguments. No
task-authored PowerShell child, script, function, loop, here-string, pipeline to
another process, redirection, encoded command, launcher, `Start-Process`, hidden
window, cmd/batch indirection, Defender exception, or command-byte substitution
is permitted.

The shared wall-clock envelope is 300 seconds. The sum of per-call hard timeouts
is 195 seconds, leaving 105 seconds for intent, durable evidence publication,
and terminal accounting. Resource limits are one native child at a time, less
than 500 MB combined resident memory, no GPU, no network, and no concurrent
ecosystem performance lease. A timeout, nonzero exit, identity mismatch,
service failure, evidence failure, or security event is terminal. There is no
retry, fallback, cleanup, distro action, or continuation after first failure.

## 4. Exact ordered commands

### C01 - WSL binary identity

Exact command field, one LF-free line:

```powershell
$p='C:\WINDOWS\system32\wsl.exe';$f=Get-Item -LiteralPath $p -Force;$h=Get-FileHash -LiteralPath $p -Algorithm SHA256;$s=Get-AuthenticodeSignature -LiteralPath $p;[ordered]@{path=$f.FullName;bytes=[int64]$f.Length;file_version=$f.VersionInfo.FileVersion;product_version=$f.VersionInfo.ProductVersion;sha256=$h.Hash;signature_status=[string]$s.Status;signer_subject=$s.SignerCertificate.Subject;signer_issuer=$s.SignerCertificate.Issuer;signer_thumbprint=$s.SignerCertificate.Thumbprint;signer_serial=$s.SignerCertificate.SerialNumber}|ConvertTo-Json -Compress
```

Execution metadata:

| Field | Frozen value |
|---|---|
| timeout_ms | `30000` |
| sandbox_permissions | `use_default` |
| escalation justification | absent |
| expected exit | `0` |
| stdout contract | exactly one UTF-8 JSON object and one terminal LF |
| stderr contract | zero bytes |

Acceptance requires exact normalized path
`C:\WINDOWS\system32\wsl.exe`, positive byte count, 64 uppercase hexadecimal
SHA-256, nonempty file/product versions, signature status `Valid`, and nonempty
signer subject, issuer, thumbprint, and serial. The observed values are evidence;
this packet does not predeclare them.

### C02 - WSL version

Exact command field:

```powershell
& 'C:\WINDOWS\system32\wsl.exe' --version
```

| Field | Frozen value |
|---|---|
| timeout_ms | `30000` |
| sandbox_permissions | `use_default` |
| escalation justification | absent |
| expected exit | `0` |
| stdout contract | preserve exact binary output; decoded text must identify WSL `2.6.1.0` |
| stderr contract | preserve exact binary output; semantic acceptance requires no error |

### C03 - WSL status

Exact command field:

```powershell
& 'C:\WINDOWS\system32\wsl.exe' --status
```

| Field | Frozen value |
|---|---|
| timeout_ms | `45000` |
| sandbox_permissions | `require_escalated` |
| escalation justification | `Allow this read-only WSL status query outside the sandbox; it changes no distribution or host state.` |
| prefix_rule | absent |
| expected exit | `0` |
| stdout contract | preserve exact binary output; decoded text must prove a functioning WSL2 service and default version `2` |
| stderr contract | preserve exact binary output; semantic acceptance requires no access-denied or service error |

### C04 - Verbose distribution enumeration

Exact command field:

```powershell
& 'C:\WINDOWS\system32\wsl.exe' --list --verbose
```

| Field | Frozen value |
|---|---|
| timeout_ms | `45000` |
| sandbox_permissions | `require_escalated` |
| escalation justification | `Allow this read-only WSL distribution enumeration outside the sandbox; it changes no distribution or host state.` |
| prefix_rule | absent |
| expected exit | `0` |
| stdout contract | preserve exact binary output and decoded ordered rows |
| stderr contract | preserve exact binary output; semantic acceptance requires no access-denied or service error |

The parsed rows must be unique and well formed. Both frozen provider names must
be absent. Every enumerated version value must be recorded without changing any
distribution.

### C05 - Quiet distribution enumeration

Exact command field:

```powershell
& 'C:\WINDOWS\system32\wsl.exe' --list --quiet
```

| Field | Frozen value |
|---|---|
| timeout_ms | `45000` |
| sandbox_permissions | `require_escalated` |
| escalation justification | `Allow this read-only WSL distribution enumeration outside the sandbox; it changes no distribution or host state.` |
| prefix_rule | absent |
| expected exit | `0` |
| stdout contract | preserve exact binary output and decoded ordered names |
| stderr contract | preserve exact binary output; semantic acceptance requires no access-denied or service error |

The names must be unique, must omit both frozen provider names, and must equal
the name projection of C04 under ordinal comparison. Empty enumeration is valid
only when both C04 and C05 are successful and both independently encode zero
rows.

## 5. Durable intent and receipt paths

No path below exists or is created by this packet. A later accepted execution
must use CreateNew semantics and retain every partial and final on all outcomes.

Campaign paths:

- `C\stage_c_intent.json.partial|json`
- `C\stage_c_report.json.partial|json`
- `C\stage_c_failure.json.partial|json`

For each check ID `C01` through `C05`, paths are:

- `C\checks\<ID>\intent.json.partial|json`
- `C\checks\<ID>\stdout.bin.partial|bin`
- `C\checks\<ID>\stderr.bin.partial|bin`
- `C\checks\<ID>\process.json.partial|json`
- `C\checks\<ID>\result.json.partial|json`

The Stage-C intent schema is:

`anysolver.no_numba_residual.provider_stage_c_intent/1`

It records the accepted packet path/bytes/external hash, all governing source
and plan identities, exact roots/names, exact five command strings and ordinal
order, command-field SHA-256 values, workdir, login/escalation metadata,
timeouts, resource envelope, preflight path state, process inventory, UTC, and
the no-mutation/no-retry boundary.

Each process receipt schema is:

`anysolver.no_numba_residual.provider_stage_c_process/1`

It records check ID/ordinal, exact command and command hash, transport identity,
native image path, PID when exposed by the accepted executor, start/exit UTC,
wall milliseconds, timeout state, exit code, stdout/stderr path/bytes/hash,
process-start and wait observations, direct-child inventory, pre/post WSL-related
process inventory, residual state, peak resident memory when exposed, sandbox
mode, escalation grant identity, and exception/security facts. If the accepted
executor cannot produce sufficient start/wait/residual evidence, the check must
not launch.

Each check result schema is:

`anysolver.no_numba_residual.provider_stage_c_check/1`

It records all process-receipt identities, raw output identities, lossless
decode method/code page, parsed fields/rows, expected-exit evaluation,
check-specific semantic gates, provider-name absence, infrastructure failures,
UTC, and success. It embeds no self-hash.

The final report schema is:

`anysolver.no_numba_residual.provider_stage_c_report/1`

It binds the intent, the five ordered check results and their external file
hashes, C01 binary/signature identity, C02 version ledger, C03 service/default
version, C04/C05 raw and parsed inventories, ordinal cross-enumeration equality,
both provider-name and both import-directory absence results, exact Windows
version/kernel/architecture, lease/process/resource accounting, no-host-mutation
proof, first-failure truth, and aggregate success. It does not hash itself or an
index. A failure report uses schema
`anysolver.no_numba_residual.provider_stage_c_failure/1` and preserves the last
completed ordinal plus the exact failed/timeout/security state.

Every binary stream is published byte-exact before its process/result final.
Every JSON final is UTF-8 without BOM, canonical key ordering, LF-final, and
durably written with file and parent-directory synchronization before its hash
can become a predecessor. No report is successful if a required receipt or raw
stream is absent, partial, contradictory, or not durably closed.

## 6. Acceptance and stop boundary

Stage C may be accepted only when all five checks complete once in order and all
of these facts are proven:

- `wsl.exe` identity and valid Microsoft signature are fully recorded;
- WSL version is exactly `2.6.1.0`;
- the WSL2 service is functioning and default version is `2`;
- verbose and quiet distribution enumeration both succeed and agree ordinally;
- both frozen provider names are absent;
- both frozen import directories are absent and are not reparse points;
- Windows version, kernel, and architecture are exact;
- no conflicting task process or ecosystem performance lease exists;
- every process is waited, no owned child remains, and resource bounds hold;
- no host, distro, repository, evidence-history, or Defender state was mutated.

Any inability to prove one item is fail-closed `evidence_limited` or failure,
never success. Stage-C acceptance authorizes no Stage-M metadata request,
artifact acquisition, distro import, provider build, Stage P, cleanup, retry,
publication, source edit, Git/GitHub action, or Defender exception. Each later
stage requires its own content-addressed command packet and explicit authority.

## 7. Current authority

Creating and hashing this Markdown packet is the only authorized action. No
Stage-C command, receipt producer, evidence root, process, capability query,
escalation request, or lease is authorized now.
