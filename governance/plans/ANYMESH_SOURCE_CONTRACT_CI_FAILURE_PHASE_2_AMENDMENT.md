# ANYmesh Source-Contract CI Failure Phase 2 Amendment

## Status and authority

- Status: proposed for independent review; no source edit authority is implied by this document.
- Governing Phase 1 plan: `C:\Github\ANYopenSoft\governance\plans\ANYMESH_SOURCE_CONTRACT_CI_FAILURE_DIAGNOSIS_PLAN.md`.
- Governing Phase 1 plan SHA-256: `B127E1ED3EA8082CB8E5AFAAA12D2992AC8626D0BEAD43C72A0E05465AEB5F3A`.
- Independent reviewer: ecosystem boss task `019ff655-abd9-7eb1-b94e-d80252ff9215`.
- Phase 2 may begin only after that reviewer accepts this exact amendment hash.
- No third GitHub Actions run, push, merge, tag, package build, publication, broad test, or performance run is authorized here.

## Exact base and worktree

- Repository: `C:\Github\ANYmesh`.
- Required source base, local `main`, and `origin/main`: `4a0424a05fc4333d46d26f4c2fca97a113d0c09c`.
- Required source tree: `659451e5f5ad140c6c6f43bf8110a6b254907102`.
- Isolated edit worktree: `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYmesh-native-hybrid-release-blockers`.
- Edit branch: `codex/native-hybrid-release-blockers`.
- The primary and isolated worktrees were clean and at the required base during Phase 1. Phase 2 must stop on base, branch, path-inventory, or status drift.
- Qualification geometry source: exact Git object `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`; import it from a fresh external archive, never from an ambient checkout.

## Phase 1 numeric classification ledger

The exact four-node reproduction against the bases above produced `4 failed` in `1.53 s`, matching corrected remote run `31700439141`.

### Mapped-only operation contracts

- Public signature: `generate_mesh(geometry, *, backend='auto', **options)`.
- Trimmed-hole fixture: face `1`, one hole.
- Omitted backend and explicit `auto` both succeeded with `108` nodes, `75` quads, and `18` triangles.
- Explicit `backend="mapped"` failed with `MeshError`: `face 1 has trimmed holes; decompose it into mapped patches before using the built-in quad backend`.
- Neutral-triangle fixture: face `1`, zero mapped corners.
- Omitted backend and explicit `auto` both failed in the native chart path with `native face 1 has no qualified surface chart: face 1 has no four-side topology parameterization...`.
- Explicit `backend="mapped"` failed with the intended mapped diagnostic: `face 1 has no four-side mapped parameterization; partition it first (triangle_to_quads handles triangles)`.
- Classification: both tests name the mapped contract but became stale when the public default changed from `mapped` to `auto`. Production default behavior is correct and must not change.

### Multiple-crossing legacy adapter

- Initial model revision: `15`; faces: `1`, `2`, `3`.
- Indexed broad-phase candidates: `(1, 2)` and `(1, 3)`.
- Both initial owner queries were classified `CROSS`, dimension `CURVE`, one component, tolerance `1e-9`, diagnostic `bounded_face_crossing`.
- Witnesses were `(0,0,0)` to `(0,2,0)` and `(0.5,0,0)` to `(0.5,2,0)` respectively.
- The `(1,2)` plan selected `FACE_IMPRINT`; application advanced revision `15 -> 16`.
- Restarted broad phase then supplied candidate `(3,4)`. Its owner query was classified `DISJOINT`, dimension `NONE`, zero components, tolerance `1e-9`, diagnostic `face_material_intervals_disjoint`.
- Owner planning correctly selected `NO_TOPOLOGY`. The legacy compatibility adapter nevertheless called apply, which raised `policy imprint has no applicable persistent operation for face/face`.
- Classification: an AABB candidate is not a qualified geometric intersection. This is an ANYmesh quarantine-adapter defect, not an ANYgeometry defect.

### Positive-area overlap ordering

- Initial model revision: `10`; faces `1`, `2`; candidate `(1,2)`.
- `find_coplanar_overlaps` returned exactly one overlap with area `1.0 m^2`.
- The first `_prepare` stopped at the existing overlap guard with the expected duplicate-stiffness diagnostic; the typed mutation event list was empty. Overlap-first ordering is therefore proven and must remain byte-order-equivalent.
- Explicit owner fragmentation advanced revision `10 -> 11`, produced faces `3`, `4`, `5`, and left zero positive-area overlaps.
- Restart candidates were `(3,4)`, `(3,5)`, and `(4,5)`. Pair `(3,5)` reached mutation after shared-edge filtering and was owner-classified `DISJOINT`, dimension `NONE`, zero components, tolerance `1e-9`, diagnostic `coplanar_faces_disjoint`.
- Owner planning again selected `NO_TOPOLOGY`; the same legacy apply error caused the second test failure.

## Exact Phase 2 edit allowlist

Only these three ANYmesh paths may change:

1. `src/anymesher/_legacy_intersections.py`
2. `tests/test_intersection_meshing.py`
3. `tests/test_operations.py`

No public backend, hybrid mesher, ANYgeometry, identity, tolerance, spatial-index, overlap, persistence, structural-topology, coordinate-coupling, packaging, workflow, or report implementation path is in scope.

## Required source correction

In `_legacy_intersections._prepare`, retain `find_coplanar_overlaps` as the first geometry gate, before cloning and before any intersection query or mutation.

For each post-filter broad-phase face pair:

1. Call public `query_intersection` on the current working model and current model-bound face handles before invoking the compatibility mutator.
2. Skip the pair only when `result.classified` is true and `result.kind is IntersectionKind.DISJOINT`.
3. For every `UNSUPPORTED`, `UNCLASSIFIED`, capability-missing, or otherwise unclassified result, continue into the existing compatibility path so the kernel result fails closed and ANYmesh preserves a precise `MeshError` with the face IDs.
4. Remove the `_NO_INTERSECTION` exception-string allowlist and its text-matched skip. Typed owner evidence becomes the sole no-intersection skip authority.
5. Preserve shared-loop-edge filtering, one-sided-shell-junction handling, successful-imprint restart ordering, mutation-count guard, clone-only mutation, and association folding.

This correction must not infer intersections or coupling from coordinates, synthesize geometry truth, reinterpret empty payloads as disjoint, or catch typed unsupported results as success.

## Required test corrections and regression

- In `test_mapped_backend_requires_a_trimmed_hole_to_be_partitioned`, add exactly `backend="mapped"` to the existing `generate_mesh` call. Keep its diagnostic assertion.
- In `test_a_neutral_triangle_is_refused_by_the_mapped_backend`, add exactly `backend="mapped"` to the existing `generate_mesh` call. Keep its diagnostic assertion.
- Preserve the two existing intersection tests as behavioral regressions for post-fragment DISJOINT skipping and overlap-first duplicate-stiffness blocking.
- Add one focused legacy-adapter regression in `tests/test_intersection_meshing.py` using a real nonplanar/spline face pair that the public owner query reports as `UNSUPPORTED` and unclassified. Assert the typed owner classification first, then assert the quarantined legacy entry raises `MeshError` without changing the original model revision or serialized model. Do not monkeypatch a successful result and do not weaken the diagnostic to accept silent success.
- Retain and run `tests/test_kernel_intersection_contract.py::test_nonplanar_face_connect_preserves_typed_unsupported_result` as the authoritative typed-owner regression; that file is test input, not an edit path.

## Focused light evidence

Create a fresh external archive of ANYgeometry object `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`, set `PYTHONPATH` to that archive's `src` followed by the isolated ANYmesh worktree's `src`, set `PYTHONDONTWRITEBYTECODE=1` and `PYTHONNOUSERSITE=1`, and assert both imported module origins before pytest.

Run exactly these focused nodes with `-p no:cacheprovider` and a fresh external `--basetemp`:

```powershell
python -m pytest -q -vv --tb=short -p no:cacheprovider `
  tests/test_operations.py::test_mapped_backend_requires_a_trimmed_hole_to_be_partitioned `
  tests/test_operations.py::test_a_neutral_triangle_is_refused_by_the_mapped_backend `
  tests/test_intersection_meshing.py::test_multiple_crossings_are_discovered_after_the_first_face_is_fragmented `
  tests/test_intersection_meshing.py::test_positive_area_coplanar_overlap_is_blocked_before_double_stiffness `
  tests/test_intersection_meshing.py::test_legacy_imprint_fails_closed_for_typed_unsupported_faces `
  tests/test_kernel_intersection_contract.py::test_nonplanar_face_connect_preserves_typed_unsupported_result
```

Then run only a light source-diff gate:

```powershell
git diff --check
git diff --name-only 4a0424a05fc4333d46d26f4c2fca97a113d0c09c --
```

The second command must print exactly the three allowlisted paths. No broad suite, build, wheel, benchmark, profiler, remote workflow, or retry is part of this phase.

## Review and stop gate

- Submit the exact diff, base/tree/status, focused command and result, per-node behavior, and unchanged-outside-allowlist proof to boss task `019ff655-abd9-7eb1-b94e-d80252ff9215`.
- An independent reviewer must confirm that only classified typed `DISJOINT` is skipped and that unsupported/unclassified paths still fail closed.
- Stop after review. Commit, integration, push, and any third CI run require separate explicit authority and, for remote CI, a fresh performance lease.
