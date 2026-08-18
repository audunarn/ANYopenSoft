# Native-Hybrid Combined Release Qualification Plan

Date: 2026-08-13 (Europe/Oslo)

Status: BLOCKED. This qualification skeleton authorizes no build, broad suite,
package publication, tag, or GitHub release. It cannot become executable until
the source-owner prerequisites below are accepted, committed, merged, pushed,
and rebound into a superseding content hash.

## Authority and objective

Governing program:
`C:\Github\ANYopenSoft\governance\plans\ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`,
SHA-256
`4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.

The objective is one dependency-complete, content-addressed qualification of
the accepted native-hybrid ecosystem. It must build exact wheels from frozen
sources, resolve them with exact hashes in clean environments, prove installed
origins and public behavior, and separate local Windows evidence from CI-only
platform evidence. It must not convert an unrun workflow or an editable-source
import into a release claim.

## Source prerequisite blockade

The currently recorded default tips are assessment anchors only and must never
enter Stage A. These owner defects must close first:

- ANYmesh must require ANYgeometry (including the planar equivalent) at
  `>=0.2.1,<0.3`, pin accepted geometry in release workflows, and commit the
  disabled-native absence/fail-hard evidence cell.
- ANYfem must require ANYgeometry and ANYmesher at `>=0.2.1,<0.3`, ANYfileio at
  `>=0.2,<0.3`, and replace every owned obsolete ANYio path with canonical
  ANYfileIO while preserving its four dirty UI/test paths outside release input.
- ANYsolver must require ANYfileio at `>=0.1,<0.3` only after accepted focused
  legacy/current source proof and committed workflow/metadata gates.
- ANYfileIO must close its post-`5513881827cdee9fd337497a2730a5912d8ea751`
  CI and base-isolation correction, then provide one final accepted default tip.
- ANYgeometry must provide the final accepted default tip containing its
  committed workflow correction; `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`
  remains a pre-closeout anchor and may not enter Stage A.

After all owner closeouts, this plan must be superseded with a new content hash
that rebinds every accepted repository tip, tree, distribution version, source
manifest, wheel filename, and wheel hash, including the post-551388 ANYfileIO
tip and final ANYgeometry workflow tip. No current tip or pre-closeout wheel is
grandfathered into Stage A.

## Pre-closeout source anchors (not Stage-A inputs)

| Distribution | Repository | Required default tip | Current version |
|---|---|---|---|
| ANYgeometry | `C:\Github\ANYgeometry` | `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa` | `0.2.1` |
| ANYmesher | `C:\Github\ANYmesh` | `c95328b604bfa4607ba82bbde76ceb8491134b1a` | `0.2.1` |
| ANYfem | `C:\Github\ANYfem` | `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2` | `0.1.0` |
| ANYsolver | `C:\Github\ANYsolver` | `12c565899e320b2142d8b23e31f5eb19702b2486` | `0.2.0` |
| ANYfileio | `C:\Github\ANYfileIO` | `5513881827cdee9fd337497a2730a5912d8ea751` | `0.2.0` |
| ANYmaterial | `C:\Github\ANYmaterial` | `4626887667f4c251479d26f321b9e73b046a2783` | `0.1.0` |

After owner closeout, every source archive is produced with `git archive` from
the superseding plan's named commit, not
from a working tree. Each archive receives a sorted path/size/SHA-256 manifest.
The plan fails if local `main`, fetched `origin/main`, and the named commit do
not agree. Untracked ANYgeometry artifacts and the four ANYfem UI/test paths are
excluded.

## Pinned ANYfileIO object contract

The ambient ANYfileIO checkout is a legacy repository-rename branch and is not
an input. Every ANYfileIO metadata, source, test, and changelog read must use Git
object `5513881827cdee9fd337497a2730a5912d8ea751` through `git show`, `git ls-tree`,
or `git archive`. No qualification command may read those files from the
checked-out worktree.

At the pinned object, ANYfileio is version 0.2.0. Its base requirement is
exactly `numpy>=1.26`. Its `semantics` extra is exactly
`ANYmesher>=0.2,<0.3` plus `ANYmaterial>=0.1,<0.2`. The legacy branch's
`ANYmesher<0.2` metadata is preserved but excluded from every source, artifact,
resolver, and claim graph.

## Existing immutable inputs

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `anygeometry-0.2.1-py3-none-any.whl` | 274758 | `99D3035806E109341E92475B555D21CA89EBB12E6D9410C13132920122CA5E95` |
| `numpy-2.4.3-cp313-cp313-win_amd64.whl` | 12312824 | `0A60E17A14D640F49146CB38E3F105F571318DB7826D9B6FEF7E4DCE758FAECD` |
| `build-1.5.0-py3-none-any.whl` | 26018 | `13F3EECB844759AB66EFEC90CA17639BBF14DC06CB2FDF37A9010322D9C50A6F` |
| `setuptools-83.0.0-py3-none-any.whl` | 1008090 | `29B23C360F22F414DC7336BB39178CC7BCBF6021ED2733CDE173F09DBA19ABB3` |
| `wheel-0.47.0-py3-none-any.whl` | 32218 | `212281CAB4DFF978F6CEDD499CD893E1F620791CA6FF7107CF270781E587ECED` |
| `packaging-25.0-py3-none-any.whl` | 66469 | `29572EF2B1F17581046B3A2227D5C611FB25EC70CA1BA8554B24B0E69331A484` |
| `pyproject_hooks-1.2.0-py3-none-any.whl` | 10216 | `9E5C6BFA8DCC30091C74B0CF803C81FDD29D94F01992A7707BC97BABB1141913` |
| `colorama-0.4.6-py2.py3-none-any.whl` | 25335 | `4F1D9991F5ACC0CA119F9D443620B77F9D6B33703E51011C16BAF57AFB285FC6` |

The existing ANYgeometry wheel is a comparator, not automatic proof for this
combined run. Stage A builds from the frozen source tip and records whether its
installed payload is equivalent. One build makes no byte-reproducibility claim.
Every listed wheel must be rebound or replaced by exact post-closeout source and
artifact identities in the superseding plan before Stage A.

Before Stage B, a separately reviewed acquisition manifest must freeze exact
filenames, versions, URLs, bytes, and SHA-256 values for every remaining
Windows CPython 3.13 runtime wheel: SciPy, threadpoolctl, Shapely, h5py,
platformdirs, and all transitive binary/runtime dependencies. Acquisition uses
official artifact URLs, no redirects, create-new partials, and hash-before-
rename. No floating index access is permitted during qualification.

## Toolchain identity

Stage A reuses the accepted Attempt-4 Windows toolchain anchors:

| Tool | SHA-256 |
|---|---|
| Windows PowerShell 5.1 | `7600FFE12DA441FE89D035B13801E8E91D064BC544A27B19A5CF49F6AB8B18F5` |
| Git | `7B7971DD13F0C3A284E538601F2F9770B3A87DFACCB5FB52D68141C67ED22364` |
| CPython 3.13.9 executable | `08A64DC73AC3E3776B49F0097C6306BDB9C8F7990A037065213324D328467BF5` |
| CPython DLL | `C9F98606D0D06F4E8AE75AE385021E58B57C90D4FD325C0313C8C42ABE1EBF63` |
| MSVC `cl.exe` | `FD30D75E6AA319673CF3A4F56AEB3A1D6106AFF87360B78966A7C5783567B78A` |
| MSVC `link.exe` | `69EE768E3BA674087B8644E1D46B81379BEF1580470461E61535A1075D1A0957` |

Paths, versions, Windows SDK identity, environment, and pre/post process trees
must also match the accepted Attempt-4 ledger. A mismatch emits failure evidence
and no accepted wheelhouse.

## Stage 0: light preflight and release-readiness gate

Stage 0 is read-only and does not consume the performance lease.

- Fetch every origin and verify the frozen default tips and clean source-object
  identities. Working-tree dirt is allowed only when excluded from `git archive`.
- Query authoritative primary-index JSON without redirects for every intended
  distribution/version. Record status, normalized project/version, response
  bytes/hash, timestamp, and source URL. Under this no-publication plan, an
  existing version or index collision is evidence only; it is not an automatic
  patch bump or blocker. Any version decision requires separate owner and
  publication authority.
- Parse all `pyproject.toml` requirements with `packaging.Requirement`; reject
  duplicate names, markers, URLs, extras outside the selected cell, or an
  unapproved range.
- Require release-readiness wording. ANYmesh, ANYsolver, ANYfileIO, and
  ANYmaterial currently have `Unreleased` sections; ANYfem has no changelog.
  Owners must add truthful release sections or a release-readiness document
  after the index decision. No document may say a wheel or platform is already
  qualified before this plan passes.
- Freeze the plan, acquisition manifest, probe programs, coordinator scripts,
  source manifests, and commands by bytes and SHA-256 before a lease request.

## Stage A: source-isolated combined wheelhouse

Build order is ANYmaterial, ANYgeometry, ANYmesher, pinned ANYfileIO 0.2.0,
ANYsolver, then ANYfem. Each build uses a fresh source archive and fresh offline
build venv. `PIP_NO_INDEX=1`, `PYTHONNOUSERSITE=1`,
`PYTHONDONTWRITEBYTECODE=1`, cleared `PYTHONPATH`/`PYTHONHOME`/`VIRTUAL_ENV`, and
`ANYMESHER_REQUIRE_NATIVE=1` are mandatory for the compiled ANYmesher wheel.

Expected current-version wheel shapes, subject to the Stage-0 version gate, are:

- `anymaterial-0.1.0-py3-none-any.whl`
- `anygeometry-0.2.1-py3-none-any.whl`
- `anymesher-0.2.1-cp313-cp313-win_amd64.whl`
- `anyfileio-0.2.0-py3-none-any.whl`
- `anysolver-0.2.0-py3-none-any.whl`
- `anyfem-0.1.0-py3-none-any.whl`

If Stage 0 requires a patch bump, its exact accepted filename replaces the
corresponding line in the input manifest; the command does not infer it.

For every wheel, validate ZIP member uniqueness/path safety, normalized
METADATA identity and requirements, WHEEL tags, complete RECORD hashes/sizes,
and import-package payload. Safe unique directory members are validated
separately and must have zero length. RECORD must name exactly every
non-directory wheel member and no directory member. The RECORD self-row must
have blank hash and size; every other non-directory row must have a valid hash
and exact size. Unexpected `RECORD.jws`, `RECORD.p7s`, or other signature files
are rejected rather than silently omitted; if a later signed-wheel cell is
approved, its RECORD semantics require a separately registered rule. The
ANYmesher wheel must contain exactly one loadable
CPython 3.13 Windows AMD64 native extension and no source-tree import path.

Stage A publishes atomically only after source, artifact, process, memory,
environment, cleanup, and worktree-state gates pass. Its bundle contains all six
wheels, complete raw logs, source manifests, toolchain manifest, wheel/RECORD
validation, resource samples, success report, and `index.json`. `index.json`
hashes every other member; the final directory is named by SHA-256 of index
bytes. Failure reports use a separate fresh path and publish no wheelhouse.

Exact future lease command:

```powershell
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File C:\Github\ANYopenSoft\governance\qualification\native_hybrid\stage_a_build_combined_wheelhouse.ps1
```

Lease envelope: one coordinator and one sequential build child at a time;
Windows CPython 3.13/MSVC; at most 4 logical CPUs, 4 GiB combined RAM, 10 GiB
fresh external disk, no GPU/network; worker timeout 900 seconds, cleanup margin
120 seconds, outer timeout 1080 seconds; ETA 10-15 minutes. No retry or tuning.

## Stage B: resolver and installed-runtime qualification

Stage B starts only after independent acceptance of a Stage-A index SHA and the
complete runtime acquisition manifest. It uses a fresh external root and no
system-site packages, editable installs, VCS URLs, checkout CWD, pip cache, or
network. The sole offline candidate set is the six wheels in the accepted
Stage-A `wheels` directory plus exact hashed runtime wheels for NumPy, SciPy,
threadpoolctl, Shapely, h5py, and platformdirs in one accepted runtime-artifact
directory. The lock may select no other project or file. Every resolver/install
command uses exactly two links, `--find-links <accepted-stage-a>/wheels` and
`--find-links <accepted-runtime-artifacts>`, together with `--no-index` and
`--require-hashes`; ambient caches and additional links are forbidden.

The canonical `runtime-win-cp313.lock` contains exact normalized package names,
versions, filenames, and `--hash=sha256:` entries for all direct and transitive
requirements. Resolver proof uses:

```powershell
python -m pip install --dry-run --ignore-installed --no-index --find-links <accepted-stage-a>/wheels --find-links <accepted-runtime-artifacts> --require-hashes --report resolver-report.json -r runtime-win-cp313.lock
```

The report must select ANYgeometry 0.2.1, ANYmesher 0.2.1, ANYfileio 0.2.0, and
the exact accepted ANYmaterial/ANYsolver/ANYfem versions with no editable, URL,
source, or ambient candidate. A second clean venv installs the same lock and records
`pip inspect`, `pip check`, `importlib.metadata`, RECORD validation, and origins.
All ecosystem and dependency origins must lie below that venv and outside every
repository, artifact cache, and user site.

### Installed behavior cells

| Cell | Required evidence |
|---|---|
| Resolver | Fully hashed lock, pip report, `pip check`, exact dependency graph, no conflict or ambient path. |
| ANYfileIO base | Install pinned-object ANYfileio 0.2.0 with NumPy only via `--no-deps`; import record/document/codec, accepted CAD-neutral exports, inspector-safe facade, and CLI surfaces without importing ANYmesher or ANYmaterial. |
| ANYfileIO semantics | Install `ANYfileio[semantics]` from the full lock; run frozen public SESAM semantic read/write probes plus pinned-object `tests/test_semantics_extra.py` and focused `tests/test_sesam.py` nodes against ANYmesher 0.2.1 and ANYmaterial 0.1.x. |
| ANYmesher native | Public `auto` selects provenance `anymesher-cpp17`; explicit `native` succeeds; repeated canonical topology hashes match. |
| Python oracle | Explicit `python` meshes the same constrained face with a hole; boundary incidence, coverage/area, cells, and canonical topology match the approved oracle. |
| Predicates | Native/Python orientation and incircle agree for deterministic true/false and one-ULP near-degenerate cases. |
| Absence fallback | In a disposable clone, remove only the verified native extension; `auto` falls back to Python with an absence-only reason. |
| Corrupt ABI | In a separate clone, replace only the verified extension with frozen invalid bytes; `auto` and `native` propagate the load error and never fall back. |
| ANYfem selector | Schema 1-5 omission preserves Python; schema 6 has one top-level selector; new auto projects record requested/selected/actual backend; nested duplicates reject; session snapshots do not change in flight. |
| ANYsolver | Import from wheel, verify semantic ANYmesher requirement `>=0.1,<0.3`, generate the neutral panel contract, and exercise accepted activity/restart smoke without source shadowing. |

All installed-wheel test modules and probe programs are frozen external copies,
not files executed from a checkout. They are UTF-8 files with frozen SHA-256 and
run from an external CWD. `PYTHONPATH`, checkout roots, repository roots, and
source-package paths are excluded and origin assertions enforce that boundary.
Values, origins, filenames, hashes, and exceptions are recorded, not represented
only as booleans.

Stage B publishes an atomic content-addressed bundle containing the accepted
Stage-A index/hash, every dependency artifact hash, lock, resolver report,
installed metadata/origins, probe source/hashes, stdout/stderr, raw resource
samples, cleanup/process state, and final report. Its final directory is the
SHA-256 of its acyclic index.

Exact future lease command:

```powershell
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File C:\Github\ANYopenSoft\governance\qualification\native_hybrid\stage_b_qualify_combined_runtime.ps1
```

Lease envelope: one coordinator and one probe/install child at a time; at most
2 logical CPUs, 2.5 GiB combined RAM, 6 GiB fresh external disk, no GPU/network
or build; worker timeout 600 seconds, cleanup margin 120 seconds, outer timeout
780 seconds; ETA 6-10 minutes. No retry or tuning.

## CI and non-Windows boundary

Local qualification claims only Windows AMD64 CPython 3.13.9. Linux, macOS,
CPython 3.11/3.12/3.14, and wheel-tag matrices require completed GitHub Actions
jobs at the exact accepted default tips. Stage A/B are blocked until the owner
workflow fixes listed in the source prerequisite blockade are committed at the
rebound tips. Evidence must record repository,
workflow file/blob SHA, run/job IDs, event, commit, runner image, matrix cell,
conclusion, artifact names/IDs/expiry, downloaded bytes/SHA-256, and installed
wheel behavior. A configured workflow or green unrelated run is not evidence.

ANYmesher CI must prove installed compiled wheels on Windows, manylinux, and
macOS in its declared matrix. ANYgeometry, ANYmaterial, ANYfileIO, ANYsolver,
and ANYfem must prove their claimed pure-wheel/import cells. Missing matrix cells
remain explicit platform gaps; they do not invalidate truthful Windows evidence
but block a full-platform release-readiness claim.

No workflow is dispatched and no artifact is downloaded under this plan until
its exact read-only evidence command is separately registered. No package
publish workflow, tag, GitHub release, TestPyPI upload, or PyPI upload is allowed.

## Acceptance and reports

Required durable outputs are:

- source/input manifest and Stage-0 primary-index/changelog report;
- accepted Stage-A content-addressed wheelhouse index;
- exact hashed runtime acquisition manifest;
- `runtime-win-cp313.lock` and pip resolver report;
- accepted Stage-B content-addressed runtime index/report;
- CI/non-Windows evidence ledger with explicit missing cells;
- release-readiness summary separating implemented `Unreleased` work from any
  later tagged or externally published release.

Completion requires independent verification of every hash DAG, exact resolver
closure, installed origins, native/oracle/fallback behavior, ANYfileIO base and
semantics cells, ANYfem selector migration, worktree preservation, and claim
boundary. A final verdict may say Windows qualification is complete while
non-Windows evidence remains open; it may not say publication-ready until all
declared release platform cells and changelog/version gates pass.

## Explicit exclusions

This plan does not authorize package publication, tags, GitHub releases,
TestPyPI/PyPI uploads, secret or environment administration, performance
benchmarks, broad scaling, destructive cleanup, force pushes, or modification
of the four ANYfem dirty UI/test files.
