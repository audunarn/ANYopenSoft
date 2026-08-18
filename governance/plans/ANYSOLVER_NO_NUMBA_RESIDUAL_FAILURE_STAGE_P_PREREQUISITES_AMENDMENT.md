# ANYsolver No-Numba Residual Failure Stage-P Prerequisites Amendment

## 1. Status and authority

This is a content-addressed, plan-only amendment. It registers the complete
Stage-P prerequisite architecture but authorizes no artifact creation,
environment creation, import, test, probe, process launch, network access,
source edit, Git or GitHub action, cleanup, performance run, or Stage-P
execution.

Stage P remains `BLOCKED` until every artifact and environment identity defined
here is concrete, hash-pinned, independently reviewed, and separately accepted.
An unresolved value may appear in this Markdown plan as an explicit blocker,
but no executable JSON manifest may contain a null, placeholder, range-only,
mutable, ambient, or unresolved identity.

Immutable governing records:

- Diagnosis plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_DIAGNOSIS_PLAN.md`
- Diagnosis plan SHA-256:
  `7472B4ECE6430B1B13BE24BCA3C24DA5074DC458BC5B92EB7E65C8C7F1AB1179`
- Immutable STATIC-S01:
  `C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_REPORT_82A9DB28.md`
- STATIC-S01 SHA-256:
  `CDF15DD7DFACD3548A15DE3871B74BFE3714A986E7F40B38670585FB345A7932`
- Accepted static correction addendum:
  `C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_CORRECTION_ADDENDUM_82A9DB28.md`
- Static correction addendum SHA-256:
  `C0F01FC58F4D6A00E9464AE3B2B3B6B72BBE28A82C7C97CD60EBC211C93B0314`
- Source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- Source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`

Stage S is closed and evidence-limited. No further static source reread is part
of this amendment.

## 2. Read-only host capability inventory

The one bounded inventory performed for this amendment established only these
facts:

- WSL executable: `C:\WINDOWS\system32\wsl.exe`
- WSL version: `2.6.1.0`
- WSL kernel version: `6.6.87.2-1`
- WSLg version: `1.0.66`
- Windows version reported by WSL: `10.0.26200.8893`
- WSL distribution enumeration: failed with
  `Wsl/EnumerateDistros/Service/E_ACCESSDENIED`; no installed distribution is
  claimed.
- Docker executable: not found through the application-command inventory.
- Python launcher `py.exe`: not found through the application-command
  inventory.
- Windows Python executable: `C:\Python\Python313\python.exe`
- Windows Python version: `3.13.9`

Consequences:

- The host Windows interpreter is suitable only for a later accepted evidence
  initializer. It is not Ubuntu-equivalent execution evidence.
- No ambient WSL distribution is accepted or assumed.
- Docker is not an available mechanism and must not silently replace WSL.
- The required CPython 3.11.15, 3.12.13, and 3.13.14 Linux lanes do not exist as
  accepted local capabilities.

No escalation, distro launch, repository import, network request, install, or
environment creation was performed during this inventory.

## 3. Canonical roots and exact names

The following names are frozen:

- Qualification root `Q`:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28`
- Evidence root `E`:
  `C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28`
- Source worktree `S`:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`
- Linux view of `S`:
  `/mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/worktrees/ANYsolver-ci-six-failure-correction`
- Linux view of `E`:
  `/mnt/c/Github/ANYopenSoft/governance/evidence/ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28`
- Dedicated WSL distribution name:
  `ANYsolver-Ubuntu-24.04-82a9db28`
- Dedicated WSL import directory:
  `Q\wsl\ANYsolver-Ubuntu-24.04-82a9db28`
- Linux qualification prefix:
  `/opt/anysolver-no-numba-residual-82a9db28`

Every later gate must require exact direct, non-reparse path ancestry. `Q`, `E`,
the WSL import directory, every environment, and every command output must be
fresh at its registered creation boundary. Foreign or pre-existing content is a
terminal failure. No cleanup or reuse is permitted after a partial failure.

## 4. Selected Ubuntu-equivalent mechanism

The sole selected primary mechanism is a dedicated WSL2 import from an immutable
Canonical Ubuntu 24.04 amd64 WSL rootfs archive. The exact later import command
shape is:

```text
& 'C:\WINDOWS\system32\wsl.exe' --import ANYsolver-Ubuntu-24.04-82a9db28 C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\wsl\ANYsolver-Ubuntu-24.04-82a9db28 <ROOTFS_ABSOLUTE_PATH> --version 2
```

`<ROOTFS_ABSOLUTE_PATH>` is deliberately not executable text. Before any import,
an accepted environment manifest must replace it with one exact absolute path
whose immutable versioned Canonical URL, byte count, SHA-256, distribution,
architecture, release, and acquisition receipt are all frozen. A `current`,
`latest`, redirect-dependent, Store-managed, ambient, or mutable rootfs is
rejected.

The dedicated distribution must report all of the following before it becomes
eligible:

- Ubuntu release exactly `24.04` with the full point-release/build identity
  frozen in the environment manifest;
- architecture exactly `x86_64`/`amd64`;
- WSL version exactly 2;
- kernel and `/etc/os-release` values recorded;
- no inherited user profile, shell rc file, host Python path, editable install,
  system site package, or source checkout on `sys.path`;
- no network route used by any environment-build or Stage-P command.

The historical GitHub runner paths are evidence, not reusable environments:

- U311: CPython `3.11.15`, hosted path
  `/opt/hostedtoolcache/Python/3.11.15/x64`
- U312: CPython `3.12.13`, hosted path
  `/opt/hostedtoolcache/Python/3.12.13/x64`
- U313: CPython `3.13.14`, hosted path
  `/opt/hostedtoolcache/Python/3.13.14/x64`

The primary local reproduction must use exact Linux CPython artifacts for those
versions. Windows CPython 3.13.9 is not a substitute.

## 5. Offline artifact provenance

### 5.1 Required source classes

The environment manifest must bind immutable members from these source classes:

1. A versioned Canonical Ubuntu 24.04 amd64 WSL rootfs archive from an official
   Canonical HTTPS origin.
2. Exact CPython 3.11.15, 3.12.13, and 3.13.14 Linux Ubuntu-24.04 amd64 toolcache
   archives from immutable `actions/python-versions` release assets, or another
   independently accepted upstream binary source with equivalent provenance.
3. Exact wheels and source-independent lock records from direct immutable
   `files.pythonhosted.org` URLs for every runtime and test dependency.
4. An exact ANYsolver wheel built from source commit
   `82a9db28d67507c82ef15c631f582a0c3bf6740e` and tree
   `00b2b20691e73a05589b797b32352f1c760a2451`, with its build inputs and wheel
   member/RECORD validation independently accepted.

The source class is frozen here; concrete URLs, filenames, byte counts, and
SHA-256 values are currently unbound because no network or artifact inventory
was authorized. That is an explicit blocker, not permission to resolve artifacts
during Stage P.

### 5.2 Artifact acquisition boundary

Artifact acquisition requires a separate, reviewed command and authority. Each
download must use a versioned direct HTTPS URL, refuse redirects, create a fresh
same-directory partial with exclusive ownership, verify HTTP status, effective
URI, Content-Length, actual bytes, and SHA-256, then rename atomically. Failure
removes only a positively owned partial and publishes no accepted artifact.

Stage-P commands have no network authority. Environment creation must install
only from the accepted offline artifact directory with `--no-index`,
`--no-deps` where resolving a single frozen wheel, and `--require-hashes` for
each complete lane lock.

### 5.3 Exact lane set

The environment manifest must define exactly four lanes:

- `U311`: CPython 3.11.15, Numba absent.
- `U312`: CPython 3.12.13, Numba absent.
- `U313`: CPython 3.13.14, Numba absent.
- `JIT313`: CPython 3.13.14, exact Numba and transitive dependency versions
  present.

For U311/U312/U313, Numba must be absent from the lock and installation record,
and the environment probe must prove that importing `numba` fails specifically
with `ModuleNotFoundError` for `numba`. For JIT313, the exact Numba version,
origin, compiled capability, LLVM dependency identity, and import result are
mandatory.

Each lane lock must bind exact versions and hashes for Python packaging tools,
NumPy, SciPy, pytest, ANYsolver, every declared/runtime test dependency, and all
transitive dependencies. It must also bind the NumPy/SciPy build tags, BLAS/LAPACK
provider and version, glibc floor, architecture, and thread-control environment.
No lane is executable until its complete immutable graph is accepted.

## 6. Exact prerequisite artifact paths

The following plain files are registered. None exists or is authorized to be
created by this amendment.

Runner source root outside `E`:

- `Q\runner\initialize_evidence_82a9db28.py`
- `Q\runner\run_one_command_82a9db28.py`
- `Q\runner\artifact_manifest.json`
- `Q\runner\environment_manifest.json`
- `Q\runner\command_manifest.json`

Canonical instrument source root outside `E`:

- `Q\instruments-src\environment_probe_82a9db28.py`
- `Q\instruments-src\corotational_backend_probe_82a9db28.py`
- `Q\instruments-src\impact_exclusion_probe_82a9db28.py`
- `Q\instruments-src\lifecycle_event_probe_82a9db28.py`
- `Q\instruments-src\selected_nlg008_report_probe_82a9db28.py`
- `Q\instruments-src\nlg008_operator_probe_82a9db28.py`

The initializer copies only hash-verified instrument bytes from the canonical
source root into fresh `E\instruments` paths with the same basenames. Commands
execute only those evidence-root copies. This supersedes any ambiguous reading
that instrument creation itself may pre-create `E` before the initializer.

Every Python source must be ordinary UTF-8 without BOM and LF-only. Creation is
via `apply_patch`, one independently reviewed content-addressed artifact set.
There may be no generated source, here-string transport, encoded payload,
PowerShell script, batch file, shell script, launcher chain, hidden process, or
Defender exception.

## 7. Plain-Python artifact contracts

### 7.1 Initializer

`initialize_evidence_82a9db28.py` must use only the Python standard library and
must not import ANYsolver or any project package. Its exact responsibilities are:

1. Require `sys.version_info[:3] == (3, 13, 9)` and executable path exactly
   `C:\Python\Python313\python.exe` after case-insensitive Windows
   canonicalization.
2. Validate its own SHA-256 and the accepted hashes of the runner, six canonical
   instruments, three JSON manifests, governing plan, STATIC-S01, and static
   correction addendum against `artifact_manifest.json`.
3. Validate `Q` and all existing ancestors as direct, non-reparse directories.
4. Require `E` absent and every registered partial/final path absent.
5. Create `E` and its exact directory tree with one-component `os.mkdir` calls;
   never recursively delete, replace, or reuse a path.
6. Copy each verified instrument into `E\instruments` using exclusive binary
   creation, flush, `os.fsync`, read-back hash validation, and no overwrite.
7. Materialize command-owned directories only for the exact 28 command IDs in
   Section 10.
8. Atomically publish `E\initialization.json` from a fresh same-directory
   `.partial` only after all gates pass. The record contains UTC start/end,
   Python identity, every input/output hash, direct/reparse checks, created-path
   inventory, and success state.
9. On failure, emit the primary exception to stderr and leave every owned path
   intact. It performs no cleanup and no retry.

The initializer launches no child process and performs no network, Git, import,
test, probe, or environment action.

### 7.2 Runner

`run_one_command_82a9db28.py` must use only the Python standard library. It is
invoked inside the dedicated WSL distribution by the exact lane interpreter and
must:

1. Require Linux, the exact accepted lane Python version/executable, and the
   exact dedicated WSL distribution/environment identity.
2. Validate its own hash, all manifest hashes, `E\initialization.json`, selected
   command row, selected lane, source commit/tree receipt, installed origins, and
   every offline artifact hash before starting a child.
3. Reject any command not in the exact 28-ID allowlist.
4. Use the manifest argv array without parsing or interpolation, with
   `subprocess.Popen(..., shell=False, stdin=DEVNULL, start_new_session=True)`.
5. Set an explicit environment from the manifest, not inherited profile state.
6. Use the exact Linux cwd and require all Python/project origins outside the
   source checkout except the absolute pytest test files themselves.
7. Create fresh `start.json`, `stdout.bin`, and `stderr.bin` records using
   exclusive creation and durable flush before waiting.
8. Enforce the row timeout, record timeout and live process-group truth without
   cleanup or retry, and make timeout terminal.
9. Record exit code, UTC timing, `resource.getrusage(RUSAGE_CHILDREN)`, selected
   environment, argv, cwd, output hashes/bytes, and process state.
10. Atomically publish `result.json` from a fresh same-directory `.partial` only
    after durable output closure and identity revalidation.
11. Never delete, overwrite, retry, run a second command, or convert a failed
    command into success evidence.

The runner may launch only the one manifest child for its selected command. It
must not invoke a shell, PowerShell, `cmd.exe`, `Start-Process`, a hidden window,
Git, GitHub CLI, package installer, environment builder, or network client.

### 7.3 Instruments

All instruments are observation-only, accept explicit argparse arguments, write
only their registered fresh `.partial` output, flush and fsync it, and atomically
rename only on success. Every temporary monkeypatch is installed once and
restored in `finally`; arguments, results, and exceptions pass through without
semantic change.

- `environment_probe_82a9db28.py` records Python executable/version/ABI,
  platform, glibc, environment variables, `sys.path`, installed package
  versions/origins, Numba presence/absence, NumPy/SciPy configuration, BLAS and
  LAPACK identity, and source-shadowing rejection.
- `corotational_backend_probe_82a9db28.py` observes the frozen C11 setup once and
  records JIT state, selected/actual backend, fallback reason, displacement and
  circle residuals, and parity-relevant diagnostics. It does not change backend
  selection.
- `impact_exclusion_probe_82a9db28.py` observes C12-C16 and records JIT state,
  primary reason, and the complete ordered exclusion tuple. It does not reorder
  or filter production diagnostics.
- `lifecycle_event_probe_82a9db28.py` observes only C17 in a fresh process and
  records ordered materialization/ownership events, state counters, and object
  identities. No synthetic predecessor sequence is in scope.
- `selected_nlg008_report_probe_82a9db28.py` executes only selected case
  `NLG-008`, never the unfiltered 130-case report. It records status, metrics,
  bounds, and exact evidence fields.
- `nlg008_operator_probe_82a9db28.py` observes only the 24- and 32-element ring
  cases plus selected NLG-008. It transparently wraps the named production and
  SciPy calls once and records branch, dimensions, operator hashes/norms,
  constraint ranks/residuals, follower symmetry, raw and filtered eigenpairs,
  signs, sorting/grouping, Rayleigh values, modal residuals, exceptions, and
  selected solver kind.

Because STATIC-S01 closed some runtime call-target details as
`evidence_limited`, instrument source bytes are not yet frozen. Their later
artifact review must prove every concrete wrapped symbol exists at the accepted
source/wheel identity and that wrapper semantics are transparent. The runner
must reject an instrument whose final accepted hash is absent from the artifact
manifest.

## 8. JSON manifest contracts

### 8.1 `artifact_manifest.json`

Schema: `anysolver.no_numba_residual.artifact_manifest/1`

Required top-level keys:

```json
{
  "schema": "anysolver.no_numba_residual.artifact_manifest/1",
  "source_commit": "82a9db28d67507c82ef15c631f582a0c3bf6740e",
  "source_tree": "00b2b20691e73a05589b797b32352f1c760a2451",
  "governing_plan_sha256": "7472B4ECE6430B1B13BE24BCA3C24DA5074DC458BC5B92EB7E65C8C7F1AB1179",
  "static_report_sha256": "CDF15DD7DFACD3548A15DE3871B74BFE3714A986E7F40B38670585FB345A7932",
  "static_correction_sha256": "C0F01FC58F4D6A00E9464AE3B2B3B6B72BBE28A82C7C97CD60EBC211C93B0314",
  "files": []
}
```

Each `files` row must contain exact role, absolute Windows path, Linux path when
applicable, bytes, SHA-256, UTF-8/LF/BOM identity, and acceptance reference.
Rows must cover the initializer, runner, six instruments, all three manifests,
all environment inputs, all lane locks, and the accepted ANYsolver wheel.

### 8.2 `environment_manifest.json`

Schema: `anysolver.no_numba_residual.environment_manifest/1`

It must contain:

- exact WSL executable/version/kernel, distribution name, import path, rootfs
  source URL/path/bytes/SHA-256/release/architecture;
- exact CPython artifact URL/path/bytes/SHA-256 and installed executable for
  U311, U312, U313, and JIT313;
- exact lane lock path/SHA-256 and every package wheel filename/path/URL/bytes/
  SHA-256/version/tag;
- exact NumPy/SciPy/BLAS/LAPACK/glibc and thread-control identities;
- exact expected import versions and accepted origins;
- explicit Numba-absence proof contract for U lanes and exact Numba/LLVM
  contract for JIT313;
- offline acquisition receipts and environment-install transcripts;
- no-network, no-editable, no-system-site, and no-source-shadowing assertions.

### 8.3 `command_manifest.json`

Schema: `anysolver.no_numba_residual.command_manifest/1`

Every row must contain exact command ID, lane, Windows top-level argv, Linux
child argv, cwd, complete environment, timeout seconds, expected exit policy,
test or instrument selection, and the unique paths for:

- `basetemp`;
- `cache/numba`;
- `cache/python`;
- `cache/matplotlib`;
- `cache/xdg`;
- `cache/joblib`;
- `tmp/temp`;
- `tmp/tmp`;
- `start.json`;
- `stdout.bin`;
- `stderr.bin`;
- `result.json.partial`;
- `result.json`.

All Python child argv begin with `-B -I`. Every pytest argv also contains
`-p no:cacheprovider`. The environment sets exact absolute values for
`NUMBA_CACHE_DIR`, `PYTHONPYCACHEPREFIX`, `MPLCONFIGDIR`, `XDG_CACHE_HOME`,
`JOBLIB_TEMP_FOLDER`, `TEMP`, and `TMP`. It also sets
`PYTHONNOUSERSITE=1` and `PYTHONDONTWRITEBYTECODE=1`.

## 9. Environment creation mechanism

After artifact acceptance and a separate authority, environments are created in
the dedicated WSL distribution under:

- `/opt/anysolver-no-numba-residual-82a9db28/envs/cpython-3.11.15-no-numba`
- `/opt/anysolver-no-numba-residual-82a9db28/envs/cpython-3.12.13-no-numba`
- `/opt/anysolver-no-numba-residual-82a9db28/envs/cpython-3.13.14-no-numba`
- `/opt/anysolver-no-numba-residual-82a9db28/envs/cpython-3.13.14-numba`

Each environment is created from its accepted CPython artifact in fresh Linux
paths. Offline installation uses the exact lane lock with:

```text
<LANE_PYTHON> -B -I -m pip install --no-index --require-hashes --only-binary=:all: --find-links <ACCEPTED_LANE_WHEELHOUSE> -r <ACCEPTED_LANE_LOCK>
```

The literal rendered command, all substituted absolute paths, and every input
hash must be frozen before execution. A normal `pip check`, installed
distribution inventory, RECORD verification, and external-origin probe are
mandatory after each install. No environment may use `--system-site-packages`,
an editable/VCS/source install, ambient cache, or online resolver.

Environment creation is a separate heavy gate from Stage-P diagnosis. A failed
lane is preserved and disqualifies the whole environment set; no tuning or retry
is automatic.

## 10. Exact command set and order

The command manifest contains exactly these 28 IDs, in this order:

1. `ENV-U311`
2. `ENV-U312`
3. `ENV-U313`
4. `ENV-JIT313`
5. `COROT-U311`
6. `COROT-U312`
7. `COROT-U313`
8. `COROT-JIT313`
9. `COROT-INST-U311`
10. `COROT-INST-U312`
11. `COROT-INST-U313`
12. `COROT-INST-JIT313`
13. `IMPACT-U313`
14. `IMPACT-JIT313`
15. `IMPACT-INST-U313`
16. `IMPACT-INST-JIT313`
17. `COMPILED-JIT313`
18. `LIFECYCLE-U313`
19. `LIFECYCLE-INST-U313`
20. `NLG-TEST-U311`
21. `NLG-TEST-U312`
22. `NLG-TEST-U313`
23. `NLG-REPORT-U311`
24. `NLG-REPORT-U312`
25. `NLG-REPORT-U313`
26. `NLG-OP-U311`
27. `NLG-OP-U312`
28. `NLG-OP-U313`

Selections are frozen as follows:

- `ENV-*`: the environment probe only.
- `COROT-*`: only
  `tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle`.
- `COROT-INST-*`: the corotational instrument for that same setup only.
- `IMPACT-*`: exactly C12-C16 from the accepted diagnosis plan.
- `IMPACT-INST-*`: impact instrumentation for exactly C12-C16.
- `COMPILED-JIT313`: exactly the ten compiled-only individual nodes C01-C10;
  no whole test file.
- `LIFECYCLE-U313`: only
  `tests/test_nonlinear_state_lifecycle.py::test_force_control_store_matches_mapping_and_materializes_owned_snapshots`.
- `LIFECYCLE-INST-U313`: that same standalone setup in a separate fresh
  process; no predecessor sequence.
- `NLG-TEST-*`: only the 24-element `[24-0.06]` and 32-element `[32-0.035]`
  follower-pressure nodes.
- `NLG-REPORT-*`: selected `NLG-008` through
  `selected_nlg008_report_probe_82a9db28.py`; never the full 130-case report.
- `NLG-OP-*`: only circumferential counts 24 and 32 plus selected `NLG-008`
  through `nlg008_operator_probe_82a9db28.py`.

Per-command hard timeouts are:

- `ENV-*`: 60 seconds.
- `COROT-*`, `COROT-INST-*`, `IMPACT-*`, `IMPACT-INST-*`, and lifecycle
  commands: 240 seconds each.
- `COMPILED-JIT313`: 600 seconds.
- `NLG-TEST-*`: 900 seconds each.
- `NLG-REPORT-*`: 900 seconds each.
- `NLG-OP-*`: 1,200 seconds each.

Commands execute sequentially, one runner and one child at a time. First failure
stops the sequence. No command is replayed, tuned, broadened, or retried.

## 11. Defender-safe direct transport

No PowerShell file, inline task-authored PowerShell program, here-string,
`-EncodedCommand`, `ExecutionPolicy Bypass`, `Start-Process`, hidden window,
batch/cmd indirection, generated launcher, nested shell, or Defender exception is
allowed.

The Codex `shell_command` fixed outer host may transport only one short literal
native invocation per tool call with `login=false`. The exact initializer call
shape is:

```text
& 'C:\Python\Python313\python.exe' -B -I C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\initialize_evidence_82a9db28.py --artifact-manifest C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\artifact_manifest.json --environment-manifest C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\environment_manifest.json --command-manifest C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\command_manifest.json --evidence-root C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28
```

Each Stage-P command uses one direct WSL call whose literal command ID is the
only changing argument:

```text
& 'C:\WINDOWS\system32\wsl.exe' --distribution ANYsolver-Ubuntu-24.04-82a9db28 --exec <LANE_PYTHON> -B -I /mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/qualification/ANYsolver-no-numba-residual-82a9db28/runner/run_one_command_82a9db28.py --artifact-manifest /mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/qualification/ANYsolver-no-numba-residual-82a9db28/runner/artifact_manifest.json --environment-manifest /mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/qualification/ANYsolver-no-numba-residual-82a9db28/runner/environment_manifest.json --command-manifest /mnt/c/Users/AudunArnesenNyhus/AppData/Local/ANYrelease/qualification/ANYsolver-no-numba-residual-82a9db28/runner/command_manifest.json --command-id <EXACT_COMMAND_ID>
```

`<LANE_PYTHON>` and `<EXACT_COMMAND_ID>` must be rendered into 28 separate
literal commands in the accepted command-manifest review packet. Placeholder
text is never executable. No loop or aggregator may execute the command set.

## 12. Resource envelopes and later lease boundaries

No lease is requested by this amendment.

Future environment import/install lease request:

- one WSL/native process at a time;
- no network, GPU, build from source, test, or benchmark;
- up to 4 logical CPU cores, 4 GiB RAM, and 12 GiB fresh disk;
- expected 15-30 minutes, hard outer limit 45 minutes;
- exact import and four offline install commands submitted literally in advance.

Future Stage-P diagnostic lease request:

- exact 28-command manifest and 28 literal direct invocations;
- sequential execution, one WSL runner plus one Python child at a time;
- no network, GPU, build, package install, source edit, or broad/full suite;
- up to 4 logical CPU cores, 6 GiB combined RAM, and 8 GiB fresh evidence/cache
  disk;
- expected 60-100 minutes;
- shared hard deadline 140 minutes, preserving 10 minutes for final evidence and
  process-state accounting;
- first failure stops; no retry, cleanup, or alternate environment.

Any acquisition, environment creation, or diagnostic qualification requires its
own exact command review and explicit PERF lease where applicable.

## 13. Acceptance gates before any artifact creation or execution

The next accepted milestone must, in order:

1. Independently accept this amendment identity.
2. Acquire and accept every immutable offline artifact, with no Stage-P action.
3. Create via `apply_patch` only the initializer, runner, six instruments, and
   three JSON manifests at the registered paths.
4. Freeze exact bytes, LF/CR/BOM state, SHA-256, AST/compile-only syntax evidence,
   schemas, and semantic review for every artifact without importing project
   code.
5. Prove all executable manifest values concrete and no placeholder remains.
6. Revalidate source commit/tree, source worktree cleanliness, frozen worktrees/
   refs, accepted reports, absent/direct/non-reparse output paths, and no task
   worker.
7. Obtain separate authority and a PERF lease for dedicated WSL import and
   offline environment creation.
8. Independently accept the completed environment report and installed origins.
9. Obtain a fresh exact Stage-P PERF lease.
10. Run the 28 commands once in order and preserve all outcomes.

Stage P must not begin if any artifact identity, environment identity, origin,
lock, BLAS detail, command argv, path, timeout, or process boundary remains
unresolved.

## 14. Preserved scope and prohibitions

- Preserve the accepted source commit and all existing worktrees, refs, dirty
  files, reports, failure evidence, caches, and qualification artifacts.
- Do not clean, delete, prune, reset, restore, overwrite, or reuse any evidence.
- Do not edit source, tests, workflows, dependency metadata, or production
  behavior under this prerequisites amendment.
- Do not install Numba into generic no-Numba lanes.
- Do not change production impact-exclusion ordering.
- Do not skip the generic corotational, impact, lifecycle, V01, or V02 ownership
  questions by broad marker or file exclusion.
- Do not run V01's full 130-case report in Stage P.
- Do not tune NLG-008 tolerances, eigensolver choices, or physics before accepted
  runtime evidence.
- Do not query GitHub, poll or rerun old CI, integrate, push, publish, tag, or
  release.
- Do not restore, whitelist, exclude, or otherwise bypass Windows Defender.

## 15. Current blocker ledger

The architecture is frozen, but execution remains blocked by facts not available
under this plan-only authority:

1. WSL distribution presence was not proven; enumeration was access-denied.
2. The immutable Ubuntu rootfs artifact is not acquired or hash-bound.
3. Exact Linux CPython artifacts are not acquired or hash-bound.
4. Exact remote-CI NumPy, SciPy, BLAS, pytest, packaging, and JIT dependency
   identities are not yet frozen into offline locks.
5. An accepted ANYsolver wheel for commit `82a9db28` is not yet bound.
6. Initializer, runner, instruments, and JSON manifests do not yet exist.
7. Evidence-limited concrete wrapper targets still require independent artifact
   review before instrument bytes can be accepted.
8. No environment or Stage-P performance lease has been requested or granted.

These are explicit prerequisites. They are not authorization to browse, acquire,
install, generate, execute, or substitute ambient state.
