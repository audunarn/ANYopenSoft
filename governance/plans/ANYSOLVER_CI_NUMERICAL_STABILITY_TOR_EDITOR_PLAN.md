# Tor editor plan: ANYsolver CI numerical stability

Base: `4030dd041c667fecf1f90211194f6ae84a5875f2`.

Tor is the sole editor of the six files listed in
`ANYSOLVER_CI_NUMERICAL_STABILITY_PREREQUISITE_PLAN.md`. Tor implements only
the rigid-complement dense buckling reduction, its fail-closed sparse boundary,
the descending/non-descending pencil regressions, and invariant triangular-shell
regression. Tor may run only the registered focused tests and must pause before
staging for independent read-only review.

Excluded: S4, activity, assembly, element mechanics, tolerances, workflows,
packaging, siblings, remote operations, cleanup, and any hidden or energetic
rank correction.
