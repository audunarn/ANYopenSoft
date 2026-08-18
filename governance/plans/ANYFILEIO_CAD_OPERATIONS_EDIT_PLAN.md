# ANYfileIO CAD Core Operations and Orchestration Editing Plan

Status: **registration candidate; this file grants no branch, worktree, edit,
test, commit, merge, push, build, resolver, publication, network, or performance
authority until the ecosystem Boss registers this exact file and SHA-256**

Owner: CAD pipeline lead (`019ff74a-63c3-7db1-8e6b-dfaa57fed80e`)

Editing agent: one direct child task only, proposed Norwegian identity
`/root/vidar_anyfileio_cad_operations`; no delegated or nested writer. A
different logical writer requires Boss approval before its first edit.

Date: 2026-08-13 (Europe/Oslo)

## 1. Objective and authoritative inputs

Implement the CAD-neutral protocol-1 operation layer in canonical ANYfileIO:

- `read_cad` with core-owned source snapshotting, normalized source identity,
  capability checks, exact mode lifecycle, and fail-closed provider-return
  validation;
- `tessellate_cad` using an existing live session or a validated transient
  reopen of retained source, with core-only provenance binding;
- `write_cad` with provider-free byte preservation or validated provider
  translation through a same-directory temporary and one atomic replace; and
- existing `anyfileio.read(path)` CAD-suffix dispatch while keeping built-in
  SESAM/CalculiX dispatch provider-free.

This is orchestration only. It consumes the accepted public records, discovery
loader, lazy semantics boundary, and frozen contract. It does not implement the
preview artifact codec, OCCT provider, ANYgeometry adapter, consumer
persistence, UI, solver, dependency qualification, or publication.

Authoritative inputs:

- source plan:
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`,
  SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`,
  SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered M2 allowlist:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`,
  SHA-256
  `87A30E18F4DCF6D7CE194AC4CE05909BC149027128A8F2CE5EFB421310185697`;
- accepted contract-freeze commit
  `5f605d0bcd63de9e45230588abf7f8b211a23b20` and its exact three documents;
- registered public-types/discovery plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_CAD_PUBLIC_TYPES_DISCOVERY_EDIT_PLAN.md`,
  SHA-256
  `C3D0E42184A9926ECBA207075C8F28451DF44144AA17122958AC3034DFA955F0`;
- Boss-accepted public-types chain ending at
  `a01c9a81ef5690873c802d9832c672ec77c6a474`;
- registered metadata/runtime plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_SEMANTICS_RUNTIME_EDIT_PLAN.md`,
  SHA-256
  `CF9A48262296CB5AA59B7DB973B451F06F406DA6E031C121B120E12C5C544780`;
- Boss-accepted metadata/runtime source commit and exact base in section 2.

Any change to the three public call signatures, protocol version, option/report
meaning, diagnostic code named by the frozen contract, provider call shape,
format/suffix mapping, source-ownership rule, or merge order is a public
contract change. Stop and report `PUBLIC CONTRACT CHANGE` / `PLAN DEVIATION`.

## 2. Repository, exact base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileIO
remote identity:   https://github.com/audunarn/ANYfileIO.git
accepted base:     1f0b5780df7f025fc786fd3db2cba9da2104fb5c
base tree:         beac80083f7df78718e1fa6f26b60b8f24633bf2
sole base parent:  a01c9a81ef5690873c802d9832c672ec77c6a474
source branch:     codex/anyfileio-semantics-runtime
new branch:        codex/anyfileio-cad-operations
branch upstream:   none (do not configure a Git tracking upstream)
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations
```

At plan creation the proposed branch and worktree path are absent, and the
source worktree is clean with no upstream. Create the branch/worktree only
after Boss registration, directly from the exact base, with no fetch, pull,
merge, rebase, or preparatory commit. Every implementation path below resolves
beneath the registered isolated worktree. Equivalent paths beneath
`C:\Github\ANYfileIO`, the contract worktree, the CAD-types worktree, and the
semantics-runtime worktree are read-only comparison paths, not edit targets.

Produce one coherent implementation commit whose direct and sole parent is
exactly `1f0b5780df7f025fc786fd3db2cba9da2104fb5c`. Proposed subject:

```text
feat: orchestrate core CAD operations
```

No fixup, generated, merge, qualification, or precursor commit is permitted.
Before branch/worktree creation and again before commit, verify the full
base/tree/parent, clean status, absent upstream, protected ancestry/digests,
starting blobs, and exact path ownership. Drift freezes work.

## 3. Protected ancestry and accepted state

Frozen ancestry:

```text
Forseti M2          0d2c7f8ef1b17f42f667d6183125e51cb650a70d
contract freeze    5f605d0bcd63de9e45230588abf7f8b211a23b20
CAD public types   085e92c5ff144fb0f9f96db4afc68c4d2dc7f099
CAD correction     a01c9a81ef5690873c802d9832c672ec77c6a474
semantics runtime  1f0b5780df7f025fc786fd3db2cba9da2104fb5c
```

Protected evidence:

- M2 parent-to-commit binary patch over `README.md`, `pyproject.toml`, and
  `tests/test_packaging.py`: 3,380 bytes, 15 insertions / 7 deletions,
  SHA-256
  `4B2763FC72F0F1FA53E808E28E3D6DEBE0973DD6DE0B2D50E0C0F6A6FA229068`;
- contract parent-to-commit binary patch over its exact three documents:
  107,797 bytes, 2,172 added lines, SHA-256
  `39139AB6DCD18787232F0ECBA0F9535B9D2C0EDC8AE8CAC07CF50DD90222047E`;
- combined accepted CAD-types patch from `5f605d0...` through `a01c9a81...`
  over its exact seven paths: 99,478 bytes, 2,425 insertions / 5 deletions,
  SHA-256
  `AFAADC1DFEE6B8717DF596ABA36D6709999110517858CF59A3827568FBD89B94`;
- accepted metadata/runtime patch from `a01c9a81...` through `1f0b5780...`
  over its exact thirteen paths: 42,266 raw binary-diff bytes, 644 insertions /
  83 deletions, SHA-256
  `8C18B315CF3745CA18EDC96D43E32983EEFC922E2F64D5BA58E9150C4D4EF7B6`.
  Reproduce with this exact argument vector and hash the raw stdout bytes; do
  not hash terminal-rendered or CRLF-transcoded output:

  ```text
  git diff --binary a01c9a81ef5690873c802d9832c672ec77c6a474 1f0b5780df7f025fc786fd3db2cba9da2104fb5c -- .github/workflows/publish.yml CHANGELOG.md README.md pyproject.toml run_gui.py src/anyfileio/__init__.py src/anyfileio/_semantic_dependencies.py src/anyfileio/calculix/deck.py src/anyfileio/diagnostics.py src/anyfileio/sesam/semantics.py tests/test_layering.py tests/test_packaging.py tests/test_semantics_extra.py
  ```

Frozen contract documents at the base:

| Path | Git blob | SHA-256 |
| --- | --- | --- |
| `docs/CAD_BACKEND_CONTRACT.md` | `f4ecd214cdd2ae448c91a6e8d46d4101b34a4ddb` | `723FE2EF33E582F3AE9A3A60A77AB1DCD709F4C838D27F0E1C8B73134D9FF374` |
| `docs/ANYGEOMETRY_0_2_ADAPTER.md` | `f828cc4a0ab6c1c93cb569c45af5191dfd723e34` | `9E79744135C83FC10DE4C8EB231CC57B29B79AB967DF7C5468F19168448D1AA8` |
| `DEPENDENCY_MATRIX.md` | `ed53d6d8fc5d315c3c5e31139032fea4353c8e60` | `BB2E28A41BD2DB773E1A501113B54E9936F0708C34F21C452C2235C48091D2E3` |

Accepted CAD implementation files consumed but excluded from edits:

| Path | Git blob |
| --- | --- |
| `src/anyfileio/cad.py` | `baa7a5fde9db1da0951def9ff0abe1cd46626c7d` |
| `src/anyfileio/cad_backend.py` | `fca05afc5f2daa7d4cdd5677d774628e67de7980` |
| `tests/test_cad_contract.py` | `d9420623a2fcaf9ed61d47a44ca13587cf9fb31c` |

The operations slice may consume private core integration functions
`cad._bind_tessellation`, `CadDocument._backend_state_for`,
`CadDocument._borrow_source_snapshot`, and `cad_backend._load_backend`. It does
not alter or duplicate their record validation, discovery cache, or provider
SPI.

## 4. Exact edit ownership

The exact edit set is seven repository-relative paths. The corresponding
absolute edit targets all begin
`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\`.
No glob ownership exists.

### 4.1 New source path

1. `src/anyfileio/cad_operations.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\src\anyfileio\cad_operations.py`.

   Own the complete new module implementing only the operation contract in
   section 5. No artifact ZIP/NPY codec or provider implementation enters it.

### 4.2 Existing source paths and transferred hunks

2. `src/anyfileio/__init__.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\src\anyfileio\__init__.py`.
   Exact starting blob
   `8c084be71b049bf9904df029d5c5cb37fffc3e18`.

   Add one import of `read_cad`, `tessellate_cad`, and `write_cad` immediately
   after the accepted CAD backend/formats import area, and add exactly those
   three strings to `__all__`. Do not alter `__version__`, semantic imports,
   `SemanticDependencyError`, existing CAD types/status exports, or any other
   facade symbol/order except the necessary deterministic placement.

3. `src/anyfileio/formats.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\src\anyfileio\formats.py`.
   Exact starting blob
   `5e16e0ae1a38b587653d9eb224c4f81ae64c36d3`.

   Transfer only these hunks:

   - `supported_suffixes()` returns the sorted keys of the already-frozen
     constant-time `_SUFFIX_INDEX`, because `read()` now recognizes the five
     core-known CAD suffixes as well as the five built-ins;
   - `read()` retains the existing `READERS` path byte-for-byte in behavior;
     when no built-in exists but `_SUFFIX_INDEX` resolves a CAD descriptor, it
     performs a function-local import of `cad_operations.read_cad` and calls it
     with `target` and the exact caller options;
   - unknown suffixes retain `FileFormatError`/`FEM010` and name the complete
     supported set.

   Do not change any descriptor, `READERS`, reader, `known_formats`,
   `available_formats`, discovery/cache behavior, or `describe()` semantics.
   Built-in reads never scan or load a CAD provider.

### 4.3 New and existing tests

4. `tests/test_cad_operations.py` (new, whole file)

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\tests\test_cad_operations.py`.

5. `tests/test_backends.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\tests\test_backends.py`.
   Exact starting blob
   `fca837d2a87d6da52450727dd113f9b7bbd21e04`.

   Replace only
   `test_supported_suffixes_remains_the_five_builtin_suffixes` with
   `test_supported_suffixes_include_core_known_cad_suffixes`, asserting the
   exact sorted ten-suffix tuple. Preserve all entry-point/provider predicates.

6. `tests/test_formats_and_cli.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\tests\test_formats_and_cli.py`.
   Exact starting blob
   `83e3fb8ae97aca76b09be792e7f0e3ec527a4e3a`.

   Transfer only:

   - update `test_every_suffix_is_described_and_dispatched` to assert the exact
     sorted ten-suffix tuple while retaining the real FEM/FRD behavior checks;
   - add `test_cad_suffix_dispatches_to_read_cad`, monkeypatching the operation
     at its defining module and proving the `Path` and exact options are passed;
   - strengthen the existing unknown-suffix assertion only as needed to prove
     the complete supported list;
   - rename `test_formats_lists_what_the_tool_reads` to
     `test_formats_lists_builtin_cli_readers_only` and assert the unchanged five
     `READERS` suffixes directly, rather than equating that deliberately narrow
     CLI command with the expanded programmatic `supported_suffixes()`.

   No new CAD CLI command, inspect behavior, GUI path, fixture, or broad rewrite.

7. `tests/test_layering.py`

   Absolute target:
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-operations\tests\test_layering.py`.
   Exact starting blob
   `b3c7eabea504649ff79af1ce6f4052d1629da3e2`.

   Add only `cad_operations.py` to `CAD_NEUTRAL_MODULES`. Preserve the
   NumPy-only unconditional-import rule, exact semantics loader exceptions, and
   forbidden optional package set (`OCP`, `cadquery`, `anyfileio_occt`,
   `anygeometry`).

No test may import the real optional provider, invoke OCP, or use network.

## 5. Exact operation contract

### 5.1 Public signatures and dependency boundary

`src/anyfileio/cad_operations.py` exports exactly:

```python
def read_cad(
    source: PathLike,
    *,
    options: CadReadOptions = CadReadOptions(),
    tessellation_options: CadTessellationOptions | None = None,
    cancellation: CancellationCheck = None,
    backend_id: str = "occt",
) -> CadDocument: ...

def tessellate_cad(
    document: CadDocument,
    *,
    options: CadTessellationOptions = CadTessellationOptions(),
    cancellation: CancellationCheck = None,
) -> CadTessellationResult: ...

def write_cad(
    document: CadDocument,
    destination: PathLike,
    *,
    options: CadWriteOptions,
    cancellation: CancellationCheck = None,
) -> CadAssetWriteReport: ...
```

The module imports only stdlib, accepted NumPy-only core records/helpers, and
the metadata discovery module; it never imports OCP, CadQuery, `anyfileio_occt`,
ANYgeometry, ANYmesher, or ANYmaterial. Provider load occurs only through
`cad_backend._load_backend()` for read, tessellation, or translation. Preserve
does not enumerate or load a provider.

Only frozen codes are promised: `cad.operation.cancelled`,
`cad.cancellation_check.failed`, `cad.source.changed`,
`cad.source.unavailable`, `cad.source.reopen_mismatch`,
`cad.preserve.healed_source`, and `cad.write.format_suffix_mismatch`, plus the
accepted backend/session/tessellation codes from `cad.py`/`cad_backend.py`.
Other invalid values use the existing `CadValidationError` default code and
other orchestration failures use the existing `CadOperationError` default code;
this slice invents no additional stable public code vocabulary.

### 5.2 Cancellation and failure preservation

A private check helper:

- does nothing for `None` or false;
- maps a true callback result to `CadOperationCancelled` with
  `cad.operation.cancelled`;
- wraps an exception raised by the callback as `CadOperationError` with
  `cad.cancellation_check.failed` and retains the cause.

The core checks before an operation and at Python-controlled boundaries: after
source copy/before provider read, before/after provider tessellation or
translation, and before atomic replace. It does not claim interruption inside
a running native call. A provider-raised `CadError` is preserved. An unrelated
provider exception is wrapped once with its cause; no retry/tuning occurs.

### 5.3 Source format, name, and owned snapshot

Infer only STEP (`.step`, `.stp`), IGES (`.iges`, `.igs`), or BREP (`.brep`)
from the frozen suffix index. Direct `read_cad` rejects other suffixes and a
missing/non-regular source before provider load or source copy: missing raises
`FileNotFoundError`; an existing non-regular path raises the existing
`CadValidationError` default. This initial stat is not a content read and
`_snapshot_source` repeats the authoritative opened-file checks. `source_name`
is Unicode-NFC normalization of
`Path(source).name`, is non-empty, and contains no separator.

Implement exact private helper:

```python
def _snapshot_source(
    path: PathLike,
    *,
    expected_sha256: str | None = None,
) -> pathlib.Path: ...
```

It accepts only an existing regular file and validates any supplied expected
hash as 64 lower-case hexadecimal before copying. It creates one unique
task-owned spool file retaining the source CAD suffix, hashes bytes while
copying, and compares exact opened-handle/path stat fields `st_dev`, `st_ino`,
`st_size`, `st_mtime_ns`, and `st_ctime_ns` before and after; access time is
deliberately excluded. Detected drift or a well-formed expected-hash
disagreement removes only that spool and raises `cad.source.changed`. The caller
path is never adopted, renamed, written, or deleted. A private companion may
return the already-computed digest to
`read_cad`; the exact public/private helper above still returns only the owned
path. The spool is logically immutable: provider access is read-only by
contract, and every later byte-authority use rechecks its SHA-256. Do not set a
filesystem read-only bit that would defeat cross-platform `release_source()`.

### 5.4 Read orchestration

Normalize/validate option record types and mode rules before provider load or
source copy. `manifest_only` rejects non-`None` tessellation options.
`preview` converts `None` to default `CadTessellationOptions()`. `live` keeps
`None` as no eager tessellation and accepts an explicit record.

Load the requested backend id (protocol 1 only), then require the source format
in `read_formats`, the mode in `import_modes`, and tessellation capability when
meshes are requested, before source data access. Pass the exact owned path,
computed SHA-256, normalized basename, normalized records, and cancellation to
the frozen provider `read` signature.

Validate the returned value before publication:

- it is `CadDocument` and its manifest source SHA/name/format, normalized read
  options, backend id/version/compatibility, and recomputed imported
  `document_id` match the request/backend;
- preview/live returns have a known normalized source unit and exact metre
  scale; only `manifest_only` may retain protocol `unknown` units;
- the core spool is still the same regular-file identity and its bytes still
  hash to the computed source SHA after provider return;
- preview/live tessellation exactly follows the requested/default option and
  one-mesh-per-prototype invariants already enforced by the core factory;
- `manifest_only` and `preview` are closed/session-free when returned;
- `live` has an open session owned by the current calling thread;
- any attached source path is exactly the core-created spool, never merely a
  same-content or provider-chosen path.

For `retain_source=True`, the returned document must own exactly that spool.
For `retain_source=False`, release an attached exact spool or unlink the
unattached spool before return, and require `source_available=False`. A wrong
attached path fails closed and is never deleted. On any read failure, close
only newly returned provider state on its owner thread when available, remove
only the core spool it owns, and preserve the caller source.

### 5.5 Tessellation and transient reopen

Require a `CadDocument`, normalized `CadTessellationOptions`, matching backend,
known source unit, declared tessellation/read/live capability, and a cancellation
check before data access.

When `document._backend_state_for(manifest.backend_id)` returns live state, call
the provider's exact `tessellate(document, ...)` signature. Otherwise enter
`document._borrow_source_snapshot()` and verify the borrowed bytes still match
`manifest.source_sha256`. Reopen through provider `read` using normalized
`CadReadOptions(mode="live", retain_source=False,` original source-unit
override and original `heal`) and no eager tessellation. The transient document
must not adopt the borrowed path.

Require the transient manifest to match the caller's source SHA/name/format,
imported document id, units/scales, backend id/version/compatibility,
binding/OCCT producer versions, prototypes, occurrences, shapes, topology
counts, and assembly identity. A differing mode/retain-source field is the only
intentional read-option difference. Any mismatch closes the transient session
and raises `cad.source.reopen_mismatch`. Execute the requested operation against
the transient live document, require its owner thread to be the current thread,
close it in `finally`, and recheck the borrowed source identity and SHA before
exiting the borrow.

In both paths the provider returns only an unlabelled
`tuple[CadPrototypeMesh, ...]`. Bind it against the original caller manifest and
requested options only through `cad._bind_tessellation`. Return a new
`CadTessellationResult`; never mutate the caller document or its published
meshes.

### 5.6 Write target and provider-free preserve

Resolve `target_format=None` to `document.manifest.source_format`. The final
destination must have a core-known CAD suffix mapping exactly to the resolved
format. Reject missing/unknown/mismatched suffixes with
`cad.write.format_suffix_mismatch` before temporary creation. The destination
parent must already be a directory; do not create directories.

Preserve mode:

- rejects a healed originating read with `cad.preserve.healed_source`;
- rejects write healing, format change, or unit change before temporary
  creation;
- does not call `backend_status`, `_load_backend`, or any provider method;
- borrows the retained spool, rechecks its SHA-256 against the manifest, copies
  its exact bytes into the unique temporary, flushes/fsyncs it, and verifies the
  output hash before replace;
- creates `CadAssetWriteReport` with source/target format and unit equal,
  original backend id/version/compatibility, `binding_version=None`,
  `occt_version=None`, equal manifest topology counts, no healing/change,
  `byte_identical=True`, `unsupported_entities=()`, no approximation/loss, no
  operation diagnostics, and `execution_mode="preserve_copy"`.

For deterministic report meaning, `exported_entities` in provider-free
preserve is the sorted unique union of every manifest prototype,
occurrence, and shape `cad_ref`; source-reader diagnostics remain on the
manifest and are not relabelled as preserve-operation diagnostics. This is an
operations-level interpretation submitted for Boss registration; a different
meaning requires contract review before edits.

### 5.7 Translation, report binding, and atomic replace

For translation, require a known normalized source unit; an explicit target
unit cannot repair an unknown source scale. Resolve `target_length_unit=None`
to that known source unit. Require provider `translate`, target write-format,
source read-format, and live-reopen capabilities before temporary creation.
Protocol 1 has no separate healing capability bit; the normalized `heal`
option is passed to the provider and its reported outcome is validated rather
than inferred.

Use the existing live document when open, otherwise the exact transient-reopen
flow in section 5.5. Create one unique regular-file temporary sibling in the
destination directory whose final suffix equals the destination CAD suffix,
and record its `st_dev`/`st_ino` identity before provider use. Call only the
provider `translate` method; the provider never sees or replaces the final path.

Validate before replace that:

- the result is `CadAssetWriteReport` with matching source document id, source
  and resolved target formats/units, backend id/version/compatibility,
  provider translation execution mode, source topology counts, and requested
  healing policy; `healing_applied` may be true only when `options.heal=True`
  and is otherwise the provider's truthful observed outcome;
- every exported/unsupported/diagnostic entity belongs to the caller document
  and to a known manifest entity reference;
- the temporary remains the same non-symlink regular-file identity created by
  the core and its freshly computed SHA-256 is exactly
  `report.output_sha256`;
- binding/OCCT versions match the validated live/transient producer.

Open the completed temporary for flush/fsync, run the final cancellation check,
then perform exactly one `os.replace(temporary, destination)`. No validation or
fallible post-processing follows a successful replace. On cancellation,
provider failure, invalid report/hash, or replace failure, remove only this
operation's temporary if it remains and leave any pre-existing destination
unchanged. Never delete/rename the caller source or another task's file.

## 6. Exact focused tests and definition of done

`tests/test_cad_operations.py` owns exact nodes:

- `test_public_operation_signatures_and_facade_exports`
- `test_snapshot_requires_regular_file_and_preserves_caller_bytes`
- `test_snapshot_hashes_exact_bytes_and_normalizes_source_name`
- `test_snapshot_detects_expected_hash_or_source_drift`
- `test_cancellation_true_and_callback_failure_use_frozen_codes`
- `test_manifest_only_rejects_tessellation_before_provider_or_copy`
- `test_read_checks_format_mode_and_capability_before_source_access`
- `test_read_passes_exact_provider_call_and_retains_owned_snapshot`
- `test_read_preview_defaults_tessellation_and_closes_session`
- `test_read_unretained_and_provider_failure_remove_only_owned_spool`
- `test_read_rejects_manifest_or_attached_source_mismatch`
- `test_live_tessellation_core_binds_provider_meshes`
- `test_closed_tessellation_reopens_retained_source_transiently`
- `test_tessellation_rejects_unavailable_or_mismatched_reopen`
- `test_preserve_is_provider_free_atomic_and_byte_identical`
- `test_preserve_rejects_heal_format_unit_or_suffix_before_temporary`
- `test_translation_uses_live_state_and_atomic_same_suffix_temporary`
- `test_translation_reopens_retained_source_without_adopting_it`
- `test_translation_rejects_report_entity_or_output_hash_mismatch`
- `test_write_failure_or_cancellation_preserves_existing_destination`

Exact affected test command, proposed LIGHT/non-lease subject to Boss
classification at registration:

```text
python -m pytest -q tests/test_cad_operations.py tests/test_backends.py::test_supported_suffixes_include_core_known_cad_suffixes tests/test_backends.py::test_builtin_dispatch_never_scans_or_loads_plugins tests/test_backends.py::test_public_import_and_metadata_queries_load_no_optional_cad_modules tests/test_formats_and_cli.py::test_every_suffix_is_described_and_dispatched tests/test_formats_and_cli.py::test_cad_suffix_dispatches_to_read_cad tests/test_formats_and_cli.py::test_an_unrecognized_suffix_names_the_ones_that_work tests/test_formats_and_cli.py::test_formats_lists_builtin_cli_readers_only tests/test_layering.py::test_third_party_imports_are_declared tests/test_layering.py::test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages
```

Run it once only after source review and explicit Boss test authority. Preserve
the first result; do not broaden, tune, install, or retry without a new ruling.
All provider behavior is exercised with local fakes and monkeypatches. No real
entry point, OCP, network, build, resolver, or native work occurs.

Always-allowed static completion proof after registered edits:

- `git diff --check`;
- AST parse of all seven owned Python files;
- exact changed-path equality to the seven paths in section 4;
- base ancestry/direct-parent and absent-upstream checks;
- protected M2/contract/CAD/runtime diff and blob reproduction;
- source scan proving no forbidden optional imports and no artifact/provider
  implementation.

Definition of done:

- exact three public signatures and facade exports match the contract;
- source snapshot ownership, hash/drift checks, mode lifecycle, capability
  checks, live/reopen operation paths, core provenance binding, provider-free
  preserve, translation validation, and atomic replacement are covered;
- `supported_suffixes` and `read` truthfully include the five CAD suffixes while
  every built-in reader remains provider-free;
- the exact seven paths are the complete diff and one direct-child commit;
- no claim is made about a real provider, artifact codec, installed wheel,
  resolver, performance, consumer, or publication.

## 7. Explicit exclusions and protected files

No edit, formatting rewrite, generated file, or transferred hunk in:

- `src/anyfileio/cad.py`, `src/anyfileio/cad_backend.py`,
  `tests/test_cad_contract.py`, or the three frozen contract documents;
- `src/anyfileio/cad_artifact.py` or any preview cache/ZIP/NPY codec path;
- `pyproject.toml`, `README.md`, `CHANGELOG.md`, `run_gui.py`,
  `.github/workflows/**`, `tests/test_packaging.py`,
  `tests/test_semantics_extra.py`, semantic dependency loader, SESAM, or
  CalculiX runtime paths;
- `src/anyfileio/__main__.py` or GUI/CLI command implementation;
- ANYfileio-occt, ANYgeometry, ANYmesh, ANYmaterial, ANYfem, ANYsolver,
  ANYstructure, ANYtk3D, ANYopenSoft governance other than this external plan,
  or any other repository;
- remotes, tags, releases, indexes, wheels, environments, qualification
  reports, benchmarks, or publication systems.

The accepted metadata/runtime changes in shared `src/anyfileio/__init__.py` and
`tests/test_layering.py` are protected except for the exact additive hunks in
section 4. The M2 `README.md`/repository identity, NumPy-only base,
`[semantics]` ranges, version 0.2.0, lazy dependency diagnostics, workflow
dependency gates, and all accepted CAD type/discovery behavior remain exact.

## 8. Risks, failure handling, rollback, and lease boundary

Primary risks and controls:

- **Caller-source destruction:** snapshot first; transfer/delete authority only
  for the exact core-created path; never adopt a provider/caller path.
- **Wrong-document meshes or reports:** bind against the original manifest and
  validate every source/producer/entity field before publication/replacement.
- **Stale retained bytes:** hash before every preserve/reopen authority use and
  fail closed.
- **Temporary/output corruption:** same-directory unique suffix-preserving
  temporary, hash/report validation, flush/fsync, one final replace, no
  post-replace failure point.
- **Optional dependency leakage:** function-local CAD dispatch and AST/subprocess
  layering predicates; built-ins never enumerate/load providers.
- **Thread-affine leak:** close only newly created transient sessions on their
  owner thread and preserve wrong-thread failure for owner cleanup.
- **Contract drift:** exact protected blobs/digests and one-owner path inventory.

Preserve the first failure, its owned temporary/spool state, and causal
exception where safe. Do not retry, tune, broaden, delete another task's data,
reset hard, rewrite history, or discard unrelated work. Rollback is a normal
revert of the one coherent commit after Boss/owner review.

The exact focused fake/static test command may run only if the Boss classifies
it LIGHT. Full/broad pytest, package builds, wheel/sdist/twine, clean installs,
resolver environments, real provider/OCP calls, native builds, import timing,
RSS/size measurement, large-file copy/stress, profiling, scaling, benchmarks,
and qualification require a fresh exact `PERF LEASE REQUEST` and explicit
`PERF LEASE GRANTED`. No such work is requested by this plan.

## 9. Commit, handoff, and frozen merge order

Frozen linear order:

```text
M2 0d2c7f8...
  -> contract 5f605d0...
  -> CAD public types 085e92c... + correction a01c9a81...
  -> semantics runtime 1f0b5780...
  -> this exact CAD core operations/orchestration commit
  -> separately registered anyfileio.cad_artifact codec commit
  -> accepted combined lightweight-core API/metadata handoff
  -> separately registered ANYfileio-occt provider slices
  -> owner-gated ANYfem V7/UI and later consumers
```

This agent does not merge, cherry-pick, rebase, push, publish, or create a PR.
The artifact plan must name the accepted full operations commit as its exact
base unless the Boss registers a different non-overlapping integration order.
Provider code consumes only the accepted combined lightweight-core handoff.

Completion evidence reports:

- this plan path/hash/bytes/lines and editing identity;
- branch/worktree/upstream and exact base/tree/parent;
- implementation commit/tree/sole parent/subject;
- exact seven-path diff/stat/final blobs;
- static checks and the first focused test result if authorized;
- protected M2/contract/CAD/runtime digest/blob reproduction;
- spool/temporary cleanup behavior and clean worktree;
- exclusions, deferred qualification, and next registered owner.

Any need to edit an eighth path, alter `cad.py`/`cad_backend.py`, add a stable
code or dependency, change a public call/provider SPI, relax validation, run a
real provider/build/resolver, or change merge order stops work and requires a
revised content-addressed plan and Boss registration.
