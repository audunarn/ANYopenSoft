# ANYmesh Native-Hybrid Release-Blocker Edit Plan

Date: 2026-08-13 (Europe/Oslo)

Status: registration candidate. Source editing starts only after this exact plan
is accepted. This plan authorizes light focused tests and one source commit, but
no build, wheel, benchmark, publication, merge, or push.

## Authority and base

- Governing program: `ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`, SHA-256
  `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.
- Repository: `C:\Github\ANYmesh`.
- Exact base: `c95328b604bfa4607ba82bbde76ceb8491134b1a`.
- Branch: `codex/native-hybrid-release-blockers`.
- Isolated worktree:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYmesh-native-hybrid-release-blockers`.
- Owner: this task only. No subagent or other repository may edit these paths.

The primary checkout must remain on its current branch and byte-identical. The
isolated path must not exist before `git worktree add`; creation is refused on
any unexpected base, branch, status, or pre-existing target.

## Owned paths

- `pyproject.toml`
- `README.md`
- `CHANGELOG.md`
- `.github/workflows/ci.yml`
- `.github/workflows/publish.yml`
- `tests/test_packaging.py`
- `reports/native_hybrid/decision_log.md`

All other files are excluded. In particular, historical compiled-triangulation
plans, thresholds, attempt scripts, final summaries, independent verification,
and evidence artifacts remain byte-exact. Existing decision-log bytes also
remain byte-exact; that file may receive one additive superseding entry only.

## Corrections

1. Change the base dependency to `ANYgeometry>=0.2.1,<0.3` and the planar extra
   to `ANYgeometry[planar]>=0.2.1,<0.3`; retain the `<0.3` cap.
2. Extend packaging metadata tests to require both exact normalized ranges.
3. Pin every ANYgeometry workflow checkout in CI and publish to accepted final
   tip `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`.
4. Add a fresh-source CI cell built with `ANYMESHER_DISABLE_NATIVE=1` that proves
   compiled capability is absent, public `auto` records absence-only Python
   fallback, and explicit `native` raises `MeshError`. It must not monkeypatch or
   treat corrupt-ABI failure as absence.
5. Correct the README ANYfileIO repository link to
   `https://github.com/audunarn/ANYfileIO`.
6. Append one dated superseding status to the decision log without replacing or
   rewriting historical claims. Record the current ANYgeometry floor as
   `ANYgeometry>=0.2.1,<0.3` (and the planar equivalent), and record pinned
   ANYfileIO main object
   `5513881827cdee9fd337497a2730a5912d8ea751` truthfully: NumPy-only base and
   semantics extra `ANYmesher>=0.2,<0.3`, `ANYmaterial>=0.1,<0.2`. Keep combined
   resolver and installed-wheel qualification explicitly open. Earlier report
   statements remain historical evidence and are not silently rewritten.
7. Add a truthful Unreleased changelog entry for these source/evidence changes.

## Light focused gate

Run once from the isolated worktree with the accepted ANYgeometry source first
on `PYTHONPATH`:

```powershell
python -m pytest tests/test_packaging.py tests/test_native_backend_defaults.py -q
```

Also parse both YAML workflow files as text through the packaging test. Do not
build an extension or wheel and do not execute a workflow locally.

## Delivery gate

Require exact base ancestry, owned-path-only diff, an append-only decision-log
diff, clean isolated worktree after commit, unchanged primary checkout status,
and one non-amended commit. Submit the plan hash, test result, changed paths,
commit SHA/tree, and primary preservation evidence for independent review. Stop
before merge or push.
