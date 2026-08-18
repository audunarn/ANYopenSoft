# ANYsolver No-Numba Residual Failure Static Correction Addendum

## Record identity

- Schema: `anysolver.no_numba_residual.static_correction_addendum/1`
- Accepted addendum plan: `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_EVIDENCE_LIMIT_ADDENDUM.md`
- Accepted addendum plan SHA-256: `6912765C1D82A035499E54B3FEC6C3278D8C103440F22501EAEB43B01D9BECB0`
- Immutable source report: `C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_REPORT_82A9DB28.md`
- Immutable source report SHA-256: `CDF15DD7DFACD3548A15DE3871B74BFE3714A986E7F40B38670585FB345A7932`
- Source commit: `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- Source tree: `00b2b20691e73a05589b797b32352f1c760a2451`
- Evidence mode: one bounded static reread; no retry after display truncation

This report supplements STATIC-S01. It does not amend, replace, overwrite, or invalidate the immutable source report as an evidence artifact. Where this addendum corrects a prior conclusion, both the original statement and this correction remain preserved in their respective records.

## Bounded reread ledger

Exactly these seven frozen source files were opened once:

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `tests/test_nonlinear_performance.py` | 17,519 | `CF94531EF34DD9FD7627F34634E2ABCA034DE58099FF16364F92E3E729C2AC02` |
| `src/anysolver/nonlinear_performance.py` | 66,871 | `FDD372DAF3EC0C6B7C8C930CA1C994E8FBD2213CE22C7AA1304E2D17F1E418FA` |
| `src/anysolver/nonlinear_performance_bootstrap.py` | 6,527 | `A348678E631C725632462E44ADDB8E8978B76DA6855E961CAA248112CDE28B02` |
| `src/anysolver/nonlinear_performance_batch_b.py` | 46,526 | `0C28309BF7E5FEA363920BADC065ACA3C52C101019C17E6A756C9C1AA70CFF01` |
| `src/anysolver/nonlinear_performance_batch_c.py` | 29,986 | `6A4768CBBD6E8497C78B8CB691349DFE1588ADD0FB33908B8BA0B638E21F1402` |
| `tests/test_follower_pressure.py` | 21,631 | `3CC5B27B8D6E7722B56DED2C5782A2173A0FADF0D535392B23844577F306E59F` |
| `src/anysolver/buckling.py` | 25,404 | `8382E1340806057D1EF1788204051D56EC63F273E95D42BFB65996A816395F3A` |

The source display truncated during this single pass. No file was reopened. Facts below are limited to text retained from that pass plus immutable facts already recorded by STATIC-S01.

## Impact exclusion correction

### Superseding finding for STATIC-S01 S-F10

`S-F10` is false if read as grouping all five impact failures under one non-JIT production defect.

Static facts:

- Production retains the ordered semantic exclusion tuple.
- When JIT is unavailable, production prepends `jit_unavailable`; it does not discard the semantic exclusions.
- `C12`, `test_direct_reduced_impact_selector_reports_all_static_exclusions`, already has partial JIT-aware expected-prefix handling.
- `C13` through `C16` still assert a semantic reason as the primary reason and therefore need later test-only JIT-aware expectations in a no-Numba lane.
- No production change is indicated by this correction.

Correction consequence:

- Preserve the production reason ordering and diagnostics.
- Later correction work should adjust only the no-JIT expectations of `C13` through `C16`, while retaining their semantic-exclusion assertions.
- Do not make generic CI install Numba and do not suppress these tests wholesale.

## Restored verification identifiers

- `V01`: `tests/test_beam_shell_verification.py::test_beam_shell_verification_report_separates_pass_and_xfail`
- `V02`: `tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]`
- Frozen comparison for `V02`: `[32-0.035]`
- `C18` and `C19` are not valid frozen identifiers and must never be used for these two verification cases.

## C04 decorator and entry-point evidence

Frozen node:

`C04 = tests/test_nonlinear_performance.py::test_mixed_initial_field_shell_batch_accelerates_initialized_elastic_element`

Exact retained facts:

- The function begins at line 222.
- Line 221 is blank. No `pytest.mark.skipif`, JIT marker, or other decorator is present immediately before the function.
- Lines 223-242 construct a simple panel and initialized states.
- Line 248 assigns `legacy = nonlinear_performance._ORIGINAL_ASSEMBLER`.
- Line 249 asserts `legacy is not None`.
- Lines 250-251 invoke the scalar/reference assembler as `legacy(model, displacement, committed, 5, tangent=True)`.
- Lines 253-254 invoke the current assembly entry point as `nonlinear_static._assemble_nonlinear_system(model, displacement, committed, 5, tangent=True)`.
- Lines 256-260 compare force, tangent, and provenance.
- Line 261 obtains `plan = get_nonlinear_assembly_plan(model, 5)`.
- Line 262 requires at least one `initial_field_accelerated_elements`.
- Line 263 requires zero `initial_field_override_elements`.
- Line 264 requires two shell elements.

Owner-path facts retained from `nonlinear_performance.py`:

- `_state_has_initial_fields` is at lines 74-75.
- `_apply_initial_field_shell_overrides` begins at line 78. Its retained documentation states that the compiled ordinary-shell kernel has no immutable initial-field inputs and that uncommon initialized entries use an exact scalar override.
- `_scatter_sum` has `@njit(cache=True)` at line 124.
- Timing fields include `initial_field_override_seconds`, `initial_field_override_elements`, and `initial_field_accelerated_elements` at lines 157-159.
- Override application and metric increments occur at lines 897-907.
- `get_nonlinear_assembly_plan` is exposed at lines 1041-1042.
- Retained comments at lines 1089-1091 say the plan encodes von Karman response, other kinematics/scales use the scalar reference, and immutable initial fields are handled exactly.
- The plan assembly call is retained at lines 1110-1112.
- Optimization installation begins at line 1527.

Bootstrap facts:

- `nonlinear_performance_bootstrap.py` imports `JIT_ENABLED` and `JIT_DISABLED_REASON` at line 16.
- Its install wrapper calls the base installer and installs batch B only when both the base path is active and `JIT_ENABLED` is true, at lines 109-117.
- Batch B/C status eligibility and disabled reason derive from JIT state at lines 131-136.
- Bootstrap replaces the public performance entry points at lines 157-162.

Batch facts retained before truncation:

- `nonlinear_performance_batch_b.py` decorates `_elastic_shell_batch_into_buffers` with `@njit(cache=True, parallel=True)` at lines 46-47.
- It imports and calls `get_nonlinear_assembly_plan` at lines 412-414.
- Its retained initial-field path begins near line 611, `_populate_initial_field_resultants` begins near line 641, and the retained call occurs near lines 833-835.

Static conclusion:

- C04 has no no-JIT skip gate and explicitly requires accelerated initial-field accounting.
- The bootstrap and batch evidence makes C04 a compiled/JIT-dependent correction candidate rather than a generic fallback correctness test.
- A later correction may skip this individual node when `JIT_ENABLED` is false and add this exact node to the dedicated Numba lane.
- The exact final batch-B/batch-C delegate chain and every post-truncation condition are `evidence_limited`; Stage P or a separately accepted static addendum is required before claiming the complete runtime call chain.

## V02 buckling branch and SciPy-call evidence

Selected frozen node:

`V02 = tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]`

Retained test facts:

- STATIC-S01 already records that the selected follower and dead-load solves pass `allow_dense_fallback=True`.
- The frozen comparison case is `[32-0.035]`.
- The retained tail computes analytical pressure as `3.0 * bending_stiffness / config.radius**3` at line 426.
- It computes relative error from `follower.critical_load_factor` at line 427.
- It requires `follower.solver_status == "ok"` at line 429.
- It requires follower-load stiffness inclusion and tangent symmetry error below `1.0e-12` at lines 432-433.
- It requires the dead-load critical value to exceed `1.20 * analytical` and the follower critical value to be below the dead value at lines 436-437.

Exact retained production branches and calls from `buckling.py`:

- SciPy imports are `from scipy import linalg`, `from scipy import sparse`, and `from scipy.sparse import linalg as sparse_linalg` at lines 19-21.
- `solve_eigenvalue_buckling` spans lines 206-586.
- Its retained defaults include `num_modes=3`, `eigen_tolerance=1e-8`, `dense_size_limit=200`, `shift_load_factor=None`, `search_factor=4`, `repeated_tolerance=1e-3`, and `allow_dense_fallback=False` at lines 209-216.
- Constraint transformation construction/use is retained at lines 271-280.
- Constrained follower-tangent symmetry uses `sparse.linalg.norm` at lines 283-285.
- A nonsymmetric follower pencil is rejected as unsupported at lines 319-344.
- The sparse branch is selected only when `n_red > dense_size_limit and 1 <= k < n_red`, at line 399.
- Without a shift, lines 401-402 call `sparse_linalg.eigsh(KG_sym.tocsc(), k=k, M=K_sym.tocsc(), which="LA")`.
- The shifted sparse path also calls `sparse_linalg.eigsh` and records solver kind `sparse_scipy_eigsh_inverted_pencil` at lines 403-430.
- Sparse exceptions are retained in `sparse_error` and clear the eigenvectors at lines 431-433.
- Dense solution/fallback occurs only when eigenvectors are absent and either `n_red <= dense_size_limit` or `allow_dense_fallback`, at line 434.
- Lines 435-439 call `linalg.eigh(KG_dense, K_dense)` and record `dense_scipy_eigh_inverted_pencil`.
- On `linalg.LinAlgError`, lines 440-444 call `linalg.eig(K_dense, KG_dense)` and record `dense_scipy_eig_general_pencil`.
- Missing eigenvectors fail closed at lines 445-461.
- Retained postprocessing includes real conversion and normalization at lines 467-477, rigid-body correlation and positive-root filtering at lines 478-499, Rayleigh load factor/range/residual candidate creation at lines 500-508, candidate sorting at line 510, mode residual/validity handling at lines 512-531, repeated-group assignment at line 537, and root/repeated/sorting diagnostics at lines 549-555.
- Constraint residual summary is retained at lines 556-560.

Static conclusion:

- The production branch is controlled by runtime `n_red`, `k`, `dense_size_limit`, shift state, sparse-call outcome, and `allow_dense_fallback`.
- `allow_dense_fallback=True` permits a dense fallback after sparse failure but does not prove that the 24-element and 32-element cases select the same primary branch.
- Exact selected-node setup arguments, reduced dimensions, root sequences, operator values, shifted-`eigsh` argument details after the retained segment, and 24/32 branch equivalence are `evidence_limited` because the single display was truncated.
- No skip, tolerance adjustment, eigensolver change, or physics change is justified by static evidence alone. The later pinned Ubuntu-equivalent Stage-P reproduction and transparent named-call instrumentation remain required for V02/NLG-008.

## Evidence-limited items carried forward

The following claims are deliberately not made:

- A complete batch-B/batch-C dispatch chain for C04.
- Exact post-truncation conditions in either batch module.
- Complete selected V02 fixture arguments or reduced system sizes.
- Identical sparse/dense branch selection for the 24- and 32-element ring cases.
- Exact shifted-`eigsh` arguments beyond the retained call classification.
- Any runtime operator, eigenpair, residual, root-order, lifecycle-event, or environment result.

Closing these limits requires the already governed later Stage-P environment manifests, fresh-process probes, and transparent instrumentation. This report does not create or authorize those artifacts.

## Later correction boundary

- Impact: test-only JIT-aware expectation corrections for C13-C16; no production change.
- C04: individual no-JIT skip plus exact dedicated-Numba selection is a supported later correction candidate, subject to Stage-P confirmation of the retained static inference.
- Corotational and lifecycle cases remain governed by their separately frozen generic/fresh-process diagnosis cells.
- V01 remains the frozen broad report identifier but is not authorized as an unfiltered 130-case Stage-P command.
- V02 remains selected NLG-008 diagnosis only; no skip or tolerance tuning is authorized.

## No-execution attestation

This addendum records static source evidence only. During this bounded pass there was no Python import, test, probe, environment creation, process launch, Git operation, GitHub query, source/test/workflow edit, cleanup, performance action, or Stage-P execution. The immutable STATIC-S01 report was not modified.
