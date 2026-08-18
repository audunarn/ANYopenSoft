# ANY Ecosystem Philosophy

## Canonical ownership

Each domain has one authoritative owner and dependencies flow downstream:

- ANYgeometry owns geometry, topology, persistent identity, tolerance,
  spatial indexing, intersections, and geometry audit truth.
- ANYmesh owns discretization and consumes qualified geometry contracts.
- ANYmaterial owns material definitions, validation, and canonical conventions.
- ANYio/ANYfileio owns interchange syntax and neutral file semantics.
- ANYsolver owns solver physics, numerical kernels, and qualification scope.
- ANYfem owns FEM workflow, projects, orchestration, and postprocessing.
- UI/application repositories consume public APIs and do not recreate domain truth.

Copied owner models, reverse imports, and coordinate-derived replacements for
owner topology are architectural defects. Compatibility facades may exist only
as thin, explicit, tested aliases.

## Contract doctrine

1. Prefer headless, public, stable contracts. Integration and UI layers use
   public APIs rather than private helpers.
2. Fail closed. Unsupported, unqualified, stale, wrong-model, or ambiguous
   inputs produce typed non-success; downstream preserves that truth.
3. Do not invent, narrow, or silently discard semantics. Preserve unknown
   interchange records, absent components, provenance, material symmetry, and
   solver-reported status.
4. Identity is model-bound and persistent. IDs are not guessed from coordinates,
   silently reused, or detached from revision/lineage.
5. Public mutation is atomic and rollback-safe. Incremental work follows explicit
   change sets and invalidation, not tolerance-based global rediscovery.
6. Boundary conventions are ecosystem contracts: SI internally, conversion once
   at ingestion/display, canonical material Voigt order, and structural protocols
   rather than concrete cross-package inheritance.

## Evidence and qualification

- Source and tests are behavioral truth. Reports are commit-, command-, and
  environment-scoped evidence, not timeless capability declarations.
- Qualification is narrower than implementation. A downstream application cannot
  broaden the solver owner's qualified scope.
- Partial runs, skipped execution, XFAIL, deck generation, and `not_executed` are
  never reported as passes.
- Failure evidence is retained. Plausible estimates, zeros, or fallbacks never
  replace a real non-success result.
- Every capability claim names the exact implementation identity, source SHA,
  contract version, command, result, platform, and remaining limits.

## Performance doctrine

Correctness and sound theory rank above performance. Implementations must be
physics-first where physics is involved and independently verifiable. Artificial
or hidden penalties, empirical tuning, invented stiffness, and other “magic”
corrections may not be introduced merely to satisfy a numerical or performance
gate. A derived formulation requires an explicit identity, derivation,
provenance, and qualification.

Performance cannot change semantics. Every acceleration keeps a correctness
oracle, explicit eligibility, lifecycle, invalidation, deterministic diagnostics,
and fail-closed fallback rules. Timing alone does not prove activation or
correctness.

No production stage may retain demonstrated global-quadratic behavior where the
governing plan requires subquadratic scaling. Memory evidence distinguishes
Python-traced allocation from process RSS and native allocation. Performance
qualification is serialized through the ecosystem-wide lease.

## Long-term stance

Prefer additive migration paths, explicit versions, and reversible compatibility.
Retire duplicated ownership rather than institutionalizing it. Frozen historical
trees remain historical and never regain authority through convenience imports.
