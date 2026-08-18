# ANYsolver no-Numba residual failure static report

```yaml
schema: anysolver.no_numba_residual.static_report/1
command_id: STATIC-S01
scope: static_read_only
governing_plan: C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_DIAGNOSIS_PLAN.md
governing_plan_sha256: 7472B4ECE6430B1B13BE24BCA3C24DA5074DC458BC5B92EB7E65C8C7F1AB1179
accepted_commit: 82a9db28d67507c82ef15c631f582a0c3bf6740e
accepted_tree: 00b2b20691e73a05589b797b32352f1c760a2451
source_root: C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction
runtime_actions: none
stage_p_authorized: false
```

## 1. Scope and method

`STATIC-S01` read only the 36 unique files in the accepted plan's frozen
allowlist. File bytes were used to calculate SHA-256 and to extract the named
test assertions, diagnostics, owner policies, and candidate NLG-008 call sites.

No source, test, workflow, metadata, or dependency file was edited. No Python
interpreter, repository import, test, probe, environment builder, Git command,
GitHub query, benchmark, profiler, or cleanup action ran. The only process
transport used was the fixed read-only PowerShell host behind the file-reading
tool; it read bytes and computed hashes without executing repository code.

This report is the only Stage-S artifact. It was created with `apply_patch`.
No runtime transcript, cache, basetemp, partial, environment, instrument, runner,
or Stage-P evidence root was created.

Two retained static-extraction displays were truncated after the allowlist files
had been read. No source was reopened after the Boss convergence directive.
Details whose exact supporting lines were not durably retained are classified
`evidence_limited`, not fact. Any later recovery requires independent acceptance
of this exact uncreated Stage-S addendum:

`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_EVIDENCE_LIMIT_ADDENDUM.md`

## 2. Frozen allowlist identities

| Path | Bytes | SHA-256 |
|---|---:|---|
| `pyproject.toml` | 1,557 | `97F272E8381506BAE1B9331C4AB7AC716306DDE8658219A32B8D119DB52CF74A` |
| `.github/workflows/ci.yml` | 16,125 | `DF73091A8C0CE5F8DFE8361C3FDB3F239FCA75B06128021A4FA0C7BCC18B6931` |
| `tests/test_advanced_s4_batches.py` | 12,068 | `E30C1622F2EBE0EE6853F1F79991B09086B233F0D9B99FAAFAB65447C4688209` |
| `tests/test_generalized_section_api_workflows.py` | 7,210 | `663E52C1AA5A13938A219E2F8725562F2FEEF997B4CDC3C27B8C85FBC1B5A8B7` |
| `tests/test_corotational.py` | 18,640 | `95E47180C6CE3A95C20648338720BC48EF57B906D8CBCF205B2BB6C8347B3E63` |
| `tests/test_impact_reduced_assembly.py` | 10,537 | `61F53E1EAE3D0DA7672018FA70BB7C3F5D1D2FB6BE1163738FFF790E06F0E230` |
| `tests/test_nonlinear_performance.py` | 17,519 | `CF94531EF34DD9FD7627F34634E2ABCA034DE58099FF16364F92E3E729C2AC02` |
| `tests/test_nonlinear_state_lifecycle.py` | 14,016 | `2952F96CD0F6E1296C154EA9FD720F36F45DE794CB046B07F8663C6E6FB340FD` |
| `tests/test_recovery_batches.py` | 6,218 | `52956E5156EB3166F21CA7E938E1FD1B0FFA9E07FF12832869D33BF3D9E1294D` |
| `tests/test_vectorized_hill48.py` | 17,131 | `1F9087448472ECC5660BD780D54906C458451E65E28FABE9614DB1F76960DD3B` |
| `tests/test_beam_shell_verification.py` | 11,442 | `5E1DFB37009AE1C1B7E4517EE33E11A37102D5B086D1A4963BE23562A6D821FB` |
| `tests/test_follower_pressure.py` | 21,631 | `3CC5B27B8D6E7722B56DED2C5782A2173A0FADF0D535392B23844577F306E59F` |
| `src/anysolver/jit_compiler.py` | 4,009 | `0616785C369052FD3AE8704FCD6DBF528B91A1977C93AC06E67C11DBF9BE8912` |
| `src/anysolver/corotational.py` | 21,290 | `5C778F42A6F2A87D7BDD719AC16DEED735B0C8CB5CF3BEACC4F49B5F4CFC9195` |
| `src/anysolver/corotational_performance.py` | 5,526 | `3972E99C80B7C7CF0BF369980EEFC70C89307350C0BBDB3E1F6A96115011991B` |
| `src/anysolver/nonlinear_performance.py` | 66,871 | `FDD372DAF3EC0C6B7C8C930CA1C994E8FBD2213CE22C7AA1304E2D17F1E418FA` |
| `src/anysolver/nonlinear_performance_bootstrap.py` | 6,527 | `A348678E631C725632462E44ADDB8E8978B76DA6855E961CAA248112CDE28B02` |
| `src/anysolver/nonlinear_performance_batch_b.py` | 46,526 | `0C28309BF7E5FEA363920BADC065ACA3C52C101019C17E6A756C9C1AA70CFF01` |
| `src/anysolver/nonlinear_performance_batch_c.py` | 29,986 | `6A4768CBBD6E8497C78B8CB691349DFE1588ADD0FB33908B8BA0B638E21F1402` |
| `src/anysolver/recovery.py` | 121,502 | `63A4D96FD5325F635792CCEF0376BA5B66A0CB5583B3201A1BF080EB44C172F6` |
| `src/anysolver/vectorized_hill48.py` | 32,375 | `8000B771B6C7011E96CDC81D71F00F98F06FB75C3C0211F2B0FB1BB3CC67E41C` |
| `src/anysolver/impact_reduced_assembly.py` | 10,558 | `1CF478E0FEF8ABA265FA8BDDC7D2FE0B2CC36D08388CE5E53C8E2DDA559FB16C` |
| `src/anysolver/nonlinear_state.py` | 62,898 | `A23E98F860957317E17A3A9EA75D81D33829FE723A557E90FA656E80EAACB94B` |
| `src/anysolver/beam_shell_verification.py` | 222,184 | `440B6903CA274E1EB7BC76BB6625029ACD3B4733F23440FBF83D705B28AE68F9` |
| `src/anysolver/buckling.py` | 25,404 | `8382E1340806057D1EF1788204051D56EC63F273E95D42BFB65996A816395F3A` |
| `src/anysolver/cylinder_benchmarks.py` | 14,675 | `527C4B95C0258D86E4CAE978415E0C8744338EF2CAA9CE88E3336D297514547B` |
| `src/anysolver/assembly.py` | 52,151 | `0526EE549D03A52AABD1EED4ACD56051A05DAF647D0845EB5C1A43807C4E1FA2` |
| `src/anysolver/matrix_assembly.py` | 42,988 | `08FDA48B505836114734073B92F7E6ECAE4FD21F0FE91AD399C19CE84222FC92` |
| `src/anysolver/boundary.py` | 24,379 | `4957C0F04874301674E562257E6549D4A39834C587CC644D2B1C4AF886F2B70D` |
| `src/anysolver/nonlinear_static.py` | 140,393 | `2BBFDEE1951D33B73B61C37B47ABC6C25EFF3BB17641D70C322D91F4393E7663` |
| `src/anysolver/arc_length.py` | 53,306 | `1B18B06E4E10ACB63CD293E076CFD184EEFBFF2D6EB4BEAD9959397F6F7B57FB` |
| `src/anysolver/elements.py` | 195,057 | `72CA40278AF27044E2DFA3EC63BE049B505F597192ADD3494A23E4759785358D` |
| `src/anysolver/fe_core.py` | 17,827 | `1B608B6C1F5619A84C1138F94ABB6D1DA95A48025BB2537F4D2CB638B6E3B8EF` |
| `src/anysolver/constraint_audit.py` | 24,184 | `229E3FA9DB27A5E55A4118D237BF53ADC537E10C93BFBDD4EE1E7A19EAB46DDA` |
| `src/anysolver/threading_policy.py` | 16,525 | `A6A3E576C4140C230EB2997A1F0170C707429E00A38BCBF6B6D7BCF02E88A4C1` |
| `src/anysolver/linalg.py` | 36,312 | `0EC810A426488518217597FF7C4C05B37F1BECA50EA1FB885927658820C38BC6` |

## 3. Fact-versus-inference findings

| ID | Class | Static finding | Evidence | Consequence |
|---|---|---|---|---|
| `S-F01` | Fact | Numba is optional, not a base dependency. Base requirements are NumPy `>=1.26`, SciPy `>=1.11`, and threadpoolctl `>=3.5`; the Numba extra is `numba>=0.59`. | `pyproject.toml:26-35` | A real no-Numba lane must omit the distribution; an environment variable cannot model this contract. Exact resolved package and BLAS versions remain a Stage-P environment-manifest requirement. |
| `S-F02` | Fact | Generic CI is the only full-suite lane. It covers Windows and Ubuntu on Python 3.11-3.14, installs `.[dev]`, and runs bare `python -m pytest`. | `.github/workflows/ci.yml:8-53` | Generic tests must remain valid without Numba. Adding the Numba extra to this lane would hide fallback defects. |
| `S-F03` | Fact | The dedicated Numba matrix covers the same OS/Python dimensions but runs only `test_batch_b_activation.py`, `test_nonlinear_performance_batch_b.py`, and `test_nonlinear_performance_batch_c.py`. | `.github/workflows/ci.yml:283-327` | None of the exact ten compiled-only residual nodes is currently selected by the dedicated lane. A later correction must add the exact nodes, not whole broad files. |
| `S-F04` | Fact | `jit_compiler` treats Numba import failure or absence as a public Python-backend diagnostic. `JIT_ENABLED`, `JIT_BACKEND`, and `JIT_DISABLED_REASON` are explicit. | `src/anysolver/jit_compiler.py:7-8,39-68` | No-JIT expectations should branch on public diagnostics; fake JIT-disable variables remain invalid evidence. |
| `S-F05` | Fact | C01/C02 install nonlinear optimizations and unconditionally assert orthotropic/generalized fast-path counts. C03 similarly expects a generalized fast-path count after installation. | `tests/test_advanced_s4_batches.py:183-236`; `tests/test_generalized_section_api_workflows.py:167-176` | These exact nodes are compiled-only qualification surfaces and need no-JIT skips plus exact Numba-lane inclusion. |
| `S-F06` | Fact | C05 unconditionally expects recovery metadata `recovery_backend == "compiled_isotropic_s4"`. C06/C07 require positive compiled call/point counts before they monkeypatch JIT off to compare scalar results. | `tests/test_recovery_batches.py:154-181`; `tests/test_vectorized_hill48.py:277-369` | These are not generic fallback assertions. Their compiled preconditions must be explicit. |
| `S-F07` | Fact | C08-C10 assert whole-batch fallback and analytical/numerical-tangent diagnostics around compiled-kernel behavior. | `tests/test_vectorized_hill48.py:446-544` | Their skip boundary is individual-node JIT availability, while the scalar fallback assertions remain unchanged in JIT lanes. |
| `S-I01` | `evidence_limited` | C04 and the batch-backed C01-C03 paths appear to belong to the same compiled-only correction class because their retained assertions require accelerated-element or fast-path diagnostics after installing optimization hooks. | `tests/test_nonlinear_performance.py:249-264`; C01-C03 evidence above; deeper owner-symbol output was not durably retained | The exact decorator/entry-point map requires the named Stage-S evidence-limit addendum before an edit plan. No source behavior change is proposed. |
| `S-F08` | Fact | The corotational circle node asserts successful completion, activated rotated tangent, `fallback_reason is None`, and analytical tip rotation/displacements. It has no no-JIT branch in the target function. | `tests/test_corotational.py:172-184` | The physical assertions stay generic, but backend/fallback expectations must become dual-mode. A standalone JIT and U311/U312/U313 no-Numba cell is required later. |
| `S-F09` | Fact | Corotational diagnostics expose `jit_enabled` and `fallback_reason` directly from `JIT_ENABLED` and `JIT_DISABLED_REASON`. | `src/anysolver/corotational_performance.py:141-155` | Transparent instrumentation can observe the existing public diagnostic without changing production execution. |
| `S-F10` | Fact | The five impact tests now prepend `jit_unavailable` only when `not JIT_ENABLED`, preserving all semantic exclusion reasons. Production likewise appends `jit_unavailable` first and retains the complete exclusion tuple. | `tests/test_impact_reduced_assembly.py:119-145,180-233`; `src/anysolver/impact_reduced_assembly.py:185-225` | The accepted `82a9db2` test correction is aligned. No production impact-order change is indicated by static evidence. |
| `S-F11` | Fact | The lifecycle node expects materialization reasons `{saved_state: len(snapshots), final_result: 1}`. The state API default is `EXPLICIT`; nonlinear static explicitly uses `SAVED_STATE` for snapshots and `FINAL_RESULT` for final materialization. | `tests/test_nonlinear_state_lifecycle.py:120-172`; `src/anysolver/nonlinear_state.py:70-75,726-767,1540-1543`; `src/anysolver/nonlinear_static.py:500-501,1492-1499` | The observed extra `explicit` count can arise only from a call using the default or explicit policy, but static evidence does not identify its runtime order or frequency. Standalone event instrumentation is required. |
| `S-F12` | Fact | No frozen allowlist artifact establishes the actual ordering of CI tests before the lifecycle node. | Full frozen allowlist | No predecessor-sequence claim or probe can be frozen from Stage S. The lifecycle scope remains standalone. |
| `S-F13` | Fact | The broad beam/shell test calls `run_beam_shell_verification()` and asserts aggregate release semantics. NLG-008 is one case in that programme. | `tests/test_beam_shell_verification.py:47-103`; `src/anysolver/beam_shell_verification.py:268,312` | Running this node would execute the full programme and remains prohibited. Only the selected follower-pressure node is eligible later. |
| `S-F14` | Fact | The selected ring test imports `solve_eigenvalue_buckling`, builds follower-pressure cases, calculates `3D/r^3`, compares critical load by relative error, and permits dense fallback. | `tests/test_follower_pressure.py:9,371-429` | Stage P must preserve the 24/32 inputs, analytical reference, and threshold while recording the actual solver branch. |
| `S-F15` | Fact | Follower pressure is assembled from the current configuration with an exact generally nonsymmetric tangent. The matrix assembly exposes load-vector, follower-tangent, and geometric-stiffness assembly. | `src/anysolver/boundary.py:323-404,448-489`; `src/anysolver/matrix_assembly.py:521,577-719,759-918` | Instrumentation must observe the production load, tangent, and geometric-stiffness calls rather than reconstructing them. |
| `S-F16` | Fact | `solve_eigenvalue_buckling` imports SciPy dense and sparse linalg, applies constraint transformation, and rejects unsupported nonsymmetric follower pencils. | `src/anysolver/buckling.py:19-25,206-324` | The exact dense/sparse SciPy function selected for the 24- and 32-element cases is a required runtime observation, not a static conclusion. |
| `S-F17` | Fact | Constraint audit, native threadpool policy, and SciPy SuperLU factorization are explicit owner seams. | `src/anysolver/constraint_audit.py:402,487,547`; `src/anysolver/threading_policy.py:13-21,234-362`; `src/anysolver/linalg.py:30-32,154-167,840-927` | The environment manifest must pin threadpool/BLAS identity; instrumentation must not bypass constraint or thread-policy owners. |
| `S-I02` | `evidence_limited` | The Python-version sensitivity of NLG-008 may originate in dense/sparse eigenbranch selection, BLAS/LAPACK implementation, assembled operator differences, constraint transformation, or eigenpair ordering/sign handling. | Facts `S-F14` through `S-F17`; historical 3.11 pass and 3.12/3.13 24-element failure ledger; exact branch lines were not durably retained | Static evidence cannot choose among these causes. Exact Ubuntu-equivalent environments and transparent one-call instrumentation are mandatory. |

## 4. Residual-node disposition from static evidence

| Group | Nodes | Static disposition |
|---|---|---|
| Compiled-only | `C01-C10` | Later correction may skip each individual node iff `not JIT_ENABLED` and must add those exact ten nodes to the dedicated Numba selection. No whole-file skip or generic-lane Numba install. |
| Dual-mode corotational | `C11` | Physical circle/displacement assertions remain generic. Backend and fallback diagnostics require explicit real no-Numba and JIT expectations. |
| Generic impact | `C12-C16` | Current accepted tests already branch on JIT availability while preserving semantic exclusions. No production change indicated. |
| Generic lifecycle | `C17` | Keep generic. Diagnose only the standalone materialization event stream; no synthetic predecessor claim. |
| NLG-008 | `C18-C19` | Keep generic with no skip or tolerance change. Reproduce selected 24/32 cases in pinned Ubuntu-equivalent 3.11/3.12/3.13 environments and observe the production eigen path. |

## 5. Exact NLG-008 call candidates for the instrumentation amendment

These are candidates, not proof that every call is reached by both selected
parameterizations. The instrumentation amendment must name only calls confirmed
from the selected production path and must remove unconfirmed candidates.

| Candidate qualified name | Classification | Static basis |
|---|---|---|
| `anysolver.buckling.solve_eigenvalue_buckling` | Fact: selected public entry point | Imported by `tests/test_follower_pressure.py:11`; selected node at lines 371-429 invokes the buckling solve. |
| `anysolver.assembly.build_constraint_transformation` | Fact: buckling owner call | Imported and used by `src/anysolver/buckling.py:23,271-280`. |
| `anysolver.constraint_audit.constraint_residual_summary` | Fact: buckling diagnostic owner | Imported by `src/anysolver/buckling.py:25`. |
| `anysolver.matrix_assembly.assemble_geometric_stiffness_matrix` | Fact: documented buckling operator owner | Defined at `src/anysolver/matrix_assembly.py:577`; referenced by the buckling contract at `src/anysolver/buckling.py:227-230`. |
| `anysolver.matrix_assembly.assemble_load_vector` | Fact: follower load owner | Defined at `src/anysolver/matrix_assembly.py:759`; follower branches are at lines 767-918. |
| `anysolver.boundary.LoadCase._consistent_pressure_load` | Fact: production pressure load | `src/anysolver/boundary.py:323-361,481-489`. |
| `anysolver.boundary.LoadCase._consistent_pressure_tangent` | Fact: production pressure tangent | `src/anysolver/boundary.py:364-404`. |
| `scipy.linalg.eigh` or another `scipy.linalg` eigen entry point | `evidence_limited`: dense branch candidate | `src/anysolver/buckling.py` imports `scipy.linalg`; the exact callable line was not durably retained and must be recovered only through the named Stage-S addendum or observed later. |
| `scipy.sparse.linalg.eigsh` or another sparse eigen entry point | `evidence_limited`: sparse branch candidate | `src/anysolver/buckling.py` imports `scipy.sparse.linalg`; the exact callable line and branch were not durably retained. |
| `numpy.linalg.eigh` in element stabilization | Fact in source, relevance unproven | `src/anysolver/elements.py:1468`; do not instrument unless selected-path tracing proves it is reached. |
| `anysolver.linalg.factorize` / `FactorizationHandle.solve` | Fact in nonlinear solvers, relevance unproven | Used by nonlinear static and arc length; do not treat as NLG-008 evidence unless selected-path tracing proves reachability. |
| `threadpoolctl.threadpool_limits` / `threadpool_info` | Fact: execution-environment owner | `src/anysolver/threading_policy.py:13-21,141-144,234-362`; observe environment identity, not physics semantics. |

The later wrapper must forward original args unchanged, invoke the original once,
and preserve the exact return or exception. Reconstructed operators, roots,
residuals, constraints, or eigenpairs are not evidence.

## 6. Lifecycle ordering evidence

`STATIC-S01` found no immutable file in the allowlist that records the real test
execution order preceding `C17`. The only source-backed lifecycle facts are the
standalone test expectations and the three materialization policies. Therefore:

- `lifecycle_order_evidence` is `absent`;
- no predecessor sequence is proposed;
- `LIFECYCLE-INST-U313` remains a standalone event probe only;
- any later predecessor proposal requires a separately accepted immutable CI
  ordering source and a plan amendment.

## 7. Required later amendments and artifacts

All entries below are uncreated and unauthorized by Stage S.

| Artifact/amendment | Required content | Status |
|---|---|---|
| Environment amendment | Exact CPython, pytest, NumPy, SciPy, Numba/llvmlite when present, threadpoolctl, loaded BLAS/LAPACK identities, immutable artifact hashes, origins, and offline lock for U311/U312/U313/JIT313 | `required_uncreated` |
| Instrumentation amendment | Content hashes and exact argv for environment, corotational, impact, standalone lifecycle, selected NLG report, and transparent NLG production/SciPy call probes | `required_uncreated` |
| Initializer | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\initialize_evidence_82a9db28.py` | `required_uncreated` |
| One-command runner | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\run_one_command_82a9db28.py` | `required_uncreated` |
| Command manifest | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28\runner\command_manifest.json` with exact `-B -I`, cwd, cache, basetemp, stdout/stderr, process-tree, partial/final mapping | `required_uncreated` |
| Old-run terminal audit | Separately authorized terminal accounting for run `31746877870` | `required_not_queried` |
| Stage-P path preflight | Exact absent/direct/non-reparse checks for all accepted Stage-P paths | `required_not_run` |
| PERF lease | Exact Stage-P subset, resources, and time bound | `required_not_requested` |
| Static evidence-limit addendum | `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_EVIDENCE_LIMIT_ADDENDUM.md`, limited to exact missing decorator/entry-point and eigen-call lines | `required_uncreated` |

## 8. Unresolved questions and narrowed claims

- Exact Ubuntu-lane NumPy, SciPy, threadpoolctl, and BLAS/LAPACK identities are
  unresolved. Project lower bounds are not evidence of resolved CI versions.
- The selected 24/32 cases' exact SciPy eigen callable, dense/sparse branch,
  operator shapes/dtypes, eigenpair ordering, residual, and sign normalization
  remain unresolved until transparent Stage-P instrumentation.
- The source of the lifecycle `explicit` count remains unresolved; only a
  standalone ordered event stream may answer it.
- Exact compiled decorator/entry-point bindings for every C01-C10 node must be
  frozen in the instrumentation amendment before a correction edit plan.
- No static evidence supports changing production impact behavior, numerical
  tolerances, analytical references, NLG mesh counts, or the no-Numba full-suite
  contract.

## 9. No-execution attestation

Stage S performed no import, test, probe, environment creation, dependency
installation, repository-code execution, Git/GitHub/run query, source edit,
workflow edit, cleanup, benchmark, profiler, or PERF action. It created only this
governance report through `apply_patch`. Stage P remains prohibited.
