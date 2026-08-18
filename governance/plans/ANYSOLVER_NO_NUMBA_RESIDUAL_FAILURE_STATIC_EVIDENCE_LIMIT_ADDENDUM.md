# ANYsolver no-Numba residual static evidence-limit addendum plan

## 1. Identity and authority boundary

This bounded Stage-S addendum is anchored to:

- accepted source commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`;
- accepted source tree:
  `00b2b20691e73a05589b797b32352f1c760a2451`;
- accepted governing diagnosis plan SHA-256:
  `7472B4ECE6430B1B13BE24BCA3C24DA5074DC458BC5B92EB7E65C8C7F1AB1179`;
- immutable `STATIC-S01` path:
  `C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_REPORT_82A9DB28.md`;
- immutable `STATIC-S01` SHA-256:
  `CDF15DD7DFACD3548A15DE3871B74BFE3714A986E7F40B38670585FB345A7932`.

`STATIC-S01` is preserved byte-for-byte. It must not be overwritten, patched,
renamed, moved, deleted, cleaned, or treated as corrected in place.

This plan authorizes no reread until its own exact bytes and SHA-256 are
independently accepted. Acceptance authorizes only the bounded static reread and
separate correction-addendum report described below. It does not authorize
Stage P.

## 2. Exact correction ledger

### 2.1 Impact row supersession

The separate correction report must supersede false `STATIC-S01` finding
`S-F10` and its grouped impact disposition with this exact boundary:

- Production `prepare_impact_reduced_assembly` retains the ordered complete
  semantic exclusion tuple and prepends `jit_unavailable` when JIT is absent.
- `C12`,
  `test_direct_reduced_impact_selector_reports_all_static_exclusions`, has
  partial JIT-aware handling: it prepends `jit_unavailable` to its expected
  exclusions when `not JIT_ENABLED`.
- `C13-C16` still assert semantic primary reasons without the no-JIT prefix and
  therefore require later test-only JIT-aware expectations.
- No production impact-order, exclusion, fallback, or activation change is
  indicated or authorized.
- No assertion may be loosened and no generic lane may install Numba to conceal
  the fallback contract.

This correction uses already retained immutable evidence. The bounded reread
does not reopen impact files.

### 2.2 Frozen verification identifiers

The verification nodes remain exactly:

- `V01`:
  `tests/test_beam_shell_verification.py::test_beam_shell_verification_report_separates_pass_and_xfail`;
- `V02`:
  `tests/test_follower_pressure.py::test_thin_ring_follower_pressure_converges_to_analytical_buckling[24-0.06]`
  and its frozen 32-element comparison parameter
  `[32-0.035]` where the governing plan requires it.

The correction report must replace every `C18` or `C19` label with `V01` or
`V02` as applicable. `C18` and `C19` are not valid identifiers and must not be
introduced in any later plan, report, test, instrument, or evidence manifest.

## 3. One bounded static reread

After independent acceptance of this plan, one static reread is authorized.
Only the exact files and selections below may be read. Each selected file may be
opened once. No second extraction or retry is permitted if output is truncated;
the correction report must retain `evidence_limited` for any missing detail.

### 3.1 C04 decorator and entry-point selection

Read only:

- `tests/test_nonlinear_performance.py`:
  decorators, definition signature, and body of
  `test_mixed_initial_field_shell_batch_accelerates_initialized_elastic_element`,
  ending immediately before the next top-level definition;
- `src/anysolver/nonlinear_performance.py`;
- `src/anysolver/nonlinear_performance_bootstrap.py`;
- `src/anysolver/nonlinear_performance_batch_b.py`;
- `src/anysolver/nonlinear_performance_batch_c.py`.

For the four owner files, read only definition/decorator/import/delegation lines
for exact names directly referenced by the selected C04 function, following
direct delegation until the compiled/scalar eligibility and implementation
entry points are identified. Do not read unrelated function bodies.

The correction report records:

- exact C04 decorators and whether a JIT skip/branch already exists;
- exact public installation/plan/assembly names called by C04;
- exact compiled entry point, scalar oracle, and eligibility diagnostic names;
- fact versus inference classification with file and line references;
- any missing link as `evidence_limited`.

### 3.2 Selected buckling dense/sparse SciPy selection

Read only:

- `tests/test_follower_pressure.py`:
  decorators, definition signature, and body of
  `test_thin_ring_follower_pressure_converges_to_analytical_buckling`, ending
  immediately before the next top-level definition;
- `src/anysolver/buckling.py`:
  SciPy imports plus the definition signature and body of
  `solve_eigenvalue_buckling`, limited to branch predicates and direct calls
  selecting dense versus sparse/general eigen solvers and the result filtering,
  ordering, residual, sign, and repeated-eigenvalue handling attached to those
  calls.

The correction report records:

- exact SciPy qualified callable names;
- exact branch predicates and thresholds selecting each callable;
- exact `V02` arguments that affect branch selection, including dense fallback;
- exact return/exception and eigenvalue/eigenvector post-processing seams that a
  later transparent instrument may observe;
- whether 24- and 32-element cases are statically guaranteed to share a branch;
  if not guaranteed, state `evidence_limited` pending Stage P.

No operator, root, residual, constraint, or eigenpair may be reconstructed.

## 4. Read transport and stop rules

The bounded reread is static text inspection only. The reader may emit exact
selected lines and line numbers. It must not import or execute repository code.

Prohibited during this addendum:

- Python or application imports;
- pytest, tests, probes, instruments, environment creation, dependency actions,
  builds, or benchmarks;
- Git or GitHub commands, run/job queries, polling, cancellation, reruns, or
  workflow dispatch;
- source, test, workflow, metadata, or `STATIC-S01` edits;
- cleanup, deletion, pruning, cache creation, PERF work, or Stage-P preparation;
- reads outside the exact seven-file allowlist in Section 3.

On missing file, selection mismatch, output truncation, unexpected path, or any
security event, stop. Preserve the first result and classify the unresolved
detail `evidence_limited`. Do not retry or broaden.

## 5. Separate immutable correction report

After the one bounded reread, create exactly this previously absent file through
`apply_patch`:

`C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_NO_NUMBA_RESIDUAL_FAILURE_STATIC_CORRECTION_ADDENDUM_82A9DB28.md`

Required schema:

- schema name/version
  `anysolver.no_numba_residual.static_correction_addendum/1`;
- this addendum plan path and accepted SHA-256;
- immutable `STATIC-S01` path and SHA-256;
- accepted commit and tree;
- an explicit statement that the report supplements but never mutates
  `STATIC-S01`;
- corrected impact ledger separating `C12` from `C13-C16` and preserving no
  production change;
- restored `V01` and `V02` identifiers and a rejection of `C18`/`C19`;
- exact retained C04 decorator/entry-point lines and classification;
- exact retained selected buckling SciPy call/branch lines and classification;
- every unresolved or truncated detail marked `evidence_limited`;
- exact later environment/instrumentation consequences without creating either;
- no-execution attestation.

The correction report does not embed its own hash. After creation, report only
its bytes, LF/CR/BOM identity, and SHA-256 for independent review. Do not edit it
after freezing.

## 6. Order and completion boundary

The only authorized order is:

1. independently accept this addendum plan hash;
2. perform the one bounded seven-file static reread;
3. create the one separate correction report via `apply_patch`;
4. report its exact identity;
5. stop Stage S for independent review.

No environment, instrument, initializer, runner, command manifest, old-run
audit, path preflight, PERF request, or Stage-P action follows automatically.
