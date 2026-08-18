# ANYsolver S4 drill-constraint certification plan

Status: executable proof-and-derivation plan under the authority delegated to
this task. This plan grants no production activation or hot-path integration.

## 1. Frozen base and identities

Repository: `C:\Github\ANYsolver`.

Execution branch: `codex/s4-drill-constraint-certification`.

Execution worktree:
`C:\Github\ANYsolver\.perf2-worktrees\s4-drill-constraint-certification`.

Frozen clean base:

- commit `587fa2efabcd48ada8a258ecf7301070b47f2b32`;
- tree `de137d6a72548b5d5908d799b96f0586dff2ba8f`;
- local `HEAD`, `main`, and `origin/main` were equal when this plan was
  authored;
- terminal hosted gate: GitHub Actions run `31838144309`, workflow `Tests`,
  attempt 1, 24/24 jobs successful.

Accepted formulation inputs are read-only. Portable hashes use UTF-8 without
BOM, CRLF converted to LF, rejection of any remaining lone CR, then SHA-256:

- `protocol.py`: `32BF05E0BD0B282C49C47392CAF9400D2C8C136B9B6D1D398B3B54451EACB089`;
- `q4_common.py`: `DE2DCDCD3BC04A90A4DB2C074EC15D4E4B097123010F146A0C718506443C3D19`;
- `mitc4_plus_d_reference.py`: `AAF44046EEE607541F2A84EA16CBA948CB98130A568BBF8B5B03B243928E9536`;
- `mitc4_plus_d_scalar.py`: `9E3F1827F813546FF9C183C77E654F268C8A67F976B63FF010749EFDEAB3118B`;
- accepted nullspace cases: raw/portable
  `223C0E1A1F03D30AA5EFBB13E8ECD8F64E5F7F0865E6F11274577D15C6691ABF`;
- accepted nullspace proof: raw SHA-256
  `713465F03BE6221119C1CCB7539301BE01324445DE54FC466D398185B7B481CD`.
- primary 2025 MITC4+/D paper PDF:
  `89C10DE1FB13056EB967111C2DBB28FE2D18179090814141455F4E8901D919EA`.

The accepted unrestricted square tuple remains
`rank(B)=16, N=8, G=1, P=7, R=6, R_N=6, R_G=0, RQ=6, Z=1`.
The positive-mass `Z` direction is not gauge.

## 2. Scientific question and selected proof hypothesis

This stage tests one parameter-free kinematic hypothesis; it does not assume
the answer. On every retained shell topology, the nodal drilling trace is the
registered quadrature-L2 projection of the full continuum infinitesimal spin
at the midsurface, computed from the same isoparametric shell kinematics. This
is a 2x2 quadrature definition, not a claim of exact integration when the
surface Jacobian is non-polynomial.

At a midsurface station, let `H_c` be the continuum displacement interpolation
without the `/D` enrichment, `g_r,g_s,g_zeta` the full covariant basis, and
`g^r,g^s,g^zeta` its reciprocal basis. Define

```text
omega_c(q) = 1/2 sum_{k in {r,s,zeta}} (g^k cross H_c,k) q,
d(q)       = sum_i N_i (d_bar dot theta_i),
```

where `d_bar` is the element's published fixed-center drill direction. This
definition is objective for an analytic rigid field: `omega_c=omega` and
`d=omega dot d_bar`.

For each retained element `e` and literal 2x2 surface Gauss station `g`, use
only the positive surface measure

```text
mu_eg = w_r w_s ||g_r cross g_s|| > 0.
```

Density, thickness, stiffness activity `alpha`, and mass activity `beta` do not
enter this kinematic projection. Positive `ElementActivity` must leave it
unchanged; only canonical hard deletion removes an element before assembly.

Let the retained-topology length `ell` be the maximum Euclidean distance among
nodes incident to retained elements; a topology with no retained element is
invalid. Use the accepted mixed-unit metric

```text
q_phys = S_q q_hat,
S_q = blockdiag(ell I_3, I_3) per declared node,
D_hat = D_phys S_q,
F_hat = F_phys S_q.
```

With `A_e` the explicit stable-ID scatter map, the global Galerkin normal
equation is

```text
C_D_sample = vertical_stack_(e,g) sqrt(mu_eg) D_hat_eg A_e,
F_D_sample = vertical_stack_(e,g) sqrt(mu_eg) F_hat_eg A_e,
C_raw q_hat = sum_(e,g) A_e^T D_hat_eg^T mu_eg
                          (D_hat_eg - F_hat_eg) A_e q_hat = 0.
```

Equivalently, `C_raw=C_D_sample^T(C_D_sample-F_D_sample)`. The positive
square root is the only row weighting.

This is a Galerkin projection equation, not differentiation of an objective
with respect to every generalized coordinate; the test field is `D_hat`.
`omega_c` may depend on non-drilling rotations. The exact full 3D sum is
required because it gives `omega_c=Omega` for the analytic rigid field
`u=c+Omega cross x_h`, including on warped/varied-director geometry.
`H_c` is the base continuum interpolation and explicitly excludes the `/D`
displacement enrichment `u_D`; the candidate is a constrained closure of the
literal B/H mechanics, not equality to the spin of the enriched displacement.

The independent row space of `C_raw` is represented by the deterministic
projector-derived orthonormal row basis `C_D`. Zero/dependent rows are removed
only by the frozen rank algebra. There is no element-by-element sequential
projection and no averaging outside this assembled statement. Orphan
coordinates remain in the declared global universe and are reported; they are
never silently compacted.

Physical support, homogeneous MPC, and declared work-conjugate coupling rows
are first transformed by `S_q`, normalized together with any matching affine
right-hand side, and concatenated with `C_D` into one matrix before any
nullspace or reduced operator is formed. Affine right-hand sides are checked
separately for feasibility and never enter the homogeneous tangent. No row is
called a gauge constraint merely because it removes a null vector.

Affine feasibility is always tested on the complete normalized system
`[C_D; C_phys_hat] q_hat = [0; d_phys_hat]`, never on the physical rows alone.
The left-hand rank and the rank after appending the complete right-hand side
must agree at each sensitivity multiplier. Every constraint fixture carries an
actual JSON Boolean `expected_feasible`. The frozen expectations are
`fixed_drill=true`, `tied_drill=true`, `dependent_drill=true`,
`weighted_affine=true`, `infeasible_affine=false`,
`abstract_shell_shell=true`, `rigid_beam_shell_work=true`, and
`orphan_support=true`, `distorted_fixed_drill=true`, and
`warped_fixed_drill=true`. A mismatch or multiplier drift blocks certification;
the deliberately false `infeasible_affine` result is required evidence, not a
suite failure.

If, and only if, the complete proof passes, an exact reduced representation may
be studied through a rank-revealed nullspace basis `T` of the combined
homogeneous rows:

```text
K_r = T^T K T,
M_r = T^T M T.
```

This congruence adds no energy and does not alter or relabel the free local
rank. The result, if certified, is named
`mitc4_plus_d_published_2025_linear_spin_constrained_research_v1`: a distinct
linear constrained five-kinematic-DOF operator. It is not literal
unconstrained MITC4+/D, local rank 18, or gauge removal, and it is not
implemented in a solver by this stage. On a flat element with uniform
directors the hypothesis removes the entire four-dimensional pure-drill
coordinate subspace, including G, Z, and the two energetic edge-difference
directions; that full effect must be reported rather than hidden.

## 3. Frozen numerical and arbitrary-precision rules

The independent oracle uses only Python's standard library plus
`mpmath==1.3.0`. `MPMATH_NOGMPY=1` must be set before import and
`mpmath.libmp.BACKEND` must equal `python`; any other backend fails closed.
All base scientific input numbers in its cases file are finite base-10 JSON
strings and enter directly through `mp.mpf`; no binary64 value may be promoted
and called high precision. Gauss `1/sqrt(3)`, director normalization, rigid
fields, powers-of-two scaling, and registered frame transforms are tagged
derived operations recomputed after each precision is set, never stored
decimal approximations masquerading as exact constants.

Every categorical result is evaluated independently at decimal precisions
`80`, `160`, and `320`. At each precision, after setting `mp.mp.dps=p`, record
the exact `mp.prec` integer and `mp.eps` tuple and define `eps_p=mp.eps`. All
scientific matrices are constructed and rounded in that target context. Rank
and projector work reconstructs those exact target mpf tuples at guard
precision `2*p+32` decimal digits and uses

```text
tau_p(A,m) = m * 64 * max(rows(A),cols(A)) * eps_p * sigma_max(A),
r_tol_p(d) = 4096 * d * eps_p,
m in {0.25,1,4}.
```

An exactly zero matrix has rank zero without division by a scale. A restricted
operator inherits the multiplier-one parent `sigma_max`; it is never rescaled
by its own roundoff-only norm. Projectors and mapped subspaces use
projector-derived bases and symmetric augmented intersections, as in the
accepted proof. Rank/projector dimensions must agree across all three
precisions and all three multipliers. Residuals use the registered parent
scales below, never a dimensioned floor of one, and must not exceed the
corresponding `r_tol_p`.

Rank and projector construction use the real symmetric eigenproblem
`mp.eigsy(A.T*A)` at guard precision, symmetrized before the call. The target
matrix is never recomputed at guard precision. This doubled-precision Gram
rule prevents same-precision `sqrt(eps)` false singular values. Eigenvalues are ascending;
singular values are their nonnegative square roots. A negative Gram eigenvalue
whose magnitude exceeds `r_tol_p(d)*sigma_max(A)^2` fails PSD; smaller negative
roundoff is set to exact zero. The null/range projector is formed from the
selected full right-eigenvector columns. Selected null/range bases must also
pass direct residual/reconstruction gates against the target-rounded matrix.
A deterministic basis is then extracted
from projector columns in increasing coordinate order with two-pass modified
Gram-Schmidt. A candidate is accepted above
`256*dimension*eps_p` relative to the unit projector scale. Its sign is chosen
from the largest-magnitude component; ties inside that same band use the
smallest coordinate index. Only projectors and projector-derived bases—not
degenerate eigensolver vectors—enter scientific comparisons or serialization.

For operator annihilation use
`||A Q||_F/(sigma_max(A)||Q||_F)`; an exactly zero parent requires exact zero
residual. Projector symmetry/idempotence/orthogonality use their absolute
Frobenius residual because the projector scale is exactly one. Equality and
covariance use `||A-B||_F/max(||A||_F,||B||_F)` with an exact-zero convention,
never a dimensioned floor of one. Restricted operators inherit the registered
parent `sigma_max`. Symmetric reduced `K` and `M` fail if their symmetry
residual exceeds `r_tol_p` or if any eigenvalue is below
`-r_tol_p(d)*max(abs(eigenvalues))`; an exact-zero spectrum is handled exactly.

Binary64 Eq. 21/Eq. 25 implementation agreement uses the whole-matrix relative
Frobenius rule above and limit `8192*max(m,n)*eps64`; an exactly zero expected
matrix must be bitwise zero. No binary64 agreement is claimed for `F_hat`, for
which no accepted public implementation API exists.

For the accepted free-nullspace partition, retain the exact prior weighted
calculus. With positive volume determinant `w_a`, density `rho_e>0`, positive
activity scales `alpha_e,beta_e>0`, and the same `S_q`, define

```text
W_B = sum_(e,a) alpha_e w_a,
W_H = sum_(e,a) rho_e beta_e w_a,
B_w = vertical_stack_(e,a) sqrt(alpha_e w_a/W_B) B_ea S_q,
H_w = vertical_stack_(e,a) sqrt(rho_e beta_e w_a/W_H) H_ea S_q/ell,
K_w = B_w^T B_w,
M_w = H_w^T H_w.
```

`B` is the accepted five-row local engineering operator and `H` is the
accepted three-row enriched displacement operator at the 2x2x2 stations. This
metric is deliberately distinct from activity-free `C_D`. Restrictions of
`B_w` and `H_w` inherit their respective parent multiplier-one scales. The
accepted definitions of `N`, `G`, `P`, `R_N`, `R_G`, `RQ`, and `Z` are reused
unchanged, including symmetric augmented intersections and quotient images.
For the constrained partition, define the projector-derived represented sum
`S_RG=R_N+G` with overlap `R_G`; define `L_C=N_C intersection S_RG` by the
symmetric augmented intersection; define `L_G_C=L_C intersection G_C`; let
`Q_L_C` be the deterministic projector-column basis of `L_C`; form
`Y_C=Pi_P_C Q_L_C`; and define
`Pi_RQ_C=proj(range(Y_C))` with inherited unit parent scale and
`Pi_Z_C=Pi_P_C-Pi_RQ_C`. Require
`rank(Y_C)=dim(L_C)-dim(L_G_C)` at every precision and sensitivity multiplier.

The oracle independently reconstructs, rather than imports, Q4 shapes, full
3D reciprocal bases, the literal 2025 Eq. 21 tensor transform, Eqs. 24-25
`Q R S` membrane map, `/D` displacement enrichment, continuum spin, positive
quadrature weights, global scatter, deletion, constraints, and congruence
checks. It may import no `anysolver` module. Binary64 comparisons to the
accepted implementation occur only in the pytest wrapper and are explicitly
labelled implementation agreement, not independent derivation.

Canonical output is UTF-8 JSON with sorted keys, compact separators and one
terminal LF. Every finite `mpf` is serialized from its exact internal tuple as
`[sign,decimal_mantissa,exponent,bitcount]`; zero is `[0,"0",0,0]` and any
nonfinite/special tuple fails closed, so decimal pretty-printing is outside the
hash domain. Matrices use C-order arrays of those tokens.

The supported lane is CPython 3.11-3.14 with little-endian byte order. Other
runtimes emit one canonical `unsupported_runtime` record and exit 2 before
scientific work. The environment manifest binds `sys.implementation.name`,
`sys.version`, `sys.hexversion`, byte order, `platform.system/release/machine`,
and SHA-256/size of resolved `sys.executable`. On Windows it additionally
resolves and hashes the matching `pythonXY.dll` beside `sys.base_prefix`; on
other systems it resolves and hashes `sysconfig.get_config_var("LDLIBRARY")`
under `LIBDIR` when present. Every loaded native extension whose module name
starts with `mpmath` is forbidden because the backend must be pure Python.

The installed mpmath distribution is obtained only through
`importlib.metadata.distribution("mpmath")`; normalized name must be `mpmath`
and version `1.3.0`. The distribution root is exactly
`Path(dist.locate_file("")).resolve()`. `dist.files` is enumerated by ordinal
`PackagePath.as_posix()`. Absolute/backslash/empty/`.`/`..`, missing,
nonregular, symlink/reparse, root-escaping, or duplicate case-folded entries
fail closed. Every regular entry except `.pyc` is hashed from actual bytes and
serialized as `[relative_name,size,sha256]`; excluded pyc names are recorded
in a separate sorted list. `RECORD`, METADATA, sources, and licenses are thus
included when installed. The manifest also records resolved
`mpmath.__file__`, `mpmath.libmp.__file__`, `mpmath.libmp.BACKEND`, and every
target `[dps,prec,eps_mpf_tuple]`. Both resolved module files must be regular,
non-reparse files contained by the verified distribution root, and their
root-relative POSIX names must occur in the hashed non-pyc `dist.files`
inventory. A shadow or otherwise unbound `mpmath` or `mpmath.libmp` import
fails closed before scientific work.
Byte-identical output is required only when complete environment-manifest
digests match. Different manifests compare only the frozen ranks, dimensions,
projectors, and normalized residuals. The cases, oracle source, stored output,
manifest, and accepted-source identities are SHA-256 linked in the completion
document.

## 4. Frozen evidence matrix

The cases must include:

- flat square, affine/skew, tapered, distorted, and warped elements;
- fully materialized one-element distorted and warped topology records that
  duplicate the corresponding local coordinates/directors and each carry one
  expected-feasible fixed-drill support fixture;
- uniform and varied directors and uniform/nonuniform thickness;
- center, four Gauss stations, and three fixed hostile interior stations for
  Eq. 21/Eq. 25 columnwise comparisons;
- cyclic numbering and anchored reversal covariance;
- one element, two shared-edge elements, regular 2x2, odd-cycle, disconnected,
  positive-activity, deletion split, and deletion-orphan topologies;
- a noncoplanar two-face fan sharing an edge, reporting `rank(C_D)` against the
  nominal drill-scalar count and failing any general coupling claim if its
  extra rotational constraints lack the declared rigid-joint derivation;
- exact support, tied/dependent/affine MPC, shell-shell work row, and beam-shell
  work row fixtures;
- analytic translations and rotations, constant drill, alternating drill,
  membrane extension, in-plane shear, bending, and transverse shear patches;
- a deterministic shell/beam torque-transfer virtual-work fixture;
- coordinate scaling by `2^-20`, `1`, and `2^20`, rigid frame rotation, and
  origin shift.

The accepted unconstrained square tuple must be reproduced before adding
`C_D`. A successful constrained result must demonstrate all of the following:

- analytic rigid motions remain in the combined homogeneous kernel whenever
  the physical support/coupling rows permit them;
- the exact zero-mass gauge and the positive-mass checkerboard are reported
  separately before constraints;
- after the kinematic drill row is included, no positive-mass zero-stiffness
  quotient direction remains in every claimed topology;
- reduced stiffness and mass are congruent to the full operators, symmetric,
  positive semidefinite within the frozen residual calculus, and conserve
  virtual work;
- constraint reactions transmit equal-and-opposite declared generalized work
  in the coupling fixtures;
- positive activity leaves `C_D` invariant, while hard deletion alone changes
  its element row contributions;
- numbering, frame, origin, and scale covariance pass without empirical
  tolerances;
- curved/warped categorical dimensions are stable across precision and
  sensitivity or are explicitly classified as a blocker.

The `one_square` probe is gated, not merely reported: constant drill must have
exact `B_w q=0` and `H_w q=0`, while the bipartite alternating drill must have
exact `B_w q=0` and strictly nonzero `H_w q`. The fully materialized
`warped_varied_directors` topology must additionally pass `C_D` rowspace-
projector covariance under cyclic numbering, anchored reversal, and the
registered proper-frame rotation. Recording these values without enforcing
the identities is insufficient.

Failure of any item produces a content-addressed no-go packet. It may not be
converted into a pass by changing a threshold, deleting a mode, adding a
penalty, or weakening a fixture.

## 5. Sole-editor extent

`Tor` is the sole editor. `Heimdall` and `Forsete` are read-only independent
auditors. The implementation may add or edit only:

- `pyproject.toml` (add `mpmath==1.3.0` to `dev` only);
- `docs/agent_plans/s4_drill_constraint_tor_agent.md`;
- `docs/reference_cases/s4_drill_constraint_cases.json`;
- `docs/reference_cases/s4_drill_constraint_oracle.py`;
- `docs/reference_cases/s4_drill_constraint_oracle_output.json`;
- `docs/S4_DRILL_CONSTRAINT_DERIVATION.md`;
- `tests/test_s4_drill_constraint_derivation.py`;

No accepted proof, formulation source, scalar operator, handoff, activity,
assembly, element, solver, package export, serialization, restart, recovery,
nonlinear, geometric-stiffness, buckling, or batch path may change.

Proof fixtures use explicit stable string node/element IDs, sorted ordinally
and reindexed through a recorded map before scatter; IDs are never assumed
dense or insertion-ordered. Each element binds its connectivity, coordinate,
thickness, director values, and prepared-director provenance fingerprint in
the cases hash. Only declared shell elements enter `C_raw`. A coupling whose
owner was deleted or not deterministically resolved fails closed. Shell-shell
rows remain explicitly abstract; the beam-shell fixture certifies only its
declared rigid work-conjugate row, not a production coupling API.

There is no accepted public continuum-spin API and the current sparse acyclic
`build_constraint_transformation` cannot consume this general dense rowspace.
Both are intentionally deferred to a later adapter plan; this proof may not
claim otherwise.

The cases grammar is closed. A base scalar is an actual JSON string matching
`^-?(0|[1-9][0-9]*)(\.[0-9]+)?$`; it denotes the exact rational with a
power-of-ten denominator and is passed directly to `mp.mpf` after precision is
set. JSON numeric scientific scalars are forbidden. The only derived forms
are: `kind=center`; `kind=gauss` with signs exactly `-1` or `1` and value
`sign/sqrt(3)`; `kind=decimal` with exact string `r,s`; normalization of a
three-string director seed; integer `2^k` coordinate scaling; the stated
three-by-three proper-frame matrix after
orthogonality and determinant-one validation; and analytic rigid fields from
exact Cartesian unit axes and each retained-component centroid. Evaluation is
depth-first in that order. Every topology is fully materialized as sorted node
and element records; no runtime topology generator is permitted. Absent
`state`, `alpha`, `beta`, or `density` means
exactly `active`, `1`, `1`, or `1`; a scalar thickness/director seed broadcasts
to four corners. A deterministic director-binding fingerprint is SHA-256 over
canonical JSON object keys `cases_sha256`, `element_id`, `connectivity`,
`director_seed_strings`, and C-order `normalized_director_mpf_tokens`, encoded
with `ensure_ascii=False`, sorted keys, compact separators, and one terminal
LF. The lowercase SHA-256 of those bytes is the fingerprint; no live geometry
object is consulted. The cases raw SHA-256, schema, governing-plan hash,
Tor-plan hash, and accepted source hashes are checked and recorded before the
first scientific case. Any grammar extension requires a plan amendment.

The sole allowed numbering-derived topology variants are the two registered
maps under `derived_variants.warped_numbering_covariance`, applied only to the
fully materialized `warped_varied_directors` topology. `cyclic` uses local
corner order `(1,2,3,0)`, old natural coordinates
`(r_old,s_old)=(-s_new,r_new)`, director sign `+1`, and the identity global-DOF
pullback because stable node IDs and global DOF order are unchanged.
`anchored_reversal` uses local corner order `(0,3,2,1)`, old natural
coordinates `(r_old,s_old)=(s_new,r_new)`, director sign `-1` at every reordered
corner to preserve the physical director orientation, and the same identity
global-DOF pullback. Connectivity, per-corner thickness, and director records
are reordered by the registered corner order; node records and coordinates are
not regenerated or reordered. No other runtime topology derivation is allowed.

Probe vectors are exact and frozen in physical DOF order. For every retained
component with centroid `x_c`: translation axis `a` has `u_i=a,theta_i=0`;
rigid rotation axis `a` has `u_i=a cross (X_i-x_c),theta_i=a`. On a flat
uniform-director component, constant drill has `u_i=0,theta_i=d_bar`; the
alternating drill signs are assigned by ordinal BFS from the smallest node ID
with sign `+1` and flip across every retained element edge, and are emitted
only when the graph is bipartite. The square patch fields are: extension
`u_i=(X_i.x,0,0),theta_i=0`; in-plane tensor shear
`u_i=(X_i.y/2,X_i.x/2,0),theta_i=0`; bending
`u_i=0,theta_i=(0,X_i.x,0)`; transverse shear
`u_i=(0,0,X_i.x),theta_i=0`. The beam-shell virtual-work row uses unit
multiplier, reaction `f=C^T`, common rigid drill trace as the zero-work test,
and the exact identity `f dot delta_q = C delta_q`; its two positive shell
coefficients must sum to `+1` and the declared beam coefficient to `-1`.

For each external support/MPC/coupling row, form `c_hat=c_phys S_q` and its
Euclidean norm. Exact zero row with exact zero RHS is omitted and reported;
exact zero row with nonzero RHS is infeasible. Otherwise divide row and RHS by
the norm, choose sign from the largest-magnitude coefficient (ties inside
`256*n*eps_p` use the smallest column), make that pivot positive, serialize in
global stable-ID DOF order, and sort rows ordinally by exact coefficient/RHS
mpf tuples. For feasibility define `C_hat=[C_D;C_phys_hat]` and
`d_hat=[0;d_phys_hat]`; require
`rank(C_hat)==rank([C_hat,d_hat])` at every multiplier. The homogeneous combined stack contains the projector-derived
orthonormal `C_D` row basis followed by these normalized physical rows; its
rowspace projector and null basis `T` use the same guard-precision rank and
projector-column canonicalization. No sequential nullspace projection is
permitted.

The free quotient partition must form `R_G=R_N intersection G` and require
`dim(RQ)=dim(R_N)-dim(R_G)` at every precision and multiplier. The constrained
partition must form `L_G_C=L_C intersection G_C` and require
`dim(RQ_C)=dim(L_C)-dim(L_G_C)` at every precision and multiplier. Each
physical constraint fixture serializes and stabilizes its expected-feasibility
Boolean plus `rank(C_hat)` and `rank([C_hat,d_hat])`; every feasible fixture
also serializes and stabilizes `N_C`, `G_C`, `P_C`, `L_C`, `L_G_C`, `RQ_C`,
and `Z_C`. Any categorical drift is a blocker.

## 6. Explicit exclusions

This stage introduces no production selector, public API, formulation token,
automatic gauge removal, imposed constraint, penalty, stabilization,
hourglass energy, tuned stiffness, rank repair, assembly mutation, cache key,
restart schema, sibling write, package publication, or benchmark claim.

It does not qualify nonlinear `/D`, geometric stiffness, buckling, recovery,
optimized batches, arbitrary shell/beam intersections, or a separately named
energetic rank-18 formulation. Even a successful proof authorizes only a later
content-addressed linear-adapter plan; it does not activate the formulation.

## 7. Focused execution and closeout

All tests use a fresh basetemp beneath the execution worktree and verify its
absence after removal. Exact commands are recorded after the worktree is
created, with pinned clean source roots and module-origin assertions. Minimum
gates are:

1. syntax/import and deterministic cases validation;
2. independent 80/160/320 precision oracle and repeated byte-identical output
   under the same manifest;
3. focused pytest wrapper including accepted binary64 Eq. 21/Eq. 25 agreement;
4. unchanged accepted `test_s4_eq21_eq25_reference.py`,
   `test_s4_nullspace_semantics_proof.py`, and restricted integration/activity
   tests;
5. `git diff --check`, exact changed-path inventory, and independent
   equation/constraint/precision audit.

Only after these gates pass may the bounded slice be committed. The completion
packet records commit/tree/parent, exact paths and raw/canonical hashes,
commands/results, deterministic output hash, independent verdicts, cleanup
inventory, and one of two outcomes:

- `CERTIFIED_FOR_LATER_LINEAR_ADAPTER_PLANNING`; or
- `NO_GO_PRODUCTION_RESTRICTION_UNCHANGED` with the minimal counterexample.

The branch is integrated without rewriting accepted history only after the
outcome is independently verified. Hosted CI must finish green before final
closeout. Canonical proof/quarantine histories and evidence are preserved.

The first exact monolithic full-catalog attempt is preserved as an execution
blocker: it reached the registered 30-minute caller deadline, exited 124, and
emitted no terminal JSON or scientific result. It authorizes no fixture,
precision, threshold, equation, or classification change.

The superseding execution is deterministically sharded by precision only. The
oracle accepts `--precision` with exactly one of `80`, `160`, or `320` together
with `--full --output PATH`; each invocation evaluates the complete registered
local/topology/covariance/activity/constraint catalog at all three sensitivity
multipliers for that precision and emits one canonical
`s4-drill-constraint-precision-shard-v1` JSON packet. It accepts
`--merge-shards SHARD80 SHARD160 SHARD320 --output PATH` only as a non-scientific
canonical merger: it rejects missing/extra/duplicate precisions, any identity,
environment-manifest, schema, or cases-hash mismatch, verifies each shard's
raw bytes equal its canonical reserialization, records each raw shard SHA-256
in the final packet, orders records as 80/160/320,
recomputes the unchanged cross-precision `_scientific_summary`, and writes the
same final scientific packet schema that the monolithic path would have
written, plus one explicitly non-scientific `execution_shards` object mapping
the ordered precision strings to raw shard SHA-256. It may not recompute, omit,
or alter scientific matrices.

Run two complete serial shard sets beneath the untracked task-owned directory
`.s4_drill_constraint_shards/`, merge the first set directly to the registered
stored-output path and the second to an untracked repeat path, and require
byte-for-byte equality and equal SHA-256. Each shard has its own 30-minute
caller deadline; merge/validation has a five-minute deadline; only one process
runs at a time, no shard consumes output from another, and no result from the
timed-out monolithic attempt is reused. The full registered catalog remains
bounded to at most 64 global generalized coordinates, starts no child workers,
performs no build/benchmark/profiler, has an aggregate 190-minute hard ceiling,
and expects peak memory below 2 GiB. The user has explicitly removed any
separate PERF lease request requirement; that does not authorize scope
expansion. All shard and repeat files remain preserved through independent
closeout and are removed only in the final task-owned cleanup.

The exact resolved shard directory is
`C:\Github\ANYsolver\.perf2-worktrees\s4-drill-constraint-certification\.s4_drill_constraint_shards`.
The only precision outputs are `set1_080.json`, `set1_160.json`,
`set1_320.json`, `set2_080.json`, `set2_160.json`, and `set2_320.json` beneath
that directory. The only merge outputs are the registered
`docs/reference_cases/s4_drill_constraint_oracle_output.json` and
`.s4_drill_constraint_shards/repeat_merged.json`. CLI modes are mutually
exclusive: validation/quick/monolithic, one `--precision` shard, or one
`--merge-shards` operation. Every supplied path is resolved and case-folded;
the oracle rejects path escape, a symlink or Windows reparse point in any
existing component, case-fold duplicate inputs, input/output alias, a shard
input outside the exact directory, an output outside its exact allowlist, and
any pre-existing output or same-directory temporary target.

Writes use an exclusive exact sibling temporary path formed by appending
`.tmp` to the target filename. Canonical bytes are fully produced in memory,
the temporary is opened with exclusive-create semantics, written, flushed,
`fsync`ed, and closed, and only then atomically replaced into the absent target.
Any timeout or nonzero result stops the remaining sequence; after confirming
that no worker remains, every completed, partial, or temporary artifact is
inventoried and preserved, and no failed/partial shard is ever merged. No
cleanup occurs before independent closeout.
