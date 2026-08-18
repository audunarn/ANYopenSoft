# ANYgeometry Retroactive Main Push Plan

## Objective and authority

Publish the accepted, already-integrated local ANYgeometry `main` tip to the configured GitHub `origin`. The user explicitly authorized this bounded push through the ecosystem Boss delegation.

## Exact repository and refspec

- Repository: `C:\Github\ANYgeometry`
- Required remote old tip: `f2d7793d7d32a6dcd772c7ed8701aca11b459288`
- Required local target tip: `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`
- Sole permitted refspec: `refs/heads/main:refs/heads/main`
- Push mode: ordinary fast-forward, never force

## Owned and excluded state

Owned mutation: GitHub `origin` branch `refs/heads/main` only.

Excluded and preserved:

- active local checkout `native_hybrid_mesher` and all local branch refs;
- worktree and index contents;
- untracked `.github/`, `.idea/vcs.xml`, and `dist_gap_closure/`;
- every other remote branch and all tags;
- package registries, releases, artifacts, and pull-request state;
- unrelated ANYopenSoft content outside this plan document.

## Procedure and safety gates

1. Verify GitHub authentication and configured origin.
2. Record exact porcelain inventory, tracked/index diffs, active branch, HEAD, local refs, and remote refs.
3. Run `git fetch --prune origin`.
4. Require remote `origin/main` to equal the exact old tip and local `main` to equal the exact target.
5. Require old tip to be an ancestor of target, with ahead 4, behind 0, and no divergence.
6. Require the dirty worktree, index, protected untracked inventory, active branch, and local refs to remain unchanged.
7. Push only the exact refspec without force.
8. Fetch/inspect the remote and require `origin/main` and the authoritative remote query to equal the exact target; recheck all preservation invariants.

## Definition of done

- Remote `main` resolves exactly to `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`.
- Local `main` and active `native_hybrid_mesher` remain at that target.
- No other local or remote ref changed because of this workflow.
- Porcelain inventory and tracked/index diffs are unchanged.
- No commit, staging, checkout, merge, rebase, reset, force push, tag push, package publication, build, benchmark, or test run occurs.

