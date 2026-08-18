# ANYsolver full-pytest optional-accelerator correction plan

Status: registration candidate; plan-only until its SHA-256 and scope receive
independent review.

## 1. Objective and frozen evidence

Repair the red hosted `Tests` workflow without changing solver mechanics,
package dependency semantics, or the accepted compatibility correction.

- repository: `C:\Github\ANYsolver`
- frozen base commit: `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- frozen base tree: `00b2b20691e73a05589b797b32352f1c760a2451`
- failed workflow run: `31808004879`
- run identity: `Tests`, `push`, `main`, `.github/workflows/ci.yml`, attempt 1
- terminal result: 24 completed jobs, 16 success, 8 failure
- failures: all Ubuntu/Windows full-pytest lanes for Python 3.11-3.14
- controls: all four compatibility jobs, both wheel jobs, all eight Numba jobs,
  and both Pardiso jobs passed

The common failure contract is deterministic: the full-pytest job installs
`.[dev]`, while `pyproject.toml` keeps Numba in the optional `numba` extra.
Seventeen tests in every failing lane require compiled/JIT behavior and instead
observe `numba_import_failed`, `jit_unavailable`, scalar fallback, or absent
compiled-path diagnostic counters. The Numba jobs install `.[dev,numba]` and
pass. Some lanes also report one to three platform/order-sensitive numerical
failures; those are verification targets, not authority for tolerance changes.

Frozen raw-byte SHA-256 inputs at the base:

- `.github/workflows/ci.yml`:
  `312CDF6A6A1663A2EE4785DA349E9CC81195A6FE665841C2CC6F22C3AC3BB1CA`
- `tests/test_anyfileio_version_compatibility.py`:
  `D11270C6BD025FE54CCF63AF6FEC28DF25216294CD4480A7FE98C2F4BD407D27`
- `pyproject.toml` (read-only contract evidence):
  `97F272E8381506BAE1B9331C4AB7AC716306DDE8658219A32B8D119DB52CF74A`

## 2. Exact ownership and branch

Coordinator/sole editor: root agent, Norwegian label `Odin` for review
metadata. Work only in a new isolated worktree and branch created from the
frozen base:

- worktree: `C:\Github\ANYsolver\.perf2-worktrees\ci-pytest-numba-fix`
- branch: `codex/ci-pytest-numba-fix`

The only source/test paths owned by this slice are:

1. `.github/workflows/ci.yml`
2. `tests/test_anyfileio_version_compatibility.py`

This plan file is governance evidence, not part of the ANYsolver commit.

## 3. Exact correction

1. Change only the full `pytest` job's editable install from `.[dev]` to
   `.[dev,numba]`.
2. Extend the existing workflow-shape test to require that exact full-pytest
   install contract and to keep the separate Numba job contract intact.
3. Do not add Numba to mandatory dependencies or the `dev` extra. Numba remains
   an optional product capability; this change makes the comprehensive hosted
   verification environment match the compiled-path assertions already in the
   full suite.
4. Do not alter skip conditions, expected diagnostics, solver tolerances,
   numerical thresholds, production source, or the accepted compatibility and
   wheel-smoke logic.

## 4. Explicit exclusions

No edit to `pyproject.toml`, `src/**`, S4 proof/handoff/plan artifacts,
activity/deletion/shared assembly, sibling repositories, package versions,
lockfiles, GitHub secrets, release/publish workflows, or existing evidence.
No retry, rerun, cancellation, push, default-branch mutation, cleanup, force,
reset, stash, rebase, broad ref mutation, or Defender exception is authorized
by this plan.

The variable secondary numerical failures may be diagnosed by the focused
tests below. Any source/test-tolerance correction requires a separately
registered amendment; it must not be folded into this environment fix.

## 5. Focused local gates

Use the accepted sibling environment already available to the isolated
worktree. Set `PYTHONDONTWRITEBYTECODE=1` and a task-specific `NUMBA_CACHE_DIR`.
Run sequentially with `-p no:cacheprovider` and a named basetemp:

1. From the isolated worktree, prepend only these accepted source roots in this
   order: local `src`, `C:\Github\ANYmaterial\src`,
   `C:\Github\ANYgeometry\src`, `C:\Github\ANYmesh\src`, and
   `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src`.
   Run a Python preflight that imports `numba`, `anysolver`, `anymaterial`,
   `anygeometry`, `anymesher`, and `anyfileio`; asserts every module origin is
   beneath its corresponding pinned root; and asserts
   `anysolver.jit_compiler.JIT_ENABLED` is true. Print the Numba version and all
   resolved origins. No ambient repository root may satisfy an import.
2. `python -m pytest tests/test_anyfileio_version_compatibility.py::test_workflows_pin_compatibility_graph_and_actions -q -p no:cacheprovider --basetemp=.pytest_tmp_ci_numba_contract`
3. Run exactly these 17 common failed node IDs in one focused invocation:

   - `tests/test_advanced_s4_batches.py::test_nonlinear_orthotropic_s4_batch_matches_scalar_force_and_tangent`
   - `tests/test_advanced_s4_batches.py::test_nonlinear_generalized_s4_batch_matches_scalar_and_state`
   - `tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle`
   - `tests/test_generalized_section_api_workflows.py::test_generalized_shell_uses_installed_extended_batch_diagnostic`
   - `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_selector_reports_all_static_exclusions`
   - `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hardening_curve]`
   - `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hill_yield]`
   - `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam2]`
   - `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam3]`
   - `tests/test_nonlinear_performance.py::test_mixed_initial_field_shell_batch_accelerates_initialized_elastic_element`
   - `tests/test_nonlinear_state_lifecycle.py::test_force_control_store_matches_mapping_and_materializes_owned_snapshots`
   - `tests/test_recovery_batches.py::test_compiled_isotropic_s4_matches_scalar_oracle_for_warped_global_output`
   - `tests/test_vectorized_hill48.py::test_global_newton_solution_and_iteration_count_match_scalar_path`
   - `tests/test_vectorized_hill48.py::test_global_arc_length_path_matches_scalar_path`
   - `tests/test_vectorized_hill48.py::test_compiled_nonconvergence_falls_back_then_preserves_fail_closed_error`
   - `tests/test_vectorized_hill48.py::test_kernel_exception_is_an_observable_whole_batch_scalar_fallback`
   - `tests/test_vectorized_hill48.py::test_invalid_analytical_row_and_requested_numerical_tangent_are_counted`

4. Run exactly these three secondary node IDs seen in some lanes:

   - `tests/test_beam_shell_verification.py::test_beam_shell_verification_report_separates_pass_and_xfail`
   - `tests/test_fe_solver_triangular_shell_backend.py::test_triangular_shell_stiffness_mass_pressure_and_geometric_assembly[node_ids0-coords0]`
   - `tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]`

   The current host has a pre-existing installed `ANYmesher 0.1.0`
   distribution record even when the accepted `0.2.1` module source is pinned.
   If that stale metadata alone makes the aggregate beam/shell report fail,
   capture the report and require all of the following rather than relabelling
   it as a numerical failure: the only non-PASS cases are `EXT-001`, `EXT-002`,
   and dependent summary `VVR-001`; every reason is `SEM002` naming the stale
   `ANYmesher 0.1.0` distribution; and `NLG-008` is `PASS`. The standalone
   follower-pressure and T3 nodes must still pass. This local-host exception
   does not apply to hosted acceptance, where the workflow installs the pinned
   sibling distributions and all 24 jobs must pass.
5. `git diff --check`
6. Verify the staged extent is exactly the two owned ANYsolver paths and create
   one atomic child commit of the frozen base.

Preserve all task basetemp/Numba-cache evidence through independent review.
Remove nothing until the standing cleanup gate and user closeout authorize an
exact inventory.

## 6. Acceptance and hosted gate

Independent read-only review must verify the two-file scope, workflow semantics,
focused results, hashes, and absence of production/test-expectation changes.
Only then may a separate integration addendum request an exclusive PERF lease
for one non-force fast-forward/push and one 24-job hosted `Tests` run.

Hosted acceptance requires the literal attempt-1 run to contain exactly the
registered 24 unique jobs, all `completed/success`, with no Publish run, rerun,
or unexpected workflow. A hosted failure permits evidence collection only and
does not authorize an unplanned correction.

## 7. Definition of done

- full pytest installs `.[dev,numba]` on all eight OS/Python lanes;
- the workflow contract test permanently enforces that fact;
- focused common tests pass with Numba present; secondary tests pass except
  for the exact captured local-host `SEM002` metadata-provenance exception in
  section 5.4, which is not a pass and is forbidden in hosted acceptance;
- no solver, packaging dependency, compatibility, S4, or tolerance semantics
  change;
- atomic two-file commit and independent acceptance packet exist;
- no main integration or hosted run occurs without a separately registered
  addendum and explicit PERF lease.
