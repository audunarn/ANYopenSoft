# ANYmesh Source-Contract CI Failure Diagnosis Plan

Date: 2026-08-13 (Europe/Oslo)

Status: Phase 1 read-only. No source/test edit, commit, push, workflow rerun,
build, wheel, benchmark, publication, tag, or release is authorized.

## Authority and frozen state

- Repository: `C:\Github\ANYmesh`.
- Exact local/default/remote main:
  `4a0424a05fc4333d46d26f4c2fca97a113d0c09c`.
- Tree: `659451e5f5ad140c6c6f43bf8110a6b254907102`.
- Preserved terminal run:
  `https://github.com/audunarn/ANYmesh/actions/runs/31700439141`.
- Prior environment-failure run remains preserved:
  `https://github.com/audunarn/ANYmesh/actions/runs/31699257852`.
- Diagnostic branch/worktree remains
  `codex/native-hybrid-release-blockers` in the registered isolated worktree.

All worktrees must remain clean during Phase 1. ANYgeometry is consumed through
its public API; no geometry source/schema edit or downstream coordinate
inference is allowed.

## Uniform failing nodes

1. `tests/test_intersection_meshing.py::test_multiple_crossings_are_discovered_after_the_first_face_is_fragmented`
2. `tests/test_intersection_meshing.py::test_positive_area_coplanar_overlap_is_blocked_before_double_stiffness`
3. `tests/test_operations.py::test_mapped_backend_requires_a_trimmed_hole_to_be_partitioned`
4. `tests/test_operations.py::test_a_neutral_triangle_is_refused_by_the_mapped_backend`

## Phase 1 read-only questions

### Mapped operation nodes

- Trace each test to the public generation call and its selected backend.
- Establish whether omission now selects public `auto` and whether an otherwise
  identical explicit `backend="mapped"` call restores the intended mapped-only
  rejection and diagnostic.
- Do not change the public `auto` default, weaken mapped validation, or make a
  native/automatic success satisfy a mapped-only refusal assertion.

### Legacy intersection nodes

- Trace the quarantined adapter through public `query_intersection`,
  `plan_imprint`, and `apply_imprint` with exact face IDs, revisions,
  classifications, dimensions, statuses, operations, and diagnostics before
  and after each mutation.
- Record broad-phase candidate pairs separately from qualified intersections.
  A typed `DISJOINT` candidate is skipped; unsupported/capability-missing/
  unclassified results remain fail-closed and are never treated as disjoint.
- Prove overlap detection/order numerically before creative imprint. A
  positive-area coplanar overlap must retain the specific overlap-first
  fail-closed diagnostic rather than be masked by an unrelated candidate.
- Preserve model-bound identity, public mutation plans, deterministic ordering,
  non-creative reuse, no coordinate inference, and no downstream geometry
  healing.

## Read-only path budget

- `src/anymesher/intersections.py`
- `src/anymesher/_legacy_intersections.py`
- the public generation/decomposition module selected by symbol tracing
- `tests/test_intersection_meshing.py`
- `tests/test_operations.py`
- public ANYgeometry records/signatures may be introspected at runtime without
  editing or parsing geometry persistence documents.

Each required file is read once. Runtime diagnosis is limited to the four named
nodes and small deterministic reproductions of those exact fixtures. No broad
suite or performance lease is needed.

## Phase 1 evidence and edit gate

Submit:

- exact plan bytes/hash;
- one numeric/call-path ledger per node;
- explicit mapped-backend counterfactual results;
- intersection candidate/query/plan/apply and revision evidence;
- overlap areas/tolerances and ordering evidence;
- the exact smallest production/test edit allowlist;
- exact focused test nodes proposed after editing;
- a clear classification of production defect, stale test, or both.

No edit begins until independent review accepts a superseding Phase 2 plan with
that exact allowlist. A later correction remains direct-child-only and must not
revive coordinate-inferred coupling or reinterpret typed non-success as empty
success.
