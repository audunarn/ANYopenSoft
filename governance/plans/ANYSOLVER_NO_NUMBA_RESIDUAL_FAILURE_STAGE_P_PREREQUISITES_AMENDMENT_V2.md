# ANYsolver No-Numba Residual Failure Stage-P Prerequisites Amendment V2

## 1. Supersession and authority

This plan mechanically supersedes the rejected prerequisite plan while retaining
its bounded Stage-P diagnosis scope.

- Rejected evidence path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STAGE_P_PREREQUISITES_AMENDMENT.md`
- Rejected evidence SHA-256:
  `FD3D4210EB25D4EB2A0E920F2D80E778F02EC5C1EFAB45E57552834D822587C1`
- Rejected evidence disposition: preserve byte-for-byte; never overwrite,
  delete, clean, or execute as authority.
- Accepted diagnosis plan SHA-256:
  `7472B4ECE6430B1B13BE24BCA3C24DA5074DC458BC5B92EB7E65C8C7F1AB1179`
- Accepted STATIC-S01 SHA-256:
  `CDF15DD7DFACD3548A15DE3871B74BFE3714A986E7F40B38670585FB345A7932`
- Accepted static correction SHA-256:
  `C0F01FC58F4D6A00E9464AE3B2B3B6B72BBE28A82C7C97CD60EBC211C93B0314`
- Source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- Source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`

This V2 plan is plan-only. It authorizes no artifact creation or acquisition,
provider import, environment creation, import, test, probe, process launch,
GitHub query, source/test/workflow edit, cleanup, PERF request, or Stage-P run.
All retained provisions of the accepted diagnosis plan remain binding unless
this V2 plan explicitly narrows or supersedes them.

Stage P is `BLOCKED` until the provider, artifacts, environments, scripts,
manifests, reports, commands, old-run audit, and lease are separately accepted.

## 2. Retained host facts and fail-closed provider boundary

Retained capability facts are limited to:

- `C:\WINDOWS\system32\wsl.exe` exists.
- WSL version is `2.6.1.0`; kernel is `6.6.87.2-1`.
- WSL distribution enumeration returned
  `Wsl/EnumerateDistros/Service/E_ACCESSDENIED`.
- Distribution availability is therefore `access_denied/unproven`.
- Docker was not found in the bounded recovered command inventory.
- `py.exe` was not found in that inventory.
- `C:\Python\Python313\python.exe` reports CPython `3.13.9` and is eligible
  only as a later accepted Windows initializer interpreter.

No ambient Linux provider is accepted. No Linux command, import, or Stage-P
action may occur until a separately accepted provider-capability manifest proves
the exact dedicated lane. No capability retry or ambient substitution is part
of this plan.

## 3. Frozen roots and provider name

- Qualification root `Q`:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28`
- Evidence root `E`:
  `C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28`
- Source worktree `S`:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`
- Linux view of `S`:
  `/mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/worktrees/ANYsolver-ci-six-failure-correction`
- Dedicated provider name:
  `ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1`
- Dedicated WSL distribution name:
  `ANYsolver-Ubuntu-24.04-82a9db28`
- Provider archive path:
  `Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar`
- Provider capability manifest path:
  `Q\provider\provider_capability_manifest.json`
- Dedicated import path:
  `Q\wsl\ANYsolver-Ubuntu-24.04-82a9db28`
- Linux qualification prefix:
  `/opt/anysolver-no-numba-residual-82a9db28`
- Linux command cwd root:
  `/opt/anysolver-no-numba-residual-82a9db28/cwd`

All paths must be exact, direct, non-reparse, and fresh at their registered
creation boundary. A foreign or pre-existing output is terminal. No general
cleanup, reuse, overwrite, or retry is allowed.

## 4. Self-contained provider contract

V2 selects one self-contained provider rather than an incomplete host rootfs plus
ambient library installation. The provider archive is a dedicated Ubuntu 24.04
amd64 WSL2 rootfs containing all four complete, offline Python environments and
all required rootfs shared libraries.

The provider must be produced by a separately reviewed provider-build plan. Its
accepted capability manifest must freeze:

- provider name and schema;
- official Canonical Ubuntu 24.04 amd64 rootfs source URL, effective URL,
  version/point release, acquisition UTC, bytes, and SHA-256;
- every provider-build input URL, path, bytes, and SHA-256;
- exact CPython `3.11.15`, `3.12.13`, and `3.13.14` Linux amd64 artifact
  provenance;
- complete `/var/lib/dpkg/status` package name/version/architecture inventory;
- complete rootfs library package inventory used by Python, NumPy, SciPy,
  llvmlite, and Numba;
- recursive ELF dependency closure for every lane Python executable and every
  installed `.so`, with interpreter, SONAME, resolved absolute path, owning
  package/version, bytes, SHA-256, and zero unresolved dependencies;
- glibc, libstdc++, libgcc, OpenBLAS/BLAS/LAPACK, OpenMP, zlib, libffi,
  OpenSSL, sqlite, bz2, lzma, ncurses/readline, UUID, and loader identities;
- exact installed lane roots and immutable lane locks;
- every installed distribution version, wheel filename/hash, RECORD validation,
  and origin;
- provider creation transcript and post-build validation report;
- no network requirement after provider acquisition;
- no editable, VCS, source-tree, user-site, or system-site package leakage.

The self-contained provider is the only accepted answer to the rootfs-library
and Python installation problem. Stage P does not run `apt`, `pip install`, a
compiler, linker, package resolver, or `actions/python-versions` setup script.
Any future switch to direct `actions/python-versions` archives requires a new
plan that freezes archive member validation, setup script hash/argv, install
prefix, and the complete offline rootfs library closure before execution.

The provider archive and capability manifest are not yet acquired or accepted.
Their absence is a terminal prerequisite blocker, not permission to discover or
build them during Stage P.

## 5. Acquisition failure truth

Any separately authorized provider/artifact acquisition must:

- use a versioned direct HTTPS URL and refuse redirects;
- create a unique same-directory partial with exclusive ownership;
- record request/effective URL, HTTP status, Content-Length, actual bytes,
  SHA-256, UTC timing, and process state;
- atomically publish a final only after all checks pass;
- preserve every failed owned partial and an atomic failure receipt;
- never delete a failed partial, foreign path, or prior evidence;
- never retry automatically.

Failed partials are ineligible inputs but remain immutable first-failure
evidence. This supersedes the rejected plan's partial-removal language.

## 6. Immutable build inputs and post-build reports

The prior mixed environment manifest is retired. V2 separates immutable inputs
from atomic post-build evidence.

### 6.1 Immutable build-input manifest

- Path: `Q\manifests\build_input_manifest.json`
- Schema: `anysolver.no_numba_residual.build_input_manifest/1`

It is frozen before provider/environment creation and contains only immutable
inputs and expected contracts:

- source commit/tree and governing evidence hashes;
- provider archive/capability-manifest identities;
- all upstream artifact URLs, paths, bytes, SHA-256 values, tags, architectures,
  and acquisition receipts;
- exact lane lock paths/hashes and expected distributions;
- exact ANYsolver wheel input/build identity;
- expected lane Python, NumPy, SciPy, BLAS/LAPACK, Numba/llvmlite, pytest,
  dependency versions, and origins;
- no post-build observations or mutable status fields.

### 6.2 Atomic post-build environment reports

- U311 partial/final:
  `Q\environment-reports\U311.environment_report.json.partial`
  and `Q\environment-reports\U311.environment_report.json`
- U312 partial/final:
  `Q\environment-reports\U312.environment_report.json.partial`
  and `Q\environment-reports\U312.environment_report.json`
- U313 partial/final:
  `Q\environment-reports\U313.environment_report.json.partial`
  and `Q\environment-reports\U313.environment_report.json`
- JIT313 partial/final:
  `Q\environment-reports\JIT313.environment_report.json.partial`
  and `Q\environment-reports\JIT313.environment_report.json`
- Schema:
  `anysolver.no_numba_residual.environment_report/1`

Each report is atomically published only after validation and records actual
provider identity, Python/platform/glibc, package inventory, origins, RECORD
verification, shared-library closure, BLAS/LAPACK/threading details, `pip check`
equivalent dependency consistency, environment variables, and source-shadowing
rejection.

U311, U312, and U313 must prove both `numba` and `llvmlite` absent from the
distribution inventory and separately prove imports fail with
`ModuleNotFoundError` naming the requested top-level package. JIT313 must prove
exact accepted Numba and llvmlite versions/origins and compiled functionality.

Reports are outputs and cannot be inputs to their own build. Each report hash is
accepted only after its atomic final exists.

## 7. Artifact-manifest self-hash repair

- Artifact manifest path: `Q\manifests\artifact_manifest.json`
- Schema: `anysolver.no_numba_residual.artifact_manifest/2`

`artifact_manifest.json` must exclude itself from its `files` rows and from every
internal hash graph. It must never claim or store its own SHA-256.

Its exact SHA-256 is an external, independently accepted launch-envelope value:

- initializer argument:
  `--artifact-manifest-sha256 <ACCEPTED_64_HEX>`
- runner argument:
  `--artifact-manifest-sha256 <ACCEPTED_64_HEX>`

The literal accepted hash replaces the placeholder in every reviewed launch
command before execution. Initializer and runner hash the manifest bytes once
and compare them to that external argument before trusting any row.

The manifest rows include the initializer, runner, six instruments,
`build_input_manifest.json`, `command_manifest.json`, provider capability
manifest, provider archive, four accepted environment reports, lane locks,
accepted ANYsolver wheel, and governing evidence. No row is self-referential.

## 8. Frozen artifact paths

Plain Python artifacts outside `E`:

- `Q\runner\initialize_evidence_82a9db28.py`
- `Q\runner\run_one_command_82a9db28.py`
- `Q\instruments-src\environment_probe_82a9db28.py`
- `Q\instruments-src\corotational_backend_probe_82a9db28.py`
- `Q\instruments-src\impact_exclusion_probe_82a9db28.py`
- `Q\instruments-src\lifecycle_event_probe_82a9db28.py`
- `Q\instruments-src\selected_nlg008_report_probe_82a9db28.py`
- `Q\instruments-src\nlg008_operator_probe_82a9db28.py`

JSON inputs:

- `Q\manifests\artifact_manifest.json`
- `Q\manifests\build_input_manifest.json`
- `Q\manifests\command_manifest.json`

All Python is plain UTF-8 without BOM and LF-only, created via `apply_patch` and
independently content-addressed. No generated source, here-string, encoded
payload, PowerShell script, shell script, batch file, hidden launcher, nested
shell orchestration, or Defender exception is permitted.

None of these artifacts exists or may be created under this V2 plan-only action.

## 9. Installed-origin and source-test isolation

Every Linux command uses a unique cwd outside `S`:

`/opt/anysolver-no-numba-residual-82a9db28/cwd/<COMMAND_ID>`

Every pytest node is passed as an absolute Linux path under `S`, for example:

`/mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/worktrees/ANYsolver-ci-six-failure-correction/tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle`

Pytest argv always includes:

- `-B -I -m pytest`
- `-p no:cacheprovider`
- `--import-mode=importlib`
- an absolute `--rootdir` equal to the Linux view of `S`
- the unique absolute `--basetemp`
- only absolute test node paths under `S`.

Only selected test modules and their test-only helpers may load from `S`. The
environment probe and runner must reject:

- `anysolver` loaded from `S`;
- any runtime dependency loaded from `S`, another checkout, an editable path,
  user site, system site outside the accepted lane, pip cache, or ambient host;
- a non-test module whose resolved origin is under `S`.

`anysolver` and every runtime dependency must resolve from the accepted installed
wheel/environment under the exact lane prefix. `PYTHONPATH` is absent. The
installed ANYsolver version, wheel SHA-256, distribution metadata, module origin,
and RECORD must match the accepted manifests.

## 10. Initializer contract

The initializer uses only the Windows Python standard library and launches no
child process. It must:

1. Require exact CPython `3.13.9` and executable
   `C:\Python\Python313\python.exe`.
2. Accept the artifact-manifest path and external accepted SHA-256 as separate
   literal arguments.
3. Validate its own hash, runner/instrument hashes, input-manifest hashes,
   provider identities, four environment report hashes, governing evidence, and
   source receipt.
4. Validate exact direct/non-reparse ancestry and require `E` absent.
5. Create `E` one component at a time with no recursive deletion or reuse.
6. Copy only verified instrument bytes to `E\instruments` using exclusive
   creation, durable file flush, parent-directory flush, and read-back hash.
7. Create all command-owned directories and no unregistered path.
8. Create and durably publish campaign intent before any Stage-P child can run.
9. Set campaign start and an absolute shared deadline exactly 140 minutes later.
10. Atomically publish `E\initialization.json`, including the hash of the
    externally validated artifact manifest.

No initializer failure is cleaned or retried.

## 11. Runner, process, timeout, and evidence contract

The runner uses only the Linux Python standard library and executes one manifest
row. Before child creation it must:

1. Validate itself, the external artifact-manifest SHA argument, all manifests,
   accepted environment report, lane, provider, predecessor receipt, source
   receipt, command row, cwd, paths, origins, and deadline.
2. Require at least `command_timeout + 600` seconds remain before the shared
   absolute deadline. Otherwise it records deadline exhaustion and launches
   nothing.
3. Write `intent.json` with argv, cwd, environment, predecessor hash, expected
   exit policy, UTC/monotonic timing, parent PID, and planned output paths.
4. Flush and `fsync` the intent file, atomically rename it, then open and `fsync`
   its parent directory before child creation.

Child creation uses `subprocess.Popen` with `shell=False`, stdin `DEVNULL`, a
fresh session/process group, and a minimal `preexec_fn` that calls Linux
`prctl(PR_SET_PDEATHSIG, SIGKILL)` and verifies the parent PID did not change
before exec. A failure to establish PDEATHSIG is infrastructure failure.

On timeout the runner must:

1. Record a durable timeout checkpoint.
2. Send `SIGTERM` only to the owned process group.
3. Wait up to 10 seconds.
4. Send `SIGKILL` only to that group if it remains alive.
5. Wait/reap the direct child.
6. Enumerate `/proc` for the original child PID, process group, session, and
   known descendant identities.
7. Record every signal, wait result, exit status, descendant, residual process,
   and inability to prove termination.
8. Treat any residual or unproven process state as infrastructure failure.

This bounded owned-process termination is required safety handling, not general
cleanup. It never deletes files, caches, partials, environments, or evidence.

## 12. Unique per-command evidence map

For every exact command ID `X`, the command manifest maps these unique paths:

- cwd: `/opt/anysolver-no-numba-residual-82a9db28/cwd/X`
- basetemp: `E\commands\X\basetemp`
- Numba cache: `E\commands\X\cache\numba`
- Python cache: `E\commands\X\cache\python`
- Matplotlib cache: `E\commands\X\cache\matplotlib`
- XDG cache: `E\commands\X\cache\xdg`
- joblib cache: `E\commands\X\cache\joblib`
- TEMP: `E\commands\X\tmp\temp`
- TMP: `E\commands\X\tmp\tmp`
- TMPDIR: `E\commands\X\tmp\tmpdir`
- intent partial/final: `E\commands\X\intent.json.partial` and
  `E\commands\X\intent.json`
- start receipt: `E\commands\X\start.json`
- stdout: `E\commands\X\transcript\stdout.bin`
- stderr: `E\commands\X\transcript\stderr.bin`
- transcript index partial/final:
  `E\commands\X\transcript\index.json.partial` and
  `E\commands\X\transcript\index.json`
- process-tree start partial/final:
  `E\commands\X\process\start.json.partial` and
  `E\commands\X\process\start.json`
- process-tree termination partial/final:
  `E\commands\X\process\termination.json.partial` and
  `E\commands\X\process\termination.json`
- process-tree final partial/final:
  `E\commands\X\process\final.json.partial` and
  `E\commands\X\process\final.json`
- instrument payload partial/final:
  `E\commands\X\instrument_payload.json.partial` and
  `E\commands\X\instrument_payload.json`
- pytest JUnit output when applicable:
  `E\commands\X\pytest-junit.xml`
- runner result partial/final: `E\commands\X\result.json.partial` and
  `E\commands\X\result.json`.

Every path is exclusive to one command. The environment maps
`NUMBA_CACHE_DIR`, `PYTHONPYCACHEPREFIX`, `MPLCONFIGDIR`, `XDG_CACHE_HOME`,
`JOBLIB_TEMP_FOLDER`, `TEMP`, `TMP`, and `TMPDIR` exactly to those paths and sets
`PYTHONNOUSERSITE=1` and `PYTHONDONTWRITEBYTECODE=1`.

## 13. Instruments

The six instruments retain the rejected plan's observation-only scope:

- environment provenance and Numba/llvmlite status;
- C11 corotational backend and physical diagnostics;
- C12-C16 complete ordered impact exclusions;
- standalone C17 ordered lifecycle materialization/ownership;
- selected `NLG-008` report only, never the 130-case report;
- 24/32 ring and selected NLG-008 operators, constraints, eigenpairs, residuals,
  signs, sorting/grouping, SciPy branch, and exceptions.

Each instrument writes only its command's unique
`instrument_payload.json.partial`, durably flushes file and parent, and
atomically publishes the final only on successful observation. Transparent
wrappers preserve arguments/results/exceptions and restore in `finally`.
Evidence-limited wrapper targets must be resolved in the independently reviewed
instrument bytes before acceptance; no further source reread is authorized by
this plan.

## 14. Command set, predecessors, and exact exit policies

The 28 command IDs and order are unchanged:

`ENV-U311`, `ENV-U312`, `ENV-U313`, `ENV-JIT313`, `COROT-U311`,
`COROT-U312`, `COROT-U313`, `COROT-JIT313`, `COROT-INST-U311`,
`COROT-INST-U312`, `COROT-INST-U313`, `COROT-INST-JIT313`, `IMPACT-U313`,
`IMPACT-JIT313`, `IMPACT-INST-U313`, `IMPACT-INST-JIT313`,
`COMPILED-JIT313`, `LIFECYCLE-U313`, `LIFECYCLE-INST-U313`,
`NLG-TEST-U311`, `NLG-TEST-U312`, `NLG-TEST-U313`, `NLG-REPORT-U311`,
`NLG-REPORT-U312`, `NLG-REPORT-U313`, `NLG-OP-U311`, `NLG-OP-U312`,
`NLG-OP-U313`.

Each result contains `ordinal`, `command_id`, and
`predecessor_receipt_sha256`. Ordinal 1 binds the initialization receipt hash;
each later ordinal binds the immediately preceding accepted `result.json` hash.
The runner refuses a missing, mismatched, out-of-order, or duplicate receipt.

Exact exit policies:

| Commands | Required process exit and diagnostic outcome |
| --- | --- |
| `ENV-U311`, `ENV-U312`, `ENV-U313`, `ENV-JIT313` | exit `0`; valid environment payload; U lanes prove both Numba and llvmlite absent; JIT lane proves both present and accepted |
| `COROT-U311`, `COROT-U312`, `COROT-U313` | pytest exit `1`; exactly C11 fails; no error/collection failure/extra node |
| `COROT-JIT313` | pytest exit `0`; exactly C11 passes |
| `COROT-INST-U311`, `COROT-INST-U312`, `COROT-INST-U313`, `COROT-INST-JIT313` | exit `0`; valid payload for exactly C11 |
| `IMPACT-U313` | pytest exit `1`; exact immutable no-JIT failure set C12-C16 and no other node |
| `IMPACT-JIT313` | pytest exit `0`; exactly C12-C16 pass |
| `IMPACT-INST-U313`, `IMPACT-INST-JIT313` | exit `0`; valid ordered-exclusion payload for exactly C12-C16 |
| `COMPILED-JIT313` | pytest exit `0`; exactly C01-C10 pass |
| `LIFECYCLE-U313` | pytest exit `1`; exactly C17 fails with the frozen counter mismatch and no error/extra node |
| `LIFECYCLE-INST-U313` | exit `0`; valid standalone C17 event payload |
| `NLG-TEST-U311` | pytest exit `0`; exact 24 and 32 nodes pass |
| `NLG-TEST-U312`, `NLG-TEST-U313` | pytest exit `1`; exact 24 node fails and exact 32 node passes |
| `NLG-REPORT-U311`, `NLG-REPORT-U312`, `NLG-REPORT-U313` | exit `0`; valid selected NLG-008 payload; internal case status preserved rather than converted to process failure |
| `NLG-OP-U311`, `NLG-OP-U312`, `NLG-OP-U313` | exit `0`; valid 24/32/NLG-008 operator payload with any production exception preserved in schema |

Pytest policy is verified from the unique JUnit file plus transcript and exact
node inventory, not exit code alone. A diagnostic exit `1` matching its exact
policy is accepted evidence and does not stop the sequence. The runner stops only
on exit-policy mismatch, infrastructure failure, invalid payload, identity
failure, process residual, or deadline refusal.

## 15. Timeouts and shared absolute deadline

Per-command hard timeouts remain:

- environment probes: 60 seconds;
- corotational, impact, lifecycle, and their instruments: 240 seconds;
- compiled JIT selection: 600 seconds;
- NLG tests and selected reports: 900 seconds;
- NLG operator instruments: 1,200 seconds.

The initializer freezes one campaign start and absolute deadline exactly 140
minutes later in `initialization.json`. Before every launch the runner revalidates
that absolute deadline and requires:

`remaining_seconds >= command_timeout_seconds + 600`

The final 600 seconds are an inviolable reserve for result/process accounting.
No command starts if it could consume that reserve. Deadline refusal is terminal,
durably recorded, and not retried. Wall-clock UTC and monotonic elapsed values are
both recorded; any contradictory or regressed clock evidence is infrastructure
failure.

## 16. Defender-safe direct transport

No task-authored inline PowerShell program, PowerShell script, `-EncodedCommand`,
here-string, `ExecutionPolicy Bypass`, `Start-Process`, hidden window, nested
shell, generated launcher, batch/cmd indirection, or Defender exception is
permitted.

Each top-level tool call contains one short literal native invocation with
`login=false`. The initializer command receives the artifact manifest hash as an
external literal argument. Each Linux command is one direct `wsl.exe --exec`
call to the accepted lane Python and runner, with one literal command ID and the
same external manifest hash. No variable, loop, pipeline, redirection,
aggregation, shell child, or placeholder is executable.

All 29 final command lines, including the concrete 64-hex manifest hash and lane
Python paths, must be frozen and parser-reviewed before any execution authority.

## 17. Separate old-run terminal audit gate

Before any Stage-P PERF lease request, run `31746877870` requires a separate,
explicitly authorized terminal audit. It must prove and preserve:

- run ID, event, branch, head SHA, workflow name, URL, status, conclusion,
  creation/update timestamps;
- exact terminal inventory and conclusions for all 24 expected Tests jobs;
- exact expected 24 unique job names;
- no active, queued, missing, duplicate, cancelled-without-accounting, or
  unexpected job;
- sole target Tests run and zero target Publish runs;
- all retained timeout/nonterminal snapshots and failure logs remain immutable;
- no rerun, retry, dispatch, cancellation, cleanup, publication, or mutation.

The terminal audit must be independently accepted. A nonterminal or incomplete
provider state blocks Stage P even if all local artifacts are ready.

## 18. Resource and lease boundaries

No PERF lease is requested now.

Provider acquisition/import validation, if later authorized, is a separate gate:
one WSL/native process at a time, no network during import, no test, no source
build, up to 4 CPU, 4 GiB RAM, 12 GiB disk, expected 15-30 minutes, hard 45
minutes.

Stage-P diagnosis requires a fresh lease only after provider/environment/script
acceptance and old-run terminal audit. Its exact envelope is:

- 28 commands sequentially;
- one WSL runner and one Python child at a time;
- no network, install, build, source edit, GPU, broad suite, Git, or GitHub query;
- up to 4 CPU, 6 GiB combined RAM, and 8 GiB evidence/cache disk;
- one shared 140-minute absolute deadline, including the 10-minute final reserve;
- first infrastructure or policy mismatch stops; no replay, tuning, or cleanup.

## 19. Acceptance order

1. Accept this V2 plan hash.
2. Separately accept the provider capability/acquisition/build plan.
3. Acquire/build and independently accept the self-contained provider,
   build-input manifest, capability manifest, lane locks, wheel, and four atomic
   environment reports.
4. Create via `apply_patch` only and accept initializer, runner, six instruments,
   artifact manifest, and command manifest.
5. Freeze the artifact manifest's own hash externally and render all 29 literal
   direct commands with no placeholder.
6. Validate source/worktree/ref/evidence preservation and fresh path gates.
7. Complete and independently accept the separate terminal audit of run
   `31746877870`.
8. Request and receive a fresh exact Stage-P PERF lease.
9. Initialize `E`, then execute 28 commands once in ordinal order.
10. Preserve all evidence and submit an independently reviewable diagnosis
    packet before any correction plan.

## 20. Prohibitions and current blockers

- No further static reread.
- No source, test, workflow, dependency, or production edit.
- No provider/artifact acquisition, environment creation, import, test, probe,
  run query, cleanup, or PERF request under this plan-only action.
- No ambient distro, Python, dependency, cache, source import, or editable path.
- No Numba or llvmlite in U lanes.
- No production impact-order change, broad skip, tolerance tuning, eigensolver
  change, or NLG physics change.
- No full 130-case report.
- No retry, overwrite, rollback, evidence deletion, Defender bypass, Git/GitHub
  mutation, push, publication, tag, or release.

Current blockers are explicit: provider availability is unproven; provider and
lane artifacts/reports are absent; scripts/manifests do not exist; artifact
manifest external hash is not frozen; evidence-limited instrument targets are
not reviewed; old run terminal audit is not accepted; and no lease exists.
