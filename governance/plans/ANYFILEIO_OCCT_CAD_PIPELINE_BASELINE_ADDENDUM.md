# ANYfileIO / OCCT CAD Pipeline Baseline Addendum

Status: **registration candidate; no implementation authority until the ecosystem Boss registers this exact file and SHA-256**

Task: `019ff74a-63c3-7db1-8e6b-dfaa57fed80e`

Date: 2026-08-12 (Europe/Oslo)

## 1. Source authority and precedence

This addendum updates the baseline and sequencing of:

`C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`

Source-plan SHA-256:

`473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`

The source plan remains authoritative except where this addendum explicitly
supersedes it. In case of conflict, this addendum wins. It does not weaken the
source plan's correctness, identity, tolerance, fidelity, lightweight-isolation,
performance, evidence, or fail-closed requirements.

The following Boss decisions are mandatory:

1. ANYgeometry is now 0.2.1 with document schema 4 and is read-only to this task.
2. Consume the active ANYmesher 0.2.x delivery; delete the proposed 0.1.1
   compatibility-bridge implementation and write scope.
3. ANYfem project persistence for CAD is version 7, after the active version-6
   native-selector migration and its UI/settings handoff have committed tips.
4. ANYsolver dependency or release changes require a separate owner handoff and
   are not direct CAD-task write authority.
5. Forseti's M1 inventory and M2 canonical metadata commit are accepted
   prerequisites. CAD work branches from the exact M2 commit and preserves its
   allocated repository-identity hunks and guard test.
6. Implementation uses isolated worktrees. Every editing agent registers its own
   content-addressed `.md` plan before editing. Exact file ownership and merge
   order are frozen before work begins.
7. Wave-0 test suites, builds, resolver environments, benchmarks, profilers, and
   other qualification runs require the ecosystem performance lease.

## 2. Authoritative starting tips

These are governance baselines, not proof that an active task is complete. Every
tip, branch, dirty path, version, and dependency constraint is revalidated at its
handoff before a worktree is created or a patch is applied.

| Repository | Authoritative starting state | CAD-task treatment |
| --- | --- | --- |
| `ANYfileIO` | accepted clean M2 commit `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` on `codex/anyfileio-repository-rename`, parent `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | Canonical lightweight-core base; preserve Forseti's exact README, pyproject, and packaging-test identity hunks. |
| `ANYfileio-occt` | `571231dc4c7d8b4131daac6b719a6b93125a20b4` on `main`; license-only baseline | Separate heavy backend; may be developed only after core contracts and worktree ownership are registered. |
| `ANYgeometry` | public tip `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`; qualified code parent `8828019e0f940b0d6f240b98f8be17d6f306155b`; version 0.2.1/schema 4 | Read-only dependency and contract authority. |
| `ANYmesh` / distribution `ANYmesher` | committed base `97058e0a1213ba7f0da506ff1a00d4ef10093d20` plus active uncommitted compiled/native work | Read-only until the active owner delivers an accepted 0.2.x tip/artifact. |
| `ANYfem` | committed base `b17f1d47ba79e5c04692301e96d23dd5ac5627cb` plus active dirty integration/version-6 work | No CAD edit until committed native-hybrid and UI/settings tips are handed off. |
| `ANYsolver` | `7daa6e8c61954cfc1bc4469457fef0db154d3375` on `native_hybrid_mesher`; separate S4 worktrees | No direct dependency/release edit; owner handoff only. |
| `ANYstructure` | `4a79b860739c2f0b24f61314d4c13d943886bdd3` on `clean-up-after-external` | Later consumer/isolation work only from an owner-approved tip. |
| `ANYmaterial` | `4626887667f4c251479d26f321b9e73b046a2783` on `main` | Read-only. |
| `ANYtk3D` | `0f49efc53670c601bbabc012d856cc8ca18dcc9b` on `main` with unrelated dirty changes | No edit unless a measured renderer blocker produces a separately approved handoff. |

The frozen former checkout `C:\Github\ANYio` is never an implementation source.
The canonical repository is `C:\Github\ANYfileIO`; distribution and import names
remain `ANYfileio` and `anyfileio` respectively.

## 3. Superseded version, schema, and dependency clauses

### 3.1 ANYgeometry

Replace every source-plan reference to ANYgeometry 0.2.0 and schema 3 with the
accepted ANYgeometry 0.2.1/schema-4 public contract. In particular:

- structural CAD mappings continue to use model-bound `EntityHandle` values;
- CAD entities continue to use `CadEntityRef`, never `EntityHandle`;
- schema-4 geometry payloads and checksums are produced only through public
  ANYgeometry serialization APIs and are never patched manually;
- public immutable stores, revision/`ChangeSet`, `TolerancePolicy`, structural
  Part/Sheet/FaceUse/Coedge/Member ownership, audit policy, units, local origin,
  and coordinate-transform semantics remain authoritative;
- the exact 0.2.1 public APIs are inspected before freezing the adapter contract;
- any required ANYgeometry change is reported as a blocker/owner handoff. This
  task does not patch ANYgeometry, including tests or documentation.

The source plan's conditional ANYgeometry write escape hatch (section 8.1) is
void. Consumer floors that previously named 0.2.0 become
`ANYgeometry[planar]>=0.2.1,<0.3` where the planar extra is required, or
`ANYgeometry>=0.2.1,<0.3` otherwise.

### 3.2 ANYmesh / ANYmesher

Delete source-plan Wave 1 / Agent 1 authority to create ANYmesher 0.1.1 or edit
ANYmesh for a compatibility bridge. The CAD pipeline consumes the active
ANYmesher 0.2.x line only after its native-hybrid owner supplies an accepted,
committed handoff tip and truthful package/index strategy.

The target dependency family is `ANYmesher>=0.2,<0.3`; the precise lower patch
floor is frozen from the delivered artifact, not guessed from the current dirty
checkout. The CAD task does not modify triangulation algorithms, compiled/native
selection, setup metadata, versioning, resolver policy, or historical evidence.

### 3.3 ANYfileIO

The lightweight/heavy split, core 0.2 target, optional semantic dependencies,
lazy backend discovery, backend-neutral public records, and zero-OCCT core remain
in scope. Any semantic extra that requires meshing targets ANYmesher 0.2.x after
handoff; the lightweight base must not require ANYmesher or ANYmaterial.

Section 4's Forseti allocation/delivery gate is satisfied by the accepted M2
commit. No CAD edit begins until this addendum is registered and an exact-file
editing plan branches from that immutable M2 base.

### 3.4 ANYsolver

Delete direct Agent 10 / Wave 1 authority to create a provisional ANYsolver 0.2.1
compatibility release or edit solver dependency metadata. The CAD task records
the dependency requirement and requests a separate owner handoff with its own
registered plan, files, migration, and regression evidence. CAD work must not
touch the native-hybrid or S4 worktrees and must not modify solver algorithms.

No publication or clean resolver claim may assume that handoff succeeded.

### 3.5 ANYfem

CAD persistence is project format version 7, not version 5. Version 7 is defined
only after the active native-selector version-6 contract and its UI/settings
presentation handoff have committed, accepted tips. The eventual migration must:

- preserve every valid version-6 field and semantic, including the sole
  top-level native-backend selector and direct/incremental runtime parity;
- migrate supported versions 1-6 forward without reusing version 6 for CAD;
- reject invalid version-7 CAD state fail-closed;
- embed only valid ANYgeometry schema-4 payloads/checksums;
- keep CAD assets reference-only and excluded from meshing/solving; and
- remain readable/viewable without importing the heavy backend when cached
  artifacts exist.

No code, persistence, UI, command, or test edit occurs in the dirty active
ANYfem checkout. CAD integration starts from the owner-approved post-V6 and
post-UI handoff tips in a separate worktree.

Two accepted ANYfem behaviours are protected public regressions, not incidental
dirty hunks:

1. **Plate ownership.** Assigning an unowned structural plate through `Project`
   creates persistent Part/Sheet/FaceUse ownership through public
   `GeometryModel` owner methods. Faces may be grouped only by an authoritative
   shared B-rep edge, never by coincident coordinates. The operation preserves
   atomic rollback. A real sketch/extrusion remains separate structural
   ownership until explicit kernel `CONNECT`; after connection, both sheets use
   the persistent shared edge/coedges, topology validates, repeated meshing is
   deterministic, and no legacy automatic shell couplings are fabricated.
2. **Version-6 selector parity.** `meshing.native_backend` is the sole canonical
   V6 selector. V1-V5 omission preserves the historical Python backend; supported
   legacy nested selectors canonicalize once; conflicting legacy values and all
   V6 missing, invalid, or nested duplicates fail closed. Direct
   `Project.generate_mesh` and incremental `NativeProjectMeshingSession` forward
   exactly one explicit selector. An incremental session validates/snapshots the
   Project selector at construction, so later Project changes affect only a new
   session.

Before a V7 worktree is created, the accepted handoff identifies the exact
commits and final test node IDs that prove both behaviours. The V7 owner records
those nodes in its registered plan and adds/updates V7 migration round trips
without weakening them. At minimum, the delivered equivalents of these current
focused tests remain in the regression set:

```text
tests/test_sketch_workflow.py::test_interior_sketch_extrusion_meshes_as_connected_shell_t_junction
tests/test_native_meshing_project.py::test_project_runtime_forwards_one_explicit_backend
tests/test_native_meshing_backend.py::test_incremental_session_snapshots_project_backend
```

No CAD loader, saver, undo command, or scene action may bypass Project ownership,
rewrite V6 selector semantics, infer coordinate connectivity, or mutate
ANYgeometry private stores.

### 3.6 ANYstructure and ANYtk3D

ANYstructure remains a later lightweight-isolation consumer. Its exact dependency
floor and administrative path changes are coordinated with its owner and Forseti;
it never gains ANYfileio-occt or OCCT binaries. ANYtk3D remains outside the write
set unless profiling under a granted lease proves a blocker and a separate plan
improvement/handoff is approved.

### 3.7 Corrected target dependency graph

The contract-freeze dependency matrix starts from these targets and records the
actual delivered patch floors before implementation/qualification:

```text
ANYfileIO base:
    numpy>=1.26

ANYfileIO semantics extra:
    ANYmesher>=0.2,<0.3
    ANYmaterial>=0.1,<0.2       # revalidate actual compatible release

ANYfem:
    ANYgeometry[planar]>=0.2.1,<0.3
    ANYmesher>=0.2,<0.3
    ANYfileio>=0.2,<0.3
    ANYsolver=<owner-delivered compatible range>

ANYfem cad extra:
    ANYfileio-occt>=0.1,<0.2

ANYstructure:
    ANYgeometry>=0.2.1,<0.3
    ANYmesher>=0.2,<0.3
    ANYfileio>=0.2,<0.3
    ANYsolver=<owner-delivered compatible range>
    no ANYfileio-occt / OCP / OCCT
```

These are target families, not resolver evidence or permission to change an
owner's metadata. Exact lower patch versions and solver bounds come only from
accepted artifacts/handoffs.

### 3.8 NumPy-only core and geometry-specific report boundary

The source plan's backend-neutral type list is refined to remove the latent
ANYgeometry dependency from the core. `ANYfileIO` has a NumPy-only base runtime:

```text
ANYfileio base dependencies:
    numpy>=1.26
```

Core CAD models may describe imported CAD identity, manifests, prototypes,
occurrences, compact tessellation arrays, diagnostics, preserve/translation
results, and `CadEntityRef`. They must not import, copy, recreate, string-shadow,
or annotate with ANYgeometry `EntityHandle`, entity-kind catalogues, models,
stores, or serializers. `import anyfileio` must not import ANYgeometry,
ANYmesher, ANYmaterial, OCP, or `anyfileio_occt`; existing semantic functionality
loads its optional dependencies only when called.

The geometry-specific mapping stays in the heavy adapter:

```text
anyfileio core:
    CadAssetWriteReport
        # imported-CAD preserve/translation information only
        # CadEntityRef is allowed; EntityHandle is not

anyfileio_occt.geometry_export (loaded only for structural export):
    CadWriteReport.geometry_to_cad:
        Mapping[anygeometry.EntityHandle, anyfileio.CadEntityRef]
    CadWriteReport.cad_to_geometry:
        Mapping[anyfileio.CadEntityRef, tuple[anygeometry.EntityHandle, ...]]
    GeometryExportDiagnostic.entities:
        tuple[anygeometry.EntityHandle, ...]
```

`CadWriteReport` and `GeometryExportDiagnostic` are defined in the adapter from
the real ANYgeometry classes; there is no surrogate handle in ANYfileIO. The
adapter's geometry-export submodule is optional and lazy:

```text
ANYfileio-occt base:
    ANYfileio>=0.2,<0.3
    numpy>=1.26
    cadquery-ocp-novtk>=7.9.3.1.1,<7.10

ANYfileio-occt geometry extra:
    ANYgeometry>=0.2.1,<0.3
```

`ANYfem[cad]` installs `ANYfileio-occt[geometry]>=0.1,<0.2`. Import, preview,
preserve, and translation remain usable without the geometry extra; structural
export reports the missing extra explicitly. Provider discovery and non-geometry
operations do not import ANYgeometry. This boundary is tested from built wheels,
including an environment with only the core's base dependency.

## 4. Accepted Forseti M1/M2 baseline and protected allocation

The prerequisite inventory is:

`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M1_CONSEQUENCE_MANIFEST.md`

Observed SHA-256 at addendum preparation:

`732FD118FC94BC5846FFEBD90EC44329AC8994A282CFF5858DE35EC74807EFF4`

Its parent rename plan is:

`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_REPOSITORY_RENAME_PLAN.md`

Registered parent-plan SHA-256:

`BCC54B83774C2ED90775026183BE189A06E15411D178C9E3029F066ABE9A9A4C`

The M1 manifest is inventory evidence, not blanket CAD write authority. Forseti
has completed the canonical M2 allocation/delivery:

```text
repository:  C:\Github\ANYfileIO
branch:      codex/anyfileio-repository-rename
parent:      82a0f5f110361fcd902cd3aac5d4c6beeaa187fa
accepted:    0d2c7f8ef1b17f42f667d6183125e51cb650a70d
status:      clean; not pushed at acceptance
commit:      Update canonical ANYfileIO repository identity
```

The accepted commit changes exactly three files (`15 insertions, 7 deletions`):

- `ANYfileIO/README.md`: repository display and editable checkout path;
- `ANYfileIO/pyproject.toml`: repository comment and canonical
  Homepage/Repository/Issues URLs;
- `ANYfileIO/tests/test_packaging.py`: repository comment plus the exact
  `test_project_urls_use_canonical_repository` guard.

Those M2 hunks are protected inputs. A CAD worktree uses the full accepted M2
commit as its base; it does not recreate, squash away, reorder ahead of, or
silently modify the repository-identity changes. CAD-specific additions to a
shared file must be disjoint from M2's hunks where practical and must retain the
same final identity text and guard assertions. Any unavoidable overlap is named
as exact transferred hunks in the editing plan and receives a combined diff
review before merge.

M1 also enumerates later consumer workflows, README/install paths, launchers,
and path-contract tests in ANYsolver, ANYfem, ANYstructure, and ANYmesh. Those
remain Forseti/consumer-owner handoffs; M2 does not grant this CAD task write
authority in those repositories.

The completed merge order for shared ANYfileIO metadata is now:

1. **Complete:** Forseti M2 repository-identity commit
   `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` from parent
   `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa`.
2. **Next after registration:** create the CAD core worktree/branch from the
   accepted M2 commit, never from its parent or the void checkout.
3. Apply registered CAD dependency/backend additions as separate commits while
   preserving the M2 identity diff and casing rules.
4. Review the combined packaging/URL/dependency diff before qualification.

The companion governance guard is:

`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`

It is regenerated only after this addendum's final hash is known, and its new
hash is submitted alongside this addendum. Its hash is deliberately not embedded
here, which avoids a circular pair of content hashes.

No two agents edit a shared file concurrently. `ANYopenSoft` portal files remain
user/portal-owner work and are not part of this CAD task.

## 5. Prerequisite DAG and implementation merge order

`G0` through `G4` are hard gates; an arrow means the right-hand work waits.

```text
G1 [SATISFIED] Forseti M1 classified inventory + M2 allocation/delivery
   accepted ANYfileIO base = 0d2c7f8ef1b17f42f667d6183125e51cb650a70d

G0 Boss registers this exact addendum/hash and its revised M2 allowlist/hash
G0 + G1
  -> Core contract freeze -> ANYfileIO core implementation

G0 -> G2 ANYmesh owner delivers accepted committed ANYmesher 0.2.x tip/artifact
       -> dependency floors + semantic integration + resolver qualification

G0 -> Core contract freeze
       -> ANYfileio-occt import/tessellation/export workstreams

G0 -> G3 ANYfem V6 native-selector tip + UI/settings tip committed/accepted
Core + heavy public contracts
       -> ANYfem V7 CAD persistence -> commands/scene/UI

G0 -> G4 solver owner dependency handoff
       -> solver metadata/regression evidence (separate owner scope)

Core + heavy + ANYfem V7
       -> ANYstructure isolation -> cross-repository qualification -> release review
```

Parallel work is allowed only for disjoint registered files after its incoming
gates are satisfied. Public-contract files are lead-owned and frozen before
provider/consumer agents implement against them.

## 6. Worktrees, agents, and exact ownership protocol

No implementation occurs in the currently active/dirty checkouts. Each repository
workstream uses an isolated worktree and a `codex/` branch from the exact accepted
handoff tip. Worktree paths, branches, bases, and owned files are recorded in the
editing agent's plan before creation/editing.

Every editing-agent plan must state:

- objective and source-plan/addendum hashes;
- repository, accepted base SHA, branch, worktree path, and upstream;
- exact owned files and explicit excluded files;
- public contracts consumed/produced and compatibility policy;
- prerequisite gates and merge/cherry-pick order;
- focused verification commands and expected evidence;
- anticipated lease-gated commands, resources, and ETA;
- rollback/handoff procedure and known risks.

The lead submits each content-addressed plan path/hash to the Boss and receives
explicit registration before that agent receives editing authority. Registration
is valid only when the plan contains the exact full base SHA, exact owned file
paths (and exact transferred hunks in a pre-existing shared file), explicit file
and repository exclusions, protected-diff digest, and exact merge/cherry-pick
order. A directory, glob, repository-wide role, abbreviated base, or verbal scope
is insufficient. Any later path/base/order change freezes the slice for a plan
revision and Boss review before further edits.

Read-only audits do not grant later write authority. One file has one active
owner. Shared contract or metadata files remain lead-owned unless an exact
handoff changes the registry. Agents commit coherent, reviewable changes before
handoff; they do not push, publish, merge, rebase another owner's work, or mutate
external services without separate user authority.

Initial planned write domains, subject to exact-file registration, are:

| Workstream | Future repository write domain | Hard exclusions |
| --- | --- | --- |
| Lead/core contracts | `ANYfileIO` contract docs and shared public API files after G1 | Geometry, mesher, solver, dirty consumer checkouts |
| Lightweight core | `ANYfileIO` backend discovery, neutral records, isolation/tests after contract freeze | OCP types/imports/binaries; Forseti-owned hunks |
| Heavy import | `ANYfileio-occt` XDE/import/unit/identity modules and focused tests | Core public-model implementation; consumer repos |
| Heavy preview/export | Disjoint `ANYfileio-occt` tessellation/export/cache modules and focused tests | Imported-CAD conversion; faceted fallback claims |
| ANYfem V7 | `ANYfem` model/persistence/headless files after G3 | V6 selector semantics and unrelated active diffs |
| ANYfem UI/scene | Disjoint `ANYfem` command/UI/scene files after V7 core | Tk calls from workers; eager assembly/tree expansion |
| Consumer isolation | Owner-approved `ANYstructure` packaging/isolation files | Heavy dependency inclusion; unrelated GUI work |

ANYsolver, ANYgeometry, ANYmesh, ANYmaterial, and ANYtk3D are not direct write
domains under this addendum.

Shared contract documents, dependency matrices, cross-workstream fixtures, and
the four final reports are lead-owned unless their registered plan delegates an
exact file. Each heavy-backend test/fixture/benchmark path is allocated to one
agent before edits; a broad `tests/**`, `benchmarks/**`, or report-directory claim
is invalid.

## 7. Revised Wave 0

Wave 0 is split so governance and light read-only inspection cannot be confused
with qualification authority.

### 7.1 Allowed before a performance lease

- verify local plan/file hashes;
- inspect local branches, SHAs, status, versions, dependency declarations, and
  public contracts without switching branches or modifying files;
- obtain owner handoffs and freeze exact file ownership/merge order;
- prepare/register planning documents;
- after registration, fetch remotes and create authorized isolated worktrees,
  subject to normal network/sandbox approval;
- design benchmark fixtures/harnesses without running heavy workloads.

These checks make no current-test, build, wheel, resolver, platform, startup, or
performance claim.

### 7.2 Metadata and protocol freeze before implementation

Before core/backend implementation, the lead commits content-addressed
`CAD_BACKEND_CONTRACT.md`, `ANYGEOMETRY_0_2_ADAPTER.md`, and
`DEPENDENCY_MATRIX.md` documents on their registered contract-owner branch. They
freeze all values below; providers and consumers do not code against provisional
metadata.

#### OCP distribution and compatibility range

The selected binding distribution is the VTK-free raw binding, not the unrelated
`ocp` project, full CadQuery, or the VTK-enabled variant:

```text
PyPI distribution:             cadquery-ocp-novtk
Python import namespace:       OCP
allowed metadata range:        >=7.9.3.1.1,<7.10
Wave-0 qualification pin:      ==7.9.3.1.1
co-install cadquery-ocp:       forbidden (same import namespace)
co-install cadquery:           forbidden/unneeded
source-build fallback:         unsupported
```

The 7.9 minor range is a compatibility boundary; widening it requires a backend
compatibility review and protocol/version decision. Official PyPI metadata
observed on 2026-08-12 reports Python `>=3.10,<3.15`, no sdist, and the wheels
below. The ecosystem supports only CPython 3.11-3.14, so CPython 3.10 is not a
target even though upstream publishes it.

Metadata source: `https://pypi.org/project/cadquery-ocp-novtk/` (revalidate and
record release-file hashes in `DEPENDENCY_MATRIX.md` before qualification).

| CPython | Windows | Linux | macOS |
| --- | --- | --- | --- |
| 3.11 | `win_amd64` | `manylinux_2_31_x86_64`, `manylinux_2_31_aarch64` | `macosx_11_0_x86_64`, `macosx_11_0_arm64` |
| 3.12 | `win_amd64` | `manylinux_2_31_x86_64`, `manylinux_2_31_aarch64` | `macosx_11_0_x86_64`, `macosx_11_0_arm64` |
| 3.13 | `win_amd64` | `manylinux_2_31_x86_64`, `manylinux_2_31_aarch64` | `macosx_11_0_x86_64`, `macosx_11_0_arm64` |
| 3.14 | `win_amd64` | `manylinux_2_31_x86_64`, `manylinux_2_31_aarch64` | `macosx_11_0_x86_64`, `macosx_11_0_arm64` |

Musllinux, Windows ARM64, PyPy, 32-bit platforms, Python outside 3.11-3.14,
Linux below glibc 2.31, and platforms lacking a matching upstream wheel are
explicitly unsupported for the heavy extra. Core ANYfileIO remains platform
independent. The leased resolver/wheel gate records every cell as pass, fail, or
unrun; availability in PyPI metadata alone is not qualification.

#### Core, geometry, and consumer dependency ranges

The dependency matrix freezes these exact declared ranges:

```text
ANYfileio 0.2 base:                 numpy>=1.26
ANYfileio semantics extra:          ANYmesher>=0.2,<0.3
                                     ANYmaterial>=0.1,<0.2
ANYfileio-occt 0.1 base:            ANYfileio>=0.2,<0.3
                                     numpy>=1.26
                                     cadquery-ocp-novtk>=7.9.3.1.1,<7.10
ANYfileio-occt 0.1 geometry extra:  ANYgeometry>=0.2.1,<0.3
ANYfem cad extra:                   ANYfileio-occt[geometry]>=0.1,<0.2
```

The delivered ANYmesher patch floor and owner-delivered ANYsolver range replace
their family floors only through an approved contract revision. No core module
imports an optional dependency eagerly.

#### Entry point and protocol version

```text
entry-point group:              anyfileio.backends
entry-point name:               occt
entry-point target:             anyfileio_occt.backend:get_backend
CAD backend protocol version:   1
backend id:                     occt
backend compatibility version: 1
```

The core enumerates entry-point metadata without importing the provider. It calls
`get_backend()` only for a requested CAD operation. The returned provider must
declare protocol version 1, backend id `occt`, compatibility version 1, and
capabilities before use. Missing or unequal protocol versions fail closed with a
structured diagnostic; the core never guesses compatibility. Any incompatible
public protocol or persisted artifact-schema change increments the corresponding
version and documents migration.

#### Wheel contents and import isolation

The freeze defines and later verifies these allow/deny lists from built wheels:

- `ANYfileio` is pure Python, contains only `anyfileio/**`, declared package data,
  license/metadata, and no `OCP`, OCCT library, `anyfileio_occt`, `cadquery`,
  ANYgeometry code, test corpus, benchmark corpus, or generated CAD artifact.
- `ANYfileio-occt` is a pure-Python adapter wheel containing
  `anyfileio_occt/**`, contract metadata, licenses/notices, and its entry point;
  it does not vendor the OCP wheel/DLL/SO/DYLIB tree, CadQuery, VTK, source CAD,
  previews, tests, or benchmarks.
- `import anyfileio`, `import anyfem`, and `import anystruct` load none of `OCP`,
  `anyfileio_occt`, or `cadquery`. `import anyfileio` also loads none of
  ANYgeometry, ANYmesher, or ANYmaterial.
- `import anyfileio_occt` and entry-point enumeration do not load `OCP` or
  ANYgeometry. The provider imports `OCP` only when a heavy CAD operation starts;
  it imports ANYgeometry only when structural export starts.
- cached manifest/preview reopen and preserve-mode byte copying work without
  importing `OCP`; core known-format/status queries work with no heavy wheel.

Wheel RECORD inspection, installed-distribution inspection, module snapshots,
and clean-environment import assertions are release gates, not source-tree
substitutes.

### 7.3 Lease-gated Wave-0 evidence

The following do not run until the Boss grants the exclusive performance lease
for exact commands, resources, and ETA:

- full repository suites or broad cross-repository regression suites;
- native/OCP builds and package builds;
- clean sdist/wheel builds, isolated installs, and `twine check`;
- clean multi-Python resolver matrices and OCP wheel/platform qualification;
- cold/warm imports, peak RSS, wheel/installed/executable size measurements;
- benchmarks, profilers, stress/scaling runs, large fixture generation, and
baseline/throughput/copy-count measurements.

The task requests this with a material `PERF LEASE REQUEST` message naming exact
commands/resources/ETA, waits for explicit `PERF LEASE GRANTED`, and reports
`PERF LEASE RELEASED` with the first observed outcome and process state. It does
not invent a local lock or treat an idle machine as a grant.

Focused, low-cost tests after an implementation slice may run only if the Boss
protocol does not classify the exact command as lease-sensitive. First failures
are preserved; no retry, tuning, or broadened run is inferred.

## 8. Revised wave and release sequence

1. Register this addendum, its revised governance allowlist, and exact ownership;
   revalidate/fetch accepted tips.
2. Branch core work from accepted Forseti M2 commit
   `0d2c7f8ef1b17f42f667d6183125e51cb650a70d`; receive the ANYmesher 0.2.x
   handoff; freeze dependency and backend contracts.
3. Implement the lightweight ANYfileIO core and core isolation tests.
4. Implement disjoint ANYfileio-occt import, instanced preview, exact structural
   export, preserve mode, and translation mode against the frozen contracts.
5. After accepted V6/UI tips, implement ANYfem project format 7, headless
   operations, commands, instanced scene/UI, selection, and analysis protection.
6. Complete owner-scoped dependency handoffs and ANYstructure isolation.
7. Request leases for the staged performance/correctness/build/wheel gates.
8. Produce implementation, dependency, performance, and known-limitations
   reports from observed evidence.
9. Request ecosystem completion review. Publishing remains a separate authorized
   action and follows actual compatible artifacts, not provisional versions.

ANYgeometry is an already delivered read-only prerequisite, not a publication
step. ANYmesher 0.1.1 and direct ANYsolver 0.2.1 creation are removed. ANYfileIO
0.2 and ANYfileio-occt 0.1 remain provisional release targets subject to package
policy and qualification. ANYfem/ANYstructure versions follow their owners'
policies; CAD persistence specifically reserves format version 7.

## 9. Correctness and definition-of-done deltas

All original correctness and performance gates remain unless impossible because
the stale baseline named the wrong version. Replace only these acceptance clauses:

- active geometry dependency: ANYgeometry 0.2.1, document schema 4;
- mesher dependency: accepted ANYmesher 0.2.x, with no CAD-task mesher bridge;
- ANYfem persistence: format 7 and supported migration from formats 1-6;
- embedded geometry: valid schema-4 payload/checksum;
- dependency qualification: truthful owner-handoff evidence for ANYsolver rather
  than a CAD-task-created compatibility release;
- regression ownership: read-only upstream suites are run only against exact
  accepted tips/artifacts and under the required lease, without editing upstream.

Completion additionally requires:

1. Accepted Forseti M2 commit
   `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` is an ancestor of the CAD core
   delivery; its exact identity hunks/guard remain present, and the combined
   metadata review is documented.
2. Every implementation commit is traceable to one registered editing-agent plan
   and exact accepted base SHA.
3. Active ANYmesh and ANYfem work is consumed only from committed handoff tips;
   no dirty-checkout state is silently copied.
4. No direct CAD-task change exists in ANYgeometry, ANYmesh, ANYsolver,
   ANYmaterial, or ANYtk3D.
5. Final reports distinguish focused evidence from lease-gated full qualification
   and state every unrun platform, resolver, performance, or external-admin gate.
6. The ecosystem Boss independently reviews the completion packet and issues the
   only closeout verdict.

## 10. Immediate hold

Until the Boss registers this addendum/hash and returns exact ownership/merge
order, the task may perform only light read-only audits and planning. It may not
edit package implementation/metadata, create implementation branches/worktrees,
run tests/builds/benchmarks, fetch as evidence, or spawn an editing agent.
