# ANY ecosystem release-blocker clearance program

Date: 2026-08-13 (Europe/Oslo)

Status: registered governing coordination plan. The user explicitly authorized
clearing release blockers for the associated ANY repositories. This plan does
not itself authorize external package publication, destructive history
rewrites, repository deletion, secret changes, billing, or third-party
administration.

## Objective

Converge the remaining accepted-but-unqualified workstreams into independently
verified, mergeable and GitHub-synchronized repository states. Correctness,
canonical ownership, deterministic fail-closed behavior, and truthful evidence
take precedence over schedule or performance.

## Pinned starting points

- ANYgeometry `main`: `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`.
- ANYmesh `main`: `c95328b604bfa4607ba82bbde76ceb8491134b1a`.
- ANYfem `main`: `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`.
- ANYsolver `main`: `12c565899e320b2142d8b23e31f5eb19702b2486`.
- ANYfileIO `main`: `5513881827cdee9fd337497a2730a5912d8ea751`.
- ANYfileio-occt `main`: `23b441c3fcabb5bf4cf077daca882b984f978b42`.
- ANYsolver S4 proof: `cfaf9c7a6e51e1cc0c3113648f84835e917fca2a`,
  quarantined until its integration plan closes formulation/policy gates.
- OCP inventory V2 plan SHA-256:
  `89EA6939C477A22E18A84ECD4805B298DDD601ADCE24661A47F2E9C31BC2CE07`;
  frozen probe SHA-256:
  `3A86FB437E804A0CB0ED205C1A41FF536B61300F38AE4F08945BFEF7B0C3EED6`.

Every repository task must re-fetch and compare these identities before edits,
merges, or qualification. Concurrent user work is preserved and never reset,
stashed, rebased, or overwritten.

## Workstreams and ownership

### 1. ANYfileio-occt / ANYfileIO native CAD line

The registered CAD task owns the V2 pinned-wheel call-shape inventory, followed
by separately content-addressed native lifecycle, reader/provider, capability
activation, and installed-wheel qualification slices. Only evidence-proven OCP
call shapes may enter production. ANYgeometry remains the sole owner of neutral
geometry/topology/identity/tolerance; ANYfileIO owns interchange and artifact
contracts; ANYfileio-occt is an optional heavy provider.

The V2 inventory is normal bounded functional work, not a performance lease.
Its exact three one-shot downloads and one controller invocation are permitted
after rechecking the frozen probe and absent V2 evidence paths. No retry occurs
without a new material review.

### 2. ANYsolver S4 integration

The S4 task owns a new integration plan based on current ANYsolver `main` plus
the accepted proof. It must explicitly decide, justify, and test formulation,
gauge/constraint, rank-policy, activity/deletion, and shared-assembly semantics.
No tuned penalty, invented stiffness, hidden stabilization, empirical threshold
tuning, or silent representative substitution is allowed. The proof commit is
not merged directly around these unresolved gates.

### 3. Native-hybrid dependency and wheel qualification

The native-hybrid task owns a content-addressed combined qualification plan for
ANYgeometry, ANYmesh, ANYfem, ANYsolver, ANYfileIO, and required dependencies.
It must freeze exact sources/artifacts, produce hashed wheels and a resolver
report/lock, prove installed origins and public behavior, exercise absence-only
fallback and strict-native failure semantics, and record platform boundaries.
CI can supply platform evidence that the local host cannot truthfully provide.

Heavy builds, broad suites, stress/scaling, and performance work require the
single ecosystem performance lease with exact command/resource/ETA packets.

### 4. Remaining migration and local changes

The ANYfileIO migration task must distinguish release-critical package/URL/
consumer compatibility from future portal or external-administration work.
Release-critical changes require a registered migration plan and focused
consumer tests; external service administration remains outside implied scope.

ANYfem's pre-existing four-path UI/test work is not implicitly accepted. Its
owner must register and independently review it, then either complete/commit it
or classify it as unrelated deferred work without altering its bytes.

## Merge and GitHub policy

Each repository slice requires its own plan, completion packet, independent
review, and `ECOSYSTEM CLOSEOUT: OK`. After that verdict it may fast-forward or
merge into the default branch, run proportionate post-integration tests, and
push normally to GitHub under the user's standing authority. No force push,
destructive rewrite, unreviewed branch, or quarantined evidence is included.

## Definition of done

1. OCP inventory and each native-provider layer have truthful accepted evidence,
   or an irreducible external blocker is precisely documented without a false
   release claim.
2. S4 is either integrated with physics-first policy and combined regressions or
   remains explicitly non-release with a concrete unresolved theoretical gate.
3. Required packages resolve from exact hashed artifacts in clean environments;
   installed origins and behavior are verified on claimed platforms.
4. Release-critical repository migration and consumer compatibility are closed.
5. All accepted code is on default branches and synchronized with GitHub.
6. Changelogs/release-readiness records distinguish implemented `Unreleased`
   work from tagged or externally published releases.
7. External publication occurs only under a later explicit publication action.

