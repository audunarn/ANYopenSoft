# ANYsolver No-Numba Residual Provider Capability, Acquisition, and Build Plan V2

## 1. Mechanical supersession

This V2 incorporates the accepted provider architecture by exact identity and
changes only the execution-contract details directed by review.

- Preserved V1 path:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_CAPABILITY_ACQUISITION_BUILD_PLAN.md`
- Preserved V1 SHA-256:
  `6C5DDC1643A055CFE39675E8B0532039B91015928A7226422143C809B0222B52`
- Governing Stage-P V3 SHA-256:
  `6F186733DD4CB1E56BE307CE9772165C68710A4FFB795D62CE24417A9A87C649`
- Source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- Source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`

V1 remains immutable evidence. Every V1 provision not explicitly superseded
below remains binding. The obsolete terminal-row recovery plan is untouched and
non-authoritative; the independently recovered terminal ledger is authoritative.

This is plan-only. It authorizes no capability query, metadata request,
acquisition, archive assembly, provider import/build/export, environment action,
process launch, source/test/workflow edit, cleanup, PERF request, or Stage P.

## 2. Signed Canonical provenance chain

### 2.1 Frozen verifier and trust root

Canonical metadata is accepted only through this trust chain:

- verifier executable: a hermetic Linux-amd64 `gpgv` bundle recorded in
  `provider_build_input_manifest.json` by exact upstream source, filename,
  version, bytes, SHA-256, ELF closure, and executable SHA-256;
- key package: official `ubuntu-keyring` `.deb`, frozen by exact versioned
  Ubuntu archive URL, bytes, SHA-256, and signed Packages-index chain;
- extracted keyring path:
  `/opt/provider-verifier/ubuntu-archive-keyring.gpg`;
- required Ubuntu archive signing fingerprint:
  `F6ECB3762474EDA9D21B7022871920D1991BC93C`;
- required Canonical image-signing fingerprint for signed image checksum
  metadata:
  `843938DF228D22F7B3742BC0D94AA3F0EFE21092`;
- signature time, key validity, issuer fingerprint, primary fingerprint, and
  exact signed-payload SHA-256 must be recorded.

The metadata stage must independently validate these fingerprint constants
against Canonical's official key publication before freezing executable inputs.
A missing, revoked, expired-at-signature-time, unexpected, or ambiguous signer
is terminal. No ambient Windows/Linux GPG keyring or verifier is trusted.

### 2.2 Rootfs chain

The Canonical rootfs must come from one immutable, versioned Ubuntu 24.04 amd64
release directory. Mutable `current`, `latest`, redirect-selected, or Store
identities are forbidden.

The accepted chain is:

1. Exact versioned release directory and rootfs filename.
2. Exact `SHA256SUMS` and detached `SHA256SUMS.gpg` bytes/hashes.
3. Hermetic `gpgv` verification of `SHA256SUMS.gpg` over `SHA256SUMS` with the
   required Canonical image signer.
4. One exact rootfs row in the signed checksums, with no duplicate filename.
5. Acquired rootfs bytes/hash exactly matching that signed row.
6. Safe archive member validation and exact Ubuntu release/amd64 identity after
   extraction.

The input manifest records every URL, effective-URL rule, response hash, byte
count, signature result, signer, checksum row, and acquisition receipt.

### 2.3 InRelease to Packages to `.deb` chain

Every rootfs overlay library is accepted only through:

1. Exact suite/pocket/component/architecture URL.
2. Exact signed `InRelease` bytes/hash.
3. Hermetic `gpgv` verification with the required Ubuntu archive signer.
4. Exact `Packages`/`Packages.xz` path, bytes, and SHA-256 selected from the
   verified InRelease checksum section.
5. Exact package stanza with package name, version, architecture, filename,
   bytes, SHA-256, `Pre-Depends`, `Depends`, and multiarch fields.
6. Exact `.deb` URL under the frozen archive origin.
7. Acquired `.deb` bytes/hash matching the signed Packages stanza.
8. Safe ar/control/data member validation and package metadata agreement.

The closure includes recursive runtime dependencies and every package owning an
ELF interpreter/shared object used by Python, NumPy, SciPy, OpenBLAS/BLAS/LAPACK,
Numba, or llvmlite. No unsigned PPA, snapshot substitute, ambient apt state, or
dependency guessed outside the signed graph is allowed.

## 3. Authoritative `actions/python-versions` chain

For CPython `3.11.15`, `3.12.13`, and `3.13.14`, the metadata stage freezes:

- repository exactly `actions/python-versions`;
- immutable release/tag and release object ID;
- exact Ubuntu 24.04 x64 asset ID, filename, size, API URL, and browser URL;
- authoritative GitHub release-asset `digest` equal to
  `sha256:<64-lowercase-hex>`;
- acquired bytes matching the API digest;
- immutable release metadata response bytes/hash and UTC;
- GitHub Artifact Attestation bundle/identity when published, verified against
  repository `actions/python-versions`, the exact source workflow/ref/commit,
  artifact digest, and GitHub's trusted root;
- explicit `attestation_status` of `verified` or `not_published`.

`not_published` is acceptable only when the authoritative release API digest is
present and independently matched; a missing API digest is terminal. An invalid
or mismatched published attestation is terminal and cannot fall back to digest
only.

The exact `gh`/attestation verifier executable, version, bytes, SHA-256, trusted
root identity, literal argv, stdout/stderr, and exit status must be frozen before
metadata acceptance. No moving release tag, HTML-only checksum, user-supplied
digest, or ambient cache is authoritative.

## 4. Builder seed and total isolation

The builder never receives provider inputs through a host mount. Before import,
a Windows plain-Python seed assembler creates a fresh builder-seed archive from:

- the signed/validated Canonical rootfs;
- all accepted artifacts copied beneath `/opt/provider-inputs`;
- accepted plain-Python provider tools beneath `/opt/provider-tools`;
- `/etc/wsl.conf` with automount disabled, interop disabled,
  `appendWindowsPath=false`, and resolver generation disabled;
- an empty regular `/etc/resolv.conf` with a frozen hash;
- no Windows credential, user profile, checkout, drive mapping, or network
  configuration.

Seed assembly is archive transformation only; it executes no archive member.
It records source-member to output-member hashes and rejects duplicate names,
traversal, link escape, devices, undeclared files, or rootfs mutation outside the
exact allowlist.

Every builder execution uses a new Linux network and mount namespace through
exact hash-allowlisted `/usr/bin/unshare`, with no shell parsing. Before any
mutation, the build tool must prove:

- only loopback interfaces exist;
- `/proc/net/route` and `/proc/net/ipv6_route` contain no non-loopback route;
- no DNS nameserver is configured;
- no `drvfs`, `9p`, `/mnt/c`, `/mnt/*`, Windows path, Plan9 share, or host bind
  mount exists anywhere in the builder mount tree;
- WSL interop is disabled and no Windows executable can launch;
- the exact input tree is distro-local and read-only;
- output/write roots are exact distro-local paths.

These checks run before and after every builder command and appear in every
command receipt. Any route, host mount, interop path, DNS resolver, or identity
drift is infrastructure failure. Network and ambient-host denial applies for the
entire imported builder lifetime, including validation and export preparation.

## 5. Exact ANYsolver wheel route

V2 chooses one route only: build one pure-Python ANYsolver wheel inside the
isolated offline provider builder from an exact source archive.

Source archive contract:

- produced separately from Git object
  `82a9db28d67507c82ef15c631f582a0c3bf6740e` only after proving tree
  `00b2b20691e73a05589b797b32352f1c760a2451`;
- deterministic `git archive` path inventory, no `.git`, submodule, untracked,
  ignored, dirty, generated, credential, or external file;
- archive filename, bytes, SHA-256, member names/modes/hashes, producing Git
  executable identity, literal argv, cwd, UTC, commit/tree, and clean-state
  receipt frozen in the input manifest;
- safely extracted to `/opt/provider-build/source/ANYsolver-82a9db28`.

Build environment:

- dedicated `/opt/provider-build/envs/wheel-build-313` using CPython `3.13.14`;
- exact offline build frontend/backend and transitive wheels from a fully hashed
  build lock;
- no system site, user site, editable install, VCS access, cache, compiler,
  network, or undeclared package;
- `SOURCE_DATE_EPOCH` equal to the accepted source commit timestamp and all
  other build environment values frozen.

Exact build route:

```text
/opt/provider-build/envs/wheel-build-313/bin/python -B -I -m build --wheel --no-isolation --outdir /opt/provider-output/wheels /opt/provider-build/source/ANYsolver-82a9db28
```

The rendered argv is executed directly with `shell=False`. Exactly one wheel
must result, with normalized project/version equal to the source metadata and
tag exactly `py3-none-any`. Native binaries or platform-specific members are
rejected.

The wheel is validated for safe members and exact RECORD semantics, then hashed
and installed unchanged into U311/U312/U313/JIT313 from the accepted offline
lane locks. Build report schema
`anysolver.no_numba_residual.anysolver_wheel_build_report/1` records source,
build-input, frontend/backend, Python, environment, argv, process, transcript,
wheel member/RECORD, output hash, and no-network proof. No prebuilt or alternate
wheel route is eligible.

## 6. Script, descendant, and write-root policy

### 6.1 `.deb` handling

No `dpkg`, `apt`, package maintainer script, trigger, preinst, postinst, prerm, or
postrm executes. The content-addressed Python builder parses ar/control/data
archives and overlays only declared data members into exact allowlisted roots.
Control scripts are hashed/inventoried as inert bytes and never executed.

Package ownership is recorded in a provider package ledger; V2 does not falsely
claim direct payload extraction as configured host dpkg state. The untouched
rootfs `/var/lib/dpkg/status` is separately recorded, and overlay packages are
identified only by the provider ledger.

### 6.2 Python artifact setup

Each `actions/python-versions` setup/install entry point is extracted as inert
data, hashed, statically reviewed, and assigned one exact descendant-exec and
write-root allowlist before execution. The command manifest freezes:

- setup entry-point path/hash and exact argv;
- interpreter path/hash;
- every permitted descendant executable path/hash and argv shape;
- maximum descendant depth/count;
- permitted read roots;
- permitted write roots limited to the exact toolcache prefix and command
  evidence paths;
- prohibited network, mount, device, credential, profile, `/etc`, `/usr`, `/var`,
  and other-lane writes;
- pre/post filesystem manifests proving no out-of-root mutation.

If the setup script's static behavior cannot be represented by a complete exact
allowlist, that artifact is ineligible and the plan must be superseded; no broad
shell or descendant wildcard is allowed.

All other provider tools are plain Python and may launch only exact manifest
argv with `shell=False`. Every descendant path/hash, argv, cwd, environment,
read/write root, timeout, and process-tree identity is enforced and recorded.

## 7. Unique receipts and schemas

### 7.1 Acquisition

For artifact ID `X`:

- partial artifact: `A\artifacts\X\payload.partial`;
- final artifact: `A\artifacts\X\payload`;
- intent partial/final: `A\receipts\X\intent.json.partial` and `intent.json`;
- transcript stdout/stderr/index under `A\receipts\X\transcript`;
- process start/termination/final under `A\receipts\X\process`;
- failure partial/final: `A\receipts\X\failure.json.partial` and
  `failure.json`;
- success partial/final: `A\receipts\X\success.json.partial` and
  `success.json`.

Schemas:

- `anysolver.no_numba_residual.provider_acquisition_intent/1`;
- `anysolver.no_numba_residual.provider_acquisition_failure/1`;
- `anysolver.no_numba_residual.provider_acquisition_success/1`;
- `anysolver.no_numba_residual.process_audit/1`;
- `anysolver.no_numba_residual.transcript_index/1`.

Producer: accepted `acquire_provider_inputs.py` only.

### 7.2 Builder commands

For command ID `X`:

- `B\commands\X\intent.json.partial|json`;
- `B\commands\X\transcript\stdout.bin`;
- `B\commands\X\transcript\stderr.bin`;
- `B\commands\X\transcript\index.json.partial|json`;
- `B\commands\X\process\start.json.partial|json`;
- `B\commands\X\process\termination.json.partial|json`;
- `B\commands\X\process\final.json.partial|json`;
- `B\commands\X\filesystem_before.json.partial|json`;
- `B\commands\X\filesystem_after.json.partial|json`;
- `B\commands\X\network_mount_audit.json.partial|json`;
- `B\commands\X\result.json.partial|json`.

Schemas:

- `anysolver.no_numba_residual.provider_command_intent/1`;
- `anysolver.no_numba_residual.provider_command_result/1`;
- process/transcript schemas from 7.1;
- `anysolver.no_numba_residual.filesystem_manifest/1`;
- `anysolver.no_numba_residual.network_mount_audit/1`.

Producer: accepted `build_provider.py` for in-distro commands and accepted
Windows coordinator tool for import/export commands. Producer identity and
external command-manifest hash are mandatory in every record.

### 7.3 All-outcome finalization

After normal success, expected diagnostic nonzero, policy mismatch, launch error,
signal, timeout, parser/payload failure, or exceptional exit, the producer must
durably publish available intent, transcript, process, filesystem, network/mount,
and result/failure truth. Linux outcomes require complete `/proc` PID/PPID/PGID/
session/descendant/residual audit. Timeout signals only the positively owned
process group, waits/reaps, and proves residual state. Any unproven residual is
infrastructure failure.

Files and parent directories are flushed/fsynced before atomic rename. Failure
partials and all prior evidence are preserved. There is no general cleanup or
automatic retry.

## 8. Exact provider-build command order and timeouts

The command manifest contains this ordinal set:

1. `PB01-VALIDATE-INPUTS`, timeout 300 seconds.
2. `PB02-ASSEMBLE-SEED`, timeout 600 seconds.
3. `PB03-IMPORT-BUILDER`, timeout 300 seconds.
4. `PB04-VERIFY-ISOLATION`, timeout 120 seconds.
5. `PB05-OVERLAY-DEB-CLOSURE`, timeout 600 seconds.
6. `PB06-SETUP-PY311`, timeout 300 seconds.
7. `PB07-SETUP-PY312`, timeout 300 seconds.
8. `PB08-SETUP-PY313`, timeout 300 seconds.
9. `PB09-CREATE-BUILD-ENV`, timeout 300 seconds.
10. `PB10-BUILD-ANYSOLVER-WHEEL`, timeout 600 seconds.
11. `PB11-VALIDATE-ANYSOLVER-WHEEL`, timeout 180 seconds.
12. `PB12-INSTALL-U311`, timeout 600 seconds.
13. `PB13-INSTALL-U312`, timeout 600 seconds.
14. `PB14-INSTALL-U313`, timeout 600 seconds.
15. `PB15-INSTALL-JIT313`, timeout 600 seconds.
16. `PB16-VALIDATE-U311`, timeout 300 seconds.
17. `PB17-VALIDATE-U312`, timeout 300 seconds.
18. `PB18-VALIDATE-U313`, timeout 300 seconds.
19. `PB19-VALIDATE-JIT313`, timeout 300 seconds.
20. `PB20-ELF-CLOSURE`, timeout 600 seconds.
21. `PB21-FINAL-FILESYSTEM-AUDIT`, timeout 300 seconds.
22. `PB22-SYNC-AND-STOP-BUILDER`, timeout 180 seconds.
23. `PB23-EXPORT-PARTIAL`, timeout 900 seconds.
24. `PB24-VALIDATE-EXPORT`, timeout 900 seconds.
25. `PB25-PUBLISH-PROVIDER-BUNDLE`, timeout 180 seconds.

Each command binds the immediately preceding accepted result hash. No ordinal is
skipped, replayed, reordered, or retried.

## 9. Absolute deadline and resource reserve

The Stage-B initializer durably freezes UTC and monotonic start plus one absolute
deadline exactly 90 minutes later. Before each command:

`remaining_seconds >= child_timeout_seconds + 600`

The final 600 seconds are reserved for transcript/process/failure accounting and
cannot be consumed by a child launch. If insufficient time remains, no child is
started; deadline exhaustion is durably recorded and terminal.

All child timeouts are the exact values in Section 8. A timeout uses bounded
owned-process-group termination and full residual proof. Wall/monotonic
contradiction or clock regression is infrastructure failure.

Resource envelope remains V1's accepted architecture: one WSL builder and one
child at a time, no network/GPU, up to 4 logical CPU, 6 GiB combined RAM, and 20
GiB fresh disk. The 90-minute absolute deadline includes import, build, export,
validation, and final accounting.

## 10. Result claim boundary

All successful provider and later Stage-P outputs must be labeled:

`Ubuntu 24.04 amd64 WSL2 reproduction`

They are not labeled GitHub-hosted-runner CI reproduction or CI equivalence.

`CI-equivalent` may be used only if a separate accepted manifest proves exact
historical identity for all materially relevant inputs:

- hosted runner image name, immutable image release/version/digest and provision
  manifest;
- kernel, glibc, CPU architecture/features, locale, filesystem, environment,
  thread settings, and resource class;
- exact setup-python action commit;
- exact `actions/python-versions` asset IDs/digests/attestations;
- exact Python, pip, wheel, NumPy, SciPy, BLAS/LAPACK, pytest, Numba/llvmlite,
  ANYsolver, and sibling artifact hashes;
- exact workflow argv/order/cwd/environment and source tree;
- no unproven runner service or ambient package difference.

Absent that full identity, similarity is reported dimension by dimension and the
claim remains Ubuntu reproduction only.

## 11. Unchanged boundaries

V1's source/science scope, four lane definitions, signed/offline intent,
self-contained provider architecture, archive/member/RECORD validation,
environment reports, provider capability/index hash DAG, Defender-safe direct
transport, acceptance order, no-publication boundary, and preservation rules are
unchanged.

No action or lease is authorized now. Current blockers remain capability proof,
accepted metadata/digests/attestations, acquired inputs, content-addressed tools
and manifests, builder/provider artifacts, environment reports, and explicit
stage grants.
