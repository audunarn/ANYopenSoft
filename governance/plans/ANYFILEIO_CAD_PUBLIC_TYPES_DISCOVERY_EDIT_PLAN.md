# ANYfileIO CAD Public-Types and Discovery Editing Plan

Status: **registration candidate; this file grants no branch, worktree, edit,
test, commit, merge, push, build, resolver, performance, or publication
authority until the ecosystem Boss registers this exact file and SHA-256**

Owner: CAD pipeline lead (`019ff74a-63c3-7db1-8e6b-dfaa57fed80e`)

Editing agent: one direct child task only, proposed canonical identity
`/root/anyfileio_cad_public_types_discovery`; no delegated/nested writer. A
different writer identity requires re-registration before any edit.

Date: 2026-08-12 (Europe/Oslo)

## 1. Objective and authoritative inputs

Implement one CAD-neutral ANYfileIO slice: the frozen NumPy-backed public CAD
records and document lifecycle, lazy entry-point discovery/status, and
core-known optional CAD format metadata. This
slice must preserve every existing SESAM/CalculiX behavior and must not import
or implement OCCT, ANYgeometry, the preview-artifact codec, semantic dependency
loading, consumer integration, or package/release metadata.

Authoritative inputs:

- original plan:
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`;
  SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`;
  SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered M2 allowlist:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`;
  SHA-256
  `87A30E18F4DCF6D7CE194AC4CE05909BC149027128A8F2CE5EFB421310185697`;
- registered contract-freeze plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_CAD_CONTRACT_FREEZE_EDIT_PLAN.md`;
  SHA-256
  `AD9076D84092E5B226A17738A1D1543C67A877CA584288B198ED3BB0830494CA`;
- accepted contract-freeze commit and exact documents from section 2.

The accepted contract documents are normative. This implementation does not
silently revise a record field, method signature, diagnostic code, identity,
cache/discovery state, unit rule, suffix rule, or lifecycle promise. A needed
change is a `PUBLIC CONTRACT CHANGE` / plan revision before editing further.

## 2. Repository, exact base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileIO
remote identity:   https://github.com/audunarn/ANYfileIO.git
accepted base:     5f605d0bcd63de9e45230588abf7f8b211a23b20
base tree:         0c8aabaf1e43dbbfe774e281a51532dc48f1c824
sole base parent:  0d2c7f8ef1b17f42f667d6183125e51cb650a70d
source branch:     codex/cad-contract-freeze
new branch:        codex/cad-public-types-discovery
branch upstream:   none (do not configure a Git tracking upstream)
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery
```

The new branch/worktree must not exist before Boss registration. After
registration, create that exact worktree directly from the exact base. The
primary checkout `C:\Github\ANYfileIO` and the clean contract-freeze worktree
are read-only comparison locations, never edit targets for this slice.

Immediately before branch/worktree creation and again before commit, verify
the full base/tree/parent, branch status, contract blobs, M2 protected blobs,
and absence of path overlap. Drift freezes the slice and is reported.

The implementation is one coherent commit whose sole parent is exactly
`5f605d0bcd63de9e45230588abf7f8b211a23b20`. No merge, preparatory, fixup,
metadata, generated, or intermediate commit is permitted.

## 3. Frozen contract and protected baseline

Accepted contract commit:

```text
commit: 5f605d0bcd63de9e45230588abf7f8b211a23b20
tree:   0c8aabaf1e43dbbfe774e281a51532dc48f1c824
parent: 0d2c7f8ef1b17f42f667d6183125e51cb650a70d
```

Protected contract documents:

| Path | Git blob | SHA-256 | Bytes / lines |
| --- | --- | --- | --- |
| `docs/CAD_BACKEND_CONTRACT.md` | `f4ecd214cdd2ae448c91a6e8d46d4101b34a4ddb` | `723FE2EF33E582F3AE9A3A60A77AB1DCD709F4C838D27F0E1C8B73134D9FF374` | 51,120 / 1,100 |
| `docs/ANYGEOMETRY_0_2_ADAPTER.md` | `f828cc4a0ab6c1c93cb569c45af5191dfd723e34` | `9E79744135C83FC10DE4C8EB231CC57B29B79AB967DF7C5468F19168448D1AA8` | 31,211 / 664 |
| `DEPENDENCY_MATRIX.md` | `ed53d6d8fc5d315c3c5e31139032fea4353c8e60` | `BB2E28A41BD2DB773E1A501113B54E9936F0708C34F21C452C2235C48091D2E3` | 22,756 / 408 |

The complete parent-to-contract binary patch over those three paths is 107,797
bytes, SHA-256
`39139AB6DCD18787232F0ECBA0F9535B9D2C0EDC8AE8CAC07CF50DD90222047E`,
and adds exactly 2,172 lines. This slice leaves all three documents byte-
identical.

Forseti M2 protected state remains:

```text
M2 commit:       0d2c7f8ef1b17f42f667d6183125e51cb650a70d
M2 binary patch: SHA-256 4B2763FC72F0F1FA53E808E28E3D6DEBE0973DD6DE0B2D50E0C0F6A6FA229068
M2 patch extent: 3,380 bytes; 15 insertions / 7 deletions
README blob:     bd89d71a6e9ba70654f6a1c4e19d3ca0f89ae02e
pyproject blob:  abae003aa442c2d363c35a5ab2ba671561185d0d
packaging blob:  56335ff7bf0109e8910a27b0da60b874fc730256
```

No protected contract or M2 path is transferred to this owner.

## 4. Exact owned paths

All implementation writes resolve beneath the isolated worktree in section 2.
The repository-relative paths and their exact worktree targets are:

### 4.1 New source files

1. `src/anyfileio/cad.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\src\anyfileio\cad.py`.
2. `src/anyfileio/cad_backend.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\src\anyfileio\cad_backend.py`.

### 4.2 Existing source files with transferred exact hunks

3. `src/anyfileio/formats.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\src\anyfileio\formats.py`.
   Base blob `c9dcf41f35986981e41d9f8b59eb51380767267e`, raw SHA-256
   `C9F402B6020ED443108BADB3F16DC19CA547009164EEA57B786B2AB698C037D6`,
   3,035 bytes / 93 lines.
4. `src/anyfileio/__init__.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\src\anyfileio\__init__.py`.
   Base blob `a4463fb355319764dd1ac956ab46e10791d4678d`, raw SHA-256
   `21ACB6A72DF26AF8BEA53C70FDBB9945195081A0A2F45813615ADCE75D377DE2`,
   3,367 bytes / 125 lines.

### 4.3 New focused tests

5. `tests/test_cad_contract.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\tests\test_cad_contract.py`.
6. `tests/test_backends.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\tests\test_backends.py`.

### 4.4 Existing test with one transferred hunk

7. `tests/test_layering.py` at
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-public-types-discovery\tests\test_layering.py`.
   Base blob `64b14ddb1038a333bb5ea28f495ae054cfac4771`, raw SHA-256
   `7CB77021317F38983B8D20F79E5D8A858AA4FC60BE13B1517FD059ACA56E7F33`,
   3,809 bytes / 101 lines.

There are exactly seven owned paths. No other existing or new file is implied.

## 5. Exact source responsibilities and hunk boundaries

### 5.1 `src/anyfileio/cad.py`

Implement the NumPy-only, slots-based, immutable boundary frozen in
`docs/CAD_BACKEND_CONTRACT.md`:

- `FormatDescriptor`, `LengthUnit`, and `CancellationCheck`;
- core `CadError` hierarchy and structured `CadDiagnostic`;
- `CadCapabilities` and `CadBackendProtocol` with exact provider signatures;
- `CadReadOptions`, `CadWriteOptions`, and `CadTessellationOptions`, including
  exact defaults, unit aliases/scales, normalization, and fail-closed validation;
- `CadEntityRef`, `CadPrototypeRecord`, `CadOccurrenceRecord`,
  `CadShapeRecord`, and `CadManifest`;
- `CadTessellation`, `CadPrototypeMesh`, and core-bound
  `CadTessellationResult` with exact `source_identity` derivation;
- `CadAssetWriteReport` (not the ANYgeometry adapter's `CadWriteReport`);
- `CadDocument` immutable public properties, context manager, idempotent close,
  retained-source borrowing/release, owner-thread checks, live-state pickle
  refusal, `_from_backend`, and `_from_preview_artifact` integration SPIs;
- compact array dtype/shape/finite/contiguity/read-only/owner-offset validation;
- exact occurrence-transform, bounds, identity vocabulary, mapping immutability,
  topology-count, diagnostic, and lifecycle invariants.

The module contains no public/private `read_cad`, `tessellate_cad`, or
`write_cad` orchestration, source-snapshot copier, or atomic output writer; and
no `importlib.metadata` scan, artifact ZIP/JSON/NPY codec, provider
implementation, OCP/CadQuery/ANYgeometry/ANYmesher/ANYmaterial import, or
consumer type. Private helpers are allowed only when required by these exact
public records and lifecycle invariants.

### 5.2 `src/anyfileio/cad_backend.py`

Implement the CAD-neutral discovery boundary:

- constants for entry-point group/name, backend id, protocol version, and
  backend compatibility version;
- `BackendStatus` and validation of the `CadCapabilities` /
  `CadBackendProtocol` values defined in `cad.py`;
- lazy `importlib.metadata` enumeration, exact `missing` / `discovered` /
  `duplicate` / `ready` / `broken` / `incompatible` states, process-lifetime
  metadata/provider/failure caching, and a private test-only reset;
- `backend_status()` without provider import; private explicit provider load and
  exact id/protocol/compatibility/capability validation; actionable missing,
  duplicate, load, compatibility, and capability diagnostics;
- one private `_load_backend()` boundary for later operation slices and focused
  fake-provider tests; it validates/caches the provider but performs no CAD I/O;
- no provider import during module import, metadata-only status, known-format
  queries, or built-in format operations.

The heavy provider registers its entry point in its own repository; this slice
does not edit ANYfileIO metadata to add one. The preview artifact reader/writer
is a future `anyfileio.cad_artifact` slice and is not implemented here.

### 5.3 Exact `src/anyfileio/formats.py` hunks

The owner may change only these conceptual regions:

1. import and `__all__` hunks: import the frozen core descriptor/discovery boundary
   and export `known_formats` and `available_formats` while retaining every
   current export;
2. immediately after the unchanged `READERS` declaration: add immutable
   built-in descriptors, exact core-known STEP/IGES/BREP descriptors, and one
   precomputed lower-case suffix index;
3. retain `supported_suffixes()` as the backward-compatible tuple of the five
   built-in readable suffixes only;
4. extend `describe()` so STEP/IGES/BREP descriptions work without provider
   discovery/import, while preserving current descriptions and `FEM010` for an
   unknown suffix;
5. add `known_formats()` and `available_formats()` with deterministic tuples;
   the former is provider-free, the latter uses cached status and never loads a
   merely discovered provider;
6. leave `read()` byte-identical. Operational CAD dispatch and source spooling
   belong to a later registered slice; existing `.fem/.sif/.frd/.dat/.inp`
   callables, option forwarding, missing-file behavior, and static `READERS`
   mapping remain unchanged and never enumerate/load plugins.

No CLI, GUI, diagnostics, SESAM, or CalculiX file is transferred. Existing CLI
format output remains the five built-in `supported_suffixes()` values until a
separate reviewed CLI contract changes it.

### 5.4 Exact `src/anyfileio/__init__.py` hunks

The owner may change only:

1. import blocks: re-export the public records/errors/protocol from `cad.py`
   and `cad_backend.py`, and add `known_formats` / `available_formats` to the
   existing formats import;
2. `__all__`: add those exact frozen public names in deterministic order while
   retaining every current FE name.

The exact additive root export set is:

```text
FormatDescriptor, LengthUnit, CancellationCheck,
CadError, CadBackendError, BackendUnavailableError, BackendDuplicateError,
BackendLoadError, BackendCompatibilityError, CadOperationError,
CadValidationError, CadOperationCancelled, CadArtifactError,
CadDiagnostic, CadCapabilities, CadBackendProtocol,
CadReadOptions, CadWriteOptions, CadTessellationOptions,
CadEntityRef, CadPrototypeRecord, CadOccurrenceRecord, CadShapeRecord,
CadManifest, CadTessellation, CadPrototypeMesh, CadTessellationResult,
CadAssetWriteReport, CadDocument,
BackendStatus, backend_status, known_formats, available_formats
```

No `read_cad`, `tessellate_cad`, `write_cad`, artifact-codec function, or
ANYgeometry adapter type is exported by this slice.

`__version__ = "0.1.0"` remains byte-identical because version and metadata are
owned by the later canonical metadata/runtime slice. The package docstring and
all existing FE imports/exports remain unchanged. Importing these modules must
not enumerate entry points or load a provider.

### 5.5 Exact `tests/test_layering.py` hunk

Do not change `ALLOWED_THIRD_PARTY`, `FORBIDDEN`,
`OPTIONAL_IMPORT_EXCEPTIONS`, or either existing test's meaning. Add only:

```text
CAD_NEUTRAL_MODULES = cad.py, cad_backend.py, formats.py
CAD_FORBIDDEN_IMPORTS = OCP, cadquery, anyfileio_occt, anygeometry
test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages
```

The new test parses only those three files and requires no module-level import
of the four heavy/provider/geometry packages. It deliberately does not change
the current base/semantics allowlists or claim that the pre-resolver package as
a whole is NumPy-only; eager semantic runtime imports belong to the separate
owner in section 8.

## 6. Focused tests and exact definitions of done

### 6.1 `tests/test_cad_contract.py`

Required nodes:

```text
test_options_normalize_units_defaults_and_reject_invalid_values
test_entity_refs_records_and_manifest_fail_closed
test_tessellation_arrays_are_compact_contiguous_and_read_only
test_owner_offsets_and_indices_are_validated
test_tessellation_result_binds_exact_source_identity
test_backend_factory_core_binds_tessellation_result
test_occurrence_transforms_and_instancing_are_preserved
test_document_close_release_and_context_are_idempotent
test_live_document_refuses_pickle_and_wrong_thread_close
test_preview_factory_loads_once_and_caches_first_failure
test_exception_hierarchy_exposes_stable_diagnostics
test_backend_protocol_has_exact_provider_call_shapes
test_core_public_annotations_contain_no_optional_package_types
```

### 6.2 `tests/test_backends.py`

Required nodes use fake entry-point/provider objects only:

```text
test_metadata_enumeration_is_lazy_and_cached
test_status_does_not_load_a_discovered_provider
test_private_load_constructs_provider_once
test_missing_duplicate_broken_and_mismatched_providers_fail_closed
test_capabilities_are_validated_before_ready_state
test_missing_backend_error_has_exact_code_and_install_hint
test_broken_provider_does_not_break_builtin_reader
test_optional_cad_formats_are_known_without_provider
test_available_formats_requires_an_already_ready_backend
test_step_iges_and_brep_suffixes_are_constant_time_and_unambiguous
test_describe_cad_is_provider_free
test_brep_requires_declared_capability
test_supported_suffixes_remains_the_five_builtin_suffixes
test_builtin_dispatch_never_scans_or_loads_plugins
test_public_import_and_metadata_queries_load_no_optional_cad_modules
test_public_cad_annotations_reference_no_heavy_or_geometry_modules
```

The subprocess import guard blocks `OCP`, `cadquery`, and `anyfileio_occt`.
It cannot block `anygeometry` on this accepted pre-runtime base: the unchanged
package facade still eagerly reaches ANYmesher, whose current package import
loads ANYgeometry. After that unchanged baseline import, the test snapshots
loaded modules and proves that discovery/format metadata queries add no optional
CAD/provider or geometry modules. The direct source/annotation checks still
forbid `anygeometry` references in the three CAD-neutral modules. Full
ANYgeometry/ANYmesher/ANYmaterial import isolation waits for the separately
owned metadata/runtime transition.

### 6.3 Existing unchanged regression nodes

Run these without editing their files:

```text
tests/test_formats_and_cli.py::test_every_suffix_is_described_and_dispatched
tests/test_formats_and_cli.py::test_options_reach_the_format_reader
tests/test_formats_and_cli.py::test_an_unrecognized_suffix_names_the_ones_that_work
tests/test_formats_and_cli.py::test_formats_lists_what_the_tool_reads
tests/test_layering.py::test_source_tree_is_importable_layout
tests/test_layering.py::test_no_module_imports_a_consumer
tests/test_layering.py::test_third_party_imports_are_declared
tests/test_layering.py::test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages
```

Definition of done:

- exact seven-path diff and one direct-child commit;
- every in-scope frozen record/protocol/status/default/diagnostic/lifecycle rule
  implemented without importing an excluded layer;
- CAD metadata queries are lazy and deterministic;
- existing five built-in readers and CLI format list retain current behavior;
- missing/duplicate/broken/incompatible discovery states fail closed without
  affecting built-in operations; no real CAD operation is implemented here;
- focused nodes pass on their first authorized run;
- contract/M2/metadata/version/runtime/consumer paths remain unchanged;
- no artifact, OCCT, geometry, resolver, wheel, performance, or release claim.

## 7. Verification commands and lease classification

Allowed static/light proof after editing:

```text
git status --short --branch
git diff --check
git diff --name-only 5f605d0bcd63de9e45230588abf7f8b211a23b20 --
git diff --exit-code 5f605d0bcd63de9e45230588abf7f8b211a23b20 -- docs DEPENDENCY_MATRIX.md README.md pyproject.toml tests/test_packaging.py .github CHANGELOG.md
git rev-parse HEAD^
targeted rg limited to the seven owned paths and protected contract constants
```

Proposed focused pytest command (do not run until the Boss explicitly classifies
this exact command as non-lease-sensitive or grants the applicable lease):

```text
python -m pytest -q tests/test_cad_contract.py tests/test_backends.py tests/test_layering.py::test_source_tree_is_importable_layout tests/test_layering.py::test_no_module_imports_a_consumer tests/test_layering.py::test_third_party_imports_are_declared tests/test_layering.py::test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages tests/test_formats_and_cli.py::test_every_suffix_is_described_and_dispatched tests/test_formats_and_cli.py::test_options_reach_the_format_reader tests/test_formats_and_cli.py::test_an_unrecognized_suffix_names_the_ones_that_work tests/test_formats_and_cli.py::test_formats_lists_what_the_tool_reads
```

Preserve the first result. Do not retry, tune, broaden, or run the full suite
without new authority.

Explicitly lease-gated and excluded from this slice:

- full `python -m pytest` or broad/cross-repository/native suites;
- `python -m build`, sdist/wheel/twine/RECORD inspection;
- clean/base-only/semantics/provider resolver or install environments;
- OCP import or native provider execution;
- wheel/platform/Python matrices, timings, RSS/size/copy counts;
- profilers, stress/scaling, large fixtures, and benchmarks.

No network, install, fetch, push, tag, PR, publication, or external mutation is
authorized.

## 8. Hard exclusions and separate ownership

Every path not listed in section 4 is excluded. This includes, explicitly:

```text
pyproject.toml
README.md
CHANGELOG.md
.github/**
tests/test_packaging.py
src/anyfileio/calculix/deck.py
src/anyfileio/sesam/semantics.py
src/anyfileio/cad_artifact.py
tests/test_cad_artifact.py and every artifact-codec test
src/anyfileio/__main__.py
src/anyfileio/diagnostics.py
src/anyfileio/gui.py
all other SESAM/CalculiX/runtime source and tests
benchmarks/**, reports/**, fixtures, generated CAD/cache/artifacts
all paths in ANYfileio-occt, ANYgeometry, ANYmesh, ANYfem, ANYsolver,
ANYstructure, ANYmaterial, ANYtk3D, and ANYopenSoft outside this plan file
```

The separately registered canonical metadata/runtime owner must later move
both `ANYmesher>=0.2,<0.3` and `ANYmaterial>=0.1,<0.2` from base requirements to
the `semantics` extra, eliminate eager semantic imports, add typed missing-extra
and version diagnostics, synchronize the package version, and prove base-only
and `[semantics]` resolver cells. The transitional legacy
`ANYmesher>=0.1,<0.3` proposal cannot merge alone and cannot count as CAD
capability. This slice neither edits nor assumes those changes.

The artifact codec `anyfileio.cad_artifact` is a separate future exact-file
plan. This slice implements only the document factory/lazy-loader integration
surface it will consume. The heavy provider and all consumers remain separate.

## 9. Dependencies, risks, and failure preservation

Dependencies:

- accepted contract commit `5f605d0...` is the immutable base;
- NumPy is already declared at the base and is the only third-party import
  permitted in the four CAD-neutral modules;
- fake entry points/providers are sufficient for this slice; no OCP artifact or
  accepted ANYmesher handoff is required to implement/test this boundary.

Risks and controls:

- public-type validation could accidentally copy or mutate arrays: normalize
  once, publish C-contiguous native-endian read-only arrays, and test ownership;
- status queries could load plugins: separate cached metadata discovery from
  the explicit private provider-load boundary and test call counts;
- provider failure could poison built-ins: isolate terminal CAD failure and run
  unchanged built-in regression nodes;
- document lifecycle could release caller-owned data: factories accept only
  paths explicitly transferred by a later core operation/artifact slice and
  tests use task-owned temporary paths;
- the current package still eagerly imports semantic dependencies: do not hide
  or broaden that known owner-blocked state in this slice;
- a needed extra path or contract change freezes work for plan/Boss review.

Rollback is a normal revert of the one coherent commit after owner/Boss review.
Never reset hard, rewrite M2/contracts, delete another task's worktree, or
discard an unrelated dirty state.

## 10. Commit, handoff, and exact merge order

One coherent commit only:

```text
contract freeze 5f605d0bcd63de9e45230588abf7f8b211a23b20
  -> this CAD-neutral public-types/discovery commit (exact seven paths)
     -> separately registered canonical metadata/runtime commit, rebased or
        freshly based on the accepted public-types commit
     -> separately registered core operations/orchestration commit owning
        read_cad, tessellate_cad, write_cad, _snapshot_source, source spooling,
        preserve/translation atomic-output control, and formats.read CAD dispatch
     -> separately registered core artifact-codec commit
     -> accepted combined lightweight-core API/metadata handoff
     -> registered ANYfileio-occt scaffold/import/write slices
     -> later ANYfem V7 and structural adapter gates
```

The metadata/runtime owner does not cherry-pick transitional resolver-only
metadata ahead of this commit and does not overwrite these source/test hunks.
Before its registration, it must name this resulting full SHA as base and prove
the protected M2/contract diff. If parallel read-only planning occurs, its
implementation plan remains non-authoritative until that exact base and merge
order are reissued.

Handoff evidence for this slice includes plan path/hash, branch/worktree/base,
commit/tree/parent, exact path/blobs, diff/stat/check results, focused first test
outcome if authorized, protected M2/contract blob proof, primary/worktree
statuses, exclusions, limitations, and downstream owner actions.

This milestone is not integration, push, release, publication, performance, or
ecosystem closeout authority.
