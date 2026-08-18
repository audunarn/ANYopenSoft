# ANYsolver No-Numba Residual Failure Diagnosis Plan

Status: PLAN ONLY. No diagnostic command, source/test edit, commit, integration,
push, CI action, cleanup, or publication is authorized until this exact document
identity is independently accepted.

## 1. Authority and immutable baseline

This plan is a bounded diagnosis follow-up to the accepted ANYsolver correction
commit:

- Commit: `82a9db28d67507c82ef15c631f582a0c3bf6740e`
- Tree: `00b2b20691e73a05589b797b32352f1c760a2451`
- Sole parent: `3cdb51efcdded232054225ea0eb9cc16dc79dde9`
- Subject: `fix: harden compatibility CI isolation`
- Existing correction worktree:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`
- Existing correction branch: `codex/ci-six-failure-correction`

The worktree must be clean at the accepted commit and tree before any diagnosis.
No new worktree or branch is authorized by this plan.

The immutable remote evidence is GitHub Actions Tests run `31746877870` at
commit `3cdb51efcdded232054225ea0eb9cc16dc79dde9`. The three completed Ubuntu
pytest logs were recovered once from these immutable job IDs:

| Python | Job ID | Result |
| --- | ---: | --- |
| 3.11 | `94603441514` | 17 failed, 748 passed, 23 skipped |
| 3.12 | `94603441506` | 19 failed, 746 passed, 23 skipped |
| 3.13 | `94603441528` | 19 failed, 746 passed, 23 skipped |

The logs must not be queried again. The run, all-jobs collection, active jobs,
and run status must not be queried under this plan.

## 2. Objective

Determine the smallest truthful correction boundary while preserving the generic
`.[dev]` job as the full no-Numba fallback lane.

The diagnosis must establish:

1. The ten individual compiled-only tests that need an explicit
   `skipif(not JIT_ENABLED, ...)` contract and exact inclusion in the dedicated
   Numba lane.
2. The corotational test's required dual-mode diagnostics while it remains in
   the generic lane.
3. The five impact exclusion tests' correct JIT-aware assertions without any
   production behavior change.
4. The ownership and ordering of nonlinear-state materialization accounting.
5. The shared `NLG-008` physics/eigenpair cause behind the Python 3.12/3.13
   beam-verification and 24-element follower-pressure failures.

This plan does not presume a correction. It gathers enough focused evidence for
a separate, content-addressed correction amendment.

## 3. Non-negotiable no-Numba contract

- The generic 2-OS by 4-Python pytest matrix continues to install exactly
  `.[dev]`.
- Numba remains optional and must not be added to `dev` or the generic job.
- The dedicated Numba jobs remain the compiled-backend qualification lane.
- A compiled-only test may be skipped only as an individual node when
  `JIT_ENABLED` is false. Whole files may not be skipped.
- Generic fallback, ownership, exclusion, reporting, and physics tests must pass
  without Numba.
- A skip must not conceal a fallback or backend-independent defect.
- No production behavior is changed during diagnosis.
- No assertion or tolerance is loosened during diagnosis.

## 4. Frozen exact 19-node ledger

### 4.1 Per-version occurrence

Python 3.11 failed the 17 common nodes `C01` through `C17` below.

Python 3.12 and 3.13 failed the same 17 common nodes plus `V01` and `V02`.

The union is exactly 19 nodes. No node outside this ledger enters diagnosis
without a superseding plan.

### 4.2 Ten compiled-only individual nodes

These nodes assert that a compiled backend executed. None currently has a
node-level JIT branch or skip. The anticipated correction is individual
`skipif(not JIT_ENABLED, ...)` plus exact dedicated-Numba selection; that
correction is not authorized here.

| ID | Exact pytest node | Occurrence | Exact observed assertion/failure |
| --- | --- | --- | --- |
| C01 | `tests/test_advanced_s4_batches.py::test_nonlinear_orthotropic_s4_batch_matches_scalar_force_and_tangent` | 3.11/3.12/3.13 | `orthotropic_elastic_fast_path_element_count == 4`; key absent |
| C02 | `tests/test_advanced_s4_batches.py::test_nonlinear_generalized_s4_batch_matches_scalar_and_state` | 3.11/3.12/3.13 | `generalized_elastic_fast_path_element_count == 4`; key absent |
| C03 | `tests/test_generalized_section_api_workflows.py::test_generalized_shell_uses_installed_extended_batch_diagnostic` | 3.11/3.12/3.13 | expected `constitutive_fallback is None`; got `general_element/generalized_shell_section` fallback |
| C04 | `tests/test_nonlinear_performance.py::test_mixed_initial_field_shell_batch_accelerates_initialized_elastic_element` | 3.11/3.12/3.13 | `initial_field_accelerated_elements >= 1`; got 0 |
| C05 | `tests/test_recovery_batches.py::test_compiled_isotropic_s4_matches_scalar_oracle_for_warped_global_output` | 3.11/3.12/3.13 | expected `compiled_isotropic_s4`; got `scalar_chunk_thread_pool` |
| C06 | `tests/test_vectorized_hill48.py::test_global_newton_solution_and_iteration_count_match_scalar_path` | 3.11/3.12/3.13 | expected compiled Hill48 `activated is True`; got false |
| C07 | `tests/test_vectorized_hill48.py::test_global_arc_length_path_matches_scalar_path` | 3.11/3.12/3.13 | expected compiled Hill48 `activated is True`; got false |
| C08 | `tests/test_vectorized_hill48.py::test_compiled_nonconvergence_falls_back_then_preserves_fail_closed_error` | 3.11/3.12/3.13 | expected `compiled_nonconverged: 1`; got `jit_unavailable: 1` |
| C09 | `tests/test_vectorized_hill48.py::test_kernel_exception_is_an_observable_whole_batch_scalar_fallback` | 3.11/3.12/3.13 | expected `compiled_kernel_exception: 2`; got `jit_unavailable: 2` |
| C10 | `tests/test_vectorized_hill48.py::test_invalid_analytical_row_and_requested_numerical_tangent_are_counted` | 3.11/3.12/3.13 | expected `analytical_tangent_invalid: 1`; key absent |

Diagnosis must prove that each node is compiled-only, that its numerical oracle
still runs in the Numba environment, and that the dedicated Numba selection
names all ten exact nodes. No whole-file selection is permitted as a substitute
for the exact-node ledger.

### 4.3 Corotational dual-mode generic node

| ID | Exact pytest node | Occurrence | Exact observed assertion/failure |
| --- | --- | --- | --- |
| C11 | `tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle` | 3.11/3.12/3.13 | expected `fallback_reason is None`; got `numba_import_failed: No module named 'numba'` |

This node remains generic. Diagnosis must prove both modes:

- With JIT: backend is compiled, `fallback_reason is None`, and the analytical
  circle/displacement assertions hold.
- Without JIT: backend/fallback diagnostics truthfully report JIT absence while
  the scalar/direct fallback still completes and satisfies the same physical
  circle/displacement assertions within the existing tolerances.

The anticipated correction is a JIT-aware diagnostic assertion inside this
node, not a skip and not a production change.

### 4.4 Five generic impact exclusion nodes

| ID | Exact pytest node | Occurrence | Exact observed assertion/failure |
| --- | --- | --- | --- |
| C12 | `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_selector_reports_all_static_exclusions` | 3.11/3.12/3.13 | expected `identity_constraint_transformation`; got `jit_unavailable` |
| C13 | `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hardening_curve]` | 3.11/3.12/3.13 | expected `plastic_material_history_unqualified`; got `jit_unavailable` |
| C14 | `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hill_yield]` | 3.11/3.12/3.13 | expected `plastic_material_history_unqualified`; got `jit_unavailable` |
| C15 | `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam2]` | 3.11/3.12/3.13 | expected `beam_fiber_plasticity_unqualified`; got `jit_unavailable` |
| C16 | `tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam3]` | 3.11/3.12/3.13 | expected `beam_fiber_plasticity_unqualified`; got `jit_unavailable` |

These five nodes remain generic. Production currently reports JIT availability
as an exclusion and retains semantic exclusions in its ordered exclusion
ledger. Diagnosis must capture the complete ordered `exclusion_reasons` in both
modes and distinguish the primary `fallback_reason` from retained semantic
reasons.

The anticipated correction is JIT-aware expected values in the five tests.
There is no authority to reorder, remove, or otherwise change production
exclusion behavior.

### 4.5 Generic nonlinear-state lifecycle node

| ID | Exact pytest node | Occurrence | Exact observed assertion/failure |
| --- | --- | --- | --- |
| C17 | `tests/test_nonlinear_state_lifecycle.py::test_force_control_store_matches_mapping_and_materializes_owned_snapshots` | 3.11/3.12/3.13 | expected `saved_state: 3, final_result: 1`; got those entries plus `explicit: 6` |

This node remains generic. Diagnosis must determine whether `explicit: 6` is a
truthful, newly visible ownership event or an unintended materialization. It
must not delete or ignore the counter merely to satisfy the old dictionary.

### 4.6 Python 3.12/3.13 shared `NLG-008` failures

| ID | Exact pytest node | Occurrence | Exact observed assertion/failure |
| --- | --- | --- | --- |
| V01 | `tests/test_beam_shell_verification.py::test_beam_shell_verification_report_separates_pass_and_xfail` | 3.12/3.13 only | expected report status `passed`; got `failed` |
| V02 | `tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]` | 3.12/3.13 only | expected relative error `< 0.06`; got `1.9648910185287414` |

Python 3.11 passes both. The 32-element ring case passes all three versions.
The beam/shell verification report includes the same `NLG-008` physical case,
so these failures are one shared physics/eigenpair diagnosis, not two unrelated
assertion changes.

Neither node may skip. The `0.06` threshold, analytical reference, mesh counts,
and report release semantics are frozen. No tolerance tuning is allowed.

## 5. Exact diagnosis read allowlist

Only these repository paths may be read during diagnosis:

- `pyproject.toml`
- `.github/workflows/ci.yml`
- `tests/test_advanced_s4_batches.py`
- `tests/test_generalized_section_api_workflows.py`
- `tests/test_corotational.py`
- `tests/test_impact_reduced_assembly.py`
- `tests/test_nonlinear_performance.py`
- `tests/test_nonlinear_state_lifecycle.py`
- `tests/test_recovery_batches.py`
- `tests/test_vectorized_hill48.py`
- `tests/test_beam_shell_verification.py`
- `tests/test_follower_pressure.py`
- `src/anysolver/jit_compiler.py`
- `src/anysolver/corotational.py`
- `src/anysolver/corotational_performance.py`
- `src/anysolver/nonlinear_performance.py`
- `src/anysolver/nonlinear_performance_bootstrap.py`
- `src/anysolver/nonlinear_performance_batch_b.py`
- `src/anysolver/nonlinear_performance_batch_c.py`
- `src/anysolver/recovery.py`
- `src/anysolver/vectorized_hill48.py`
- `src/anysolver/impact_reduced_assembly.py`
- `src/anysolver/nonlinear_state.py`
- `src/anysolver/beam_shell_verification.py`
- `src/anysolver/buckling.py`
- `src/anysolver/cylinder_benchmarks.py`
- `src/anysolver/assembly.py`
- `src/anysolver/matrix_assembly.py`
- `src/anysolver/boundary.py`
- `src/anysolver/nonlinear_static.py`
- `src/anysolver/arc_length.py`
- `src/anysolver/elements.py`
- `src/anysolver/fe_core.py`

No sibling repository is in the diagnosis read set. If a required owner path is
missing from this list, diagnosis stops and a plan amendment is required.

## 6. Read-only diagnosis sequence

### D0. Baseline and environment gates

Before any test or probe:

- Prove worktree HEAD and tree equal the accepted commit/tree.
- Prove worktree and index are clean.
- Prove the frozen 28 pre-existing worktrees are unchanged and the accepted
  correction worktree is the only 29th worktree.
- Prove the stable 36-ref oracle remains unchanged under the accepted TAB/SPACE
  canonicalization.
- Record Python, platform, NumPy, SciPy, pytest, Numba presence/version, and
  `JIT_ENABLED/JIT_DISABLED_REASON`.
- Refuse ambient source roots outside the accepted ANYsolver worktree.

These are read-only gates. Any mismatch stops diagnosis.

### D1. Static JIT-placement map

For `C01` through `C10`, record:

- exact current decorators and imports;
- exact compiled-only assertion;
- compiled implementation entry point;
- scalar oracle used by the same test;
- exact dedicated Numba job selection before correction;
- whether the node is absent from that selection.

For `C11`, record the backend, JIT, fallback, convergence, and analytical-circle
diagnostics in both modes.

No test edit is permitted.

### D2. Impact exclusion map

For `C12` through `C16`, capture in JIT and no-JIT modes:

- `active`;
- `fallback_reason`;
- `fallback_detail`;
- full ordered `exclusion_reasons`;
- identity/weighted transformation classification;
- material-history classification;
- beam formulation classification.

The diagnosis must show whether every semantic reason remains present when
`jit_unavailable` is primary. Production ordering is evidence, not an edit
target under this plan.

### D3. Nonlinear-state lifecycle map

For `C17`, capture persistent and mapping-fallback paths independently through
the registered lifecycle instrumentation artifact in Section 7.4:

- ordered materialization events by generation and element;
- reason and count for `explicit`, `saved_state`, and `final_result`;
- state keys and array ownership before solve, after each accepted increment,
  at snapshot creation, and at final result publication;
- `activated`, `eligible_batch_count`, `generation`, and
  `stale_token_error_count`;
- snapshot count and whether arrays share memory;
- equality of status, load factor, displacements, states, and serialized steps.

The instrument must record an ordered event sequence, not reconstruct order from
aggregate counters. The conclusion must classify `explicit: 6` as required truthful accounting,
duplicate accounting, or an unintended materialization. No counter is removed
or normalized during diagnosis.

### D4. `NLG-008` and ring eigenpair map

Run the same read-only observation protocol through the registered NLG-008
instrumentation artifact in Section 7.4 for 24- and 32-element rings and for
selected verification case `NLG-008`.

Capture these exact observables:

- Python/platform and deterministic model identity inputs;
- radius, thickness, height, material constants, pressure sign, and analytical
  reference `q_cr = 3*E*I/R^3` per unit axial width;
- node/element counts and exact 24/32 circumferential discretization;
- all boundary conditions, MPC equations, constrained DOFs, transformation
  dimensions/rank, and maximum constraint residual;
- unreduced and reduced elastic stiffness operator dimensions, finite-value
  checks, symmetry norm, and sign convention;
- follower-load stiffness operator dimensions, finite-value checks, symmetry
  norm, pressure derivative sign, and sign used in the eigenproblem;
- all finite candidate eigenvalues before selection, their ordering, real and
  imaginary parts, and duplicate/near-zero classification;
- residual norm for each retained eigenpair;
- selected eigenvalue, selected mode index, mode normalization, and reason for
  selection;
- analytical critical pressure/load factor and signed/absolute relative error;
- `NLG-008` result status, metrics, expected bounds, required evidence, and the
  exact child result that makes the aggregate report fail;
- repeat equality of operators, candidate eigenvalues, selected index, and
  residuals within one process, without making a performance claim.

The frozen lane boundary is exact:

- Ubuntu CPython 3.11.15, job `94603441514`: `V01` and both ring parameters
  passed in the real no-Numba `.[dev]` lane.
- Ubuntu CPython 3.12.13, job `94603441506`: `V01` failed and `V02[24-0.06]`
  failed with relative error `1.9648910185287414`; the 32-element parameter
  passed in the real no-Numba `.[dev]` lane.
- Ubuntu CPython 3.13.14, job `94603441528`: the same `V01` and
  `V02[24-0.06]` failures and the same 24-element relative error occurred; the
  32-element parameter passed in the real no-Numba `.[dev]` lane.

The diagnosis must compare these immutable lanes, but it must not re-query the
logs. Any new cross-version reproduction requires the exact fresh environments
and environment-manifest acceptance defined below; a single ambient interpreter
cannot establish the Python-version boundary.

## 7. Environment, instrumentation, commands, and evidence

### 7.1 Real environment rule

`FE_SOLVER_DISABLE_JIT` is not a supported ANYsolver switch and is prohibited.
No monkeypatch, import blocker, package shadow, renamed module, `python -S`
substitute, or simulated absence may qualify the no-Numba contract.

The immutable remote no-Numba provenance is:

| Lane | Exact interpreter origin from log | Python | pytest | Numba evidence |
| --- | --- | --- | --- | --- |
| U311 | `/opt/hostedtoolcache/Python/3.11.15/x64` | CPython 3.11.15 | 9.1.1 | import failed: package absent |
| U312 | `/opt/hostedtoolcache/Python/3.12.13/x64` | CPython 3.12.13 | 9.1.1 | import failed: package absent |
| U313 | `/opt/hostedtoolcache/Python/3.13.14/x64` | CPython 3.13.14 | 9.1.1 | import failed: package absent |

Those paths are historical hosted-runner evidence, not reusable local
interpreters. Any new probe must use a real, isolated environment with no
system-site packages and must be bound to one of these exact prospective roots:

- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.11.15-no-numba\Scripts\python.exe`
- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.12.13-no-numba\Scripts\python.exe`
- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe`
- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-numba\Scripts\python.exe`

These roots are registrations, not assertions that the environments currently
exist. Environment creation, dependency acquisition, and installation are not
authorized by this plan. Before any dynamic probe, a content-addressed
environment amendment must independently accept, for every used environment:

- fresh root and no `pyvenv.cfg` inheritance through system-site packages;
- exact CPython executable path, bytes, SHA-256, version, implementation, DLL,
  architecture, and platform;
- exact pip origin/version and complete freeze;
- exact versions, distribution metadata, file hashes, and origins for ANYsolver,
  NumPy, SciPy, pytest, and every imported dependency;
- ANYsolver origin under the accepted worktree or an exact immutable artifact;
- no editable/VCS/source origin outside the accepted graph;
- no-Numba lanes: no `numba` or `llvmlite` distribution and import produces the
  recorded package-absence result;
- JIT lane: exact `numba` and `llvmlite` versions/origins and
  `JIT_ENABLED is True` in a fresh process;
- exact hash-pinned offline inputs and install transcript;
- `pip check` success and no network during probe execution.

Exact package versions are deliberately not guessed from incomplete old logs.
Dynamic execution remains blocked until the environment amendment supplies and
binds those exact values and artifact hashes. Static reading may proceed after
this plan is accepted.

### 7.2 STATIC-S01 report and Stage-P evidence boundary

Stage S writes exactly one governance artifact via `apply_patch`:

`C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_REPORT_82A9DB28.md`

Its command ID is `STATIC-S01`. It is a content-addressed static report, not a
runtime transcript. Its required schema is:

- schema name and version `anysolver.no_numba_residual.static_report/1`;
- governing plan path and SHA-256;
- accepted commit and tree;
- exact frozen allowlist paths read and SHA-256 for each file;
- findings keyed by file and symbol, with fact/inference classification;
- exact production and SciPy qualified-call candidates for selected NLG-008;
- whether immutable evidence identifies actual lifecycle CI predecessors;
- proposed environment, instrumentation, initializer, runner, and command-manifest
  amendment paths, each explicitly marked uncreated or content-addressed;
- unresolved questions and narrowed claims;
- an attestation that no import, test, probe, environment action, run query,
  process launch, or source edit occurred.

The report does not embed its own hash. After `apply_patch`, its byte count,
LF/CR/BOM identity, and SHA-256 are reported externally for independent review.
No other Stage-S output, cache, temp path, transcript, partial, or manifest is
created.

The registered Stage-P evidence root `E` remains:

`C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28`

`E` and every parent component must satisfy the later accepted Stage-P
absent/direct/non-reparse preflight. Stage S has no dependency on `E`.

### 7.3 Pytest cache and fresh-process policy

Every pytest invocation must be a new process from one exact accepted
interpreter. Every invocation includes `-p no:cacheprovider` and one unique
absolute `--basetemp`.

Before each invocation, these exact task-owned paths must be absent, have a
canonical absolute parent under the evidence root, and have no reparse-point
component:

- the command's `--basetemp` path;
- `caches\<command-id>\numba`;
- `caches\<command-id>\pycache`;
- `caches\<command-id>\mpl`;
- `caches\<command-id>\xdg`;
- `caches\<command-id>\joblib`;
- `tmp\<command-id>`.

The process environment sets exact absolute values for `NUMBA_CACHE_DIR`,
`PYTHONPYCACHEPREFIX`, `MPLCONFIGDIR`, `XDG_CACHE_HOME`, `JOBLIB_TEMP_FOLDER`,
`TEMP`, and `TMP` to those command-owned paths. It sets
`PYTHONNOUSERSITE=1`, clears `PYTHONHOME` and `PYTHONPATH`, and does not set a
JIT-disabling variable. All paths and resulting residue are recorded and
preserved. Any pre-existing path, reparse point, outside-root resolution, or
unexpected cache path stops the command before Python starts.

### 7.4 Registered read-only instrumentation artifacts

These exact external paths are registered:

- `instruments\environment_probe_82a9db28.py`
- `instruments\impact_exclusion_probe_82a9db28.py`
- `instruments\lifecycle_event_probe_82a9db28.py`
- `instruments\nlg008_operator_probe_82a9db28.py`
- `instruments\selected_nlg008_report_probe_82a9db28.py`

No instrument exists or may execute under this plan revision. Static reading
must first establish the exact owner seams. Then a separate content-addressed
instrumentation amendment must create these files via apply_patch, freeze their
bytes/SHA-256/AST/import set/output schema, and prove:

- read-only imports from the accepted ANYsolver tree only;
- no source/test/workflow modification;
- no monkeypatch of numerical production behavior;
- no dependency install, network, child shell, hidden process, launcher,
  encoded command, or Defender exception;
- output opened with CreateNew/atomic semantics from Section 7.2;
- lifecycle hooks observe existing materialization calls and preserve original
  call order, arguments, returns, exceptions, and identity;
- NLG hooks observe assembled operators, constraints, eigenpairs, residuals,
  signs, references, and selection without changing arrays or solver choices;
- impact hooks observe both primary and full ordered exclusion diagnostics
  without changing production precedence.

The exact commands below remain blocked until that amendment supplies accepted
instrument hashes. This staged gate avoids pretending that `--showlocals` alone
can prove ordered events or operator/eigenpair ownership.

### 7.5 Frozen fresh-process command selections

The following are logical argv contracts. The environment amendment must render
them with the exact accepted interpreter paths and Section 7.3 environment.
No shell alias or ambient `python` is permitted.

#### G-COROT: standalone real no-Numba corotational (superseded by 7.7)

### 7.7 Final execution-safety supersession

This subsection supersedes every earlier execution example, generic environment
token, cache path, and lifecycle predecessor claim in this document. Earlier
classification and read-scope text remains evidence, but only the command IDs and
rules below can become executable after independent acceptance.

#### Frozen source roots and working directories

- Windows supplemental cwd:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`
- Ubuntu-equivalent primary cwd:
  `/opt/anyrelease/worktrees/ANYsolver-ci-six-failure-correction-82a9db28`
- Both roots must resolve to commit
  `82a9db28d67507c82ef15c631f582a0c3bf6740e` and tree
  `00b2b20691e73a05589b797b32352f1c760a2451` before any command.
- A command may run only from its frozen cwd. Repository/source paths are not
  writable inputs and no ambient checkout is eligible.

#### Final read-only source allowlist additions

The following paths are added to the diagnosis-only read allowlist:

- `src/anysolver/matrix_assembly.py`
- `src/anysolver/boundary.py`
- `src/anysolver/nonlinear_static.py`
- `src/anysolver/arc_length.py`
- `src/anysolver/constraint_audit.py`
- `src/anysolver/threading_policy.py`
- `src/anysolver/linalg.py`

No write authority follows from this addition.

#### Durable initializer and runner gate

Stage P may not begin until a separate content-addressed amendment creates and
independently accepts these previously absent plain Python artifacts outside the
absent Stage-P evidence root `E`:

- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\initialize_evidence_82a9db28.py`
- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\run_one_command_82a9db28.py`
- `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\command_manifest.json`

Stage S explicitly requires none of these artifacts.

That amendment must freeze bytes and SHA-256 for both programs and the complete
command manifest. Creation is CreateNew only. The runner must use an argv array,
`shell=False`, no nested shell, and one fresh child process per command. For every
command it must durably record before atomic finalization:

- command ID, exact argv, cwd, executable path/hash/version/origin, full inherited
  and overridden environment, UTC start/end, timeout, and host/platform identity;
- raw stdout and stderr byte paths, byte counts, and SHA-256 values;
- exit code or launch exception without coercion;
- root PID plus observed descendant PID/image/start/end/exit state, timeout state,
  and post-exit process-tree state;
- every preflight path identity, absent/non-reparse result, and whether any output
  was created.

A timeout or initializer/runner/report failure is terminal. No retry, cleanup, or
second command is permitted. Partial, transcript, stdout, stderr, cache, and process
evidence is preserved.

#### Exact command-to-evidence mapping

Evidence root `E` is exactly:

`C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28`

The complete command-ID set is:

`ENV-U311`, `ENV-U312`, `ENV-U313`, `ENV-JIT313`, `COROT-U311`,
`COROT-U312`, `COROT-U313`, `COROT-JIT313`, `COROT-INST-U311`,
`COROT-INST-U312`, `COROT-INST-U313`, `COROT-INST-JIT313`,
`IMPACT-U313`, `IMPACT-JIT313`, `IMPACT-INST-U313`,
`IMPACT-INST-JIT313`, `COMPILED-JIT313`, `LIFECYCLE-U313`,
`LIFECYCLE-INST-U313`, `NLG-TEST-U311`, `NLG-TEST-U312`,
`NLG-TEST-U313`, `NLG-REPORT-U311`, `NLG-REPORT-U312`,
`NLG-REPORT-U313`, `NLG-OP-U311`, `NLG-OP-U312`, and `NLG-OP-U313`.

For each ID `X`, the mapping is uniquely and literally:

| Item | Exact path |
|---|---|
| pytest basetemp | `E\commands\X\basetemp` |
| NUMBA cache | `E\commands\X\cache\numba` |
| XDG cache | `E\commands\X\cache\xdg` |
| matplotlib cache | `E\commands\X\cache\matplotlib` |
| Python cache prefix | `E\commands\X\cache\pycache` |
| joblib cache | `E\commands\X\cache\joblib` |
| TEMP | `E\commands\X\tmp\temp` |
| TMP | `E\commands\X\tmp\tmp` |
| transcript | `E\commands\X\transcript.jsonl` |
| stdout | `E\commands\X\stdout.bin` |
| stderr | `E\commands\X\stderr.bin` |
| process tree | `E\commands\X\process-tree.json` |
| result partial | `E\commands\X\result.json.partial` |
| result final | `E\commands\X\result.json` |

Here `E` and `X` are deterministic notation in this plan, not executable
placeholders: the accepted command manifest must render and hash every resulting
absolute path. All mapped roots and files must be absent before initialization;
each ancestor must be a direct non-reparse directory. Each command gets its own
mapping even where pytest basetemp is unused. The runner sets
`NUMBA_CACHE_DIR`, `XDG_CACHE_HOME`, `MPLCONFIGDIR`,
`PYTHONPYCACHEPREFIX`, `JOBLIB_TEMP_FOLDER`, `TEMP`, and `TMP` to that
command's mapped paths and records them. All Python argv include `-B -I` in
that order; all pytest argv include
`-p no:cacheprovider`. Nothing is removed after a run.

#### Environment provenance and NLG platform boundary

`FE_SOLVER_DISABLE_JIT` is unsupported and prohibited. No environment variable,
module masking, import hook, or monkeypatch may simulate package absence. The
U311/U312/U313 lanes must prove a real failed `numba` distribution lookup and
import in a fresh process. JIT313 must prove the exact accepted Numba distribution
and import origin outside all repositories.

Before any Stage P command, the environment amendment must bind exact SHA-256,
version, and origin for CPython, pytest, NumPy, SciPy, Numba when present, and the
loaded BLAS/LAPACK implementation and libraries. It must also bind a fully hashed
offline artifact/lock input for each lane. Null, range-only, ambient, editable,
VCS, or source-shadowed identities fail closed.

The NLG-008 primary reproduction is Ubuntu-equivalent U311/U312/U313, matching
the hosted lane Python patch versions 3.11.15, 3.12.13, and 3.13.14 and its exact
resolved NumPy/SciPy/BLAS stack. Those exact dependency values are not inferred
or guessed here: Stage P remains blocked until the separately reviewed environment
manifest freezes them from accepted immutable artifacts. Windows commands below
are supplemental diagnostics only and cannot qualify or overturn the Linux result.

#### Corotational lane observations and exact cells

Historical immutable jobs `94603441514`, `94603441506`, and `94603441528`
show the corotational node failed in U311, U312, and U313 respectively. The
retained logs establish test failure in each no-Numba lane, but do not by
themselves prove which physical assertion or diagnostic field was first causal.
The instrument must therefore record the physical circle/displacement residual,
selected backend, `JIT_ENABLED`, fallback reason, and exception unchanged.

The exact supplemental fresh-process corotational pytest cells are:

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.11.15-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\COROT-U311\basetemp tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.12.13-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\COROT-U312\basetemp tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\COROT-U313\basetemp tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle
```

The accepted instrumentation amendment must add
`corotational_backend_probe_82a9db28.py` and bind its exact argv to each of
`COROT-INST-U311`, `COROT-INST-U312`, `COROT-INST-U313`, and
`COROT-INST-JIT313`. It may observe only the named test setup and production
calls, preserving arguments, results, and exceptions.

#### Impact and lifecycle instrumentation binding

The accepted instrumentation amendment must bind
`impact_exclusion_probe_82a9db28.py` to the exact `IMPACT-U313` and
`IMPACT-JIT313` invocations and output through `IMPACT-INST-U313` and
`IMPACT-INST-JIT313`. It records JIT state, primary fallback reason, every
semantic exclusion reason, and the unchanged public result.

Only the standalone lifecycle node is in scope. No predecessor-sequence command,
artifact, comparison, or ordered-predecessor claim exists in this plan. If
STATIC-S01 finds immutable CI-ordering evidence, a later content-addressed
amendment may propose the actual predecessors. `lifecycle_event_probe_82a9db28.py`
is bound only to the standalone invocation through `LIFECYCLE-INST-U313`. It
records event order, reason, owner, state identity, materialization count, and
result without changing code or execution order.

#### NLG-008 transparent instrumentation

Selected 24- and 32-element NLG-008 pytest cells are the only primary test
surface. The 130-case beam report remains prohibited. Static Stage S must first
identify the exact production and SciPy callable qualified names actually reached
by these two cases. A content-addressed instrumentation amendment must then freeze
those names and one transparent observation wrapper per call. Each wrapper runs
once, forwards the original arguments unchanged, calls the original exactly once,
returns or raises the original result/exception unchanged, and records argument,
result, exception, dtype/shape/sign, operator, constraint, root, residual, and
eigenpair metadata that the original call exposes.

Reconstructing an operator, root, residual, eigenpair, or constraint result in a
probe is explicitly not production evidence. If a named call cannot be observed
without semantic change, the associated claim is removed rather than inferred.
The Linux U311/U312/U313 commands are frozen only in the later accepted
environment/instrument command manifest; the concrete Windows commands below are
supplemental and use the same selected 24/32 test inputs.

#### Sole authoritative stage order

1. Independently accept this plan hash.
2. Run Stage S read-only against only the frozen allowlist and write only
   `STATIC-S01` via `apply_patch`.
3. Independently accept content-addressed `STATIC-S01` plus the separately frozen
   environment, instrumentation, initializer, runner, and command-manifest
   amendments.
4. Obtain separately authorized terminal accounting for old GitHub run
   `31746877870`.
5. Independently accept all Stage-P artifacts and exact absent/direct/non-reparse
   path preflights.
6. Obtain an exclusive PERF lease for the exact Stage-P command subset.
7. Run Stage P.

No source edit, test, probe, runner, environment creation, run query, integration,
push, cleanup, or PERF action is authorized by this subsection.

Run once in each accepted U311/U312/U313-equivalent no-Numba environment as a
fresh process. Resource envelope per lane: less than 750 MiB, up to 3 minutes,
no GPU/network. Preserve first result.

#### G-IMPACT: five generic real no-NumBa exclusions

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\IMPACT-U313\basetemp tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_selector_reports_all_static_exclusions tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hardening_curve] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hill_yield] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam2] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam3]
```

Run in one accepted no-Numba environment, followed in the same fresh process by
the accepted impact instrumentation only if the instrumentation amendment
defines that combined argv. Resource envelope: less than 750 MiB, up to 3
minutes, no GPU/network.

#### J-IMPACT: five generic JIT exclusions

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\IMPACT-JIT313\basetemp tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_selector_reports_all_static_exclusions tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hardening_curve] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_ordinary_plastic_material_history[hill_yield] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam2] tests/test_impact_reduced_assembly.py::test_direct_reduced_impact_excludes_element_owned_fiber_plasticity[beam3]
```

Expected current result: 5 passed. Resource envelope: less than 1 GiB, up to 5
minutes because first-use Numba compilation may occur. PERF lease required.

#### J-COMPILED: exact ten compiled-only nodes

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\COMPILED-JIT313\basetemp tests/test_advanced_s4_batches.py::test_nonlinear_orthotropic_s4_batch_matches_scalar_force_and_tangent tests/test_advanced_s4_batches.py::test_nonlinear_generalized_s4_batch_matches_scalar_and_state tests/test_generalized_section_api_workflows.py::test_generalized_shell_uses_installed_extended_batch_diagnostic tests/test_nonlinear_performance.py::test_mixed_initial_field_shell_batch_accelerates_initialized_elastic_element tests/test_recovery_batches.py::test_compiled_isotropic_s4_matches_scalar_oracle_for_warped_global_output tests/test_vectorized_hill48.py::test_global_newton_solution_and_iteration_count_match_scalar_path tests/test_vectorized_hill48.py::test_global_arc_length_path_matches_scalar_path tests/test_vectorized_hill48.py::test_compiled_nonconvergence_falls_back_then_preserves_fail_closed_error tests/test_vectorized_hill48.py::test_kernel_exception_is_an_observable_whole_batch_scalar_fallback tests/test_vectorized_hill48.py::test_invalid_analytical_row_and_requested_numerical_tangent_are_counted
```

Expected current result: 10 passed. Resource envelope: less than 1.5 GiB, up
to 10 minutes, no GPU/network. PERF lease required.

#### J-COROT: standalone fresh-process JIT corotational

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\COROT-JIT313\basetemp tests/test_corotational.py::test_corotational_beam_cantilever_rolls_up_to_analytic_circle
```

Expected current result: 1 passed with compiled backend and no fallback.
Resource envelope: less than 1 GiB, up to 5 minutes. PERF lease required if the
JIT cache is cold.

#### L-STANDALONE: standalone lifecycle no-Numba

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\LIFECYCLE-U313\basetemp tests/test_nonlinear_state_lifecycle.py::test_force_control_store_matches_mapping_and_materializes_owned_snapshots
```

Run in a fresh no-Numba process with no preceding test. The accepted lifecycle
instrument writes through the unique `LIFECYCLE-INST-U313` mapped partial/final
result. Resource envelope: less than 750 MiB, up to 3 minutes.

#### NLG-PY311, NLG-PY312, NLG-PY313

Each accepted real no-Numba interpreter runs a separate fresh process with the
same exact selection:

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.11.15-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-TEST-U311\basetemp tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06] tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[32-0.035]
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.12.13-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-TEST-U312\basetemp tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06] tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[32-0.035]
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I -m pytest -p no:cacheprovider -vv --showlocals --basetemp C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-TEST-U313\basetemp tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06] tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[32-0.035]
```

The unfiltered
`test_beam_shell_verification_report_separates_pass_and_xfail` node is
prohibited because it runs the full 130-case programme. Correlation uses only
the accepted `selected_nlg008_report_probe_82a9db28.py`, invoked as:

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.11.15-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\selected_nlg008_report_probe_82a9db28.py --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-REPORT-U311\result.json.partial
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.12.13-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\selected_nlg008_report_probe_82a9db28.py --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-REPORT-U312\result.json.partial
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\selected_nlg008_report_probe_82a9db28.py --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-REPORT-U313\result.json.partial
```

Operator/eigenpair evidence uses only:

```text
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.11.15-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\nlg008_operator_probe_82a9db28.py --circumferential 24 32 --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-OP-U311\result.json.partial
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.12.13-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\nlg008_operator_probe_82a9db28.py --circumferential 24 32 --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-OP-U312\result.json.partial
C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\envs\cpython-3.13.14-no-numba\Scripts\python.exe -B -I C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\instruments\nlg008_operator_probe_82a9db28.py --circumferential 24 32 --case NLG-008 --output C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_82A9DB28\commands\NLG-OP-U313\result.json.partial
```

Expected immutable boundary to reproduce or explain: 3.11 passes both ring
parameters and selected NLG-008; 3.12/3.13 fail the 24-element case with the
recorded relative error while 32 passes. Resource envelope per version: less
than 1.5 GiB, up to 10 minutes. PERF lease required. No full report node runs.

### 7.6 Execution staging and old-run gate

Section 7.7's sole authoritative stage order supersedes this earlier staging
text. Stage S needs only acceptance of this plan. It reads only the frozen
allowlist and writes only `STATIC-S01` via `apply_patch`; it performs no test,
import, probe, environment action, process launch, run query, or PERF work.

Every dynamic command belongs to Stage P and remains blocked through steps 3-6
of the sole authoritative order. No command is retried or substituted after
failure.

## 8. Evidence and preservation

For Stage S, preserve only the content-addressed `STATIC-S01` report and its
externally reported identity. No runtime transcript, manifest harness, cache,
basetemp, environment, or process evidence is created.

For a later authorized Stage P action:

- preserve first exit/result; no tuning or retry;
- record exact argv, cwd, interpreter/environment identity, wall time,
  pass/fail/skip, selected-node result, and resource envelope;
- hash and link every accepted per-command runner output through the Stage-P
  manifest;
- prove accepted correction worktree remains clean at `82a9db2`;
- prove 28 frozen worktrees plus the accepted 29th and 36 durable refs remain
  exact;
- inventory every basetemp, Numba cache, Python cache, Matplotlib/XDG/joblib
  cache, and task TEMP/TMP path without deleting it;
- preserve all old qualification/failure evidence;
- stop on unexpected path, process, network access, state change, or artifact.

No cleanup is authorized.

## 9. Prohibited scope

- No source, test, workflow, metadata, documentation, or plan-adjacent code edit.
- No commit, amend, merge, integration, ref mutation, fetch, push, dispatch,
  rerun, cancellation, tag, release, package build, or publication.
- No full test suite.
- No full 130-case beam/shell verification programme.
- No broad cross-version matrix.
- No benchmark, profiler, scaling, stress, or performance claim.
- No generic `.[dev,numba]` change.
- No Numba dependency-floor or default change.
- No production impact-exclusion ordering change.
- No follower-pressure tolerance, mesh, analytical reference, sign, or
  eigenvalue-selection change.
- No assertion weakening, blanket skip, whole-file skip, or xfail conversion.
- No cleanup of worktrees, refs, caches, basetemps, logs, reports, or old
  first-failure artifacts.
- No execution of retired PowerShell scripts or launchers and no Defender
  exception, restore, exclusion, or workaround.

## 10. Required diagnosis verdict

The completion packet must state, for each of the 19 exact nodes:

- per-version occurrence;
- current JIT marker/branch;
- compiled-only versus generic ownership;
- exact observed assertion;
- exact owner path;
- proposed later action: individual skip plus exact Numba selection, JIT-aware
  generic assertion, test expectation correction, or production investigation;
- focused evidence obtained and remaining uncertainty.

It must separately report:

- the exact ten-node compiled selection and J1 result;
- corotational JIT/no-JIT backend and physical parity;
- complete ordered impact exclusions in both modes;
- lifecycle materialization event order and ownership conclusion;
- 24/32 ring and `NLG-008` operators, eigenpairs, residuals, constraints, signs,
  analytical reference, selected-mode logic, and Python-version boundary;
- all preservation gates and any basetemp residue.

## 11. Anticipated later correction-amendment gate

Diagnosis grants no automatic edit authority. Before any correction, a new
content-addressed amendment must be independently accepted and must freeze:

- exact base commit/tree, branch/worktree, and path allowlist;
- exact ten individual skip decorators and dedicated Numba node selection;
- exact corotational dual-mode assertions;
- exact five impact JIT-aware expectations with no production diff;
- lifecycle correction ownership and expected counters;
- `NLG-008` root cause and the smallest physics/eigenpair correction, with no
  tolerance tuning;
- exact focused no-JIT and JIT tests;
- independent exact-diff review and preservation gates;
- one direct-child commit boundary;
- separate integration/push/remote-CI plan and PERF lease.

Until that amendment is accepted, `82a9db2` remains the accepted correction tip
and all diagnosis is read-only.
