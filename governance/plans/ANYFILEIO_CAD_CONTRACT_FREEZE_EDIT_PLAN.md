# ANYfileIO CAD Contract-Freeze Editing Plan

Status: **registration candidate; no worktree or repository edit is authorized
until the ecosystem Boss registers this exact file and SHA-256**

Owner: CAD pipeline lead (`019ff74a-63c3-7db1-8e6b-dfaa57fed80e`)

Date: 2026-08-12 (Europe/Oslo)

## 1. Objective and source authority

Freeze the versioned, backend-neutral contracts that every lightweight-core,
heavy-provider, and consumer implementation slice must use. This slice writes
documentation only. It does not implement backend discovery, CAD models, OCCT
operations, consumer integration, package metadata, tests, builds, benchmarks,
or releases.

Authoritative inputs:

- original plan:
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`;
  SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`;
  SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered M2 governance allowlist:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`;
  SHA-256
  `87A30E18F4DCF6D7CE194AC4CE05909BC149027128A8F2CE5EFB421310185697`;
- accepted read-only ANYgeometry contract: public tip
  `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`, qualified code parent
  `8828019e0f940b0d6f240b98f8be17d6f306155b`, version 0.2.1, schema 4;
- accepted Forseti M2 core base, section 2 below.

If an input hash or accepted tip changes, this plan freezes for revision before
the first edit or further edit.

## 2. Repository, base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileIO
remote identity:   https://github.com/audunarn/ANYfileIO.git
accepted base:     0d2c7f8ef1b17f42f667d6183125e51cb650a70d
base tree:         bd379bf23b1b2b2c8f5d6a6474d4d556e288102a
base parent:       82a0f5f110361fcd902cd3aac5d4c6beeaa187fa
source branch:     codex/anyfileio-repository-rename
new branch:        codex/cad-contract-freeze
branch upstream:   none (do not configure a Git tracking upstream)
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-contract-freeze
```

The base was observed clean when this plan was prepared. Immediately before
worktree creation, revalidate the full commit, tree, parent, branch, status, and
M2 protected digest. Drift freezes this slice and is reported to the Boss.

Creating the branch/worktree is a later normal implementation setup step after
registration. This plan itself creates neither.

## 3. Exact owned files

This owner may add exactly these three repository-relative UTF-8 Markdown files
at exactly these isolated-worktree paths:

1. `docs/CAD_BACKEND_CONTRACT.md` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-contract-freeze\docs\CAD_BACKEND_CONTRACT.md`
2. `docs/ANYGEOMETRY_0_2_ADAPTER.md` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-contract-freeze\docs\ANYGEOMETRY_0_2_ADAPTER.md`
3. `DEPENDENCY_MATRIX.md` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-contract-freeze\DEPENDENCY_MATRIX.md`

There are no transferred hunks and no existing-file edits. `ANYGEOMETRY_0_2`
names the compatible 0.2.x adapter family; its contents freeze the active floor
at 0.2.1/schema 4 and do not claim compatibility with 0.2.0/schema 3.

The corresponding paths beneath the primary checkout
`C:\Github\ANYfileIO` are repository-location labels only and are not edit
targets. All reads/writes for this slice occur in the isolated worktree above.

## 4. Explicit exclusions and protected state

Every path not listed in section 3 is excluded. In particular, do not edit:

- protected M2 files `README.md`, `pyproject.toml`, and
  `tests/test_packaging.py`;
- `.github/**`, `CHANGELOG.md`, `MIGRATION.md`, `MANIFEST.in`, `run_gui.py`,
  `LICENSE`, `.gitignore`;
- all `src/anyfileio/**` implementation;
- all `tests/**` and repository fixtures;
- ANYfileio-occt, ANYgeometry, ANYmesh, ANYfem, ANYsolver, ANYstructure,
  ANYmaterial, ANYtk3D, ANYopenSoft portal, or another repository;
- Git remotes, tags, releases, external services, package indexes, and local
  primary checkouts.

Forseti M2 protected state:

```text
commit:          0d2c7f8ef1b17f42f667d6183125e51cb650a70d
tree:            bd379bf23b1b2b2c8f5d6a6474d4d556e288102a
stable patch-id: ffc7ceadd7b89f02e90568602ac1a27dd0e19bec
binary diff:     SHA-256 4B2763FC72F0F1FA53E808E28E3D6DEBE0973DD6DE0B2D50E0C0F6A6FA229068
binary extent:   3,380 bytes
changed paths:   README.md; pyproject.toml; tests/test_packaging.py
diff extent:     15 insertions; 7 deletions
target blobs:    README.md bd89d71a6e9ba70654f6a1c4e19d3ca0f89ae02e
                 pyproject.toml abae003aa442c2d363c35a5ab2ba671561185d0d
                 tests/test_packaging.py 56335ff7bf0109e8910a27b0da60b874fc730256
```

The one final docs commit must have direct parent exactly
`0d2c7f8ef1b17f42f667d6183125e51cb650a70d` (not merely contain it as an
ancestor), and `git diff 0d2c7f8... --` must show only the three owned new
documents. No preparatory, fixup, merge, or intermediate commit is permitted.

## 5. Contract contents and decisions

### 5.1 `docs/CAD_BACKEND_CONTRACT.md`

Freeze, without implementation:

- terminology and separation among repository, distribution, import package,
  backend id, protocol version, compatibility version, and artifact schema;
- protocol version 1, backend id `occt`, compatibility version 1;
- entry-point group/name/target:
  `anyfileio.backends` / `occt` /
  `anyfileio_occt.backend:get_backend`;
- core-known STEP/IGES/optional BREP `FormatDescriptor` semantics;
- capability flags, normalized options, diagnostics, missing/broken/incompatible
  backend failure behavior, cached discovery, and provider-load timing;
- backend-neutral imported-CAD records, `CadEntityRef`, deterministic identity,
  runtime-document lifetime, context/close semantics, and prohibition on public
  OCP types;
- prototype/occurrence instancing, compact array schemas/dtypes/origins,
  ownership ranges, precision selection, and no JSON geometry arrays;
- source/artifact lifecycle, SHA-256 identity, preserve-mode core operation,
  preview reopen without OCP, and content-addressed cache keys;
- thread/process/global-OCCT-state expectations and cooperative cancellation;
- compatibility/change rules and explicit future solid-to-shell boundary;
- the split between core `CadAssetWriteReport` and adapter-only structural
  `CadWriteReport`.

### 5.2 `docs/ANYGEOMETRY_0_2_ADAPTER.md`

Freeze the read-only ANYgeometry 0.2.1/schema-4 adapter contract:

- real `EntityHandle` mappings live only in lazy
  `anyfileio_occt.geometry_export`; core never copies or imports that identity;
- GeometryExportView captures public immutable store references without clone,
  topology/design snapshots, or schema serialization in the hot path;
- revision/`ChangeSet` cache identity and invalidation;
- committed versus certified export/audit caching and fail-closed diagnostics;
- structural Part/Sheet/FaceUse/Coedge/Member/MemberEdgeUse ownership,
  orientation/order, unowned geometry, Attachment/Junction metadata, and no raw
  edge-to-member inference;
- exact supported planar/cylindrical/conical/ruled mappings and explicit
  unsupported-surface failure without faceting/thickening/capping/healing;
- `TolerancePolicy`, units, `model_local`/`external` coordinate spaces, exact
  transform order, and no double conversion;
- schema-4 checksum ownership, source model UUID/revision, and exact structural
  report fields;
- no mutation of ANYgeometry, no sewing across Parts, and no solid-to-shell work.

### 5.3 `DEPENDENCY_MATRIX.md`

Freeze:

- NumPy-only ANYfileIO base; lazy `semantics` extra; no eager ANYgeometry,
  ANYmesher, ANYmaterial, OCP, CadQuery, or provider import;
- ANYfileio-occt base and `[geometry]` extra ranges exactly as registered;
- `cadquery-ocp-novtk>=7.9.3.1.1,<7.10`, qualification pin 7.9.3.1.1,
  Python 3.11-3.14/platform wheel matrix, unsupported cells, no source fallback,
  and same-namespace co-install prohibitions;
- accepted geometry/mesher and provisional owner-delivered solver/consumer
  ranges, with unresolved values visibly blocked rather than guessed;
- core/provider/consumer wheel allow/deny contents and module-import isolation;
- clean-wheel/resolver/build/size/import/performance gates and which require a
  performance lease;
- release/publication ordering as a gated future action, not authority.

The documents cross-link each other and state the source-plan/addendum hashes,
accepted repository SHAs, unresolved handoffs, and versioning rules.

## 6. Verification and evidence

Allowed light checks after editing:

```text
git status --short --branch
git diff --check
git diff --name-only 0d2c7f8ef1b17f42f667d6183125e51cb650a70d --
git rev-parse HEAD^
git diff -- README.md pyproject.toml tests/test_packaging.py
rg contract consistency searches limited to the three owned documents
```

Required evidence:

- only the three exact new paths changed;
- `HEAD^` equals exactly `0d2c7f8ef1b17f42f667d6183125e51cb650a70d`;
- no M2 file diff;
- no unresolved placeholder presented as a frozen value;
- backend/geometry/dependency documents agree on names, ranges, protocol and
  compatibility versions, identity ownership, import boundaries, and gates;
- `git diff --check` succeeds.

No pytest command, import timing, resolver environment, dependency installation,
build, wheel, `twine`, native compile, benchmark, profiler, fixture generation,
or broad search is needed or authorized for this documentation-only slice.
If later requested, it requires the applicable performance lease.

## 7. Milestone, commit, handoff, and merge order

Single milestone and commit:

1. revalidate base/protected state;
2. create only the three documents;
3. cross-review them against the registered addendum;
4. run section 6 light checks;
5. commit one coherent documentation-only commit;
6. report full commit/tree SHAs, paths, diff/stat, checks, and limits to the Boss.

Exact merge/consumption order:

```text
Forseti M2 0d2c7f8ef1b17f42f667d6183125e51cb650a70d
  -> this contract-freeze commit
     -> registered ANYfileIO lightweight-core implementation plan/base
     -> registered ANYfileio-occt scaffold plan (cross-repository contract input)
        -> disjoint provider specialists
     -> later registered consumer plans
```

No implementation plan may replace this slice with code in the same commit.
Downstream editing plans name the resulting full contract commit SHA; until that
exists, they remain read-only planning drafts rather than editing authority.

## 8. Risks, failure preservation, and rollback

- A contract ambiguity is resolved here before code, never independently by
  implementation agents.
- A needed public-contract change after freeze is a material plan improvement and
  version/compatibility review, not a silent document patch.
- Existing dirty primary checkouts are never used for editing.
- First validation failure is preserved and reported; no broadening or tuning is
  inferred.
- Rollback is a normal revert of the single documentation commit after owner/Boss
  review. Never reset hard, rewrite M2, or delete another task's worktree.

This plan grants no push, PR, publication, external-service, performance, or
closeout authority.
