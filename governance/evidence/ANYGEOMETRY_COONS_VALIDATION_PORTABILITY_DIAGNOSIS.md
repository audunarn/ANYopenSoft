# ANYgeometry Coons Validation Portability Diagnosis

## Decision

The warped eight-edge fixture is a valid topology-backed Coons face. The
portability failure is caused by using a generic, unqualified closest-point
inverse to recover parameters for points whose authoritative boundary
parameters are already known from topology. The resulting UV polygon is an
invalid intermediate representation and can falsely self-intersect. This is
outcome 1 from the governing diagnosis plan.

No ANYgeometry source or test file was changed during Phase 1.

## Frozen source and CI evidence

- Repository: `C:\Github\ANYgeometry`
- Branch and local/origin tip:
  `db5548449e2522bd7915fad0d84c64964f38c382`
- GitHub Tests run:
  `https://github.com/audunarn/ANYgeometry/actions/runs/31700097367`
- The same three fixtures failed on Windows and Ubuntu under Python 3.11,
  3.12, and 3.14 with `face 1 loop 0 self-intersects`; each cell otherwise
  passed 386 tests.
- Both Python 3.13 cells passed 389 tests.
- Every cell used Shapely 2.1.2. Python 3.11 resolved NumPy 2.4.6; Python
  3.12, 3.13, and 3.14 resolved NumPy 2.5.2. Therefore neither Shapely nor
  the NumPy release alone partitions passing from failing cells.
- CI patch versions were CPython 3.13.14 and 3.14.6. Local probes used
  CPython 3.13.9 and 3.14.2.

## Mathematical reconstruction

The perimeter vertices are the four unit-square corners at `z=0` and the four
side midpoints at `z=1`. With loop corners `(0, 2, 4, 6)`, the topology Coons
surface is

`S(u, v) = (u, v, T(u) + T(v))`,

where `T` is the triangular tent with values `T(0)=T(1)=0` and
`T(0.5)=1`. The first two coordinates are exactly `(u, v)`, so this patch is
an injective graph over the unit square. A deterministic 41-by-41 derivative
probe found `min |du x dv| = 1`; the center is `(0.5, 0.5, 2)`, intentionally
above the boundary AABB.

The sampled boundary has SVD singular values
`(1.6583123951777001, 1.6583123951776997, 1.414213562373095)` and world
extent `sqrt(3)`. Its smallest singular value is far above the effective
surface residual `1e-8`; this is not a planarity-threshold or SVD-basis
ambiguity.

The authoritative side parameters give this 16-point UV loop:

```
(0,0), (.25,0), (.5,0), (.75,0),
(1,0), (1,.25), (1,.5), (1,.75),
(1,1), (.75,1), (.5,1), (.25,1),
(0,1), (0,.75), (0,.5), (0,.25)
```

It has signed area `1`, zero world-space residual, and no intersecting
segment pair. Its UV extent is `sqrt(2)`, effective area tolerance is about
`2e-14`, and the unchanged segment-predicate tolerance is `1e-10`.

## Defective intermediate representation

For topology-backed Coons faces, `_validate_face_geometry` samples the known
construction boundary and calls `face_local_uv` for every sample. That method
wraps the same patch in `closest_uv`, which runs one clipped,
forward-difference Gauss-Newton solve from `(0.5, 0.5)` with no residual
qualification or global-inverse guarantee.

For exact corner target `(0,0,0)`, the initial surface point is
`(0.5,0.5,2)`. The forward derivatives are approximately `(1,0,-2)` and
`(0,1,-2)`. Thus `J^T J=((5,4),(4,5))`, its determinant is `9`, and the
first least-squares step is `(7/18,7/18)`, moving to `(8/9,8/9)` instead of
`(0,0)`. This is a step toward the wrong local stationary basin, not harmless
roundoff.

Local probes under CPython 3.13.9/NumPy 2.4.3 and CPython 3.14.2/NumPy 2.3.5
produced identical bad UV bytes under `PYTHONHASHSEED` 0, 1, 42, and 123456:

- maximum UV error: `0.8888888889163018`;
- maximum reconstructed world residual: `1.3333333333333333`;
- projected polygon area: `0.44444444433504704`.

An isolated CPython 3.14.2 probe installed only the exact CI NumPy 2.5.2
wheel:

- wheel: `numpy-2.5.2-cp314-cp314-win_amd64.whl`;
- wheel SHA-256:
  `7587F53DFBD5EDC0F7B87C6217B4C6D2D1F2EF9C3DA70BC1315E7DB5F8D7EC9D`;
- isolated NumPy module SHA-256:
  `A6958CB364663B7ACCE81CCFD58EEB65A2B34D5376157F924777B97211A73BE4`.

It still produced maximum UV error `0.8888888889711276`, maximum world
residual `1.3333333333333335`, and area `0.44444444440974695`. It happened
not to cross on local CPython 3.14.2. The exact first pair from CI is
unavailable because the failed workflow did not log its polygon and the same
NumPy wheel on a different CPython patch/runner still landed in a non-crossing
bad basin. This does not weaken the conclusion: an intermediate representation
with order-one parameter and world residuals is unqualified regardless of
whether a particular numeric lane happens to classify it as crossed.

The isolated probe child was verified absent after cleanup. Ambient
interpreters and repository bytes were unchanged.

## Rejected explanations and fixes

- The fixture is not geometrically self-intersecting; it is an injective graph.
- The SVD planarity decision is not near its tolerance.
- Hash iteration is not involved.
- NumPy pinning cannot fix a defective inverse and does not partition CI.
- Python exclusion, tolerance inflation, fixture special-casing, assertion
  removal, and disabling self-intersection validation would hide the defect.

## Invariant-preserving correction boundary

The authoritative outer-loop UV must be generated directly from `Face.sides()`
and the same cumulative edge-length convention used by topology Coons
evaluation:

- side 0 fraction `s` -> `(s, 0)`;
- side 1 fraction `s` -> `(1, s)`;
- side 2 fraction `s` -> `(1-s, 1)`;
- side 3 fraction `s` -> `(0, 1-s)`.

An oriented edge sample at local fraction `q` has side fraction
`(cumulative_length + q * edge_length) / side_length`. This is exact for the
construction parameterization and independent of closest-point inversion.

Because canonical parameter-space sides form a unit square by definition, a
separate translation-invariant physical 3D boundary check must keep rejecting
genuine non-adjacent boundary intersections. Existing UV predicates and
tolerances remain unchanged for all other supports and hole qualification.

## Independent review

The read-only reviewer `/root/final_plan_audit` independently reached the same
outcome: valid fixture, unqualified generic inverse, exact side-parameter fix
in `model.py`, and no dependency pin or Shapely change. The reviewer made no
file change.
