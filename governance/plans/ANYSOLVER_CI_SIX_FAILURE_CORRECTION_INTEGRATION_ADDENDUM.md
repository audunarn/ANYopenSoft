# ANYsolver CI six-failure correction integration addendum

Date: 2026-08-14 (Europe/Oslo)

Status: **PLAN-ONLY REGISTRATION CANDIDATE.** This file authorizes no fetch,
branch update, push, workflow observation, test, build, cleanup, S4 action, or
other mutation until its exact SHA-256 is independently accepted and the Boss
grants the exclusive PERF lease described below.

## 1. Bounded objective

Integrate the already accepted CI-only correction by fast-forwarding ANYsolver
`main` from `3cdb51e` to its accepted direct child `82a9db28`, push only
`refs/heads/main`, and evaluate exactly one resulting 24-job hosted `Tests`
workflow. No new source correction is permitted.

CalculiX/PrePoMax remains on HOLD. S4 plans, proof/handoff commits, worktrees,
branches, evidence, and cleanup state remain immutable. A green result closes
only the compatibility prerequisite; it does not itself authorize an S4 merge.

## 2. Accepted identities

- Repository: `C:\Github\ANYsolver`.
- Old/main commit:
  `3cdb51efcdded232054225ea0eb9cc16dc79dde9`.
- Old/main tree: `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7`.
- Accepted correction commit:
  `82a9db28d67507c82ef15c631f582a0c3bf6740e`.
- Correction tree: `00b2b20691e73a05589b797b32352f1c760a2451`.
- Correction sole parent:
  `3cdb51efcdded232054225ea0eb9cc16dc79dde9`.
- Correction subject: `fix: harden compatibility CI isolation`.
- Accepted correction amendment:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CI_SIX_FAILURE_CORRECTION_AMENDMENT.md`,
  SHA-256
  `E8D92692A0AC07F06BF2F140D47532147D7320B97BD1BDEB5B0FFB7219614827`.
- Accepted transport/job-oracle reference:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NATIVE_HYBRID_SAFE_TRANSPORT_AMENDMENT.md`,
  SHA-256
  `8F6ABA69C0FAAC4C60E3CAB2EAFF4A9103C08E5FE1932B4D767AB99C56185307`.

The correction changes exactly these paths:

1. `.github/workflows/ci.yml`, blob
   `7583109c00f0e16075892c9a3057015a396ddce9`;
2. `tests/test_anyfileio_version_compatibility.py`, blob
   `de86424fa6d1445a17a496c641ec38d1a4b4280e`;
3. `tests/test_anymesher_version_compatibility.py`, blob
   `593d4cd88e091a3ffc8023a8d69b13de64d29a21`.

The correction worktree is
`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`
on `refs/heads/codex/ci-six-failure-correction` and must remain clean at the
accepted correction commit.

## 3. Frozen prior failure truth

The only push-triggered `Tests` run on the old main is GitHub Actions run
`31746877870`, `completed/failure`, head `3cdb51e`, created
`2026-08-13T21:43:04Z`, updated `2026-08-13T23:26:37Z`. Independent terminal
accounting records exactly 24 jobs: 10 success and 14 failure. It is immutable
failure evidence and must not be rerun, retried, cancelled, deleted, or used as
green evidence.

The accepted correction addresses only its registered three-path CI isolation
defects. Eight generic pytest-lane failures remain evidence-limited and are not
silently claimed fixed. The new 24-job run is therefore decisive: any non-green
job, timeout, missing job, extra job, unexpected workflow, or transport failure
is preserved as a blocker. No second push, rerun, workflow dispatch, or source
correction is authorized by this addendum.

## 4. Preservation and security gates

Before any mutation, independently require:

- primary ANYsolver worktree clean on `main` at the old commit;
- local `main` and local `origin/main` equal the old commit;
- authoritative GitHub `refs/heads/main` equals the old commit;
- correction worktree clean at the accepted correction commit;
- correction commit has the exact parent/tree/subject/path/blob identities above;
- the complete 29-worktree inventory retains every accepted path, HEAD,
  branch/detached state, and porcelain status; the same full inventory is
  repeated after the push, with only the primary HEAD changing from old to
  correction;
- after excluding only `refs/codex/turn-diffs/*`, the accepted source branch,
  the correction branch, local `main`, local `origin/main`, and symbolic
  `origin/HEAD`, the 36 ordinal ref lines reproduce direct-TAB SHA-256
  `8C449F6DE6C0893289B59C8A3692655F3B7B6803511236F1464DA600A9E373A6`
  and TAB-to-SPACE SHA-256
  `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928`;
  the exact ref check is repeated after the push;
- canonical activity commits `1fd1c196518ac92b9dee920676f54c2d0cf58d26`
  and `7daa6e8c61954cfc1bc4469457fef0db154d3375` remain ancestors of both old and
  correction commits;
- the registered S4 plan remains SHA-256
  `D1D5713F1B58D7ECF15AD86BD2A7EAE61DB33BD533887881A48182141F2B9069`;
- proof `cfaf9c7a6e51e1cc0c3113648f84835e917fca2a` and handoff
  `931ed76943dc84fb9d01b26a5d6dd4c46af3d74a` retain their accepted identities;
- no existing `Tests` or `Publish` workflow run targets the correction commit.

Stop on any mismatch. Do not reset, rebase, checkout another branch, stash,
restore, force, prune worktrees, delete refs, remove evidence, or clean any path.

Windows Defender transport policy is binding. Use only transparent top-level
commands. Prohibited: large inline or encoded PowerShell, here-string source
generation, hidden windows, nested PowerShell, `Start-Process` chains, Defender
restore/allow/exclusion/whitelist actions, and any previously quarantined
launcher. No script is generated by this addendum.

The host `gh` authentication is invalid and `gh` is therefore prohibited for
this gate. Hosted-run reads use only the connected GitHub API tool
`mcp__codex_apps__github_fetch`; it performs no workflow mutation. If that
connection is unavailable or returns an incomplete/paginated result, stop and
report an authentication/transport blocker. Do not fall back to `gh`, raw
tokens, workflow dispatch, or a rerun.

The frozen transport URL for both fetch and push is exactly
`https://github.com/audunarn/ANYsolver.git`; both configured fetch and push
origin URLs must be that single line. All mutating Git commands override
`core.hooksPath` to the deliberately absent path
`C:/Github/ANYsolver/.git/codex-no-hooks-82a9db28`. The path must be absent
before and after execution. No repository, global, system, template, or
worktree hook may run.

### 4.1 Exact full-inventory block W

Invoke this exact block once before the fast-forward and once after terminal
reconciliation. Each command is a separate top-level command. Compare the first
output to the accepted 29-worktree contract and the second output to the first;
only the primary HEAD may change from old to correction. Every status output
must remain byte-identical to its accepted/pre-mutation counterpart.

```text
git worktree list --porcelain
git -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\analysis-session' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\baseline' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\corotational' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\damage-matrix' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\docs' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\functional-merge' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\hill48' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\impact' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\impact-reduced' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\integration' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\numerical-baseline' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-39846da' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-d596648' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-eb41e73' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\recovery' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-baseline-61e2f45' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-batch-qualification' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-geometry-handoff' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-improved-integration' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-nullspace-semantics' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-production-integration' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-reference-core' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\shell-batches' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\state-storage' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\thread-scaling' status --porcelain=v1 --untracked-files=all
git -C 'C:\Github\ANYsolver\.perf2-worktrees\verification' status --porcelain=v1 --untracked-files=all
git -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction' status --porcelain=v1 --untracked-files=all
git -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' status --porcelain=v1 --untracked-files=all
```

### 4.2 Exact invariant-ref block R

Invoke this command once before the fast-forward and once after terminal
reconciliation:

```text
git for-each-ref '--format=%(refname)%09%(objectname)'
```

From the captured direct output, exclude exactly
`refs/codex/turn-diffs/*`,
`refs/heads/codex/native-hybrid-release-blockers`,
`refs/heads/codex/ci-six-failure-correction`, `refs/heads/main`,
`refs/remotes/origin/main`, and symbolic `refs/remotes/origin/HEAD`. Require 36
remaining lines, each `refname<TAB>40-lowercase-hex`; ordinal-sort complete
lines, join with LF plus one final LF, and encode UTF-8 without BOM. Require the
two hashes frozen above before and after. The SPACE form replaces the sole TAB
in each already-sorted line with one SPACE and changes no other byte. This
review is performed from captured output, not a shell pipeline or generated
helper.

## 5. Exact Phase A operations: preflight, fast-forward, push, reconcile

Run each command separately from `C:\Github\ANYsolver`; do not combine commands
with shell operators or command substitution. Run full-inventory block W and
invariant-ref block R first, then run these direct commands in order:

```text
git status --porcelain=v1 --untracked-files=all
git symbolic-ref --quiet HEAD
git rev-parse HEAD
git rev-parse refs/heads/main
git rev-parse refs/remotes/origin/main
git remote get-url --all origin
git remote get-url --push --all origin
python -c "from pathlib import Path; p=Path(r'C:\Github\ANYsolver\.git\codex-no-hooks-82a9db28'); assert not p.exists(), p"
git show --no-patch --format=%H 82a9db28d67507c82ef15c631f582a0c3bf6740e
git show --no-patch --format=%T 82a9db28d67507c82ef15c631f582a0c3bf6740e
git show --no-patch --format=%P 82a9db28d67507c82ef15c631f582a0c3bf6740e
git show --no-patch --format=%s 82a9db28d67507c82ef15c631f582a0c3bf6740e
git diff-tree --no-commit-id --name-status -r 82a9db28d67507c82ef15c631f582a0c3bf6740e
git ls-tree 82a9db28d67507c82ef15c631f582a0c3bf6740e -- .github/workflows/ci.yml tests/test_anyfileio_version_compatibility.py tests/test_anymesher_version_compatibility.py
git -C C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction status --porcelain=v1 --untracked-files=all
git merge-base --is-ancestor 1fd1c196518ac92b9dee920676f54c2d0cf58d26 82a9db28d67507c82ef15c631f582a0c3bf6740e
git merge-base --is-ancestor 7daa6e8c61954cfc1bc4469457fef0db154d3375 82a9db28d67507c82ef15c631f582a0c3bf6740e
git show -s --format=%H%n%T%n%P cfaf9c7a6e51e1cc0c3113648f84835e917fca2a
git show -s --format=%H%n%T%n%P 931ed76943dc84fb9d01b26a5d6dd4c46af3d74a
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CI_SIX_FAILURE_CORRECTION_AMENDMENT.md SHA256
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NATIVE_HYBRID_SAFE_TRANSPORT_AMENDMENT.md SHA256
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_S4_RESTRICTED_INTEGRATION_PLAN.md SHA256
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CI_SIX_FAILURE_CORRECTION_INTEGRATION_ADDENDUM.md SHA256
git ls-remote --refs https://github.com/audunarn/ANYsolver.git refs/heads/main
git ls-remote --symref https://github.com/audunarn/ANYsolver.git HEAD
```

These two remote reads occur before the first fetch and must prove authoritative
remote main and symbolic HEAD are the old commit/main. Now perform connected
API call A0 and require `total_count=0` with an empty `workflow_runs` list:

```text
mcp__codex_apps__github_fetch({"url":"https://api.github.com/repos/audunarn/ANYsolver/actions/runs?head_sha=82a9db28d67507c82ef15c631f582a0c3bf6740e&per_page=100"})
```

Only after A0 succeeds, resume the direct commands:

```text
git -c core.hooksPath=C:/Github/ANYsolver/.git/codex-no-hooks-82a9db28 fetch --no-tags --no-prune https://github.com/audunarn/ANYsolver.git refs/heads/main:refs/remotes/origin/main
git rev-parse HEAD
git rev-parse refs/heads/main
git rev-parse refs/remotes/origin/main
git status --porcelain=v1 --untracked-files=all
git merge-base --is-ancestor 3cdb51efcdded232054225ea0eb9cc16dc79dde9 82a9db28d67507c82ef15c631f582a0c3bf6740e
git -c core.hooksPath=C:/Github/ANYsolver/.git/codex-no-hooks-82a9db28 merge --ff-only 82a9db28d67507c82ef15c631f582a0c3bf6740e
git symbolic-ref --quiet HEAD
git rev-parse HEAD
git rev-parse refs/heads/main
git status --porcelain=v1 --untracked-files=all
git diff-tree --no-commit-id --name-status -r 3cdb51efcdded232054225ea0eb9cc16dc79dde9 82a9db28d67507c82ef15c631f582a0c3bf6740e
```

Repeat A0 and require it remains empty. Then run this final pre-push remote CAS
read and the sole push as adjacent direct commands; authoritative remote main
must still be old:

```text
git ls-remote --refs https://github.com/audunarn/ANYsolver.git refs/heads/main
git -c core.hooksPath=C:/Github/ANYsolver/.git/codex-no-hooks-82a9db28 push --porcelain https://github.com/audunarn/ANYsolver.git 82a9db28d67507c82ef15c631f582a0c3bf6740e:refs/heads/main
git -c core.hooksPath=C:/Github/ANYsolver/.git/codex-no-hooks-82a9db28 fetch --no-tags --no-prune https://github.com/audunarn/ANYsolver.git refs/heads/main:refs/remotes/origin/main
git rev-parse HEAD
git rev-parse refs/heads/main
git rev-parse refs/remotes/origin/main
git ls-remote --refs https://github.com/audunarn/ANYsolver.git refs/heads/main
git ls-remote --symref https://github.com/audunarn/ANYsolver.git HEAD
python -c "from pathlib import Path; p=Path(r'C:\Github\ANYsolver\.git\codex-no-hooks-82a9db28'); assert not p.exists(), p"
```

Pre-fast-forward requirements are empty primary/correction porcelain, symbolic
HEAD `refs/heads/main`, exact old HEAD/main/origin-main/remote identities,
exact correction path/blobs, accepted 29-worktree/status and stable-ref
manifests, successful activity ancestry checks, exact S4/proof/handoff/plan
hashes, the Boss-registered SHA for this addendum, and zero target runs.

`git merge --ff-only` is permitted only under those clean exact-old conditions.
Because the correction is the verified sole child and old is its ancestor, this
is an atomic expected-old ref update: any concurrent local-main movement or
non-fast-forward condition must make it fail. It coherently advances the
primary worktree, index, HEAD, and `refs/heads/main` together; no detach,
checkout, manual index update, or fallback ref edit is allowed. Immediately
afterward, HEAD and main must be the correction and porcelain empty.

The repeated A0 and adjacent pre-push `ls-remote` freeze the target-run and
remote-old CAS state immediately before the push. A failure at any point stops
without rollback or substitution. The single ordinary push is the only remote
mutation; its source is the literal correction commit, its destination is only
`refs/heads/main`, and it has no force flag, no tags, and no other refspec. The
ordinary Git receive-pack non-fast-forward check is the remote CAS against the
adjacent advertised old commit. If its outcome is ambiguous, never repeat it;
use only post-push reconciliation.

Post-push requirements are local main, local origin/main, authoritative remote
main, and symbolic remote HEAD all resolving to the accepted correction commit;
empty porcelain; and a connected all-workflow target inventory containing
exactly one `Tests/push/main` run and no `Publish` or unexpected workflow. Call
the same all-runs URL immediately after reconciliation. If it returns zero
runs, poll only that URL at 30-second intervals for at most five minutes (11
total calls including the first). Any count greater than one or any wrong
workflow is a blocker. If the five-minute discovery window ends with zero runs
or an API ambiguity while the push-triggered hosted work may still be active,
retain the exclusive lease and switch to sparse all-runs reads no more
frequently than once per five minutes until the target appears or authoritative
provider evidence proves no hosted run remains active. Never cancel, dispatch,
or rerun. Record the sole positive integer run ID, URL, timestamps, status,
exact head SHA, branch, event, name, path, and `run_attempt`; require
`run_attempt == 1`. Do not infer or substitute an ID or attempt.

## 6. Literal-run-ID checkpoint and connected Phase B reads

Phase A does not authorize monitoring an inferred or substituted run. After the
post-push API result returns exactly one row, report its positive integer
`id`, URL, timestamps, status, and head SHA to the Boss. Independent
continuation must bind that literal decimal ID in place of `RUN_ID` below before
Phase B starts. Use only these connected read calls; `RUN_ID` is not a shell
variable:

```text
mcp__codex_apps__github_fetch({"url":"https://api.github.com/repos/audunarn/ANYsolver/actions/runs/RUN_ID"})
mcp__codex_apps__github_fetch({"url":"https://api.github.com/repos/audunarn/ANYsolver/actions/runs/RUN_ID/attempts/1/jobs?per_page=100"})
mcp__codex_apps__github_fetch({"url":"https://api.github.com/repos/audunarn/ANYsolver/actions/runs?head_sha=82a9db28d67507c82ef15c631f582a0c3bf6740e&per_page=100"})
git status --porcelain=v1 --untracked-files=all
git rev-parse HEAD
git rev-parse refs/heads/main
git rev-parse refs/remotes/origin/main
git remote get-url --all origin
git remote get-url --push --all origin
git ls-remote --refs https://github.com/audunarn/ANYsolver.git refs/heads/main
git show -s --format=%H%n%T%n%P cfaf9c7a6e51e1cc0c3113648f84835e917fca2a
git show -s --format=%H%n%T%n%P 931ed76943dc84fb9d01b26a5d6dd4c46af3d74a
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_S4_RESTRICTED_INTEGRATION_PLAN.md SHA256
certutil -hashfile C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CI_SIX_FAILURE_CORRECTION_INTEGRATION_ADDENDUM.md SHA256
python -c "from pathlib import Path; p=Path(r'C:\Github\ANYsolver\.git\codex-no-hooks-82a9db28'); assert not p.exists(), p"
```

Begin with one exact-run API call. While its status is `queued` or
`in_progress`, repeat only that exact-run call no more frequently than once per
60 seconds. Every response must retain `run_attempt == 1`. At the 120-minute
Phase-B caller deadline, if GitHub still reports `queued` or `in_progress`, do
not release the exclusive lease and do not cancel or rerun. Retain the lease,
switch to sparse read-only exact-run calls no more frequently than once per five
minutes, and continue until GitHub reports a provider-terminal state. Once
terminal, call the attempt-1 jobs URL once and the all-runs URL once, then
run the complete terminal preservation command block and repeat full-inventory
block W and invariant-ref block R exactly once.

The exact run must be terminal `completed/success`, and its immutable identity
must remain `Tests/push/main`, correction head SHA, `.github/workflows/ci.yml`,
the bound run ID, and `run_attempt == 1`. The attempt-1 jobs response must have
`total_count=24`, exactly the 24 unique ordinal job names frozen in the accepted
transport amendment, and all 24 jobs `completed/success`; no second page is
permitted. The all-runs response must have `total_count=1`, contain only this
same attempt-1 run, and report no second attempt, which proves no `Publish`,
rerun, or unexpected target workflow. Main identities remain correction,
primary porcelain stays empty, all 29 worktree/status records are preserved
apart from the expected primary HEAD advance, and both stable-ref hashes remain
exact. A terminal failure permits only the listed read-only final-state calls;
it grants no retry or correction.

## 7. Exclusive PERF lease request

After this addendum is independently accepted, request one exclusive lease:

- holder: `ANYSOLVER CI six-failure correction integration`;
- local work: one serial `git` process or one connected GitHub API read at a
  time, below 500 MB RAM, negligible sustained CPU, no GPU, and no task-created
  build/test output;
- remote work: the sole push-triggered 24-job GitHub `Tests` matrix;
- Phase-A Git ETA: 2-5 minutes, followed by at most five minutes of connected
  dense run discovery; expected Phase-A checkpoint: within 10 minutes from
  lease grant, followed by terminal-safe sparse discovery if provider state is
  not yet visible;
- literal-run checkpoint: at most 10 minutes after discovery for the Boss to
  bind the reported run ID and attempt 1; if continuation is delayed while the
  hosted run remains active, retain the lease and use only sparse five-minute
  exact-run reads until continuation or provider-terminal state;
- hosted run ETA: 90-120 minutes based on the prior exact run;
- Phase-B dense-polling cutoff: 120 minutes from explicit continuation, then
  provider-terminal sparse monitoring if still active;
- final Git/W/R evidence cap: five minutes;
- total expected lease ETA: up to 150 minutes, covering the expected
  10 + 10 + 120 + 5 minute stage bounds plus five minutes of transport margin;
  if GitHub remains active beyond that estimate, the lease is terminal-bound
  and remains exclusively held through sparse monitoring and final evidence;
- operations: exactly blocks W/R and sections 5 and 6, with the Phase-B run ID
  and attempt 1 bound literally after independent Phase-A continuation;
- no local test, build, wheel, benchmark, profiler, workflow dispatch, rerun,
  tag, release, package publication, or other repository action.

Release `PERF LEASE RELEASED` immediately after provider-terminal success or
failure and final preservation evidence, or after a transport/API ambiguity
only when no hosted heavy run remains active. Never release merely because a
caller/ETA deadline elapsed while GitHub is queued or running; retain the lease
and sparse-monitor to terminal. Report every command outcome, the run/job
ledger, final refs/status, and confirmation that no local `git` child or
outstanding connected API call remains.

## 8. Completion and handoff

Compatibility-gate completion requires:

1. accepted addendum SHA and explicit Phase-A lease grant;
2. exact non-force fast-forward and single main-only push;
3. synchronized clean local/tracking/authoritative main at `82a9db28`;
4. explicit literal-run-ID Phase-B continuation;
5. exactly one target Tests run, 24/24 terminal success, and no Publish run;
6. preserved correction, S4, CalculiX, worktree, ref, and failure evidence;
7. independent completion review and `ECOSYSTEM CLOSEOUT: OK`.

Only after this closeout may the existing S4 restricted-integration plan be
superseded to bind main commit `82a9db28...` and tree `00b2b206...`, then
re-registered under its existing gates. This addendum does not merge S4 proof or
handoff commits, edit solver physics/shared assembly/activity, run S4 tests, or
activate the improved formulation.

No cleanup occurs before independent terminal verification and Boss closeout.
After closeout, submit an exact cleanup inventory; preserve canonical
proof/quarantine history and remove only Boss-authorized task-owned disposable
residue.
