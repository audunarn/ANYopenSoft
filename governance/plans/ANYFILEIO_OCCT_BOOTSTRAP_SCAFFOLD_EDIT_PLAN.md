# ANYfileio-occt import-safe bootstrap/scaffold editing plan

Status: **registration candidate**. This content-addressed file grants no
branch, worktree, edit, test, build, resolver, native OCP, merge, push,
publication, or performance authority until the ecosystem Boss registers its
exact absolute path and SHA-256.

Date: 2026-08-13 (Europe/Oslo)

Editing agent: one direct child only, proposed identity
`/root/eir_anyfileio_occt_bootstrap`; no nested or delegated writer. A writer
change requires re-registration before any edit.

## 1. Objective and authority

Create one minimal source bootstrap for the separate `ANYfileio-occt` 0.1
distribution. This slice owns only packaging metadata and the registered entry
point, an import-safe package/backend protocol shell with zero advertised CAD
capabilities, and small static/fake isolation tests. It performs no OCP import
or CAD operation.

The bootstrap establishes a deterministic boundary for later separately
registered native slices. It is not a usable provider, built wheel, release
candidate, installed-entry-point proof, or capability claim.

Authoritative inputs:

- source plan
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`,
  SHA-256 `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`,
  SHA-256 `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered lightweight-core handoff
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_LIGHTWEIGHT_CORE_HANDOFF_PLAN.md`,
  SHA-256 `739EE860455966EC157BB029FD806EB3B42500562EC06D9F4C430AC85E3AC15F`;
- accepted core handoff commit
  `5513881827cdee9fd337497a2730a5912d8ea751`, tree
  `68d703646c5d9b556c1ecdbdb96f677a4ba9a381`, sole parent
  `a3725201a87d39a19ccf7edd1ae35d6d3c3f5089`;
- frozen core blobs:
  `src/anyfileio/cad.py`
  `baa7a5fde9db1da0951def9ff0abe1cd46626c7d`,
  `src/anyfileio/cad_backend.py`
  `fca05afc5f2daa7d4cdd5677d774628e67de7980`,
  `docs/CAD_BACKEND_CONTRACT.md`
  `f4ecd214cdd2ae448c91a6e8d46d4101b34a4ddb`, and
  `DEPENDENCY_MATRIX.md`
  `ed53d6d8fc5d315c3c5e31139032fea4353c8e60`.

Any change to distribution/import identity, dependency ranges, entry-point
coordinates, backend id/protocol/compatibility version, call shapes,
capability meaning, license file, or provider sequence is a material
`PUBLIC CONTRACT CHANGE` and stops this slice.

## 2. Exact base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileio-occt
remote identity:   https://github.com/audunarn/ANYfileio-occt.git
source branch:     main
source/base HEAD:  571231dc4c7d8b4131daac6b719a6b93125a20b4
base tree:         bf3f59f47f185149a7133ba08b9b38b9a67c5426
base parent:       none (root commit)
origin/main:       571231dc4c7d8b4131daac6b719a6b93125a20b4
new branch:        codex/anyfileio-occt-bootstrap
branch upstream:   none
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap
```

At plan creation the repository is clean and contains exactly one tracked path,
`LICENSE`. The proposed branch/worktree does not exist. Create it only after
registration, directly from the exact base, without fetch, pull, merge, rebase,
or precursor commit. The primary checkout and every ANYfileIO worktree are
read-only inputs, not edit targets.

Produce one coherent implementation commit whose direct and sole parent is
exactly `571231dc4c7d8b4131daac6b719a6b93125a20b4`, with proposed subject:

```text
feat: scaffold import-safe OCCT backend
```

No remote tracking, push, tag, PR, publication, or integration is authorized.

## 3. Protected state

The existing `LICENSE` is excluded from every edit and normalization:

```text
Git blob:   f288702d2fa16d3cdf0035b15a9fcbc552cd88e7
SHA-256:    230184F60BAE2FEAF244F10A8BAC053C8FF33A183BCC365B4D8B876D2B7F4809
size:       35,823 checkout bytes
```

The final commit must retain that exact blob, and
`git diff --exit-code 571231dc4c7d8b4131daac6b719a6b93125a20b4 HEAD -- LICENSE`
must be empty. No `.gitattributes`, formatter, or metadata edit may rewrite it.

The accepted core remains in another repository and is never copied or edited
here. Before source handoff, revalidate its exact tip and the four consumed
blobs in section 1. Drift in either repository freezes work.

## 4. Exact five-path ownership

All owned paths are new at the base; no existing hunk is transferred.

| Repository-relative path | Exact worktree edit target |
| --- | --- |
| `pyproject.toml` | `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\pyproject.toml` |
| `src/anyfileio_occt/__init__.py` | `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\src\anyfileio_occt\__init__.py` |
| `src/anyfileio_occt/backend.py` | `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\src\anyfileio_occt\backend.py` |
| `tests/test_bootstrap.py` | `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\tests\test_bootstrap.py` |
| `tests/test_layering.py` | `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\tests\test_layering.py` |

The corresponding paths below `C:\Github\ANYfileio-occt` are not edit
targets. No glob, generated-file, README, notice, type-marker, workflow, or
other metadata ownership is implied.

### 4.1 Packaging metadata and entry point

`pyproject.toml` freezes only:

- setuptools/wheel build-backend declarations; no build is run;
- distribution `ANYfileio-occt`, version `0.1.0`, Python
  `>=3.11,<3.15`, the existing `LICENSE` as the license file, canonical
  author, and canonical repository URLs;
- exact base requirements `ANYfileio>=0.2,<0.3`, `numpy>=1.26`, and
  `cadquery-ocp-novtk>=7.9.3.1.1,<7.10`;
- metadata-only extra
  `geometry = ["ANYgeometry>=0.2.1,<0.3"]`; it implements no adapter and
  imports no geometry package;
- a `dev` extra containing pytest only;
- exact entry point:

```toml
[project.entry-points."anyfileio.backends"]
occt = "anyfileio_occt.backend:get_backend"
```

- `src` discovery restricted to `anyfileio_occt*`, and focused pytest source
  configuration. No package data is declared in this slice.

There is no dependency on `cadquery`, `cadquery-ocp`, VTK, ANYfem,
ANYsolver, or ANYstructure and no source-build fallback. Later qualification
pins the distribution `cadquery-ocp-novtk==7.9.3.1.1`; `OCP` is only its
import namespace, and runtime `occt_version` is observed independently.

### 4.2 Import-safe package and zero-capability shell

`anyfileio_occt.__init__` contains only a package docstring and source
`__version__ = "0.1.0"`. It does not import or re-export `backend`,
`get_backend`, ANYfileIO, OCP, CadQuery, or ANYgeometry. Installed-wheel
version equality remains an unrun qualification gate.

`anyfileio_occt.backend` imports only stdlib plus public types from
`anyfileio.cad`. It defines one private singleton protocol shell with:

```text
backend_id:                    "occt"
protocol_version:              1
backend_compatibility_version: 1
backend_version:               "0.1.0"
capabilities:                  CadCapabilities()
```

`CadCapabilities()` means every format/mode set is empty and every boolean is
false. `get_backend()` has the exact no-argument entry-point shape, imports no
native/geometry module, and returns that same singleton.

The shell has the exact protocol-1 `read`, `tessellate`, and `translate`
parameter names and kinds. Each direct call immediately raises the existing
`BackendLoadError` with `CadDiagnostic` code `cad.backend.load_failed` and
an operation detail, without inspecting arguments, invoking cancellation,
touching paths/documents, doing I/O, or mutating state. No new diagnostic code
is introduced.

Under accepted core `551388...`, metadata discovery may truthfully report
`discovered`. Operation-time loading validates the exact identity first, then
rejects the zero capability set as `broken / cad.backend.load_failed` before
any shell method or native import. It must never report `ready` or make STEP,
IGES, or BREP available. Do not spoof an identity/version mismatch
(`incompatible`) and do not advertise capabilities backed only by stubs.

There is no binding/runtime OCCT version probe or value in this bootstrap.

### 4.3 Focused source/fake tests

`tests/test_bootstrap.py` contains exactly these nodes:

- `test_project_metadata_and_entry_point_are_frozen`
- `test_license_is_protected_and_metadata_is_minimal`
- `test_package_import_is_core_and_native_independent`
- `test_backend_and_factory_import_under_blocker`
- `test_factory_is_singleton_with_exact_identity_and_zero_capabilities`
- `test_protocol_shell_has_exact_call_shapes`
- `test_protocol_stubs_fail_typed_before_io`
- `test_core_fake_entry_point_transitions_discovered_to_broken`

`tests/test_layering.py` contains exactly:

- `test_provider_source_imports_only_stdlib_and_anyfileio`
- `test_no_native_geometry_or_future_provider_modules_exist`

The blockers reject exact/qualified `OCP`, `cadquery`, and `anygeometry`
module names while allowing literal distribution metadata. Package import must
remain independent even of ANYfileIO; backend/factory import may load only the
accepted core and must not load a native/geometry module.

The fake entry point supplies exact group/name/target and distribution metadata
to the accepted core's private test reset/load boundary. It proves
`discovered -> broken`, cached typed `cad.backend.load_failed`, zero
capabilities, no shell-method call, and no native/geometry import. It performs
no installed metadata enumeration, real entry-point installation, CAD I/O,
network, or native operation.

## 5. Explicit exclusions

Do not edit/create `LICENSE`, README, third-party notices, `py.typed`,
workflows, changelog, migration, benchmark, report, fixture, example CAD,
generated artifact, cache, build output, lockfile, or release file.

Do not create native/provider modules for documents, XDE, STEP, IGES, BREP,
units, locking, diagnostics, arrays, prototypes, tessellation, cache,
translation/export, or geometry. Do not import/call/probe OCP, CadQuery, or
ANYgeometry; implement CAD formats/operations; or touch another repository.

Build/sdist/wheel/twine/RECORD, venv/pip/resolver/platform cells, OCP import,
real installed entry points, full/broad suites, benchmarks/profilers/stress,
consumers, merge/rebase/push/PR/tag/publication, indexes, and network are
outside this plan. No nice-to-have hardening is in scope.

## 6. Verification and evidence boundary

Always-allowed post-edit static checks:

- `git diff --check` and exact five-path equality;
- Python AST parsing without bytecode generation;
- base/tree/parent, LICENSE blob, no-upstream, and protected-core blob checks.

After source review, request Boss classification before running this exact
focused command once:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONPATH='C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap\src;C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src'
python -m pytest -q -p no:cacheprovider --basetemp 'C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-bootstrap-pytest' tests/test_bootstrap.py tests/test_layering.py
```

Before the run, revalidate the read-only core worktree at exact
`5513881827cdee9fd337497a2730a5912d8ea751`. Preserve the first outcome; no
retry, node/environment change, or broader suite follows without new
authority. The basetemp is external task-owned evidence and is never committed.

A green focused run establishes only source metadata, import isolation,
zero-capability/fail-closed behavior, and call shapes. It does not establish a
wheel, resolver, installed entry point/origin, OCP import, native correctness,
CAD support, platform support, performance, consumer integration, release, or
publication.

All builds/installs/resolvers, native/OCP work, broad suites, timing/RSS/size,
benchmarks, profiling, stress, and scaling remain separately authorized and,
when classified heavy, require `PERF LEASE REQUEST` and the exact token
`PERF LEASE GRANTED`.

## 7. Definition of done and commit packet

- Exactly five new paths and one direct-child commit; LICENSE stays exact.
- Metadata, dependencies, entry point, package discovery, identity, versions,
  zero capabilities, method shapes, and typed no-I/O failures match this plan.
- Package import is core-independent; backend/factory import is native- and
  geometry-independent.
- The core fake entry point stays non-ready and transitions
  `discovered -> broken / cad.backend.load_failed`.
- Static proofs are clean; report the first focused outcome if authorized.
- Worktree is clean after commit and branch upstream remains none.

Report commit SHA/tree/sole parent, exact five paths/blobs, protected LICENSE
blob, static/focused evidence, clean worktree, and absence of upstream,
merge/push/build/network/publication.

## 8. Frozen future sequence

This bootstrap must receive ecosystem closeout before later slices consume it:

1. this scaffold/package shell;
2. separately registered native foundation: OCP load boundary,
   locking/ownership, units, document/XDE and STEP/IGES/BREP import;
3. prototype/occurrence extraction and tessellation;
4. translation/write and integrated imported-CAD API;
5. separately leased build/wheel/OCP/real-CAD qualification;
6. owner-gated ANYfem V7, structural adapter, UI, and consumer work in the
   registered ecosystem order.

ANYmesher is not a prerequisite for disjoint imported-CAD provider source.
Geometry, consumers, solver/ANYstructure handoffs, and publication remain
outside this plan. A changed base, overlap, capability claim, public-contract
change, or sequence change requires a revised content-addressed plan.
