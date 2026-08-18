# ANYfem Native-Hybrid Release-Blocker Edit Plan

Date: 2026-08-13 (Europe/Oslo)

Status: superseding registration candidate. This plan grants no worktree
creation, source edit, test, commit, merge, or push until its exact bytes and
SHA-256 are independently accepted. After acceptance it authorizes only the
six-path source scope and LIGHT focused gate defined below. It never authorizes
a build, broad GUI suite, performance run, publication, merge, or push.

## Authority and immutable source graph

- Governing program: `ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`, SHA-256
  `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.
- Repository: `C:\Github\ANYfem`.
- Exact clean ANYfem base:
  `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`.
- Future branch, only after plan acceptance:
  `codex/native-hybrid-release-blockers`.
- Future isolated worktree, only after plan acceptance:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYfem-native-hybrid-release-blockers`.
- Owner: this task only. No subagent or other repository may edit the owned
  paths.

Every sibling used by workflow installs or focused tests is pinned to one Git
commit. Moving branches, tags, ambient checkouts, editable installs from the
normal repository directories, and unrecorded source roots are forbidden.

| Sibling | Canonical repository | Accepted commit |
| --- | --- | --- |
| ANYsolver | `audunarn/ANYsolver` | `12c565899e320b2142d8b23e31f5eb19702b2486` |
| ANYmaterial | `audunarn/ANYmaterial` | `4626887667f4c251479d26f321b9e73b046a2783` |
| ANYgeometry | `audunarn/ANYgeometry` | `939e047f19177692c861a68eaef0eaa18b2976c5` |
| ANYmesh | `audunarn/ANYmesh` | `979f6a88f0d81507e1ac61b854f1f56362ce5e37` |
| ANYfileIO | `audunarn/ANYfileIO` | `48c6423c2aaf1f94f7bea8e7a971adf99500a91f` |
| ANYtk3D | `audunarn/ANYtk3D` | `0f49efc53670c601bbabc012d856cc8ca18dcc9b` |

The workflow must also replace moving third-party action tags with these exact
reviewed Git commits:

- `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`
- `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
- `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`

Plan execution must first prove every sibling commit exists as a commit object,
record its tree identity, and prove the ANYfem base and future branch ancestry.
No source may be read from a checked-out sibling merely because its path exists.

## Frozen dirty primary checkout

The primary ANYfem checkout remains outside this slice. Its exact four-path
status and content baseline is:

| Status | Path | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| modified | `src/anyfem/ui/scene.py` | 51,567 | `9E636A2ADC8BDE28A73632694C9D91AAA12AA229E0CABF5D4F045E30845C97DB` |
| modified | `src/anyfem/ui/viewport.py` | 41,357 | `6BCDA7DA5FF7E81AEB860311B6EB94BA476381390D9CBFC8EAFBE9517AE90A10` |
| modified | `tests/test_scene.py` | 22,433 | `E6AD70C9E1D410EE6536B64D2404934BD47F5E2741635691CDC3243FD78A1C81` |
| untracked | `tests/test_overlap_and_generator_ui.py` | 2,252 | `BED351383B22585AF4F65ECEBAC8ADA02797293584B618CEF4DC157D074200E0` |

Before worktree creation, before and after every authorized source/test phase,
and before delivery, require the same four statuses, byte lengths, and hashes,
with no additional primary-checkout path. No command may checkout, copy, stage,
clean, format, or otherwise touch these files. The beam-overlay/coupling and
overlap/generator failures remain separate follow-up work and are not release
inputs.

## Owned source paths

- `pyproject.toml`
- `.github/workflows/tests.yml`
- `README.md`
- `run_gui.py`
- `tests/test_migration.py`
- new `tests/test_release_dependencies.py`

All other ANYfem paths are excluded. The final diff and commit must contain
exactly this allowlist or a strict subset; no generated cache, report, archive,
or test residue may enter the repository.

## Required corrections

1. In `pyproject.toml`, require these exact semantic dependency contracts while
   retaining all unrelated requirements and upper bounds:
   - `ANYgeometry[planar]>=0.2.1,<0.3`
   - `ANYmesher>=0.2.1,<0.3`
   - `ANYfileio>=0.2,<0.3`
2. Replace obsolete `audunarn/ANYio`, `.ecosystem/ANYio`, and
   `C:\Github\ANYio` references in owned paths with canonical
   `audunarn/ANYfileIO`, `.ecosystem/ANYfileIO`, and
   `C:\Github\ANYfileIO`. Reject legacy `ANYio` path/repository tokens without
   treating the canonical `ANYfileIO` spelling as a match.
3. In both workflow jobs, pin every sibling checkout with the exact `ref` in
   the immutable source table and use only the matching `.ecosystem/<name>`
   install path. Pin every third-party action to the exact commit listed above.
   No checkout or install may omit its pin, follow a default branch, use the
   ambient machine checkout, or substitute `ANYio`.
4. Preserve dependency install order so ANYgeometry precedes ANYmesh, canonical
   ANYfileIO is installed before ANYsolver where the existing workflow installs
   both, and the final ANYfem install consumes those exact sibling trees.
5. Correct README persistence wording: ANYgeometry 0.2.0 is below the required
   0.2.1 floor and cannot read canonical schema-4 documents written by 0.2.1.
6. Update `run_gui.py` and the migration test's ecosystem source list to the
   canonical `ANYfileIO/src` path. Do not add lazy imports or an alternate
   compatibility alias.
7. Add focused tests that parse requirements semantically rather than by raw
   order; prove exact normalized names, extras, lower/upper bounds, and absence
   of markers, URLs, duplicate requirements, or unapproved ranges.
8. Add focused workflow assertions for the exact six sibling repository/path/
   commit triples, exact three action commits, install-source correspondence,
   and absence of moving action tags or default-branch sibling checkouts.

## Frozen-source LIGHT test environment

After plan acceptance, create the isolated ANYfem worktree only from the exact
base. Separately create one fresh external qualification root under
`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification`; refuse a
pre-existing target. Materialize each sibling with `git archive` from its exact
commit into a distinct child directory. Before extraction, require the local
repository object to resolve to the registered commit and record its tree SHA.
Never copy from, add a worktree in, or put an ambient sibling checkout on
`PYTHONPATH`.

The new focused test must receive the six expected archive roots explicitly,
launch a clean subprocess, import each public package it exercises, and assert
that every resolved module origin is under its matching archive root and outside
all normal `C:\Github\<sibling>` checkout roots. It must also prove the workflow
pins and semantic requirements against the immutable tables above. An origin
mismatch, missing module, duplicate source, or dependency range mismatch fails
closed.

Run exactly this LIGHT scope once from the isolated ANYfem worktree, with the
archive `src` roots in the registered order and no ambient `PYTHONPATH` entries:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONNOUSERSITE='1'
$env:PYTHONPATH='<isolated-anyfem>\src;<archive-ANYgeometry>\src;<archive-ANYmesh>\src;<archive-ANYfileIO>\src;<archive-ANYsolver>\src;<archive-ANYmaterial>\src;<archive-ANYtk3D>\src'
python -m pytest -p no:cacheprovider --basetemp <fresh-external-basetemp> tests/test_release_dependencies.py tests/test_migration.py -q
```

The placeholders must be replaced by the exact registered absolute paths in the
accepted execution packet; they are not shell wildcards. Before execution,
assert imported source roots and the current working directory. After execution,
verify the test did not modify either repository worktree, then remove only the
owned external archive/basetemp paths after resolving them beneath the registered
qualification root and rejecting reparse points. Require no `__pycache__`,
`.pytest_cache`, basetemp, or archive residue in either repository. This gate is
headless source evidence only: no wheel, build, full GUI suite, verification
campaign, performance run, or remote CI is authorized.

## Review, commit, and stop gate

After the LIGHT gate, submit the exact six-path-or-subset diff, result, module
origin ledger, sibling commit/tree ledger, and primary-dirty preservation ledger
for independent review. Only after exact-diff acceptance may this task create one
non-amended direct-child commit of
`7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`. Require a clean isolated
worktree and repeat the primary status/byte/hash gates. Stop before merge, local
main update, fetch, push, workflow dispatch, tag, release, or package
publication. Those actions require a separate content-addressed integration plan
and explicit authority.
