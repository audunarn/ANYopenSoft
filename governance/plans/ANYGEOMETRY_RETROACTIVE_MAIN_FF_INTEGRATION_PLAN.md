# ANYgeometry Retroactive Main Fast-Forward Integration Plan

## Objective and authority

Integrate the independently accepted ANYgeometry kernel update into the inactive local `main` branch by fast-forwarding only its Git ref. This work is explicitly user-authorized through the ecosystem Boss delegation.

## Repository and exact refs

- Repository: `C:\Github\ANYgeometry`
- Preserved active checkout: `native_hybrid_mesher`
- Required old `main`: `f2d7793d7d32a6dcd772c7ed8701aca11b459288`
- Accepted target: `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`
- Update method: `git update-ref refs/heads/main <target> <old>`

## Owned and excluded state

Owned mutation: only `refs/heads/main` in the local ANYgeometry repository.

Excluded and preserved:

- the checked-out `native_hybrid_mesher` branch, index, and worktree;
- untracked `.github/`, `.idea/vcs.xml`, and `dist_gap_closure/`;
- all remotes and remote-tracking refs;
- all files in ANYgeometry;
- unrelated ANYopenSoft work outside this plan document.

## Procedure and invariants

1. Verify the active branch and HEAD, exact old and target refs, worktree occupancy, and clean fast-forward ancestry.
2. Record this plan and its SHA-256 before changing the ref.
3. Atomically compare-and-swap local `main` from the exact old SHA to the exact target SHA.
4. Verify `main` equals the target, the active checkout/HEAD is unchanged, ancestry is fast-forward-only, protected untracked paths remain present, and no remote ref changed.

## Definition of done

- Local `main` resolves exactly to `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`.
- `native_hybrid_mesher` remains checked out at the same SHA.
- Only the inactive local `main` ref changed in ANYgeometry.
- The specified untracked paths remain untouched.
- No checkout, merge commit, push, publication, test, build, or benchmark is performed.

