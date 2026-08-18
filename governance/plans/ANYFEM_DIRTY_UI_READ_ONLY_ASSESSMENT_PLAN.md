# ANYfem Dirty UI/Test Read-Only Assessment Plan

Date: 2026-08-13 (Europe/Oslo)

Status: read-only assessment plan. No byte modification is authorized during
assessment.

## Authority and pinned state

This assessment is required by the release-blocker program at
`C:\Github\ANYopenSoft\governance\plans\ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`,
SHA-256
`4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.

ANYfem default/HEAD is
`7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`. Preserve these exact paths and
content identities:

| Status | Path | SHA-256 |
|---|---|---|
| modified | `src/anyfem/ui/scene.py` | `9E636A2ADC8BDE28A73632694C9D91AAA12AA229E0CABF5D4F045E30845C97DB` |
| modified | `src/anyfem/ui/viewport.py` | `6BCDA7DA5FF7E81AEB860311B6EB94BA476381390D9CBFC8EAFBE9517AE90A10` |
| modified | `tests/test_scene.py` | `E6AD70C9E1D410EE6536B64D2404934BD47F5E2741635691CDC3243FD78A1C81` |
| untracked | `tests/test_overlap_and_generator_ui.py` | `BED351383B22585AF4F65ECEBAC8ADA02797293584B618CEF4DC157D074200E0` |

The index, branch, and every other worktree path are outside ownership.

## Two independently classified slices

### Beam overlay slice

`scene.py` adds `Polyline.draw_overlay`, sets it only for structural beam lines
in geometry, mesh, and result scenes, and leaves plain lines false. `viewport.py`
passes the flag to the renderer. `test_scene.py` checks beam/plain distinction
and a coplanar diagonal beam's continuous overlay/coupled-node topology.

Read-only acceptance requires field/default consistency, propagation at every
beam construction site, no selection-owner regression, and the two focused
tests passing without repository writes.

### Overlap/generator contract-test slice

The untracked test is independent of the overlay change. It verifies atomic,
feature-backed, undoable coplanar-overlap fragmentation and generator-form
field filtering. It is coherent only if both tests pass against the pinned
default source with no production-file change required.

## Exact light assessment command

Use canonical sibling sources, disable bytecode and pytest cache, require a
fresh external base temp, and compare branch/status/file hashes before and
after:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='C:\Github\ANYfem\src;C:\Github\ANYgeometry\src;C:\Github\ANYmesh\src;C:\Github\ANYsolver\src;C:\Github\ANYmaterial\src;C:\Github\ANYfileIO\src'; python -m pytest -p no:cacheprovider --basetemp C:\Users\AudunArnesenNyhus\AppData\Local\Temp\anyfem_dirty_ui_read_only_v1 tests\test_scene.py::test_beams_are_drawn_differently_from_plain_lines tests\test_scene.py::test_coplanar_diagonal_beam_is_connected_and_drawn_continuously tests\test_overlap_and_generator_ui.py -q
```

This is a light focused run: one CPython process, no GPU/network/build, less
than 750 MiB RAM, ETA below 30 seconds. It does not consume the performance
lease. Refuse a pre-existing base-temp path and remove only the exact owned
external path after safe parent/leaf validation.

## Classification and completion rule

- If a slice passes, is internally coherent, and preserves every hash/status,
  report it as independently verifiable and propose a separate logical commit.
- Do not combine the overlay implementation with the unrelated contract-only
  test unless the completion review explicitly accepts one commit.
- If a test fails because the slice is incomplete or depends on unowned work,
  classify that slice as deferred and leave all bytes unchanged.
- No edit, format, cleanup inside the repository, staging, commit, or push occurs
  until the read-only evidence packet receives an explicit completion verdict.

## Output

Record exact command/result, test-node outcomes, branch/status before and after,
the four content hashes, coherence findings, ownership split, and a final
`complete` or `defer` recommendation for each slice.
