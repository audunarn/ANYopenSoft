# ANYfileIO release-CI fast-forward integration and main-push addendum

Date: 2026-08-13 (Europe/Oslo)

Status: registration candidate. This content-addressed addendum grants no Git
fetch, ref update, push, workflow execution, rerun, publication, or release
authority until its exact SHA-256 and extent are accepted and the remote-CI
performance lease is explicitly granted.

## 1. Objective and frozen inputs

Integrate and publish only the accepted ANYfileIO release-CI source commit:

- repository: `C:\Github\ANYfileIO`;
- accepted edit plan SHA-256:
  `7D306B2BC4CB156773D97A1A4293628F82E13844058C1B6D8C4506D6E123BCF7`;
- required old local and fetched `origin/main`:
  `5513881827cdee9fd337497a2730a5912d8ea751`;
- accepted target:
  `48c6423c2aaf1f94f7bea8e7a971adf99500a91f`;
- target tree: `5c6c64a195bf36155180676b6f7d927228caefd7`;
- sole parent: `5513881827cdee9fd337497a2730a5912d8ea751`;
- accepted source branch: `codex/anyfileio-release-ci-cells`, clean with no
  upstream;
- origin: `https://github.com/audunarn/ANYfileIO.git`.

The old commit is the direct parent of the target; directional counts are
exactly zero old-only and one target-only. Local `main` is inactive in all
linked worktrees. The primary checkout remains untouched on
`codex/anyfileio-repository-rename` at
`0d2c7f8ef1b17f42f667d6183125e51cb650a70d`.

## 2. Exact accepted tree and protected state

The target changes exactly these seven paths/blobs:

| Path | Target blob |
| --- | --- |
| `.github/workflows/ci.yml` | `b5144949092709d5697a777acaf43ee13235f6d1` |
| `DEPENDENCY_MATRIX.md` | `d7e7c965899df9f60d8bfc8ef6d6a0fe036ee448` |
| `tests/test_calculix.py` | `f4e4831e4ca8b2920921772d54b6c1fc4340a4e4` |
| `tests/test_formats_and_cli.py` | `aa98cff40e02e0f0ae5ed1cadf2284939ee3fa6e` |
| `tests/test_gui.py` | `7ef11d28610766b096face7b982fceec8f792c0d` |
| `tests/test_packaging.py` | `9dfe5ff23eb980b6ed53c3156243b91e018f3f4a` |
| `tests/test_sesam.py` | `54e41d1881dcb6f5fcd0cf20937e60ca09e33cd9` |

At the target, reproduce the parent identities for every protected area:

- `src/anyfileio` tree `6be5f48f5df9ca1ce8bc84c06d35a022f5a2b70a`;
- `docs` tree `0c536d17b568fb2cbb2028664cec682a38600aee`;
- `pyproject.toml` `39ea8fd4e6e7554d87d42ad4382489cc68eec833`;
- `.github/workflows/publish.yml`
  `51fdef44630971bcc4b3b23eee8c318f98e90252`;
- `README.md` `c8873f0c4244a7f1603ec46915c1d3cdf37e3730`;
- `CHANGELOG.md` `f18ef6a7aeefee8f981eda4b7ce41a27bc90892c`;
- `LICENSE` `f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`;
- `MANIFEST.in` `57ae840ce4286a9c932992391ce7312a09a88d28`.

Before mutation, snapshot all local heads, tags, remote-tracking refs, config,
and all seven linked worktrees with path, branch, HEAD, index, worktree, and
untracked state. Require every worktree clean and preserve every non-`main` ref
and checkout exactly.

## 3. Remote preflight and local fast-forward

Only after this addendum and the exact performance lease are granted:

1. Run exactly one `git fetch --prune --no-tags origin` and one authoritative
   `git ls-remote --heads origin refs/heads/main`.
2. Fail closed unless fetched and authoritative remote `main` both equal
   `5513881827cdee9fd337497a2730a5912d8ea751`, local inactive `main` equals the
   same commit, origin is the frozen HTTPS URL, and remote `main` is an exact
   ancestor of the target with zero divergence.
3. Reproduce the target commit/tree/parent, seven target blobs, protected state,
   clean source branch, and all frozen worktree/ref states.
4. Atomically update only inactive local `main` with compare-and-swap:

   ```text
   git update-ref refs/heads/main 48c6423c2aaf1f94f7bea8e7a971adf99500a91f 5513881827cdee9fd337497a2730a5912d8ea751
   ```

5. Recheck local `main`, tree, protected objects, source branch, unrelated refs,
   and every worktree before any push.

Any drift or failed check stops the operation. Do not reset, rebase, force,
retry, roll back, or update another branch.

## 4. Exact push and remote-CI trigger

Under the same granted launch lease, push exactly one refspec without force:

```text
git push origin refs/heads/main:refs/heads/main
```

Then run one authoritative `ls-remote` and one post-push
`git fetch --prune --no-tags origin`. Require local `main`, `origin/main`, and
authoritative remote `main` all equal the accepted target, with zero/zero
ahead-behind.

The push event is the sole workflow trigger. Never dispatch or rerun a workflow.
Capture exactly one `.github/workflows/ci.yml` run whose event is `push`, branch
is `main`, and head SHA is the accepted target. If a unique run is not visible
within the lease's bounded observation window, stop and report `BLOCKED`; do not
trigger another run.

The accepted workflow expands to exactly 18 GitHub-hosted jobs:

- `base-only`: 8 (Windows and Ubuntu, Python 3.11-3.14);
- `semantics`: 8 (the same matrix);
- `coexists-with-anyio`: 1 (Ubuntu/Python 3.12);
- `wheel`: 1 (Ubuntu/Python 3.12).

Seventeen jobs run the full pytest suite. The wheel job builds, installs, and
smoke-tests the NumPy-only base wheel. The semantics cells perform 24 total
immutable owner VCS installs: geometry, mesh, then material in each of eight
cells, always `--no-deps`. The workflow contains no OCP/native, GPU, benchmark,
artifact upload, release, or package publication job. `publish.yml` is only
`workflow_dispatch`/release-triggered and must not run.

Release the exclusive launch lease immediately after exact remote-tip and
unique run-ID/URL capture, reporting that the 18 recorded remote jobs may still
be running. Terminal CI conclusions are later evidence from that same run, not
authority for a rerun. A green run is source-CI evidence only; installed-wheel
resolver and release qualification remain `UNRUN`/`BLOCKED` as frozen in the
accepted dependency matrix.

## 5. Failure preservation, exclusions, and completion packet

If any step fails, preserve the first outcome and truthful partial state. A
successful local fast-forward is not rolled back if a later push fails, and a
successful push is never rewritten if run capture fails.

Excluded: feature-branch or tag push, force/delete refspec, source edit, new
commit, checkout, reset/rebase, local test/build/install/resolver, manual
workflow dispatch or rerun, cancellation except at the lease's hard
administrative ceiling, OCP/provider/evidence paths, other repositories,
package upload, tag, release, or publication.

The completion packet reports:

- this addendum's path/SHA-256/bytes/LF/CR and the granted lease token;
- pre/post local, fetched, and authoritative remote SHAs and ancestry counts;
- exact CAS and push outputs, final tree/blobs, worktree/ref preservation;
- workflow run ID/URL/event/branch/head SHA and the exact 18 job identities;
- first outcome, elapsed time, current job conclusions, and no-rerun fact;
- absence of a publish run and final local process state.

No integration or push occurs during registration of this addendum.
