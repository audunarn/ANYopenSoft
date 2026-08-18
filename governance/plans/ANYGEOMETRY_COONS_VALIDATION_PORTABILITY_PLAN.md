# ANYgeometry Coons Validation Portability Plan

## Objective and evidence trigger

Diagnose and, only after an independently reviewed root-cause decision, correct the
Python-version-sensitive validation of the same warped eight-edge topology-backed
Coons face. GitHub Tests run `31700097367` proved that the fixture commits on Python
3.13 on Windows and Ubuntu, but fails on Python 3.11, 3.12, and 3.14 on both systems
with `GeometryError: face 1 loop 0 self-intersects`. Each failing cell otherwise
passed 386 tests. The build/Twine/external-wheel job and isolated missing-planar
capability job passed.

## Repository and immutable baseline

- Repository: `C:\Github\ANYgeometry`
- Branch: `main`
- Exact local and remote starting commit:
  `db5548449e2522bd7915fad0d84c64964f38c382`
- Accepted kernel parent remains in history:
  `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`
- Preserve the workflow run, all existing commits, `.idea/vcs.xml`, and
  `dist_gap_closure/` exactly.

## Phase 1: read-only diagnosis scope

No ANYgeometry file may be edited during Phase 1. Read-only inspection is bounded to:

- `src/anygeometry/model.py`
- `src/anygeometry/surfaces.py`
- `src/anygeometry/curves.py`
- `src/anygeometry/tolerance.py`
- the three failing fixtures in:
  - `tests/test_changed_region_and_indexed_queries.py`
  - `tests/test_local_structural_validation.py`
  - `tests/test_strict_audit.py`
- `pyproject.toml` and installed interpreter/dependency metadata needed to explain
  version behavior
- terminal GitHub logs for run `31700097367`

The diagnosis must reconstruct the validation polygon and identify the first segment
pair classified as intersecting. It must compare projected UV values, basis or
orientation choice, residuals, determinant/cross-product values, and effective
tolerances across Python 3.11, 3.12, 3.13, and 3.14 where evidence is available. It
must also check whether Python hash seed, NumPy version, linear-algebra backend, or
dependency resolution changes the result.

The diagnosis must decide one of these outcomes with numeric evidence:

1. the boundary is valid and production parameter projection or orientation is
   nondeterministic/unstable;
2. the boundary is valid but the segment predicate mishandles a qualified endpoint,
   degeneracy, or tolerance boundary;
3. the fixture is genuinely self-intersecting in authoritative Coons parameter
   space and the Python 3.13 pass is the defect;
4. evidence is insufficient, in which case the result stays blocked and fail-closed.

## Non-negotiable invariants

- Preserve fail-closed topology validation.
- Do not loosen or delete assertions.
- Do not exclude supported Python versions.
- Do not inflate global/model tolerances.
- Do not special-case fixture IDs, test names, vertex counts, or coordinates.
- Do not weaken strict audit, spatial bounds, or transaction rollback.
- Do not change schema, public signatures, identity, mutation policy, or package
  version.
- Do not edit workflow files as part of this plan.

## Phase 1 accepted diagnosis

Phase 1 is complete and accepted as outcome 1. The evidence is recorded at:

- `C:\Github\ANYopenSoft\governance\evidence\ANYGEOMETRY_COONS_VALIDATION_PORTABILITY_DIAGNOSIS.md`

The fixture is the injective graph `S(u,v)=(u,v,T(u)+T(v))`. Exact topology
side parameters give a simple unit-square loop with area 1, zero residual, and
sampled `min |du x dv|=1`. Generic closest-point inversion gives order-one
parameter and world-space residuals; the exact NumPy 2.5.2 wheel reproduces
that bad inverse. The failed CI polygon was not logged, so its first
intersecting pair remains truthfully unavailable, but a representation with
residual `1.33333333333` is unqualified whether or not a particular numeric
lane happens to classify it as crossed.

Rejected responses are dependency pinning, Python exclusion, tolerance
inflation, fixture special-casing, assertion weakening, and disabling
self-intersection checks.

## Phase 2 exact branch, worktree, and file allowlist

Implementation remains blocked until the ecosystem boss accepts the SHA-256
of this amendment. Once accepted, edits are limited to exactly:

- production: `C:\Github\ANYgeometry\src\anygeometry\model.py`;
- focused tests:
  `C:\Github\ANYgeometry\tests\test_coons_validation_portability.py`.

The worktree must remain `C:\Github\ANYgeometry`, branch `main`, with starting
`HEAD == main == origin/main == db5548449e2522bd7915fad0d84c64964f38c382`.
Tracked/index state must be clean. Existing `.idea/vcs.xml` and
`dist_gap_closure/` remain untouched. No existing fixture, workflow,
dependency, schema, documentation, or package file may be edited under this
amendment.

## Phase 2 invariant-preserving algorithm

Add one private topology-Coons outer-loop UV builder in `model.py`. It must use
`Face.sides()` and the same cumulative edge-length convention as
`_chain_point_and_derivative`. For an oriented sample at local side-edge
fraction `q`, compute:

`s = (preceding_edge_lengths + q * current_edge_length) / total_side_length`.

Map it authoritatively as:

- side 0: `(s, 0)`;
- side 1: `(1, s)`;
- side 2: `(1-s, 1)`;
- side 3: `(0, 1-s)`.

`face.corners[0]` is not required to be loop index zero. Associate every
side-derived sample with its original `Face.loop` edge position and assemble
the returned polygon in the existing loop order, including the wrapped fourth
side. Do not rotate the public trim merely because the mapped parameter origin
starts later in the loop.

The validation replacement is deliberately narrower than the public mapping
helper. Use exact construction UV during `_validate_face_geometry` only when
all of these are true: the authoritative surface is an empty-boundary
`CoonsSurface`, there are four mapped corners, the outer loop contains only
`Straight` edges, and `face.holes` is empty.
Any topology-Coons outer loop containing an `Arc` or `Spline` retains the
entire existing generic-inverse/self-intersection validation route until a
separately qualified conservative curve-curve predicate exists. Finite sampled
chords must not be claimed to certify curved intersections between samples.
Likewise, any topology-Coons face with one or more holes retains the entire
existing generic-inverse route for both outer and hole loops. This phase must
never compare canonical construction UV for the outer loop against generic
projected UV for a hole in a different coordinate frame.

Within that restricted validation path:

1. `_validate_face_geometry` must use the validation sampler's existing
   per-edge counts but must not call generic `closest_uv` for that construction
   boundary.
2. `face_trim_loops_uv` may use its requested straight/curved sample counts and
   the same exact construction mapping for the outer loop only when
   `face.parameterization is None` and `face.holes` is empty. When an optional
   explicit parameterization or any hole exists, retain the current
   parameterization-first/generic `face_local_uv` mapping consistently for all
   loops.
3. Holes and every non-topology-Coons support retain their current
   qualification path.

Canonical construction UV is necessarily a unit-square perimeter, so retain
fail-closed physical validity independently for the all-Straight restricted
path. Let `participating_points` be the sampled outer-loop 3D points in loop
order, compute the translation-invariant
`extent = feature_extent(participating_points)`, and compute exactly
`distance_tolerance = self.tolerance.effective_length(extent)`. For every
non-adjacent pair of bounded straight boundary segments, excluding closing
adjacency, call the owner `qualified_segment_segment` with the model tolerance
policy and explicit `characteristic_length=extent`.

Handle its closed result algebra explicitly:

- `DISJOINT` is the only accepted non-intersection result;
- `TOUCH_POINT`, `CROSS`, `OVERLAP_CURVE`, `CONTAINED`, and `COINCIDENT` reject
  with the existing `face <id> loop <n> self-intersects` error when the
  qualified component maximum residual is `<= distance_tolerance`;
- `UNCLASSIFIED`, `UNSUPPORTED`, `CAPABILITY_MISSING`, nonfinite witnesses or
  residuals, degenerate segments, or ill-conditioned results reject fail
  closed as invalid/self-intersecting geometry rather than being treated as
  disjoint.

The owner predicate already handles parallel/collinear cases without unstable
division and classifies a zero-length segment as unclassified, which therefore
rejects. No merge, coincidence, parameter, area, or surface-residual tolerance
may substitute for the exact effective length tolerance above. The existing
2D polygon predicate and its tolerance are not changed.

The correction must not call Shapely, add a dependency, change a public
signature, or change serialization. It remains proportional to the existing
O(B^2) self-intersection check and allocates only O(B) sampled boundary/UV
storage.

## Phase 2 focused tests and rollback gates

The new focused test file must prove all of the following:

1. The unchanged eight-edge warped fixture commits and its public outer trim
   is the exact deterministic unit-square perimeter at requested sample
   positions.
2. Monkeypatching generic topology `closest_uv` to raise does not affect
   construction validation or outer-trim extraction, proving the invalid
   inverse is not consulted.
3. Unequal side-edge lengths, reversed stored edge directions, and a nonzero
   first mapped-corner index map by oriented cumulative side length while
   preserving original `Face.loop` output order; they must not depend on
   vertex order, world axes, or hash order.
4. A genuinely non-planar topology-Coons boundary whose non-adjacent straight
   segments cross in 3D remains rejected with `self-intersects`.
5. That rejection is atomic: face store, reverse incidence, revision, and
   pre-existing model state are unchanged; monotonic allocator high-water
   behavior is not rewound.
6. Existing planar bow-tie construction rejection remains green.
7. A topology-backed Coons support with a nontrivial explicit
   `face.parameterization` retains parameterization-first public trim UV.
8. A topology-Coons outer loop containing a curved edge retains the current
   generic-inverse validation route; a spy/monkeypatch proves the restricted
   straight-edge replacement did not claim curved qualification.
9. A topology-Coons face with a hole retains one common existing projected UV
   frame for its outer and hole loops; a spy/monkeypatch proves neither
   validation nor public trim extraction mixes exact outer UV with generic
   hole UV.

Do not alter the three CI fixtures. Their unchanged behavior is part of the
focused evidence.

## Phase 2 light cross-version commands

After amendment acceptance, run these LIGHT selections only. Each command must
use a unique, prevalidated external-TEMP `--basetemp` child, record exact
CPython/NumPy/platform metadata, and remove only that exact child afterward:

```powershell
C:\Python\Python313\python.exe -m pytest -q `
  tests/test_coons_validation_portability.py `
  tests/test_changed_region_and_indexed_queries.py::test_changed_region_uses_conservative_coons_interior_bounds `
  tests/test_local_structural_validation.py::test_coons_interior_is_in_maintained_face_bounds_and_candidates `
  tests/test_strict_audit.py::test_coons_interior_outside_boundary_aabb_is_broad_phased_fail_closed `
  tests/test_identity_topology.py::test_public_mutations_reject_self_intersection_and_zero_length `
  tests/test_serialization.py::test_construction_rejects_a_self_intersecting_face `
  --basetemp <verified-external-temp-child-for-py313>

C:\Python\Python314\python.exe -m pytest -q `
  tests/test_coons_validation_portability.py `
  tests/test_changed_region_and_indexed_queries.py::test_changed_region_uses_conservative_coons_interior_bounds `
  tests/test_local_structural_validation.py::test_coons_interior_is_in_maintained_face_bounds_and_candidates `
  tests/test_strict_audit.py::test_coons_interior_outside_boundary_aabb_is_broad_phased_fail_closed `
  tests/test_identity_topology.py::test_public_mutations_reject_self_intersection_and_zero_length `
  tests/test_serialization.py::test_construction_rejects_a_self_intersecting_face `
  --basetemp <verified-external-temp-child-for-py314>
```

Locally available lanes are CPython 3.13.9/NumPy 2.4.3 and CPython
3.14.2/NumPy 2.3.5. Repeat only the new focused file under
`PYTHONHASHSEED` 0, 1, 42, and 123456 on both interpreters. Python 3.11/3.12
and the exact CI patch lanes remain remote evidence and require a later fresh
PERF lease for one full Tests workflow. No full suite, build, benchmark,
profiler, package publication, tag, or release is authorized by this phase.

## Phase 2 risks, reviewer, and definition of done

Primary risks are a mismatch between validation/public sampling counts,
mishandled reversed edge orientation, rotating output when the first mapped
corner is not loop index zero, overriding explicit parameterization, claiming
sampled-chord certification for curved edges, hiding a physical straight-edge
crossing behind canonical UV, mixing canonical outer and projected hole
coordinate frames, or changing rollback/high-water behavior. The tests above
directly gate each risk.

Independent reviewer: `/root/final_plan_audit` (Boyle). The reviewer owns
neither allowed path and must approve this amended algorithm before edits,
then inspect the exact diff and focused results before any commit or remote
run.

This plan is complete only when:

- the amended plan hash is explicitly accepted;
- the approved two-file correction passes focused valid/invalid, rollback,
  hash-seed, and locally available cross-version checks;
- independent review confirms fail-closed mathematical behavior;
- the change is committed as a non-amended direct child with exact scope;
- a lease-controlled remote matrix reaches a truthful terminal result, or a
  precise residual blocker is reported;
- protected paths remain unchanged and no publication action occurs.
