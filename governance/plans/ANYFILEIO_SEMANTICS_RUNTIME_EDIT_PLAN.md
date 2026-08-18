# ANYfileIO Canonical Metadata and Semantics-Runtime Editing Plan

Status: **registration candidate; this file grants no branch, worktree, edit,
test, build, resolver, commit, merge, push, publication, or performance
authority until the ecosystem Boss registers this exact file and SHA-256**

Owner: CAD pipeline lead (`019ff74a-63c3-7db1-8e6b-dfaa57fed80e`)

Editing agent: one direct child task only, proposed canonical identity
`/root/skuld_anyfileio_semantics_runtime`; no delegated or nested writer. A
different writer identity requires re-registration before any edit.

Date: 2026-08-13 (Europe/Oslo)

## 1. Objective and authoritative inputs

Produce the canonical ANYfileIO 0.2 metadata/runtime transition as one bounded
slice. The installed base becomes NumPy-only. `ANYmesher>=0.2,<0.3` and
`ANYmaterial>=0.1,<0.2` move to the exact `semantics` extra. Package, SESAM,
CalculiX, CLI, GUI, record/document, and accepted CAD-neutral public imports no
longer load either semantic package merely by being imported. The two semantic
operations load the extra lazily, validate both installed distributions before
importing either namespace, and fail with typed, stable diagnostics.

This slice also synchronizes source/package version `0.2.0`, documents the
install boundary, and prepares truthful publication dependency gates. It must
prove a base-only installed-wheel cell and a real `[semantics]` installed-wheel
cell before completion. It does not implement CAD operations, source spooling,
the CAD artifact codec, OCCT, ANYgeometry adaptation, or consumer integration.

Authoritative inputs:

- source plan:
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
- accepted contract-freeze commit
  `5f605d0bcd63de9e45230588abf7f8b211a23b20` and its exact three documents;
- registered public-types/discovery plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_CAD_PUBLIC_TYPES_DISCOVERY_EDIT_PLAN.md`;
  SHA-256
  `C3D0E42184A9926ECBA207075C8F28451DF44144AA17122958AC3034DFA955F0`;
- Boss-accepted public-types/discovery chain and exact base in section 2.

The dependency boundary is a public contract change. Any proposed range,
diagnostic code, import timing, public export, version, or merge-order change
freezes work and is reported as `PUBLIC CONTRACT CHANGE` / `PLAN DEVIATION`.

## 2. Repository, exact base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileIO
remote identity:   https://github.com/audunarn/ANYfileIO.git
accepted base:     a01c9a81ef5690873c802d9832c672ec77c6a474
base tree:         349ff94ff2f62b1eee53fdb0c6c2945ad21c6333
sole base parent:  085e92c5ff144fb0f9f96db4afc68c4d2dc7f099
source branch:     codex/cad-public-types-discovery
new branch:        codex/anyfileio-semantics-runtime
branch upstream:   none (do not configure a Git tracking upstream)
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-semantics-runtime
```

The new branch and worktree do not exist at plan creation. Create them only
after Boss registration, directly from the exact base, with no fetch, pull,
merge, rebase, or preparatory commit. Every implementation path resolves below
the registered isolated worktree. `C:\Github\ANYfileIO`, the contract worktree,
and the public-types/discovery worktree are read-only comparison locations and
are not edit targets for this slice.

The implementation is one coherent commit whose direct and sole parent is
exactly `a01c9a81ef5690873c802d9832c672ec77c6a474`. Qualification reports remain
external/task-owned evidence and are not committed. No fixup, generated,
qualification, merge, or metadata-only precursor commit is permitted.

Immediately before branch/worktree creation and again before commit, verify the
full base/tree/parent, clean status, absent upstream, protected CAD blobs, M2 and
contract ancestry, and exact path ownership. Drift freezes work.

## 3. Protected ancestry and accepted CAD state

Frozen linear ancestry:

```text
Forseti M2        0d2c7f8ef1b17f42f667d6183125e51cb650a70d
contract freeze  5f605d0bcd63de9e45230588abf7f8b211a23b20
CAD types         085e92c5ff144fb0f9f96db4afc68c4d2dc7f099
CAD correction    a01c9a81ef5690873c802d9832c672ec77c6a474
```

Protected evidence:

- M2 parent-to-commit binary patch over `README.md`, `pyproject.toml`, and
  `tests/test_packaging.py`: 3,380 bytes, 15 insertions / 7 deletions,
  SHA-256
  `4B2763FC72F0F1FA53E808E28E3D6DEBE0973DD6DE0B2D50E0C0F6A6FA229068`;
- contract parent-to-commit binary patch over the three frozen documents:
  107,797 bytes, 2,172 added lines, SHA-256
  `39139AB6DCD18787232F0ECBA0F9535B9D2C0EDC8AE8CAC07CF50DD90222047E`;
- combined accepted CAD-types patch from `5f605d0...` through `a01c9a81...`
  over its exact seven paths: 99,478 bytes, 2,425 insertions / 5 deletions,
  SHA-256
  `AFAADC1DFEE6B8717DF596ABA36D6709999110517858CF59A3827568FBD89B94`.

The six accepted CAD-owned paths not shared with this slice remain
byte-identical:

| Path | Accepted Git blob |
| --- | --- |
| `src/anyfileio/cad.py` | `baa7a5fde9db1da0951def9ff0abe1cd46626c7d` |
| `src/anyfileio/cad_backend.py` | `fca05afc5f2daa7d4cdd5677d774628e67de7980` |
| `src/anyfileio/formats.py` | `5e16e0ae1a38b587653d9eb224c4f81ae64c36d3` |
| `tests/test_backends.py` | `fca837d2a87d6da52450727dd113f9b7bbd21e04` |
| `tests/test_cad_contract.py` | `d9420623a2fcaf9ed61d47a44ca13587cf9fb31c` |
| frozen contract documents / matrix | blobs recorded in the registered public-types plan |

Two shared files are transferred only at exact runtime hunks:

- `src/anyfileio/__init__.py` starts at blob
  `f6e944b6803278bed104b5316c7ee005a57799cb`; every accepted CAD import and
  `__all__` entry remains byte-identical;
- `tests/test_layering.py` starts at blob
  `0702f980515a26ec9c6c70699add3c9d8f59e919`; its
  `CAD_NEUTRAL_MODULES`, `CAD_FORBIDDEN_IMPORTS`, and
  `test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages` block
  remains semantically and textually unchanged.

M2 identity protection remains mandatory after the transferred metadata edits:

- preserve the repository/distribution-name comment and exact project URLs in
  `pyproject.toml`;
- preserve the repository-vs-`anyio` identity paragraph and exact
  `C:\Github\ANYfileIO[dev]` development-install line in `README.md`;
- preserve the canonical repository URL test and its explanatory comment in
  `tests/test_packaging.py`.

## 4. Exact owned paths and starting blobs

All paths below resolve beneath
`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-semantics-runtime`.
There are exactly thirteen owned paths.

### 4.1 Existing metadata and documentation

| # | Repository-relative path | Starting blob | Raw SHA-256 | Bytes / lines |
| --- | --- | --- | --- | --- |
| 1 | `pyproject.toml` | `abae003aa442c2d363c35a5ab2ba671561185d0d` | `5B16D30CE8B6EDA400DF8FD7E86BA78B641C302D579754EE4F4D635A6FC1B04C` | 2,555 / 74 |
| 2 | `README.md` | `bd89d71a6e9ba70654f6a1c4e19d3ca0f89ae02e` | `4F0D7CB6E9E9BC12724680F64A076D0CFBC35CAEF0182ACBA27FABC031842AE9` | 6,480 / 152 |
| 3 | `CHANGELOG.md` | `90918231892c4753be0f3171cade0738c8877600` | `892FF7B196CB6EA735C27FECFCF2AA273D5BEB2D60CFB53DEE7EE2D6AAF30786` | 4,907 / 92 |
| 4 | `.github/workflows/publish.yml` | `70bae2b378b4dc248c9275327751788139c013a2` | `DFF898101B91C92C144B87744F7A9BE8280E68CCD7EFA058715F33A84152A0AA` | 2,123 / 73 |

### 4.2 Existing runtime source

| # | Repository-relative path | Starting blob | Raw SHA-256 | Bytes / lines |
| --- | --- | --- | --- | --- |
| 5 | `src/anyfileio/diagnostics.py` | `4ed78f373b0a47f2287c244bb6b13ca70639bb7d` | `08546573427A068C9B64A98A6649B1F1CFC850F0B89AE601179C8ED4AB4CB7F2` | 3,645 / 105 |
| 6 | `src/anyfileio/sesam/semantics.py` | `73892a074b0bedf1daf65843d419c22429bd2466` | `2F9203DD65C2234135B18C7E46959352796F8AA0E2DFD4FFE7A31B0475E20A9B` | 20,306 / 507 |
| 7 | `src/anyfileio/calculix/deck.py` | `307bcd0733d9f7b8ff4f5c85175c3165df67ab7c` | `0A8EC0F05ECB3C70089239222F9ED0869172542C7371B006DC74159AA987711B` | 19,893 / 485 |
| 8 | `src/anyfileio/__init__.py` | `f6e944b6803278bed104b5316c7ee005a57799cb` | `2EFF804907D00D8DC5F868F3D1E3C758EA64C3618F18AA223325A596214FF6D6` | 4,944 / 197 |
| 9 | `run_gui.py` | `80f135f2560e0fda61e74b808ec65a121f5a048f` | `66214F4DD3FA5AFA81ED5472B87C8C4AE7D7B2558496E2C9973E7080EF8986E5` | 1,298 / 37 |

### 4.3 Existing and new tests

| # | Repository-relative path | Starting blob | Raw SHA-256 | Bytes / lines |
| --- | --- | --- | --- | --- |
| 10 | `tests/test_layering.py` | `0702f980515a26ec9c6c70699add3c9d8f59e919` | `12FD84062B1323CEE8E395F01B91FB36C0AA1FBA63B55F58BFB62761AE1364AF` | 4,383 / 114 |
| 11 | `tests/test_packaging.py` | `56335ff7bf0109e8910a27b0da60b874fc730256` | `4EC6684F0C85F1F9A97E8116E20CACDE49119F1EED9A31268C57523E2565F9EE` | 3,446 / 93 |
| 12 | `src/anyfileio/_semantic_dependencies.py` | new; must be absent at base | n/a | n/a |
| 13 | `tests/test_semantics_extra.py` | new; must be absent at base | n/a | n/a |

No glob ownership or implicit generated path exists. The equivalent paths in
the primary checkout or either prior isolated worktree are not edit targets.

## 5. Frozen metadata and runtime contract

### 5.1 Package metadata

`pyproject.toml` changes only these transferred regions:

1. `[project].version` changes exactly `0.1.0 -> 0.2.0`;
2. replace the explanatory dependency comment and dependency array so the base
   is exactly `dependencies = ["numpy>=1.26"]`;
3. insert under `[project.optional-dependencies]` exactly:

   ```toml
   semantics = [
     "ANYmesher>=0.2,<0.3",
     "ANYmaterial>=0.1,<0.2",
   ]
   ```

No name, Python floor, build backend, classifier, script, GUI script, package
discovery, pytest setting, URL, `gui`, or `dev` hunk changes. The transitional
legacy proposal `ANYmesher>=0.1,<0.3` has no source or workflow hunk here and
never counts as CAD/semantic capability.

The publish workflow may change only the sibling dependency-gate wording and
the two requirements passed to `pip download --no-deps`: exact
`ANYmesher>=0.2,<0.3` and `ANYmaterial>=0.1,<0.2`. It must not alter event
triggers, permissions, credentials, build/upload commands, environments, or
dispatch a workflow. This source edit is not publication authority.

### 5.2 Typed semantic dependency failures

`src/anyfileio/diagnostics.py` adds and exports only
`SemanticDependencyError(FileFormatError)`. Every instance has one of these
stable codes and at least one matching error-severity `FemDiagnostic`:

- `SEM001`: one or both required distributions are absent;
- `SEM002`: a distribution version is present but outside its accepted stable
  numeric release family;
- `SEM003`: validated metadata exists but importing the namespace or retrieving
  a required symbol fails.

All three diagnostics include `extra="semantics"` and exact install hint
`pip install "ANYfileio[semantics]"`. `SEM001` lists missing distribution names
in deterministic normalized-name order. `SEM002` identifies distribution,
required range, and observed metadata version. `SEM003` identifies import name,
required symbols, and the causal exception type/message. It never converts a
normal semantic-domain `ValueError` raised after capabilities load into a
dependency failure.

`src/anyfileio/__init__.py` changes only:

1. add `SemanticDependencyError` to the existing diagnostics import;
2. add that name to `__all__` without changing any accepted CAD or FE export;
3. change only `__version__ = "0.1.0"` to `"0.2.0"`.

Every accepted CAD import/export remains byte-identical. No lazy `__getattr__`,
CAD operation, artifact, provider, or geometry export is added.

### 5.3 Sole lazy capability gate

New `src/anyfileio/_semantic_dependencies.py` is private and stdlib-only. It is
the sole runtime owner of semantic distribution discovery and imports.

It freezes these distribution contracts:

| Distribution | Import name | Accepted stable release | Required symbols |
| --- | --- | --- | --- |
| `ANYmesher` | `anymesher` | `>=0.2,<0.3` | `Mesh` |
| `ANYmaterial` | `anymaterial` | `>=0.1,<0.2` | `MaterialSpec`, `elastic_compliance_matrix`, `material_symmetry` |

The private `require_semantics()` performs this exact order:

1. query `importlib.metadata.version` for both distributions before importing
   either namespace;
2. report all missing distributions together as `SEM001`;
3. parse versions without adding `packaging`: only dot-separated non-negative
   integer release components are accepted; pre/dev/post/local/epoch or other
   nonnumeric forms fail `SEM002`; compare zero-padded numeric tuples against
   the exact half-open ranges above;
4. only after both versions pass, import `anymesher` then `anymaterial` and
   retrieve every required symbol; a module or symbol failure is `SEM003`;
5. return one frozen private capability bundle containing the five callables or
   types and cache successful bundles only. Missing, version, import, and symbol
   failures are never cached. A private reset exists only for focused tests.

No module imports ANYgeometry, OCP, CadQuery, a provider, a solver, or a
consumer. Merely importing `anyfileio`, `anyfileio.sesam`,
`anyfileio.sesam.semantics`, `anyfileio.calculix`,
`anyfileio.calculix.deck`, `anyfileio.gui`, the CLI, or the accepted CAD modules
does not query distribution metadata and does not import `anymesher` or
`anymaterial`.

### 5.4 SESAM semantic boundary

`src/anyfileio/sesam/semantics.py` changes only dependency plumbing:

- external `Mesh` and `MaterialSpec` imports become `TYPE_CHECKING`-only;
- add the private capability-gate import and a private mesh default factory;
- class annotations remain source-compatible under postponed evaluation;
- `SesamSemantics(document=...)` without an explicit mesh invokes the lazy gate
  at instance construction, while class/module import remains base-only;
- `read_sesam_semantics` calls `require_semantics()` as its first executable
  operation, before reading or inspecting `source`, and constructs the mesh from
  the returned capability;
- `_material_specs` receives the returned `MaterialSpec` type explicitly;
- no mesh topology, material constants, diagnostics, strict/lenient behavior,
  source parsing, IDs, units, sections, supports, loads, or public signatures
  change.

### 5.5 CalculiX semantic boundary

`src/anyfileio/calculix/deck.py` changes only dependency plumbing:

- external `Mesh` becomes `TYPE_CHECKING`-only and both material helper imports
  are removed from module runtime;
- add the private capability-gate import;
- `write_deck` calls `require_semantics()` before analysis validation,
  `Path(path)`, destination existence checks, directory creation, or output;
- pass the returned material helper callables explicitly into private material
  and section helpers; do not install them in module globals;
- preserve every public signature and all numerical, ordering, refusal,
  overwrite, formatting, report, and file-output behavior after the gate.

Constructing or inspecting `DeckModel`, `DeckSupport`, or `DeckReport` does not
load the extra. The semantic gate is required only when writing a deck.

### 5.6 Checkout launcher and documentation

`run_gui.py` keeps only the repository's own `src` bootstrap. Remove the two
sibling source-root candidates and stale wording that semantic siblings are
required for inspection. It must not add an install, subprocess, resolver, or
network fallback.

`README.md` may change only the install/layer/development/publish-order and
checkout-launcher prose needed to state:

- `pip install ANYfileio` provides NumPy-only records, documents, built-in
  formats, inspector, CLI, and accepted CAD-neutral records/discovery;
- `pip install "ANYfileio[semantics]"` enables SESAM semantic materialization
  and CalculiX deck writing;
- missing/incompatible semantic packages fail with the typed install hint;
- the existing explicit sibling editable installs remain valid development
  setup and the protected `[dev]` line remains exact;
- publication order requires compatible ANYmesher 0.2.x and ANYmaterial 0.1.x
  wheels before semantics qualification, without claiming publication.

`CHANGELOG.md` adds only an Unreleased 0.2.0 transition entry: NumPy-only base,
exact semantics extra, lazy typed failures, base-safe facades, and preservation
of accepted CAD-neutral exports. It makes no release, resolver, performance, or
publication-success claim.

## 6. Exact test ownership and required regressions

### 6.1 `tests/test_layering.py`

The runtime owner may change only the introductory dependency prose, base and
optional semantic allowlist/analyzer helpers, and append focused runtime tests.
Freeze unconditional `ALLOWED_THIRD_PARTY` to exactly `{"numpy"}`. A
context-aware AST check permits `anymesher` / `anymaterial` names only beneath
`if TYPE_CHECKING` in the two semantic modules; runtime acquisition is owned
only by `_semantic_dependencies.py` through `importlib`. No module-level or
function-local direct external import is allowed elsewhere.

Required added/updated nodes:

```text
test_third_party_imports_are_declared
test_base_third_party_allowlist_is_numpy_only
test_semantic_imports_are_type_checking_or_loader_owned
```

Preserve the consumer-direction test and the entire accepted CAD-neutral
constants/test block unchanged.

### 6.2 `tests/test_packaging.py`

Retain the M2 identity and URL assertions. Add exact assertions for:

```text
test_base_dependencies_are_numpy_only
test_semantics_extra_has_exact_family_ranges
test_optional_runtime_imports_are_declared_in_the_matching_extra
test_version_matches_pyproject
test_run_gui_bootstraps_without_semantic_sibling_paths
```

The dependency parser must distinguish base dependencies from extras rather
than flattening them when validating the NumPy-only claim.

### 6.3 New `tests/test_semantics_extra.py`

Use fake metadata/modules/import blockers for failure and caching behavior; do
not access an index, install a package, or import an owner checkout. Required
nodes:

```text
test_base_import_and_facades_do_not_load_semantic_packages
test_semantic_record_types_can_be_defined_without_the_extra
test_missing_distributions_raise_sem001_before_any_semantic_import
test_incompatible_or_nonrelease_versions_raise_sem002_before_import
test_module_or_symbol_failure_raises_sem003
test_successes_are_cached_and_failures_are_not
test_read_semantics_fails_before_reading_the_source
test_write_deck_fails_before_inspecting_or_creating_destination
test_cli_summary_reports_the_typed_missing_extra
test_diagnostics_have_exact_codes_context_and_install_hint
```

Subprocess/base-import guards block qualified prefixes `anymesher.`,
`anymaterial.`, and their indirect `anygeometry.` imports while allowing literal
distribution-name strings and metadata. They also prove accepted CAD exports
remain present and that `OCP`, `cadquery`, and `anyfileio_occt` remain unloaded.

## 7. Definition of done

- Diff paths are exactly the thirteen paths in section 4: eleven bounded
  existing-file modifications and two new files.
- One direct-child implementation commit from the exact accepted base.
- Source and wheel metadata report version `0.2.0` consistently.
- Base dependencies contain exactly `numpy>=1.26`; semantic requirements occur
  only in the exact `semantics` extra.
- Importing the base package, format facades, GUI module, CLI module, and CAD
  public records/status with neither semantic distribution installed succeeds
  and loads neither semantic namespace.
- Semantic entry points validate both distribution versions before import,
  lazy-load once on success, and fail `SEM001` / `SEM002` / `SEM003` with exact
  deterministic diagnostics and no destination/source side effect.
- Existing SESAM semantic output and CalculiX deck output pass focused success
  regressions in the accepted real-wheel semantics environment.
- The base-only and `[semantics]` clean installed-wheel cells in section 8 both
  pass on their first authorized runs; wheel METADATA/RECORD and import origins
  are recorded.
- Accepted CAD files, exports, contract documents, M2 identity semantics, and
  built-in record/document behavior remain protected.
- No transitional legacy range, operations, artifact, provider, consumer,
  resolver-source fallback, network fallback, publish, or performance claim is
  introduced.

## 8. Verification and resolver cells

### 8.1 Static and focused source checks

Always-allowed read-only/static checks after editing:

```text
git status --short --branch
git diff --check
git diff --name-only a01c9a81ef5690873c802d9832c672ec77c6a474 --
git rev-parse HEAD^
AST inspection limited to the thirteen owned paths
exact blob/diff checks for protected CAD and contract paths
exact hunk review for __init__.py, test_layering.py, and M2 identity lines
```

Proposed focused source command (run once only after the Boss classifies this
exact command LIGHT/non-lease or grants a lease):

```text
python -m pytest -q tests/test_layering.py tests/test_packaging.py tests/test_semantics_extra.py
```

It uses fakes/blockers, performs no install/network/native work, and preserves
its first outcome. No retry, node change, or broader suite follows without
separate authority.

### 8.2 Qualification inputs

Installed-wheel qualification is blocked until all inputs are named by exact
path, filename, SHA-256, source commit, distribution name, and version:

- the task-built `anyfileio-0.2.0-py3-none-any.whl` from the final runtime
  implementation commit;
- an accepted ANYmesher 0.2.x owner wheel/commit satisfying `>=0.2,<0.3`;
- an accepted ANYmaterial 0.1.x owner wheel/commit satisfying `>=0.1,<0.2`;
- platform-compatible NumPy and build/test tooling artifacts or an explicitly
  authorized index strategy.

Dirty checkouts, source-root injection, editable installs, a bare committed
ancestor, or the transitional 0.1 mesher evidence do not satisfy this gate.

Before running, submit one exact `PERF LEASE REQUEST` naming the finalized
commands, commit, wheelhouse and hashes, task-owned output/venv paths, resources
(no GPU; at most 4 CPU, 8 GiB RAM, and 5 GiB task-owned disk), and ETA 15-25
minutes. Wait for exact `PERF LEASE GRANTED`; preserve first outcomes and send
`PERF LEASE RELEASED` with outcome and process state immediately after the
bounded run. Network/index access is separate authority from the lease.

### 8.3 Base-only installed-wheel cell

In a clean task-owned virtual environment:

1. install the exact ANYfileIO wheel with binary-only resolution under the
   accepted wheelhouse/index strategy, without the `semantics` extra;
2. record `pip freeze`, `pip check`, distributions, versions, wheel hashes,
   METADATA, RECORD, and import origins;
3. prove only NumPy is an ANYfileIO runtime dependency and neither `ANYmesher`
   nor `ANYmaterial` is installed;
4. under an import blocker for `anymesher`, `anymaterial`, `anygeometry`, OCP,
   CadQuery, and `anyfileio_occt`, import `anyfileio`, SESAM/CalculiX facades,
   GUI and CLI modules, CAD records/status, and known-format metadata;
5. run the focused base-only/import-isolation tests from the installed wheel;
6. invoke one SESAM semantic read and one deck write against task-owned sentinels
   and require typed `SEM001` before source read, destination inspection, or
   output creation.

Any sdist fallback, undeclared semantic distribution, checkout-origin module,
or missing CAD export fails the cell.

### 8.4 `[semantics]` installed-wheel cell

In a separate clean task-owned virtual environment:

1. install exact `ANYfileio[semantics]==0.2.0` from the accepted real wheel set
   with binary-only resolution;
2. record and verify exact distribution versions/hashes/origins and `pip check`;
3. prove metadata selects ANYmesher 0.2.x and ANYmaterial 0.1.x, never the
   transitional 0.1 mesher as capability;
4. run installed-wheel lazy-load/cache tests plus unchanged
   `tests/test_sesam.py::test_semantics_resolves_a_neutral_mesh_and_records` and
   `tests/test_calculix.py::test_writing_a_plate_deck_produces_readable_calculix`;
5. prove semantic imports occur only on those semantic operations and that CAD
   discovery remains OCP/provider-free.

An incompatible, source-checkout, editable, unhashed, or sdist-derived semantic
package fails the cell. No retry/tuning is implied.

### 8.5 Explicitly separate qualification/publication work

These remain lease-gated and unauthorized until their exact later request:

- `python -m build`, wheel/sdist/twine/RECORD checks, and clean virtualenvs;
- pip resolution/install/download or any network/index access;
- the two cells above, the full repository suite, cross-repository suites, or a
  Python/platform matrix;
- timings, RSS/size, profilers, stress/scaling, benchmarks, and large fixtures.

Tagging, pushing, opening a PR, dispatching `publish.yml`, uploading to TestPyPI
or PyPI, or calling 0.2.0 released requires a later explicit Boss publication
gate after both cells and the broader release evidence. This plan grants none.

## 9. Hard exclusions

Every path not listed in section 4 is excluded, including explicitly:

```text
src/anyfileio/cad.py
src/anyfileio/cad_backend.py
src/anyfileio/formats.py
src/anyfileio/cad_artifact.py
src/anyfileio/__main__.py
src/anyfileio/gui.py
src/anyfileio/sesam/__init__.py
src/anyfileio/calculix/__init__.py
all SESAM/CalculiX parsing, document, exporter, result, and numerical hunks
tests/test_cad_contract.py
tests/test_backends.py
tests/test_formats_and_cli.py
tests/test_sesam.py
tests/test_calculix.py
tests/test_gui.py
.github/workflows/ci.yml
docs/** and DEPENDENCY_MATRIX.md
MANIFEST.in, MIGRATION.md, LICENSE
benchmarks/**, fixtures/**, reports/**, dist/**, generated resolver artifacts
all paths in ANYfileio-occt, ANYgeometry, ANYmesh, ANYmaterial, ANYfem,
ANYsolver, ANYstructure, ANYtk3D, and ANYopenSoft outside this plan file
```

No `read_cad`, `tessellate_cad`, `write_cad`, `_snapshot_source`, source spool,
atomic CAD output, CAD suffix dispatch, preview artifact, OCCT entry point,
geometry mapping, project persistence, UI, solver/mesher change, or consumer
dependency hunk is implied.

The historical `ANYmesher>=0.1,<0.3` broadening remains a separate evidence-only
owner proposal. It cannot merge alone into the 0.2 CAD line, cannot appear in
this branch, cannot satisfy the semantic gate, and cannot weaken `SEM002`.

## 10. Risks, failure preservation, and rollback

- **Facade still loads semantics accidentally:** keep external imports behind
  `TYPE_CHECKING`, centralize runtime imports in one private gate, and test all
  public facades under blockers.
- **Metadata passes but namespace is incompatible:** validate required symbols
  after exact version checks and fail `SEM003` without caching failure.
- **Version parsing silently accepts prereleases:** accept only strict numeric
  release components and test boundary/nonrelease strings.
- **A dependency failure creates/reads user paths:** call the gate first in both
  semantic operations and test with sentinels that make any access visible.
- **Shared CAD/M2 hunk is overwritten:** exact hunk and blob checks freeze the
  edit; any overlap beyond the transferred lines is a plan deviation.
- **Source-root tests masquerade as wheel evidence:** source tests use fakes;
  qualification accepts only recorded clean real-wheel origins and hashes.
- **Publication wording outruns evidence:** changelog remains Unreleased and no
  workflow/tag/upload is authorized.

Preserve every first failure and its environment/process state. Do not tune,
retry, broaden, or replace a failed resolver cell without Boss review. Rollback
is a normal revert of the one coherent implementation commit after owner/Boss
review; never rewrite history, reset hard, delete another task's worktree, or
discard unrelated state.

## 11. Commit, handoff, and frozen merge order

One coherent direct-child implementation commit only, proposed subject:

```text
feat: isolate optional semantics runtime
```

Frozen order:

```text
M2 0d2c7f8...
  -> contract 5f605d0...
  -> CAD public types 085e92c... + correction a01c9a81...
  -> this canonical metadata/runtime commit (exact thirteen paths)
  -> separately registered core operations/orchestration commit
     (read_cad, tessellate_cad, write_cad, source snapshot/spooling,
      preserve/translation atomic-output control, formats.read CAD dispatch)
  -> separately registered anyfileio.cad_artifact codec commit
  -> accepted combined lightweight-core API/metadata handoff
  -> registered ANYfileio-occt provider slices
  -> owner-gated ANYfem V7 / UI and later consumer integrations
```

No resolver-only legacy commit is inserted before or after this slice. No
cherry-pick, merge, rebase, push, publication, or consumer handoff is authorized
by registration. Every later plan names the accepted full runtime commit as its
base and proves protected M2/contract/CAD diffs.

Completion evidence reports plan path/hash, editing identity, branch/worktree,
base/tree/parent, implementation commit/tree/parent, exact thirteen-path
diff/stat/blobs, focused first test result, qualification lease and first cell
results, wheel/distribution hashes and origins, protected hunk/blob proofs,
clean worktree/upstream state, exclusions, limitations, and downstream actions.

This milestone is not integration, operations, artifact, provider, consumer,
performance, push, publication, or ecosystem-closeout authority.
