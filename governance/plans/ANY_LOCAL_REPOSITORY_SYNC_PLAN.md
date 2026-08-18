# ANY local repository synchronization plan

## Objective and authority

Synchronize configured `origin` tracking refs and safely advance only local
branches that are provably behind their upstream by a strict fast-forward.
This is repository administration only: no implementation, contract, history,
or publication change is authorized.

Registered repositories and preflight identities:

| Repository | Checked-out branch | Preflight HEAD | Default remote branch |
| --- | --- | --- | --- |
| `C:\Github\ANYopenSoft` | `main` | `7d29eaef1c899fc56681a723184c97e2ed04abb0` | `origin/main` |
| `C:\Github\ANYstructure` | `clean-up-after-external` | `4a79b860739c2f0b24f61314d4c13d943886bdd3` | `origin/master` |
| `C:\Github\ANYmaterial` | `main` | `4626887667f4c251479d26f321b9e73b046a2783` | `origin/main` |
| `C:\Github\ANYio` | `main` | `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | `origin/main` |
| `C:\Github\ANYtk3D` | `main` | `0f49efc53670c601bbabc012d856cc8ca18dcc9b` | `origin/main` |
| `C:\Github\ANYbuckling` | `main` | `3fe06c9ea126fcd59f2cd0ce825a029540b479e9` | `origin/main` |
| `C:\Github\ANYintelligent` | `move_solver` | `a1f58f3488e6a250fa0ce5b189fbfc8f658415ff` | `origin/main` |
| `C:\Github\ANYtimeseries` | `main` | `c578e910fd9d1ea481b4fae144a75bd66549beaf` | `origin/main` |
| `C:\Github\ANY3dView` | `main` | `cd2098dd55f12a60ea7ccbe9379989ef84933ae5` | `origin/main` |

## Procedure and safety boundary

1. Capture exact branch, HEAD, upstream, ahead/behind, worktree status, remotes,
   remote default, and linked worktrees before network access.
2. Run one ordinary `git fetch --prune origin` per repository with a configured
   origin. Fetch is the only network action.
3. Recompute ancestry and ahead/behind after fetch.
4. Preserve every tracked modification and untracked path. A dirty checked-out
   branch is never switched, merged, reset, or otherwise advanced.
5. A clean checked-out tracking branch may use `git merge --ff-only <upstream>`
   only when local HEAD is an ancestor of its upstream. An inactive local
   tracking ref may be advanced only when it is not checked out in any worktree,
   its local tip is an ancestor of the upstream, and an atomic compare-and-swap
   `git update-ref <ref> <new> <old>` changes only that exact ref. Equal refs are
   unchanged.
6. Diverged, ahead-only, missing-upstream, gone-upstream, detached, ambiguous,
   or inaccessible states are reported without mutation.
7. Capture exact post-state and verify that no user-owned worktree path changed.

## Exclusions and ownership

No reset, rebase, force operation, checkout, stash, clean, deletion, merge commit,
feature-branch integration, push, tag, PR, release, dependency resolution,
implementation edit, build, test, benchmark, or performance run. Existing task
worktrees and user artifacts remain owned by their original tasks/users. The
only plan file written by this task is this document.

## Acceptance and evidence

- The plan identity is recorded by absolute path, byte length, and SHA-256.
- Every configured origin has one preserved fetch result.
- Each repository has exact pre/post local and remote refs, status, and
  ahead/behind evidence.
- Every branch mutation is a strict fast-forward to its exact upstream; no
  branch with dirty checked-out state is mutated.
- Divergence and missing/gone upstreams remain visible and unchanged.
- `git diff --check` is not used as a substitute for status preservation, and
  no functional qualification claim follows from synchronization.

This work is light repository metadata/network administration and requires no
performance lease. Risks are remote movement during the run, authentication or
network failure, stale tracking configuration, and inaccessible worktree paths;
all fail closed without retry-driven history changes.
