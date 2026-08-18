# ANYfileIO accepted-main fast-forward integration plan

Date: 2026-08-13 (Europe/Oslo)

This content-addressed plan covers only two local fast-forward integrations and
their post-integration remote comparison. It creates no source commit and grants
no rebase, reset, force update, push, tag, release, package publication, or V2
OCP-evidence execution authority.

## 1. Accepted inputs and exact targets

The accepted V2 probe source remains frozen and outside both repositories:

- path `C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v2\probe.py`;
- SHA-256 `3A86FB437E804A0CB0ED205C1A41FF536B61300F38AE4F08945BFEF7B0C3EED6`;
- 139,062 bytes/3,238 LF/0 CR.

Integrate exactly:

| Repository | Required old local `main` | Accepted new local `main` | Accepted tree |
| --- | --- | --- | --- |
| `C:\Github\ANYfileIO` | `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | `5513881827cdee9fd337497a2730a5912d8ea751` | `68d703646c5d9b556c1ecdbdb96f677a4ba9a381` |
| `C:\Github\ANYfileio-occt` | `571231dc4c7d8b4131daac6b719a6b93125a20b4` | `23b441c3fcabb5bf4cf077daca882b984f978b42` | `a996a21a31c775660eb9dac3d491160231ba8cc1` |

The ANYfileIO target is the accepted NumPy-only lightweight-core handoff from
plan SHA-256 `739EE860455966EC157BB029FD806EB3B42500562EC06D9F4C430AC85E3AC15F`.
The provider target is the accepted capability-zero native-foundation follow-up.

## 2. Preflight and protected state

Before either update, fail closed unless:

1. both old and new commits resolve locally, each required old commit is an
   ancestor of its new commit, and both new trees equal section 1;
2. each `refs/heads/main` equals its required old value;
3. every linked worktree in both repositories is clean, its branch/HEAD equals
   the preflight snapshot, and ANYfileIO `main` is not checked out in any
   worktree;
4. the primary ANYfileio-occt checkout is clean on `main` at its required old
   value and tracks `origin/main` without local divergence;
5. remotes remain exactly the existing HTTPS `origin` remotes;
6. ANYfileIO's fourteen public/dependency blobs listed in the accepted handoff
   plan match the accepted target; and provider target blobs remain exact:
   `LICENSE=f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`,
   `pyproject.toml=e3bebec031dfb31daa0b8b35483c819e0122687d`,
   `src/anyfileio_occt/__init__.py=269ea984b66b7cc9b02a1b4f4cd9e019f69ea0af`,
   `src/anyfileio_occt/backend.py=d417ede2064352e377a543b345269c22baa5fc3d`,
   and `tests/test_bootstrap.py=261053280a9e186a07999742d34fa5d53b5f2e3a`;
7. the V2 task root contains only the frozen probe, V2 final/pending/sentry paths
   are absent, and the retired seven-file receipt remains byte-exact with
   `SHA256SUMS.txt` SHA-256
   `5AB56F7750DAA11650FECF698F108435A08B0083E0525A43106BFB3414E5A7F5`
   and `OUTCOME.json` SHA-256
   `D996AEAF89B7A6248601B7B00E8393664A874883AF753E9EEF0EEB3608EFBAB7`.

## 3. Exact local fast-forwards

Perform no checkout in ANYfileIO. Because its `main` is inactive, update it with
one compare-and-swap ref transaction:

```text
git update-ref refs/heads/main 5513881827cdee9fd337497a2730a5912d8ea751 82a0f5f110361fcd902cd3aac5d4c6beeaa187fa
```

In the clean primary ANYfileio-occt checkout, update its checked-out `main` and
working tree with exactly:

```text
git merge --ff-only 23b441c3fcabb5bf4cf077daca882b984f978b42
```

Stop on any ref drift, checkout dirt, conflict, hook failure, non-fast-forward,
or unexpected path change. Do not rewrite history and do not update any other
local branch.

## 4. Additive origin synchronization

Only after both local fast-forwards succeed, run exactly once per repository:

```text
git fetch --prune --no-tags origin
```

This is the sole network authority. It may update/prune `refs/remotes/origin/*`
under the repository's existing fetch refspec, but it must not update local
branches, fetch tags, push, authenticate for publication, or merge an origin
commit. Record the final `origin/main` SHA and
`git rev-list --left-right --count refs/heads/main...refs/remotes/origin/main`
as local-only and remote-only counts. Remote divergence is reported, never
resolved in this plan.

## 5. Definition of done

After fetch, require and report:

- both local `main` refs and trees equal section 1 exactly;
- ANYfileio-occt primary checkout is clean and its index/worktree equal the
  accepted target tree; ANYfileIO's inactive ref update changed no worktree;
- every linked worktree branch/HEAD and clean state matches preflight;
- all protected blobs and the frozen V2/retired-receipt checks still pass;
- exact local/remote main SHAs and ahead/behind counts for both repositories;
- no source diff, new commit, rebase, reset, force operation, push, tag,
  publication, or evidence execution occurred.

No test rerun is required: these are FF-only integrations to already accepted
trees. Exact ref/tree equality, clean checkout/index proof, protected blobs, and
unchanged worktree inventories are the proportionate integration checks.
