# ANYsolver CI numerical-stability prerequisite plan

Status: amended execution plan for the red-main prerequisite blocking S4
integration.

## Frozen base and evidence

- Repository: `C:\Github\ANYsolver`.
- Base commit: `4030dd041c667fecf1f90211194f6ae84a5875f2`.
- Base tree: `4cac95ad6897e7d3012fa02ae479bda422bb86ef`.
- Failed GitHub Actions run: `31823623517`, attempt 1.
- The run contains 24 jobs: 18 passed and six full-pytest jobs failed.
- The common defect is a free-ring buckling pencil whose elastic matrix retains
  six rigid modes. `solve_eigenvalue_buckling` sends that singular pencil to a
  generalized eigensolver and filters rigid correlation only after the solve.
  Backend-dependent mixtures therefore admit a near-null root or discard the
  physical first root.
- A separate triangular-shell test counts zero modes at exactly
  `1e-8*lambda_max`, while the declared hourglass stiffness is also
  `1e-8*lambda_max`; roundoff changes the count between six and seven.
- The first registered implementation gate established a mandatory physical
  boundary: for a free BeamElement with imposed dead axial prestress, the
  elastic operator descends to the analytic rigid quotient but the geometric
  operator does not (`geometric_null_residual=0.36892527714080564` and
  `geometric_cross_residual=0.32997679932191626`). That pencil has no
  representative-independent quotient eigenproblem and must remain an
  explicit `invalid_rigid_quotient`; neither `allow_free_mechanisms` nor a
  post-solve filter may turn it into a successful result.

## Exact correction

Create a clean worktree at
`C:\Github\ANYsolver\.perf2-worktrees\ci-rigid-projection-fix` on branch
`codex/ci-rigid-projection-fix`, based exactly on the frozen base.

Owned files are limited to:

- `src/anysolver/buckling.py`;
- `src/anysolver/beam_shell_verification.py`;
- `tests/test_fe_solver_buckling.py`;
- `tests/test_fe_solver_triangular_shell_backend.py`;
- `tests/test_beam_shell_verification.py`;
- `tests/test_follower_pressure.py`.

In the dense buckling path, when `Q_rigid` is nonempty, first establish one
dimensionless reduced-coordinate metric. Let `ell` be the Euclidean diagonal
of the model-coordinate bounding box; reject non-finite or non-positive
`ell`. Let `S_inv` be diagonal in full node-major DOFs, with `1/ell` for each
translation and `1` for each rotation. For the existing constraint map
`q_full=T z`, compute an economic/reduced float64 QR

```text
S_inv T = Q_T R_T,       y = R_T z.
```

This yields a square `R_T` because `T` has full column rank. Require `R_T`
nonsingular under the frozen threshold below. Transform the reduced operators
and rigid candidates into `y` coordinates:

```text
K_y = R_T^-T K_red R_T^-1,
G_y = R_T^-T (KG_red + Kload_red) R_T^-1,
Y_r = R_T Q_rigid.
```

Orthonormalize `Y_r` by full QR to `Q_r` and use the remaining full-QR columns
as `Q_f`. Require that both operators define a quotient:

```text
K_y Q_r = 0,  G_y Q_r = 0,
Q_r^T K_y Q_f = 0,  Q_r^T G_y Q_f = 0
```

within the frozen residual rule. Then form `K_f=Q_f^T K_y Q_f` and
`G_f=Q_f^T G_y Q_f`, solve the symmetric pencil, and map every vector back as
`z=R_T^-1 Q_f v` before existing candidate checks and full-DOF recovery.
Projection is forbidden if either operator does not descend to the quotient.
For the projected path, do not apply the legacy Euclidean
`Q_rigid.T@z > 0.90` rejection: the representative is orthogonal in the
registered dimensionless `y` metric, not necessarily in Euclidean `z`
coordinates. Compute and report `BucklingMode.rigid_body_correlation` as
`max(abs(Q_r.T@y_mode))` after normalizing `y_mode=Q_f v`; use mapped `z` for
Rayleigh values, residuals, constraint mapping, and full-DOF recovery. The
legacy correlation/rejection path remains unchanged when no projection is
applied.

All numerical rules are fixed before execution:

- arrays are finite IEEE-754 float64 and `eps=2.220446049250313e-16`;
- `tau(A)=64*max(m,n)*eps*sigma_max(A)`, with an exact-zero matrix having
  `tau=0` and rank zero;
- `r_tol(d)=4096*d*eps`;
- orthonormality is `||Q^T Q-I||_F <= r_tol(number_of_rows)`;
- operator-null residual is
  `||A Q_r||_F / max(||A||_F, smallest_normal_float) <= r_tol(d)`;
- cross residual uses the same denominator and bound;
- transformed/projected symmetry uses
  `||A-A^T||_F/max(||A||_F,smallest_normal_float) <= r_tol(d)`;
- `K_f` is positive definite only when its smallest symmetric eigenvalue is
  strictly greater than `tau(K_f)`; this predicate is repeated at fixed
  multipliers `0.25`, `1`, and `4`, and a categorical change fails closed.

The projection is an exact coordinate reduction and adds no stiffness, mass,
penalty, tolerance tuning, or mode deletion beyond the analytic rigid space.
`allow_free_mechanisms` does not authorize solving a singular elastic pencil:
if `K_f` is not positive definite, return `singular_projected_stiffness`
whether the flag is true or false. Preserve the public
`free_mechanism_handling` value (`retained` or `rigid_body_roots_filtered`)
and add the separate `rigid_body_handling` value `projected`.

The non-descending dead-prestress finding is a permanent fail-closed
regression, not a request to weaken the quotient test. Replace the former
free-free dead-beam success expectation with an exact
`invalid_rigid_quotient` expectation and the frozen residual-category checks.
Exercise the successful projected path in two ways: (1) a synthetic symmetric
pencil constructed to annihilate the analytic rigid span in the registered
dimensionless metric, including a nontrivial translation/rotation scale and a
deterministic rigid-basis rotation; and (2) the real free thin-ring follower
pressure case, whose combined geometric plus load-tangent operator must pass
the same quotient checks and retain the unchanged analytical tolerance. The
same ring with only imposed dead prestress must now return
`invalid_rigid_quotient`; do not report an arbitrary dead-load eigenvalue from
a non-descending pencil. This changes no follower-pressure formula or
acceptance tolerance.

For only the registered Q4 regular-polygon ring fixtures, use their exact
discrete equilibrium prestress rather than the continuum cylinder value. With
`n` chord facets, circumradius `R`, `alpha=pi/n`, and positive configured
pressure magnitude `p` (the load case stores `-p`), set the compression-positive
local chord-direction state to

```text
membrane_compression_x = p*R*cos(alpha),
membrane_compression_y = membrane_compression_xy = 0.
```

This is the exact consistent-load vertex balance: the chord length is
`2R*sin(alpha)`, and the two adjacent pressure half-loads balance the two
adjacent chord membrane forces only at `N=pR*cos(alpha)`. Apply it identically
in `tests/test_follower_pressure.py` and `_run_nlg_008` in
`src/anysolver/beam_shell_verification.py`. Do not generalize it to Q8/curved
facets or to the continuum cylinder nominal-stress API.

Branching uses the original reduced dimension `n_red`. If `Q_rigid` is
nonempty and `n_red <= dense_size_limit`, use the dense quotient above. If
`Q_rigid` is nonempty and `n_red > dense_size_limit`, use the dense quotient
only when `allow_dense_fallback=True`; otherwise return
`rigid_projection_requires_dense` without attempting a sparse eigenproblem.
If `Q_rigid` is empty, preserve the existing sparse/dense selection and
fallback behavior. A zero-dimensional `Q_f` returns
`empty_flexible_subspace`. Never test sparse positive definiteness or send a
known rigid-singular pencil to `eigsh`/general `eig`.

On success set solver identity to `dense_scipy_eigh_rigid_quotient`. The
literal metric version is `dimensionless_full_dof_bbox_v1`. Add a
`rigid_projection` diagnostics mapping with exact keys `applied`,
`metric_version`, `characteristic_length`, `original_dofs`, `projected_dofs`,
`rigid_rank`, `orthonormality_residual`, `elastic_null_residual`,
`geometric_null_residual`, `elastic_cross_residual`,
`geometric_cross_residual`, `elastic_min_eigenvalue`,
`elastic_max_eigenvalue`, `spd_tolerance`, and `spd_sensitivity`.
`spd_sensitivity` is a mapping with literal string keys `0.25`, `1`, and `4`;
each value contains `threshold` and `positive_definite` for that multiplier.
Quotient-validation failure
returns status `invalid_rigid_quotient`; the two size/SPD cases return the
statuses named above. Each failure includes `reason`, `solver`, and the same
available `rigid_projection` fields.

Replace the triangular-shell eigenvalue-count assertion with an invariant
test using the same dimensionless metric and frozen `tau`/`r_tol` definitions:
construct the six analytic rigid vectors, obtain their orthonormal span and
complement, verify `K` annihilates the rigid span, and require the stiffness
restricted to the complement to be positive at all three fixed multipliers.
Do not change the element's hourglass stiffness or any production tolerance.

## Exclusions

Do not edit S4-improved branches or plans, element stiffness, hourglass
coefficients, material/geometry code, activity/deletion, shared assembly,
workflow files, packaging, sibling repositories, or verification tolerances.
Do not skip, xfail, or weaken the follower-pressure analytical check. The
dead-prestress comparison is replaced only because the registered quotient
test proves that its free pencil is not representative-independent.
Do not rerun or cancel an existing hosted workflow.

## Focused gates

Use one CPython process with `PYTHONDONTWRITEBYTECODE=1` and this ordered
`PYTHONPATH`: execution-worktree `src`;
`C:\Github\ANYmaterial\src` at `4626887667f4c251479d26f321b9e73b046a2783`;
`C:\Github\ANYgeometry\src` at `939e047f19177692c861a68eaef0eaa18b2976c5`;
`C:\Github\ANYmesh\src` at `979f6a88f0d81507e1ac61b854f1f56362ce5e37`;
`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src`
at `5513881827cdee9fd337497a2730a5912d8ea751`. Before pytest, assert each
import origin lies beneath its pinned root and `anysolver` lies beneath the
execution worktree.

Run these exact commands sequentially with pytest cache disabled:

1. `python -m pytest tests/test_fe_solver_buckling.py -q -p no:cacheprovider --basetemp=.pytest_tmp_ci_rigid_buckling`
2. `python -m pytest "tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]" "tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[32-0.035]" -q -p no:cacheprovider --basetemp=.pytest_tmp_ci_rigid_follower`
3. `python -m pytest tests/test_fe_solver_triangular_shell_backend.py -q -p no:cacheprovider --basetemp=.pytest_tmp_ci_rigid_triangle`
4. Add and run the metadata-independent node
   `tests/test_beam_shell_verification.py::test_nlg_008_follower_pressure_case_passes`.
   It calls `run_beam_shell_verification(selected_ids={"NLG-008"})` and
   requires that single case to pass:
   `python -m pytest tests/test_beam_shell_verification.py::test_nlg_008_follower_pressure_case_passes -q -p no:cacheprovider --basetemp=.pytest_tmp_ci_rigid_report`
5. `git diff --check` and exact six-file extent verification.

Do not delete the four basetemps before independent review; they are
task-owned evidence. No ambient sibling checkout may precede the pinned roots.

Every new regression must assert the projected solver diagnostics, verify
rigid-basis invariance under a deterministic orthogonal change of basis, and
include nontrivial translation/rotation scaling that proves a projected
physical root is not rejected by legacy Euclidean correlation.
Clean no artifact before independent review; preserve test evidence.

After focused acceptance, create one atomic commit. A separate integration
step may fast-forward and push only after independent review; hosted CI must
finish 24/24 successful before the S4 integration plan is rebound.
