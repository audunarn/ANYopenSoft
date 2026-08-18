# ANYmesh Release-Blocker Integration and Push Addendum

Date: 2026-08-13 (Europe/Oslo)

Status: source closeout accepted; push remains performance-lease gated.

## Frozen identities

- Accepted owner plan SHA-256:
  `6C2EFC61DD056AB1D57C0C60096B1BB9F87843A6B2C7A917D925FB7A992BBDD6`.
- Repository: `C:\Github\ANYmesh`.
- Primary branch: `main`.
- Required old local/remote main:
  `c95328b604bfa4607ba82bbde76ceb8491134b1a`.
- Accepted direct child:
  `e676783256833f0c17e8ff6536f0f73365998928`.
- Accepted tree: `5b6cf22cb1b669e4f4ff5f65f0314aae85b1c408`.
- Source branch: `codex/native-hybrid-release-blockers`.

## Preflight and local fast-forward

1. Fetch/prune origin, then require `origin/main` and authoritative
   `ls-remote refs/heads/main` to equal the old SHA exactly.
2. Require primary `HEAD`/`main` at the old SHA, branch `main`, and a clean
   primary status. Require the source worktree clean at the accepted child and
   verify its sole parent is the old SHA.
3. Capture all local refs, worktrees, branches, and statuses. Stop on any
   unexpected drift or divergence.
4. Run exactly one local `git merge --ff-only` from old main to the accepted
   child. Verify primary `HEAD`/`main`, source branch, commit/tree, worktree
   statuses, and all unrelated refs afterward. No rebase, reset, checkout,
   deletion, force operation, or additional commit is allowed.

## Lease-gated push

Only after an explicit performance lease grant, run one non-force push:

```powershell
git push origin refs/heads/main:refs/heads/main
```

No other refspec, branch, tag, package, workflow dispatch, release, or artifact
publication is authorized. Immediately verify the returned status and
`git ls-remote --heads origin refs/heads/main` equals the accepted child.

## Triggered remote workload

The push event triggers only `.github/workflows/ci.yml` at the accepted commit:

- `pytest`: 12 jobs (Windows, Ubuntu, macOS times Python 3.11-3.14);
- `native-absent`: 1 Ubuntu/Python 3.13 disabled-native source-build job;
- `gmsh`: 4 jobs (Windows/Ubuntu times Python 3.11/3.12);
- `wheel`: 3 platform jobs, each building/testing CPython 3.11-3.14 wheels via
  cibuildwheel.

Total matrix expansion: 20 GitHub-hosted jobs. Local resources are one short
Git network process, negligible RAM/disk, no GPU. Remote ETA is 20-40 minutes;
the wheel matrix dominates. The push does not trigger `publish.yml`.

## Completion evidence

Record plan bytes/hash, pre/post local and remote main SHAs, exact push output,
final source/main worktree statuses, preserved non-main refs, workflow URL/run
identity if immediately available, and the distinction between triggered CI
and completed CI. Release the performance lease immediately after push and
remote-ref verification; remote jobs may continue under their recorded run.
