# ANYsolver No-Numba Residual Provider Capability, Acquisition, and Build Plan

## 1. Authority and baseline

This is a content-addressed plan only. It defines the provider program required
by the accepted Stage-P prerequisites but authorizes no capability command,
network request, artifact acquisition, provider import/build/export, environment
creation, package action, import, test, probe, Git/GitHub query, source edit,
cleanup, or PERF request.

Governing records:

- Accepted Stage-P V3 plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STAGE_P_PREREQUISITES_AMENDMENT_V3.md`
- Accepted Stage-P V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`
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

The rejected FD3D, V2, and all historical artifacts remain immutable evidence.
This plan neither edits nor cleans them.

## 2. Objective and fail-closed state

Produce and independently qualify one self-contained Ubuntu 24.04 amd64 WSL2
provider archive containing four installed-wheel environments:

- `U311`: CPython `3.11.15`, Numba absent, llvmlite absent;
- `U312`: CPython `3.12.13`, Numba absent, llvmlite absent;
- `U313`: CPython `3.13.14`, Numba absent, llvmlite absent;
- `JIT313`: CPython `3.13.14`, exact accepted Numba and llvmlite present.

Current capability is insufficient:

- `C:\WINDOWS\system32\wsl.exe` exists and reports WSL `2.6.1.0`, kernel
  `6.6.87.2-1`;
- distribution enumeration is `access_denied/unproven`;
- Docker was not found in the bounded inventory;
- Windows CPython `3.13.9` is not Linux or Ubuntu-equivalent evidence.

No provider action may begin until Stage C below proves the exact WSL capability.
No ambient distro, package, Python, cache, checkout, or network state is an
accepted input.

## 3. Frozen roots, names, and outputs

Qualification root `Q`:

`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28`

Provider input root `A`:

`Q\provider-inputs`

Provider build root `B`:

`Q\provider-build`

Provider name:

`ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1`

Builder WSL distribution:

`ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`

Builder import directory:

`Q\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1`

Final provider archive:

`Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar`

Final provider capability manifest:

`Q\provider\provider_capability_manifest.json`

Final provider index:

`Q\provider\provider_index.json`

Builder scripts, created only after separate review via `apply_patch`:

- `Q\provider-tools\acquire_provider_inputs.py`
- `Q\provider-tools\validate_provider_inputs.py`
- `Q\provider-tools\build_provider.py`
- `Q\provider-tools\validate_provider.py`

Input/build/output records:

- `Q\provider-manifests\provider_build_input_manifest.json`
- `Q\provider-manifests\provider_command_manifest.json`
- `B\provider_build_intent.json`
- `B\provider_build_transcript.json`
- `B\provider_build_report.json`
- `B\provider_build_failure.json`
- `Q\environment-reports\U311.environment_report.json`
- `Q\environment-reports\U312.environment_report.json`
- `Q\environment-reports\U313.environment_report.json`
- `Q\environment-reports\JIT313.environment_report.json`

All registered partials are same-path plus `.partial`. Every existing ancestor
must be a direct non-reparse directory. Every owned target must be absent at its
creation boundary. No output may be overwritten, reused, or silently repaired.

## 4. Stage C: provider capability proof

Stage C is a separately authorized, read-only capability gate. It creates no
distro and changes no host state. The later exact command packet must contain
short, literal, Defender-safe native calls only, with `login=false`:

1. Hash, size, version, and signature identity for
   `C:\WINDOWS\system32\wsl.exe`.
2. `wsl.exe --version`.
3. `wsl.exe --status`.
4. `wsl.exe --list --verbose`.
5. `wsl.exe --list --quiet`.

The packet must record stdout, stderr, exit code, UTC timing, and process state
for each call. It may require sandbox escalation only to overcome the already
observed access-denied service boundary; escalation cannot change command bytes.

Acceptance requires:

- WSL version `2.6.1.0` and a functioning WSL2 service;
- successful distribution enumeration;
- builder and final provider names absent;
- registered builder/final import directories absent;
- no conflicting process or active ecosystem performance lease;
- exact Windows version/kernel/architecture recorded;
- no host mutation.

Any nonzero exit, access denial, conflicting name/path, version drift, or
unproven state blocks all later stages. No retry is automatic.

## 5. Stage M: immutable metadata and input manifest

Stage M is a separately authorized metadata-only network gate. It must resolve
official, immutable identities before bytes are acquired.

Required source classes:

1. A versioned Canonical Ubuntu 24.04 amd64 WSL-compatible rootfs archive from an
   official Canonical HTTPS origin.
2. Exact `actions/python-versions` Ubuntu 24.04 x64 release artifacts for
   CPython `3.11.15`, `3.12.13`, and `3.13.14` from immutable release-asset
   identities.
3. Signed Ubuntu 24.04 repository `InRelease` metadata and matching `Packages`
   indices sufficient to compute the exact offline `.deb` dependency closure.
4. Exact direct PyPI wheel artifacts for all build, runtime, and test
   dependencies in four complete lane locks.
5. Exact accepted sibling/runtime wheels required by ANYsolver.
6. Exact ANYsolver wheel-build frontend/backend inputs.

Metadata must be obtained from primary upstream APIs/pages only. Every record
freezes project/release, exact URL, effective URL policy, filename, bytes,
SHA-256, architecture/tag, yanked/security state where applicable, source UTC,
and raw metadata response hash. Mutable `latest`/`current` identities are
rejected.

Ubuntu package metadata must be verified against a separately accepted Ubuntu
archive-key file and exact fingerprint. The dependency closure algorithm must:

- parse signed indices without invoking `apt`;
- select exact `amd64` versions from the frozen Ubuntu 24.04 suite/pockets;
- include recursive `Pre-Depends` and `Depends`, choosing alternatives only by a
  frozen deterministic rule;
- include every package owning an ELF interpreter or shared object needed by
  Python, NumPy, SciPy, OpenBLAS/BLAS/LAPACK, Numba, or llvmlite;
- record package, version, architecture, URL, bytes, SHA-256, dependency edge,
  and reason;
- fail on an unresolved dependency, ambiguous alternative, unsigned index,
  version drift, or architecture mismatch.

The result is `provider_build_input_manifest.json`, schema
`anysolver.no_numba_residual.provider_build_input_manifest/1`. It is immutable
provider pre-build authority and is distinct from V3's post-provider
`local_import_input_manifest.json`.

The manifest excludes itself. Its SHA-256 is frozen externally after creation
and passed literally to every acquisition/build command.

## 6. Stage A: ownership-safe acquisition

Stage A requires separate exact commands and network authority. The accepted
plain-Python acquisition tool must use the standard library only and receive the
external manifest SHA-256.

For every artifact, sequentially:

- validate direct/non-reparse root ancestry;
- refuse a pre-existing final or partial;
- open a unique same-directory partial with exclusive creation;
- disable redirects;
- require exact requested and effective HTTPS URL;
- require HTTP 200 and exact Content-Length;
- stream to disk while counting and hashing;
- flush and `fsync` file and parent;
- verify bytes and SHA-256;
- atomically rename only after verification;
- publish an acquisition receipt with UTC, URL, status, bytes, hash, and process
  state.

On failure, preserve the owned partial and an atomic failure receipt. Never
delete a partial, foreign path, successful prior artifact, or empty directory.
No automatic retry, pip cache, install, import, build, or test is allowed.

Stage A finishes only when every artifact in the manifest exists at the exact
path/hash and one aggregate acquisition report links all receipts.

## 7. Input archive validation

Before builder import, `validate_provider_inputs.py` must validate all archives
without extraction into a trusted path.

For tar/zip/wheel/deb members it must reject:

- duplicate normalized member names;
- absolute paths, drive paths, `..` traversal, NULs, or path aliases;
- links escaping the extraction root;
- unexpected devices, FIFOs, sockets, sparse aliases, or hardlink cycles;
- unsupported compression or checksum failure;
- member count/size outside manifest limits;
- unexpected executable/setuid/setgid bits;
- any member not permitted by the accepted artifact-specific inventory.

Python-version archives require an exact accepted member inventory and exact
SHA-256 for their setup/install entry point. The later setup contract is frozen
as:

- toolcache root: `/opt/hostedtoolcache`;
- exact target prefixes:
  `/opt/hostedtoolcache/Python/3.11.15/x64`,
  `/opt/hostedtoolcache/Python/3.12.13/x64`, and
  `/opt/hostedtoolcache/Python/3.13.14/x64`;
- environment: empty except exact `PATH=/usr/bin:/bin`, `HOME=/root`,
  `AGENT_TOOLSDIRECTORY=/opt/hostedtoolcache`,
  `RUNNER_TOOL_CACHE=/opt/hostedtoolcache`, locale, and offline cache paths;
- entry-point hash and exact no-shell argv must be frozen from the acquired
  artifact before execution;
- setup may write only beneath the exact toolcache prefix and registered
  transcript paths;
- any network attempt, undeclared child, write outside allowed roots, unresolved
  library, or unexpected output is terminal.

Concrete setup argv cannot be rendered until the accepted archive's entry-point
contract is read and content-addressed. It must be added to
`provider_command_manifest.json` before Stage B; no placeholder is executable.

Wheel validation requires filename/tag/version identity, no duplicate members,
safe unique zero-length directory members handled separately, RECORD self-row
with blank hash/size, hash/size validation for every other non-directory member,
and rejection of unexpected signatures.

## 8. Stage B: isolated offline provider build

Stage B requires a fresh exclusive PERF lease. It uses the newly imported
builder distro only; network is disabled and verified before the first build
action.

Import shape, rendered literally after all hashes are accepted:

```text
& 'C:\WINDOWS\system32\wsl.exe' --import ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1 C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1 <ACCEPTED_ROOTFS_PATH> --version 2
```

The exact rootfs path replaces the placeholder before execution. Builder actions
are direct `wsl.exe --distribution ... --exec <absolute executable> <literal
args>` calls. No PowerShell script, inline task-authored PowerShell program,
shell command string, encoded payload, hidden launcher, or Defender exception is
allowed.

`build_provider.py` is plain Python, content-addressed, and may invoke only an
exact argv allowlist from `provider_command_manifest.json` with `shell=False`:

- `/usr/bin/dpkg-deb` for package inspection/extraction;
- `/usr/bin/dpkg` for exact offline package configuration if required by the
  accepted closure;
- accepted Python-version setup entry points with exact hashes/argv;
- lane Python `-B -I -m pip` using only accepted local wheelhouses,
  `--no-index`, `--require-hashes`, and `--only-binary=:all:`;
- lane Python environment probes and `pip check` equivalent;
- `/usr/bin/readelf`, `/usr/bin/ldd` only with `LD_TRACE_LOADED_OBJECTS` safety
  constraints, or an accepted pure-parser equivalent for ELF closure;
- `/usr/bin/sync` only at registered durable checkpoints.

No compiler, linker, source build, apt network action, editable install, user
site, system-site leakage, or ambient package resolution is permitted.

The builder must:

1. Validate provider-build manifest external hash and all input hashes.
2. Durably publish build intent before mutation.
3. Establish exact offline environment and DNS/network denial proof.
4. Install/extract the frozen `.deb` closure and record every filesystem member.
5. Install exact Python toolcache artifacts into their prefixes.
6. Build the ANYsolver wheel only if a separately accepted wheel-build command
   and complete offline build stack are in the manifest; otherwise consume an
   independently accepted wheel.
7. Install four lane locks and accepted ANYsolver wheel offline.
8. Prove Numba and llvmlite absent in U lanes and present/functional in JIT313.
9. Validate all installed distribution RECORD files and origins.
10. Compute full ELF/shared-library closure and zero unresolved dependencies.
11. Record NumPy/SciPy configuration and BLAS/LAPACK/thread identities.
12. Remove no evidence. Build-only transient files remain inventoried inside the
    provider or registered build root until closeout.
13. Atomically publish each lane environment report and aggregate build report.

A first failure preserves the builder distro, build intent, transcripts,
partials, process-tree evidence, and failure report. No retry or cleanup is
automatic.

## 9. Provider export and capability validation

Only a green, independently reviewed Stage-B build may proceed to export under a
fresh exact authority.

Before export:

- no build/test process remains;
- all filesystems are durably synced;
- provider input/build reports and four environment reports are final;
- the builder contains no credentials, network cache, editable checkout, user
  profile mutation, or unregistered path;
- every lane origin and ELF closure is green.

Export is one exact non-overwriting native command to a fresh partial archive.
The final archive is published only after command success, bytes/hash validation,
archive safety scan, and atomic same-volume rename. One build establishes
identity only, not byte reproducibility.

`validate_provider.py` then validates the archive offline and produces:

- `provider_capability_manifest.json`, schema
  `anysolver.no_numba_residual.provider_capability_manifest/1`;
- `provider_index.json`, schema
  `anysolver.no_numba_residual.provider_index/1`.

The capability manifest records provider/archive identity, Ubuntu release and
architecture, complete dpkg inventory, Python/lane identities, package and
RECORD inventories, shared-library closure, BLAS/LAPACK/threading, Numba/
llvmlite proofs, source/wheel identities, no-network/no-shadowing proof, build
report hashes, tool/script/command hashes, and all process/resource evidence.

The index is acyclic: it hashes the provider archive, capability manifest,
build report, four environment reports, transcripts, and input manifest. Those
members do not hash the index. The archive and all matching evidence form one
atomic accepted bundle; an archive without matching evidence is invalid.

## 10. Process, timeout, and resource truth

Every acquisition/build/validation tool must use durable prelaunch intent,
exclusive stdout/stderr, process start/final records, process-group/session
ownership, Linux PDEATHSIG where applicable, and complete normal/error/timeout
accounting. Timeout termination is limited to the positively owned process group,
followed by wait/reap and `/proc` residual proof. No general cleanup occurs.

Proposed later lease envelopes:

- Stage C: read-only, under 5 minutes, one native process, under 500 MB.
- Stage M: metadata-only network, under 10 minutes, one process, under 500 MB.
- Stage A: sequential acquisition, one process, no install/build, under 2 GiB,
  duration/bytes frozen after metadata acceptance.
- Stage B: one WSL builder and one child at a time, no network/GPU, up to 4 CPU,
  6 GiB RAM, 20 GiB fresh disk, expected 30-60 minutes, hard 90 minutes with 10
  minutes reserved for failure/final accounting.
- Export/validation: one WSL/native process, up to 2 CPU, 4 GiB RAM, expected
  10-20 minutes, hard 30 minutes.

Every stage requires its own exact command packet and explicit grant. Failure is
preserved; no command is retried or tuned under the same authority.

## 11. Defender-safe transport

All Windows top-level execution is one short literal native command per tool call
with `login=false`. No task-authored inline PowerShell program, PowerShell file,
here-string, `-EncodedCommand`, `ExecutionPolicy Bypass`, `Start-Process`, hidden
window, nested shell, generated launcher, cmd/batch indirection, or Defender
exception is permitted.

Plain Python tools are created only via `apply_patch`, independently hashed and
AST/compile-only reviewed, and invoked by absolute accepted Python path with
`-B -I`. Linux builder tools run through direct `wsl.exe --exec` argv. No shell
parses command text.

## 12. Required acceptance order

1. Accept this plan hash.
2. Create and accept exact plain-Python tools and JSON schemas without execution.
3. Obtain Stage-C authority and prove provider capability.
4. Obtain Stage-M authority and freeze the immutable provider-build input
   manifest and exact command manifest.
5. Obtain Stage-A authority and acquire all inputs once.
6. Independently accept all input hashes and archive validation.
7. Obtain Stage-B PERF lease and build once offline.
8. Independently accept build report and four lane reports.
9. Obtain export/validation authority and produce the atomic provider bundle.
10. Independently accept provider archive/capability/index hashes.
11. Only then freeze V3's `local_import_input_manifest.json` before final provider
    import and Stage-P prerequisites.

## 13. Prohibitions and current blockers

- No action is authorized by this plan creation.
- No further capability retry or GitHub query in this turn.
- No ambient provider, distro, Python, dependency, cache, source import, or
  editable path.
- No source/test/workflow edit, broad test, Stage P, publication, push, tag, or
  release.
- No cleanup, unregister, delete, overwrite, rollback, retry, or Defender bypass.

Current blockers: WSL distro capability is unproven; artifact metadata and bytes
are not frozen; tools/manifests do not exist; no builder/provider distro exists;
no environment report or provider bundle exists; and no stage lease is active.
