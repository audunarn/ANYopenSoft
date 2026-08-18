# ANYsolver Native-Hybrid Release-Blocker Integration and Main-Push Plan

## Status and authority boundary

- Status: proposed for exact-content review and exclusive performance-lease
  queueing only.
- This plan authorizes no fetch, checkout, detach, ref update, push, workflow
  dispatch, build, test, retry, tag, release, package publication, or other
  mutation until the ecosystem boss accepts this exact file hash and grants an
  exclusive performance lease.
- Governing source plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NATIVE_HYBRID_RELEASE_BLOCKERS_EDIT_PLAN.md`,
  SHA-256
  `7A635F28B6BD068B9DBF24220C4B668D78CD1910D87105E34F1AD9BC0A9A8C02`.
- Accepted source commit:
  `3cdb51efcdded232054225ea0eb9cc16dc79dde9`.
- Accepted source tree:
  `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7`.
- Sole parent and frozen old local/tracking/remote main:
  `12c565899e320b2142d8b23e31f5eb19702b2486`.
- Commit subject: `fix: widen ANYfileIO compatibility`.
- This is integration and remote-CI qualification only. It grants no package,
  TestPyPI, PyPI, tag, GitHub Release, or publication authority.

## Repository and preservation baseline

- Repository and primary worktree: `C:\Github\ANYsolver`.
- Origin: `https://github.com/audunarn/ANYsolver.git`.
- Required initial primary state: branch `main`, HEAD and local main at
  `12c565899e320b2142d8b23e31f5eb19702b2486`, clean index and worktree.
- Accepted source worktree:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers`.
- Required source-worktree state: branch
  `codex/native-hybrid-release-blockers`, HEAD
  `3cdb51efcdded232054225ea0eb9cc16dc79dde9`, clean index and worktree.
- Required initial local `refs/heads/main`, local
  `refs/remotes/origin/main`, and authoritative remote `refs/heads/main`:
  `12c565899e320b2142d8b23e31f5eb19702b2486`.
- Frozen pre-source preservation manifest:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\pre_edit_state_manifest.json`,
  SHA-256
  `001F38163946A4126CC9294429C1DBB458792631476F7A6530F687ADABDE60DC`.
  Of its 27 worktrees, 26 non-primary worktrees must retain exact path, HEAD,
  branch/detached state, and full
  `status --porcelain=v1 --untracked-files=all` inventory throughout. The
  primary is the intentional transition: clean `main`/HEAD at old main before
  CAS and clean `main`/HEAD at the target afterward. The accepted source
  worktree is the separately registered 28th worktree and must remain clean at
  the target throughout.
- Frozen archive manifest remains read-only:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\archive_manifest.json`,
  SHA-256
  `BA4D2E5D20CCC9A33EDE7F6F5FE142BB2152ED0FA88D3E821D1AAF3212FA5EE4`.
- Local invariant-ref contract: exclude only volatile
  `refs/codex/turn-diffs/*`, the accepted source branch
  `refs/heads/codex/native-hybrid-release-blockers`, the two authorized moving
  refs `refs/heads/main` and `refs/remotes/origin/main`, and the local symbolic
  ref `refs/remotes/origin/HEAD`. The remaining 36 exact `ref object` lines,
  ordinal-sorted, LF-joined with one final LF, and encoded UTF-8 without BOM
  have SHA-256
  `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928`.
  Require exact line equality and this digest before and after execution.
- Gate local `refs/remotes/origin/HEAD` separately from the resolved-object
  invariant: its symbolic target must remain exactly
  `refs/remotes/origin/main`, and its resolved object must equal `origin/main`.
  Both remain at old main through CAS and push, and transition to the target
  only after the exact post-push main-only fetch. This gate is distinct from
  the remote server's `git ls-remote --symref origin HEAD` evidence.
- Capture a fresh exact `git ls-remote --refs origin` inventory before mutation
  and compare it after the push. This excludes the pseudo-ref `HEAD` by
  construction. Excluding only `refs/heads/main`, every remote line must be
  byte-identical. Separately require
  `git ls-remote --symref origin HEAD` to report
  `ref: refs/heads/main HEAD` before and after, with the advertised HEAD object
  moving from old main to the target. No non-main local or remote ref, tag,
  worktree branch, S4 branch, performance branch, or instrumentation ref may be
  mutated or deleted.

## Accepted target gate

Before any network or ref mutation, independently require that the target:

1. Is a commit with exactly one parent, the frozen old main.
2. Has exact tree `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7`.
3. Has exact subject `fix: widen ANYfileIO compatibility`.
4. Is a fast-forward descendant of old main.
5. Changes exactly these seven paths and no others:
   - `.github/workflows/ci.yml`
   - `.github/workflows/publish.yml`
   - `CHANGELOG.md`
   - `README.md`
   - `pyproject.toml`
   - `tests/test_anyfileio_version_compatibility.py`
   - `tests/test_anymesher_version_compatibility.py`

Any identity, ancestry, path, status, worktree, manifest, ref, or artifact
mismatch is a hard stop. Do not reset, rebase, force, amend, recover, retry, or
tune under this plan.

## Fresh lease-time preflight

After exact-plan acceptance and explicit performance-lease grant, run only
bounded Git/GitHub checks before mutation:

```powershell
git -C C:\Github\ANYsolver ls-remote --exit-code origin refs/heads/main
git -C C:\Github\ANYsolver fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main
git -C C:\Github\ANYsolver merge-base --is-ancestor 12c565899e320b2142d8b23e31f5eb19702b2486 3cdb51efcdded232054225ea0eb9cc16dc79dde9
gh run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
```

Required results:

- The first authoritative remote query returns exactly old main.
- The explicit fetch changes at most `refs/remotes/origin/main`, which remains
  exactly old main. It fetches no tag, wildcard, or non-main ref and never
  prunes.
- The target ancestry, target object, both registered worktrees, all manifests,
  the 26 non-primary frozen worktrees, the primary clean at old main, and the
  36-ref invariant remain exact. Local `origin/HEAD` remains symbolically bound
  to `origin/main`, with both resolving to old main.
- The target has zero pre-existing push-event `Tests` runs.
- An exact read-only `ls-remote --refs` inventory and a separate `--symref HEAD`
  record have been captured for post-push comparison.
- No prior coordinator, Git, GitHub CLI, Python, compiler, or workflow process
  owned by this operation remains.

Remote drift, an existing target run, an unexpected process, or any local
preservation drift stops the run before detach.

## CAS fast-forward of inactive local main

The primary initially has `main` checked out. Make it inactive before the
compare-and-swap ref update:

```powershell
git -C C:\Github\ANYsolver switch --detach 12c565899e320b2142d8b23e31f5eb19702b2486
git -C C:\Github\ANYsolver update-ref refs/heads/main 3cdb51efcdded232054225ea0eb9cc16dc79dde9 12c565899e320b2142d8b23e31f5eb19702b2486
git -C C:\Github\ANYsolver switch main
```

Gates and failure truth:

- Before `update-ref`, primary HEAD is detached at old main and clean; local
  main is still old main; every other worktree is unchanged.
- `update-ref` is the sole local branch mutation and uses old main as the CAS
  expected value.
- After reattachment, primary HEAD and local main equal the target and exact
  target tree, with clean index/worktree. The accepted source worktree remains
  clean on its feature branch at the same target.
- Recheck the 26 frozen non-primary worktrees byte-exact; require the primary
  clean on `main`/HEAD at the target and the registered 28th source worktree
  clean at the target; then recheck the 36 invariant refs, manifests, local
  `origin/HEAD` symbolic target/resolved-old phase gate, and full statuses.
- On any nonzero exit or state mismatch, preserve and report the exact partial
  state. Do not automatically roll back, repeat a command, or continue to push.

## Exact main-only non-force push

Immediately before push, repeat the authoritative remote-old query, local
  target/tree/ancestry/status checks, target-run count, manifests, phase-aware
  worktrees, 36-ref invariant, local `origin/HEAD` symbolic target/resolved-old
  phase gate, `ls-remote --refs` inventory, and remote `--symref HEAD` gate.
  Then run exactly once:

```powershell
git -C C:\Github\ANYsolver push origin refs/heads/main:refs/heads/main
```

No force option, force-with-lease, wildcard, tag, secondary refspec, deletion,
PR, workflow dispatch, release, or package publication is allowed.

After push:

```powershell
git -C C:\Github\ANYsolver ls-remote --exit-code origin refs/heads/main
git -C C:\Github\ANYsolver fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main
```

The authoritative remote, advertised remote HEAD object, local HEAD, local
main, and `origin/main` must all equal the target; remote HEAD must remain
symbolically bound to `refs/heads/main`. Local `origin/HEAD` must remain
symbolically bound to `origin/main`, and both must now resolve to the target.
The `ls-remote --refs` inventory may differ only at `refs/heads/main`; the 36
local invariant refs, the 26 frozen non-primary worktrees, the source worktree,
phase-adjusted primary status, and every manifest identity remain exact. Any
push or reconciliation failure is terminal for this plan; do not retry.

## Unique push-triggered Tests gate

The exact target workflow defines 24 expected jobs:

| Job family | Matrix | Count |
| --- | --- | ---: |
| `pytest` | Windows and Ubuntu x Python 3.11, 3.12, 3.13, 3.14 | 8 |
| `ANYmesher ... compatibility` | Windows/Python 3.13 x ANYmesher 0.1.0, 0.2.1 | 2 |
| `ANYfileio ... compatibility` | Windows/Python 3.13 x ANYfileIO 0.1.0, 0.2.0 | 2 |
| `Wheel smoke ...` | Windows and Ubuntu x Python 3.13 | 2 |
| `numba` | Windows and Ubuntu x Python 3.11, 3.12, 3.13, 3.14 | 8 |
| `pardiso` | Windows and Ubuntu x Python 3.11 | 2 |
| **Total** | | **24** |

Required run identity:

- Workflow: `Tests`.
- Event: `push`.
- Branch: `main`.
- Head SHA: `3cdb51efcdded232054225ea0eb9cc16dc79dde9`.
- Run count for this event/SHA: exactly one.
- Job count: exactly 24.
- Terminal result: all 24 jobs `success`; zero failed, cancelled, skipped,
  timed-out, neutral, stale, queued, or in-progress jobs.

Monitor the unique run to terminal with read-only GitHub CLI operations, for
example:

```powershell
gh run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
gh run watch <unique-run-id> --repo audunarn/ANYsolver --exit-status --interval 15
gh run view <unique-run-id> --repo audunarn/ANYsolver --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt,jobs
gh run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
```

Record the run ID/URL/timestamps and every job ID/name/URL/conclusion. Query all
workflows for the target and require exactly the one expected Tests push run.
In particular, no `Publish` workflow may run. Publish is configured only for
manual dispatch or published releases, neither of which is authorized.

If the run or any job fails, preserve the root failure and terminal accounting,
release the lease, and stop. Do not rerun, dispatch, tune, amend, or push a
follow-up under this plan.

## Exclusive performance-lease request

- Requested holder: ANYsolver native-hybrid release-blocker main integration
  and remote CI.
- Local work: one pre-push and one post-push no-tags/no-prune main-only fetch,
  bounded status/ref/worktree/object checks, one detach/CAS/reattach sequence,
  one non-force main push, and read-only GitHub monitoring.
- Local envelope: one PowerShell coordinator plus bounded Git/GitHub CLI child
  processes, under 500 MB RAM, negligible sustained CPU, no GPU, and no local
  build, test, benchmark, profiler, or package operation.
- Remote workload: exactly one 24-job GitHub-hosted Tests matrix. It may occupy
  up to 24 provider-managed runners concurrently, subject to GitHub queue and
  account concurrency limits. No fixed per-runner hardware claim is made.
- ETA: 20-45 minutes including queueing; request a 60-minute exclusive lease
  for terminal monitoring and accounting.
- Network: the exact origin queries/fetch/push and GitHub Actions/API monitoring
  above only.
- No retry, second push, workflow dispatch, Publish run, tag, release, package,
  or other ref operation is authorized under the lease.

## Completion packet and stop gate

Release the performance lease immediately after terminal run/job/process/state
accounting. Submit:

- this plan's path, bytes, and SHA-256;
- exact pre/post local and remote main values, target ancestry/tree/parent/
  subject/path inventory, phase-adjusted primary and frozen non-primary
  worktrees, statuses, manifests, 36-ref invariant, local `origin/HEAD`
  symbolic/resolved phase evidence, `ls-remote --refs` inventory, and remote
  `--symref HEAD` binding/object;
- exact CAS and push commands/results plus authoritative remote confirmation;
- unique Tests run ID/URL/timestamps and all 24 job results;
- proof that no Publish or unexpected workflow ran;
- confirmation that no process remains and no force, retry, tag, release,
  package, dispatch, publication, or other ref was touched.

Stop for independent integration review. This plan does not self-close the
broader native-hybrid program; the next owner may proceed only after the exact
boss verdict `ECOSYSTEM CLOSEOUT: OK` for this integration slice.
