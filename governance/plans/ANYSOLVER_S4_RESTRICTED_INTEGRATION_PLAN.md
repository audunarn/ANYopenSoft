# ANYsolver S4 restricted integration plan

Status: executable restricted-integration plan under the authority delegated to
this task. Merge execution remains conditional on the exact rebound-main hosted
run recorded below completing successfully.

## 1. Authority and frozen inputs

This plan is governed by `C:\Github\ANYopenSoft\governance\plans\ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`, raw SHA-256 `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.

Repository: `C:\Github\ANYsolver`.

Execution worktree to create after the hosted prerequisite is green:
`C:\Github\ANYsolver\.perf2-worktrees\s4-restricted-integration-4db31b6`.

Execution branch: `codex/s4-restricted-integration-4db31b6`.

Frozen inputs:

- exact rebound `main` base: `4db31b633d0f886fcb4ad82946a982eb6fadde0e`, tree `beb5b2d0a599500bb8e2b00e99254540e18323e9`;
- accepted S4 formulation/nullspace proof: `cfaf9c7a6e51e1cc0c3113648f84835e917fca2a`;
- accepted geometry handoff tip: `931ed76943dc84fb9d01b26a5d6dd4c46af3d74a`;
- accepted batch/qualification research scaffold: `89ea46d8c1b1365b1d4a390ce6f34e2609c434f9`;
- canonical activity delivery already present exactly once on `main`: `1fd1c196518ac92b9dee920676f54c2d0cf58d26`, with ledger `7daa6e8c61954cfc1bc4469457fef0db154d3375`.

The rebound base contains the file-IO compatibility delivery, the Numba CI
contract correction, and the rigid-quotient numerical-stability correction.
Local `HEAD`, `main`, `origin/main`, and authoritative GitHub `main` were
reconciled exactly at this identity after one non-force push. Its sole hosted
prerequisite is GitHub Actions run `31830371310`, workflow `Tests`, path
`.github/workflows/ci.yml`, event `push`, branch `main`, head `4db31b6...`,
attempt `1`. Do not create the execution worktree or perform an S4 merge unless
that exact run is provider-terminal successful with the complete 24-job
attempt-1 matrix and no unexpected workflow run for the head.

Text hashes for this plan use UTF-8 without BOM, CRLF normalized to LF, rejection of remaining lone CR, then SHA-256. Git commit identities remain Git SHA-1 object IDs.

## 2. Release decision

Legacy S4 behavior remains the default for old, absent, and explicitly legacy formulation records. This task must not alter legacy stiffness, drilling stabilization, serialization meaning, activity behavior, or assembly results.

The merged improved formulation remains a dormant, non-default research implementation. Production activation is unavailable and must fail closed when any of the following applies:

- the accepted audit finds a positive-mass zero-stiffness mechanism `Z`;
- the curved or warped nullspace classification changes under the registered threshold-sensitivity multipliers;
- shell coupling is present and has not been independently qualified;
- nonlinear response, geometric stiffness or buckling, recovery, or optimized batch execution is requested.

Only an exact zero-mass subspace `G = ker(B) intersection ker(H_w)` may ever be removed, and only by an explicit deterministic constraint whose existence, dimension, equation, topology/constraint fingerprint, and before/after ranks are reported. A positive-mass checkerboard or other `Z` mode is never a gauge and must never be hidden, filtered, relabelled, or constrained as one. This restricted integration does not add a gauge constraint.

The following remain separately named research and are not release blockers for this task: a generally usable energetic rank-18 formulation, nonlinear MITC4+/D, geometric stiffness, optimized batches, recovery, and production coupling.

No penalty, hourglass term, invented stiffness, tuned stabilization, empirical threshold change, silent rank repair, or contract relaxation is permitted.

## 3. Frozen integration order

The sole integration coordinator is `Odin`. `Forsete` is the independent read-only reviewer. No editing subagent is authorized without a registered plan amendment.

The order is mandatory:

1. Require the exact hosted prerequisite above to be green, recheck clean local
   `main == origin/main == 4db31b6...`, and verify canonical activity/native
   assembly remains present exactly once. Do not duplicate or reinterpret
   `1fd1c196` or `7daa6e8c`.
2. Create the fresh execution branch/worktree from `4db31b6...`.
3. Merge `cfaf9c7a6e51e1cc0c3113648f84835e917fca2a` with history preserved and a non-fast-forward merge commit. Do not cherry-pick its tip alone.
4. Merge `931ed76943dc84fb9d01b26a5d6dd4c46af3d74a` with history preserved and a non-fast-forward merge commit. This must retain its complete accepted lineage; never cherry-pick `277f9b0f841b7a833f45ef41739b4f8c1117ecdb` alone.
5. Merge `89ea46d8c1b1365b1d4a390ce6f34e2609c434f9` with history preserved and a non-fast-forward merge commit. Its qualification contract, scripts, fixtures, and reports remain dormant research evidence: do not run benchmarks or expose a production batch selector.
6. Add one policy/provenance/test commit implementing only the restrictions in this plan.
7. Run focused light gates, obtain independent review, and then run the single combined regression in section 7.

The accepted proof and handoff files are imported without scientific rewrites. Their reference, oracle, director, provenance, and quality modules remain dormant: no package export, public formulation selector, solver hot-loop dispatch, or live geometry/document call is introduced by this task.

## 4. Owned policy/provenance/test extent

The policy commit may add or edit only these paths:

- `CHANGELOG.md`;
- `docs/S4_RESTRICTED_RELEASE_STATUS.md`;
- `docs/reference_cases/s4_restricted_release_contract.json`;
- `src/anysolver/shell_formulations/s4_restricted_policy.py`;
- `tests/test_s4_restricted_integration.py`;
- `tests/test_s4_restricted_activity.py`.

The policy module is cold-path metadata and validation only. It records the legacy default, the dormant improved identity, stable reason codes for unavailable activation, the accepted proof/provenance hashes, and the rule that only explicitly reported exact zero-mass `G` is gauge-removable. It must not assemble matrices, alter constraints, call geometry, or mutate models.

The release contract is versioned independently of the historical 113-claim qualification contract. It records the complete accepted square tuple: `rank(B)=16`; `N=dim ker(B)=8`; `G=dim(ker(B) intersection ker(H_w))=1` using the accepted positive weighted-displacement operator `H_w`; `P=7`; physical rigid space `R=6`; `R_N=dim(R intersection N)=6`; `R_G=dim(R_N intersection G)=0`; `RQ=rank(Pi_P Q_RN)=6`; and `Z=P-RQ=1`. It does not modify or weaken historical evidence.

All other paths are excluded, including activity/deletion policy, shared assembly, element dispatch, formulation reference/scalar code, geometry handoff code, nonlinear, buckling, recovery, batch, sibling repositories, packaging, and publication. Any required edit outside the six paths above stops work and requires a registered amendment.

## 5. Activity, geometry, and provenance invariants

- Preserve canonical `ElementActivity` and element-local pre-scatter scaling. Do not create a second activity map or apply global post-constraint scaling.
- Positive activity is scaling, not a constraint. Hard deletion changes topology. Neither may silently change gauge classification.
- Preserve existing orphan-DOF diagnostics; do not auto-remove orphan coordinates as S4 gauge.
- ANYgeometry owns neutral geometry/topology/identity/tolerance and schema migration. ANYsolver consumes immutable numeric arrays only.
- Source face-use orientation remains validated cold provenance; finalized connectivity defines directors and the positive reference Jacobian.
- The accepted handoff does not establish end-to-end sibling activation. Missing, stale, mismatched, or unqualified provenance remains fail-closed.

## 6. Focused LIGHT gates

Run sequentially from the rebound execution worktree with `PYTHONDONTWRITEBYTECODE=1`, one CPython process, and pytest cache disabled. `PYTHONPATH` is frozen in this exact order: rebound ANYsolver `src`; `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src` at `5513881827cdee9fd337497a2730a5912d8ea751`; `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anymaterial-4626887667f4c251479d26f321b9e73b046a2783-s4-artifact\src`; `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anymesh-c95328b604bfa4607ba82bbde76ceb8491134b1a-s4-artifact\src`; and `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anygeometry-37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa-s4-artifact\src`. The final three are clean detached worktrees or archives made from exactly those accepted commits; create them before testing if absent, then require exact HEAD/object or archive-manifest identity and clean content. Never use an ambient repository root.

Before pytest, import `anyfileio`, `anymaterial`, `anymesher`, and `anygeometry` in a clean process, require every resolved module origin to be contained by its respective pinned `src` root, and record the ordered `sys.path`, commit/archive identity, module origin, and content hash in the completion packet. Reject any origin beneath ambient `C:\Github\ANYfileIO`, `C:\Github\ANYmaterial`, `C:\Github\ANYmesh`, or `C:\Github\ANYgeometry`. The primary ANYfileIO checkout is the legacy `0d2c7f8` lineage and is forbidden. These are light gates and do not require a performance lease:

1. `python -m pytest tests/test_s4_eq21_eq25_reference.py tests/test_s4_nullspace_semantics_proof.py tests/test_s4_improved_qualification.py -q -p no:cacheprovider --basetemp=.pytest_tmp_s4_restricted_reference`
2. `python -m pytest tests/test_s4_geometry_handoff.py tests/test_s4_director_field.py tests/test_extracted_package_wiring.py -q -p no:cacheprovider --basetemp=.pytest_tmp_s4_restricted_handoff`
3. `python scripts/check_s4_geometry_handoff.py --full`
4. `python -m pytest tests/test_s4_restricted_integration.py tests/test_s4_restricted_activity.py tests/test_element_activity.py tests/test_element_activity_integration.py tests/test_constraint_audit.py -q -p no:cacheprovider --basetemp=.pytest_tmp_s4_restricted_policy`
5. `git diff --check` and exact changed-path/hash verification.

Immediately after each pytest command, clean its one literal basetemp. If the path exists, resolve it, require that its parent is the rebound execution worktree, remove only that resolved directory, and then require `Test-Path` to be false. Perform and record this absence check separately for `.pytest_tmp_s4_restricted_reference`, `.pytest_tmp_s4_restricted_handoff`, and `.pytest_tmp_s4_restricted_policy`, including after a failed test command. A cleanup failure blocks the stage.

Required assertions include: merge-input hashes unchanged; legacy remains default and byte-compatible; the improved identity is dormant and returns stable fail-closed reasons for every reserved capability; `Z` is not classified as gauge; no gauge constraint is added; activity blobs and local pre-scatter behavior are unchanged; no production import of ANYgeometry exists.

## 7. One later combined regression

The user transferred execution approvals to this task; no separate performance
lease request is required. Do not overlap this run with another heavy local
operation. After all focused gates and independent review pass, run this exact
packet once:

- working directory: the rebound execution worktree recorded in the superseding exact-base plan revision;
- environment: `PYTHONDONTWRITEBYTECODE=1`; `OMP_NUM_THREADS=1`; `OPENBLAS_NUM_THREADS=1`; `MKL_NUM_THREADS=1`; the exact five-root `PYTHONPATH` and module-origin preflight from section 6; no ambient repository source injection;
- command, run once: `python -m pytest tests -q -p no:cacheprovider --basetemp=.pytest_tmp_s4_restricted_combined`;
- envelope: one CPython process, no parallel workers, less than 8 GB RAM, less than 2 GB temporary disk, estimated 30-90 minutes;
- output: complete exit/result/timing plus the pytest terminal record captured in the completion packet;
- cleanup: remove only the resolved worktree-local basetemp and verify no pytest/Python child remains.

No benchmark or performance claim is part of this clearance.

## 8. Completion and closeout

Completion requires:

- the three history-preserving merge commits and one policy/provenance/test commit;
- exact parent/tree/path/blob identities and a clean worktree;
- focused gate results and the combined-regression command/result packet;
- proof that current-main activity blobs and behavior remain unchanged;
- proof that legacy S4 is still the default and improved production activation remains unavailable under every reserved condition;
- an independent Forsete review with no unresolved material finding;
- a content-addressed completion packet and `ECOSYSTEM CLOSEOUT: OK` before any default-branch merge or push.

No package build, wheel, publication, release tag, sibling write, or external publication is authorized.
