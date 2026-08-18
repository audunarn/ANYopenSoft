# ANYfileIO accepted-main exact push plan

Date: 2026-08-13 (Europe/Oslo)

This bounded plan authorizes only two sequential, non-force pushes of already
accepted local `main` histories. It grants no feature-branch/tag push, force,
delete, rebase, reset, package publication, release, or OCP/V2 evidence action.

## Exact pairs

| Repository | Required fetched `origin/main` | Required local `main` | Target tree |
| --- | --- | --- | --- |
| `C:\Github\ANYfileIO` | `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | `5513881827cdee9fd337497a2730a5912d8ea751` | `68d703646c5d9b556c1ecdbdb96f677a4ba9a381` |
| `C:\Github\ANYfileio-occt` | `571231dc4c7d8b4131daac6b719a6b93125a20b4` | `23b441c3fcabb5bf4cf077daca882b984f978b42` | `a996a21a31c775660eb9dac3d491160231ba8cc1` |

The local integrations were governed by plan SHA-256
`20202DE9744270B5BCA2C0957EEBE5AD08CA96E41AA26400EF1F45403343FFF5`.

## Pre-push gate

For each repository, run one `git fetch --prune --no-tags origin`, then fail
closed unless local and fetched remote SHAs equal the exact pair above,
`origin/main` is an ancestor of local `main`, the directional counts are exactly
9/0 and 3/0 local-only/remote-only respectively, and no divergence exists.

Before the first push, require all nine linked worktrees clean and unchanged;
the accepted 14 ANYfileIO and five provider protected blobs exact; V2 probe
`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v2\probe.py`
at SHA-256 `3A86FB437E804A0CB0ED205C1A41FF536B61300F38AE4F08945BFEF7B0C3EED6`
(139,062 bytes/3,238 LF/0 CR); V2 final/pending/sentries absent; and the retired
receipt `SHA256SUMS.txt`/`OUTCOME.json` at
`5AB56F7750DAA11650FECF698F108435A08B0083E0525A43106BFB3414E5A7F5` /
`D996AEAF89B7A6248601B7B00E8393664A874883AF753E9EEF0EEB3608EFBAB7`.

## Exact pushes and confirmation

Push core first, provider second, with explicit source/destination and no force:

```text
git -C C:\Github\ANYfileIO push origin refs/heads/main:refs/heads/main
git -C C:\Github\ANYfileio-occt push origin refs/heads/main:refs/heads/main
```

After each push, fetch that origin once with `--prune --no-tags` and require
`refs/remotes/origin/main == refs/heads/main ==` the exact accepted target.
Record zero/zero ahead-behind. If the first push succeeds but the second fails,
stop and report the truthful partial state; never roll back, force, retry, or
widen scope.

## Definition of done

Both remote `main` tips equal the accepted targets, all local heads/worktrees and
protected/V2/retired-receipt state remain exact, and no branch or tag other than
the two named remote `main` refs was updated. No tests are rerun because this is
a publication of byte-identical, already accepted commit graphs; ref, ancestry,
tree, blob, clean-state, and remote-tip equality are the proportionate checks.
