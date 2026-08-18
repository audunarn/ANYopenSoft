# Native-Hybrid Default-Branch Fast-Forward Plan

## Authority and objective

Following `ECOSYSTEM CLOSEOUT: OK` and explicit user authorization, integrate the
accepted native-hybrid repository core into inactive local `main` refs by exact
compare-and-swap fast-forward updates. This action changes refs only. It does not
checkout branches, modify working files, push, publish, build, or run tests.

## Exact ref updates

| Repository | Required current `main` | Accepted target |
|---|---|---|
| `C:\Github\ANYmesh` | `e31f8c700b91796b93a8d2b21a6d44f70145eaed` | `c95328b604bfa4607ba82bbde76ceb8491134b1a` |
| `C:\Github\ANYfem` | `c1c8ccb662eb8ecd8e4f08242855adf5b5d45166` | `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2` |
| `C:\Github\ANYsolver` | `61e2f45ae2ca4fa87a6e149b0f89fabf209e5279` | `12c565899e320b2142d8b23e31f5eb19702b2486` |

## Preconditions and method

- Require each active branch to remain `native_hybrid_mesher`.
- Require each local `main` to equal its recorded starting SHA.
- Require each starting SHA to be an ancestor of its accepted target.
- Update only `refs/heads/main` with `git update-ref <ref> <target> <old>` so
  drift fails closed and no worktree is switched.
- Preserve all working-tree bytes and status entries, including ANYfem's
  unrelated `scene.py`, `viewport.py`, `test_scene.py`, and
  `test_overlap_and_generator_ui.py` work.

## Verification and exclusions

- Verify exact post-update `main`, unchanged active branch, target ancestry, and
  byte-for-byte identical porcelain status output in all three repositories.
- Do not modify or push remote refs.
- Do not commit or alter unrelated ANYopenSoft governance/application work.
- Do not run tests, builds, benchmarks, wheels, resolver qualification, or
  publication steps.

## Additive post-integration local Git sync

After the three accepted-target updates and their local checks pass:

- Run `git fetch --prune origin` in ANYmesh, ANYfem, and ANYsolver.
- Record exact `main` and `origin/main` SHAs, ancestry direction, and commit
  ahead/behind counts.
- Keep each checked-out `native_hybrid_mesher` branch fixed. Preserve all
  working-tree status bytes, including ANYfem's unrelated dirty UI/test files.
- Restrict any post-fetch local update to the inactive local `main` ref. It is
  eligible only when `origin/main` exists, is a strict fast-forward descendant
  of local `main`, and the accepted native-hybrid target remains its ancestor.
  Use compare-and-swap `update-ref`; otherwise report ahead, equal, or diverged
  state without changing the ref.
- Never rebase, reset, force, checkout, merge, push, or update a remote ref.

## Completion criterion

Completion requires all three compare-and-swap updates and all post-update
identity/status checks to pass. Any drift or status mismatch stops the action
without repair, reset, checkout, or retry.

## Explicit multi-repository push amendment

The user explicitly authorizes publication of only the completed accepted local
`main` updates to each repository's existing `origin` remote:

| Repository | Required fetched `origin/main` | Required local `main` |
|---|---|---|
| ANYmesh | `e31f8c700b91796b93a8d2b21a6d44f70145eaed` | `c95328b604bfa4607ba82bbde76ceb8491134b1a` |
| ANYfem | `c1c8ccb662eb8ecd8e4f08242855adf5b5d45166` | `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2` |
| ANYsolver | `61e2f45ae2ca4fa87a6e149b0f89fabf209e5279` | `12c565899e320b2142d8b23e31f5eb19702b2486` |

For each repository, re-fetch and prune `origin`, require the exact pair above,
and prove remote-old is an ancestor of local-new. Capture the active branch,
porcelain status, and protected ANYfem file hashes before publication. Push
sequentially with the non-force refspec `refs/heads/main:refs/heads/main` and
confirm the exact remote SHA using `git ls-remote` before continuing.

Stop on any remote drift, divergence, rejection, or preservation mismatch. Do
not push `native_hybrid_mesher`, any other feature/quarantined branch, tags, or
packages. Do not checkout, merge, rebase, reset, force, delete, or publish a
package. Final verification must show unchanged active branches and worktree
state, exact remote `main` targets, and no additional ref publication.

### ANYfem preservation-baseline amendment

A concurrent read-only audit established that ANYfem is now benignly checked
out on `main` at the accepted target
`7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`, while `origin/main` remains at
`c1c8ccb662eb8ecd8e4f08242855adf5b5d45166`. Its same four unrelated dirty
UI/test paths remain present. For push execution, require and preserve this
exact checked-out `main` baseline and the protected file hashes/status. Continue
to require `native_hybrid_mesher` for ANYmesh and ANYsolver. Do not checkout or
otherwise alter ANYfem's branch, index, or working files.

### ANYsolver preservation-baseline amendment

A subsequent independent audit established that the primary ANYsolver worktree
is now benignly checked out on clean `main` at
`12c565899e320b2142d8b23e31f5eb19702b2486`, while `origin/main` remains at
`61e2f45ae2ca4fa87a6e149b0f89fabf209e5279`. Separate performance and S4
worktrees, including quarantined proof/integration refs, remain out of scope.
For push execution, require and preserve this exact clean primary `main`
baseline. Do not inspect, checkout, update, or publish any separate worktree or
its refs. Continue to require `native_hybrid_mesher` only for ANYmesh.
