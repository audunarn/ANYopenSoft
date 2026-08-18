# ANYfileIO 0.2 NumPy-only lightweight-core handoff plan

Status: **registration candidate**. This content-addressed planning artifact
grants no source edit, branch, worktree, test, build, resolver, merge, push,
provider, consumer, publication, or performance authority until the ecosystem
Boss registers its exact path and SHA-256.

Date: 2026-08-13 (Europe/Oslo)

## 1. Purpose and authority

This plan hands off the Boss-accepted, linear ANYfileIO 0.2 lightweight-core
source tip for separately registered heavy-provider work. It records what is
implemented in source, the exact dependency/import contract, the evidence that
actually exists, and every qualification or owner gate that remains open.

Authoritative inputs:

- source plan
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`,
  SHA-256 `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`,
  SHA-256 `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered M2 allowlist
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`,
  SHA-256 `87A30E18F4DCF6D7CE194AC4CE05909BC149027128A8F2CE5EFB421310185697`;
- accepted contract, public-types/discovery, semantics-runtime, operations, and
  preview-artifact plans, respectively:
  `AD9076D84092E5B226A17738A1D1543C67A877CA584288B198ED3BB0830494CA`,
  `C3D0E42184A9926ECBA207075C8F28451DF44144AA17122958AC3034DFA955F0`,
  `CF9A48262296CB5AA59B7DB973B451F06F406DA6E031C121B120E12C5C544780`,
  `5EF3F06E58D70EEA029E6BF74C2469F2AA735E5FED706B1221A6DE9EB966D452`,
  and `96AD1CBE03404F19FD1D57B6FD98251E3BB68A4CDA9B5FC4E8B8D2E351990F49`.

No implementation worktree is assigned by this plan. The observed clean
handoff worktree is evidence only:
`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact`,
branch `codex/anyfileio-cad-artifact`, upstream `none`.
The primary checkout remains clean at M2
`0d2c7f8ef1b17f42f667d6183125e51cb650a70d`; naming the accepted handoff
object does not integrate it there.

## 2. Exact accepted source chain

The handoff anchor is exactly
`5513881827cdee9fd337497a2730a5912d8ea751`, tree
`68d703646c5d9b556c1ecdbdb96f677a4ba9a381`, with sole parent
`a3725201a87d39a19ccf7edd1ae35d6d3c3f5089`.

| Milestone | Commit | Tree | Sole parent |
| --- | --- | --- | --- |
| Forseti M2 canonical identity | `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` | `bd379bf23b1b2b2c8f5d6a6474d4d556e288102a` | `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` |
| CAD contract freeze | `5f605d0bcd63de9e45230588abf7f8b211a23b20` | `0c8aabaf1e43dbbfe774e281a51532dc48f1c824` | `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` |
| CAD-neutral types/discovery | `085e92c5ff144fb0f9f96db4afc68c4d2dc7f099` | `ca41a26cdc7feb8574aabf78997c07889c84bcb6` | `5f605d0bcd63de9e45230588abf7f8b211a23b20` |
| Discovery correction | `a01c9a81ef5690873c802d9832c672ec77c6a474` | `349ff94ff2f62b1eee53fdb0c6c2945ad21c6333` | `085e92c5ff144fb0f9f96db4afc68c4d2dc7f099` |
| NumPy-only semantics runtime | `1f0b5780df7f025fc786fd3db2cba9da2104fb5c` | `beac80083f7df78718e1fa6f26b60b8f24633bf2` | `a01c9a81ef5690873c802d9832c672ec77c6a474` |
| CAD operations/orchestration | `7e7538e76a847cf700fee2535cdeae5c1c046c78` | `94e13ac0a62082fea8c98d1ea249c98b1c04fd0b` | `1f0b5780df7f025fc786fd3db2cba9da2104fb5c` |
| Operations ownership correction | `da8fd8dd562dfd266124a222973e43d65f7db064` | `1c101bd525f858f8ac3f560db575d720dff51e45` | `7e7538e76a847cf700fee2535cdeae5c1c046c78` |
| OCP-free preview artifacts | `a3725201a87d39a19ccf7edd1ae35d6d3c3f5089` | `d8f68eb05d4094bd2042a4759d51a335622b872d` | `da8fd8dd562dfd266124a222973e43d65f7db064` |
| Artifact metadata/hash correction | `5513881827cdee9fd337497a2730a5912d8ea751` | `68d703646c5d9b556c1ecdbdb96f677a4ba9a381` | `a3725201a87d39a19ccf7edd1ae35d6d3c3f5089` |

This is an accepted source chain, not a merge into `main`, a release tag, a
built artifact, or publication authority. Rebase, squash, cherry-pick, or
merge requires a separately registered order and fresh protected-diff proof.

## 3. Frozen public and dependency blobs at the handoff

| Contract or source surface | Git blob at `551388...` |
| --- | --- |
| `pyproject.toml` | `39ea8fd4e6e7554d87d42ad4382489cc68eec833` |
| `src/anyfileio/__init__.py` | `02ee5271e924c6e579a733f0c5163dc29c71d4be` |
| `src/anyfileio/cad.py` | `baa7a5fde9db1da0951def9ff0abe1cd46626c7d` |
| `src/anyfileio/cad_backend.py` | `fca05afc5f2daa7d4cdd5677d774628e67de7980` |
| `src/anyfileio/cad_operations.py` | `4e9d5585d3e19da4b4a97b504466e5550b7ee845` |
| `src/anyfileio/cad_artifact.py` | `61c2c63ae387fdeeac727e4a91d606dab76d1f78` |
| `src/anyfileio/formats.py` | `3db2439554a927426d064eadb3a9bdedda1e123b` |
| `src/anyfileio/diagnostics.py` | `82116cd6627f6cf747c6ada3dbd545bcdd37fdc2` |
| `src/anyfileio/_semantic_dependencies.py` | `10cc652c6bef5deae313d37ccbdb1f2f17c0c1e7` |
| `src/anyfileio/calculix/deck.py` | `834e1edbd07362da627aa0cb6cabebdbedab4233` |
| `src/anyfileio/sesam/semantics.py` | `5c59cfd020f8b3d80537360f97511353d501f576` |
| `docs/CAD_BACKEND_CONTRACT.md` | `f4ecd214cdd2ae448c91a6e8d46d4101b34a4ddb` |
| `docs/ANYGEOMETRY_0_2_ADAPTER.md` | `f828cc4a0ab6c1c93cb569c45af5191dfd723e34` |
| `DEPENDENCY_MATRIX.md` | `ed53d6d8fc5d315c3c5e31139032fea4353c8e60` |

Any future provider plan consumes these blobs without silently revising their
public symbols, option defaults, diagnostics, protocol values, lifecycle,
artifact schema, or dependency ranges. A needed revision is a material
`PUBLIC CONTRACT CHANGE` and returns to the ecosystem Boss.

## 4. Dependency, import, and protocol handoff

- Distribution/source version: `ANYfileio` `0.2.0`; Python `>=3.11`.
- Base requirement: exactly `numpy>=1.26`; the base contains no ANYgeometry,
  ANYmesher, ANYmaterial, OCP, CadQuery, or ANYfileio-occt requirement.
- `semantics` extra: exactly `ANYmesher>=0.2,<0.3` and
  `ANYmaterial>=0.1,<0.2`. The four-object semantic capability bundle loads
  only at SESAM/CalculiX semantic operation boundaries and fails with typed
  `SEM001`/`SEM002`/`SEM003` diagnostics. A broad legacy install range never
  proves CAD semantic capability.
- Core CAD records, backend metadata discovery, source spooling, preserve,
  operations orchestration, and preview-artifact reopen are stdlib+NumPy and
  provider-neutral. Public stored values and annotations contain no OCP,
  CadQuery, ANYfileio-occt, or ANYgeometry identity.
- Provider metadata is fixed to group `anyfileio.backends`, name `occt`, target
  `anyfileio_occt.backend:get_backend`, backend id `occt`, protocol version `1`,
  and compatibility version `1`. Enumeration is metadata-only; provider load
  occurs only for a requested heavy operation and fails closed.
- The future `ANYfileio-occt` `0.1.x` base is Python `>=3.11,<3.15` with
  `ANYfileio>=0.2,<0.3`, `numpy>=1.26`, and
  `cadquery-ocp-novtk>=7.9.3.1.1,<7.10`; its geometry extra adds only
  `ANYgeometry>=0.2.1,<0.3`. Native qualification pins the distribution
  `cadquery-ocp-novtk==7.9.3.1.1`, forbids `cadquery-ocp`/`cadquery`
  coexistence, and permits no source-build fallback. `OCP` is the import
  namespace; runtime `occt_version` is observed separately and is never
  inferred from the distribution version.
- Preview persistence is `anyfileio.cad-preview` schema `1`, implemented by
  `anyfileio.cad_artifact`; open/self-validation is OCP-free.
- ANYgeometry is consumed read-only at `>=0.2.1,<0.3`, schema `4`, only by the
  future heavy geometry extra. Core never copies `EntityHandle` identity.

The source tip implements this boundary. Installed-wheel isolation remains a
separate observed qualification gate; source imports and synthetic blockers do
not substitute for it.

## 5. Truthful evidence boundary

The ecosystem Boss accepted each source milestone after bounded independent
review and its registered focused evidence. That establishes a coherent
source-level public contract and implementation at `551388...` only:

- discovery tests used fake entry points; no real provider distribution was
  loaded;
- semantic tests used fake/static cases plus unchanged source-owner success
  nodes; no accepted hash-pinned owner-wheel resolver cell exists;
- operations tests used synthetic providers and task-owned temporary files;
  they are not native OCCT correctness evidence;
- artifact tests used small synthetic ZIP/NPY payloads and corruption cases.
  The preserved first result was `30 passed, 10 failed`; bounded corrections
  then passed `2/2`, the directed follow-up passed `5/5`, and Boss independently
  passed the two strengthened eager-metadata/digest predicates;
- `git diff --check`, exact-scope, ancestry, blob, and clean-worktree proofs
  were observed at the individual closeouts.

No statement above is a full-suite, built-wheel, resolver, platform, native
provider, real-CAD corpus, consumer, performance, or release claim.

## 6. Open qualification and owner gates

The following remain `UNRUN`, `BLOCKED`, or outside this handoff:

1. `python -m build`, sdist/wheel, `twine check`, `RECORD`, wheel contents,
   clean install, and Python/platform resolver matrices.
2. Base-only installed-wheel isolation is `UNRUN`; it depends only on this
   accepted core tip, NumPy, and a separately authorized build/install gate.
   The `[semantics]` installed-wheel cell remains `BLOCKED` on accepted
   hash-pinned ANYmesher and ANYmaterial owner artifacts. Both gate release
   claims, not this source tip.
3. ANYfileio-occt packaging, OCP wheel import/isolation, real STEP/IGES/BREP,
   XDE assembly/metadata, tessellation, preserve/translation, and native error
   behavior. The provider repository remains a separate owner scope.
4. ANYgeometry structural export. Protocol 1 supports only `model_local`;
   external/CRS requests remain typed `BLOCKED` until a geometry-owner
   directional helper/formula and regressions exist. Exact-object committed
   read synchronization remains blocked on an accepted owner lease/snapshot.
5. ANYfem format-V7 persistence/offline preview/live CAD UI. Work waits for
   accepted V6, native-selector, UI/settings, plate-ownership, and selector-
   parity tips. CAD assets remain reference-only and outside mesh/solve.
6. Solver dependency changes, ANYstructure isolation, and their returned
   owner commits/wheels. CAD has no direct write authority in those repos.
7. Full/cross-repository/native suites, benchmarks, profiling, scaling,
   stress, large fixtures, timing/RSS/size, release/tag/upload, and publication.

Builds, broad suites, native qualification, resolvers, and performance work
require their own exact command authorization and, where classified heavy, an
exclusive `PERF LEASE REQUEST` followed by `PERF LEASE GRANTED`.

## 7. Frozen provider and consumer sequence

Registration of this exact handoff plan may establish `551388...` as the sole
accepted lightweight-core input. It does not itself authorize the steps below.

1. Revalidate the clean ANYfileio-occt repository tip
   `571231dc4c7d8b4131daac6b719a6b93125a20b4` and register exact-file plans,
   isolated worktrees, exclusions, protected LICENSE blob, and cherry-pick
   order before any provider edit.
2. Land provider scaffold/metadata/shared-model ownership first; then disjoint
   imported-CAD slices for STEP/IGES/BREP XDE read, tessellation, and
   preserve/translation/write; integrate them in a separately frozen order.
   Every slice consumes the protocol/blobs above and must not copy core types.
3. Qualify the integrated imported-CAD API with exact OCP wheels only after
   source integration. This is the first native/provider gate; ANYmesher is not
   a prerequisite for disjoint imported-CAD provider implementation.
4. After accepted ANYfem V6/native/UI tips, implement owner-controlled format
   V7 persistence and the default-install OCP-free cached-preview path.
5. After an accepted exact-object read lease/snapshot, integrate the separate
   ANYgeometry structural adapter. External/CRS remains blocked independently.
6. Add ANYfem live CAD scene/UI only after persistence and provider handoffs;
   then obtain solver/ANYstructure owner returns and run leased integration,
   resolver, correctness, and performance gates.
7. Publication follows only a separate ecosystem-Boss completion review and
   explicit release authority.

Any overlap, changed base, public-contract change, owner-gate shortcut, or
merge-order change requires a new content-addressed plan or registered
deviation. No active dirty worktree or ancestor SHA is treated as a handoff.

## 8. Registration and completion of this planning gate

For registration, report this file's absolute path, SHA-256, byte count, line
count, and a static check that its anchor/tree/parent and listed blobs match
`5513881827cdee9fd337497a2730a5912d8ea751`. No test, build, resolver, branch,
worktree, merge, push, network, provider, consumer, or publication action is
part of this gate.

This planning gate is complete only when the ecosystem Boss accepts the exact
file identity and names the next separately registered owner plan. Registration
does not retroactively authorize implementation.
