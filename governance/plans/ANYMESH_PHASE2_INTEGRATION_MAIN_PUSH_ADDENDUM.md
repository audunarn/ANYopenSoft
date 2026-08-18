# ANYmesh Phase 2 Integration and Main-Push Addendum

## Status and authority boundary

- Status: proposed for exact-plan review and performance-lease queueing only.
- This document authorizes no fetch, checkout, ref update, push, workflow dispatch, build, test, tag, release, package publication, or retry until the ecosystem boss accepts this exact content hash and grants the exclusive performance lease.
- Governing Phase 2 amendment: `C:\Github\ANYopenSoft\governance\plans\ANYMESH_SOURCE_CONTRACT_CI_FAILURE_PHASE_2_AMENDMENT.md`, SHA-256 `5D63ABF79A55E34AC7670130E3737BED795CA782664CC979155217B522DF11C3`.
- Accepted source commit: `979f6a88f0d81507e1ac61b854f1f56362ce5e37`.
- Accepted source tree: `dbf935cf030d21f28176a79a2a0cd8707039f8e0`.
- Sole parent and frozen old local/remote main: `4a0424a05fc4333d46d26f4c2fca97a113d0c09c`.
- Commit subject: `fix: qualify legacy intersection candidates`.
- No ecosystem closeout follows until the exact integration is verified and the sole push-triggered Tests workflow reaches terminal state with all 20 jobs successful.

## Repositories, worktrees, and preservation baseline

- Repository: `C:\Github\ANYmesh`.
- Primary worktree: `C:\Github\ANYmesh`; required initial branch `main`, HEAD `4a0424a05fc4333d46d26f4c2fca97a113d0c09c`, clean worktree and index.
- Accepted source worktree: `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYmesh-native-hybrid-release-blockers`; required branch `codex/native-hybrid-release-blockers`, HEAD `979f6a88f0d81507e1ac61b854f1f56362ce5e37`, clean worktree and index.
- Required initial local `refs/heads/main`, `refs/remotes/origin/main`, and authoritative remote `refs/heads/main`: `4a0424a05fc4333d46d26f4c2fca97a113d0c09c`.
- All non-main local and remote refs, tags, linked-worktree branches, worktree paths, and status inventories are exclusion baselines. Capture them before execution and require them unchanged afterward, except for normal `origin/main` movement caused by the authorized main fetch/push.
- Recovery evidence under `C:\Users\AUDUNA~1\AppData\Local\Temp\ANYmesh-phase2-recovery-53b5cc5c312e400ea6960c9746d9c9dd` is read-only and must retain these exact SHA-256 values:
  - `primary-three-path.patch`: `9BA3AF92EAF1A80C869A1D004C6B1908EE7540ECAECF8DFC1404749463E0ED79`.
  - `isolated-three-path.patch`: `9BA3AF92EAF1A80C869A1D004C6B1908EE7540ECAECF8DFC1404749463E0ED79`.
  - `pre_recovery_manifest.json`: `266C215BD49E242B57B39DA8A4180BDB9105DA5E21FECD8F1FE933AE502231B7`.
  - `recovery_manifest.json`: `48B676489EB69542ADAB7075EDFB476B6E4114488BE0C563B5A1264796D05F77`.

## Fresh preflight and fail-closed conditions

Under the granted lease, capture a fresh status/ref/worktree inventory and stop before mutation if any condition fails:

1. Both worktrees have the exact branches, commits, and clean index/worktree states above.
2. `git merge-base --is-ancestor 4a0424a05fc4333d46d26f4c2fca97a113d0c09c 979f6a88f0d81507e1ac61b854f1f56362ce5e37` succeeds.
3. The target has exactly one parent, the frozen old main, exact tree `dbf935cf030d21f28176a79a2a0cd8707039f8e0`, exact subject, and exactly these three paths:
   - `src/anymesher/_legacy_intersections.py`
   - `tests/test_intersection_meshing.py`
   - `tests/test_operations.py`
4. A read-only `git ls-remote --exit-code origin refs/heads/main` returns exactly the frozen old SHA. A read-only full `ls-remote` inventory may be captured for non-main preservation evidence.
5. One explicit main-only fetch, `git fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main`, succeeds, after which `origin/main` remains the frozen old SHA. Do not prune or fetch any wildcard, tag, or non-main refspec.
6. No process from a prior ANYmesh run remains, and no unexpected workflow already exists for the target SHA.

Remote drift, ancestry failure, status drift, an extra path/ref/worktree change, artifact mismatch, or an existing target workflow is a hard stop. Do not force, reset, rebase, retry, or tune.

## CAS local-main integration with inactive-main preservation

The primary worktree initially has `main` checked out. Make `main` inactive before its compare-and-swap update so no checked-out branch is moved behind a worktree:

```powershell
git -C C:\Github\ANYmesh switch --detach 4a0424a05fc4333d46d26f4c2fca97a113d0c09c
git -C C:\Github\ANYmesh update-ref refs/heads/main 979f6a88f0d81507e1ac61b854f1f56362ce5e37 4a0424a05fc4333d46d26f4c2fca97a113d0c09c
git -C C:\Github\ANYmesh switch main
```

Required gates:

- Before `update-ref`, verify the primary is detached at the old SHA and clean, while every other linked worktree remains on its frozen branch/SHA/status.
- `update-ref` is the sole local-ref mutation and uses the old SHA as its CAS argument.
- After reattachment, primary `HEAD` and local `main` must equal the target, with clean index/worktree and exact target tree.
- The accepted source worktree remains on `codex/native-hybrid-release-blockers` at the target and clean.
- Recompare the complete worktree/ref/status inventory. Stop on any unrelated difference.
- If a step fails, preserve and report the exact state. Do not automatically roll back or continue to push.

## Exact main-only non-force push

Immediately before pushing, repeat the remote-old `ls-remote`, local-main/target, ancestry, clean-state, tree, recovery-artifact, and preservation gates. Then run exactly:

```powershell
git -C C:\Github\ANYmesh push origin refs/heads/main:refs/heads/main
```

Constraints:

- No force option, force-with-lease, tag, wildcard, secondary refspec, branch deletion, PR, workflow dispatch, release, or package publication.
- After push, `git ls-remote --exit-code origin refs/heads/main` must return exactly `979f6a88f0d81507e1ac61b854f1f56362ce5e37`.
- Local `HEAD`, local `main`, `origin/main`, and remote `main` must converge on the target after one post-push `git fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main` and status reconciliation. Do not prune or fetch any wildcard, tag, or non-main refspec.
- Every non-main ref, tag, worktree branch, and excluded artifact remains unchanged.

## Unique Tests workflow gate

The push may trigger only the repository's normal `Tests` workflow for the exact target SHA.

- Expected event: `push`.
- Expected branch: `main`.
- Expected head SHA: `979f6a88f0d81507e1ac61b854f1f56362ce5e37`.
- Expected workflow-run count for this target: exactly one.
- Expected job count: exactly 20.
- Expected terminal requirement: all 20 jobs `success`; zero failure, cancelled, skipped, timed-out, neutral, or in-progress jobs.
- Expected matrix scope: ordinary pytest matrix, Gmsh matrix, disabled-native contract job, and platform wheel jobs as defined by the accepted workflow at the target.
- Prior failed runs `31699257852` and `31700439141` remain immutable historical evidence and are not rerun.

Monitor the unique run and every job until terminal. Record the workflow URL, run ID, creation/completion times, all job IDs/names/URLs/conclusions, and root logs for any failure. Also query every workflow associated with the target SHA and prove no `Publish` workflow, manual dispatch, tag workflow, or other unexpected run occurred.

If the Tests run or any job fails, preserve the failure and release the lease. Do not rerun, tune, amend, push another commit, or dispatch a workflow under this addendum.

## Lease request and resource envelope

- Exclusive holder: ANYmesh Phase 2 main integration and remote CI.
- Local operations: one pre-push and one post-push no-tags main-only fetch, bounded Git/ref/status checks, one CAS fast-forward, one non-force main push, and read-only GitHub monitoring.
- Remote workload: exactly one 20-job GitHub Actions Tests matrix.
- Local resources: one lightweight PowerShell/Git/GitHub CLI coordinator, under 500 MB RAM, negligible CPU, no GPU, no local build/test/benchmark.
- Remote ETA: 20-40 minutes; request a 50-minute lease envelope to include queueing and terminal accounting.
- Network: origin fetch/push and GitHub Actions/API monitoring only.
- No retry or second push under this lease.
- ANYfileIO currently owns the exclusive lease; this request remains queued until its terminal `PERF LEASE RELEASED` and a fresh explicit ANYmesh grant.

## Completion packet and stop gate

Release the performance lease immediately after all target jobs and process/state accounting are terminal. Submit:

- addendum path/bytes/SHA-256;
- exact before/after local and remote refs, ancestry, trees, branches, worktrees, and statuses;
- exact push command/result and authoritative remote confirmation;
- unique Tests run URL/ID and all 20 terminal job results;
- proof that no Publish or unexpected workflow ran;
- recovery-artifact immutability and non-main preservation evidence;
- confirmation that no process remains and no tag, release, package, force, retry, or other ref was touched.

Stop for independent completion review. Final closeout requires the exact boss verdict `ECOSYSTEM CLOSEOUT: OK`.
