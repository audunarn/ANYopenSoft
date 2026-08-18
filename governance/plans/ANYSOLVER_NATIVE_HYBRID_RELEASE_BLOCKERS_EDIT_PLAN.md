# ANYsolver Native-Hybrid Release-Blocker Edit Plan

Date: 2026-08-13 (Europe/Oslo)

Status: superseding registration candidate. This plan grants no worktree
creation, source edit, test, commit, merge, push, workflow run, build, wheel,
resolver qualification, or publication until its exact bytes and SHA-256 are
independently accepted. After acceptance it authorizes only the seven-path
source scope and LIGHT focused gates below.

## Authority, base, and preservation boundary

- Governing program: `ANY_RELEASE_BLOCKER_CLEARANCE_PROGRAM.md`, SHA-256
  `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`.
- Repository: `C:\Github\ANYsolver`.
- Exact clean base: `12c565899e320b2142d8b23e31f5eb19702b2486`.
- Future branch, only after plan acceptance:
  `codex/native-hybrid-release-blockers`.
- Future isolated worktree, only after plan acceptance:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers`.
- Owner: this task only.

The primary checkout is clean on `main` at the exact base. All existing
`perf2/*`, S4, qualification, detached, and other worktrees and refs are
excluded. Before creating the future worktree, record a content-addressed
manifest of every existing worktree path, HEAD, branch/detached state, porcelain
status, and every ref. Require byte-identical status and ref identity before and
after each authorized phase. No excluded worktree or ref may be checked out,
updated, staged, cleaned, rebased, merged, or otherwise modified.

## Immutable compatibility graph

The source and workflow proof must use only these Git objects. Moving defaults,
tags, VCS requirements without `@<commit>`, and ambient sibling checkouts are
forbidden.

| Role | Repository | Commit | Expected package version |
| --- | --- | --- | --- |
| material, both cells | `audunarn/ANYmaterial` | `4626887667f4c251479d26f321b9e73b046a2783` | `0.1.0` |
| legacy geometry | `audunarn/ANYgeometry` | `f2d7793d7d32a6dcd772c7ed8701aca11b459288` | `0.2.0` |
| current geometry | `audunarn/ANYgeometry` | `939e047f19177692c861a68eaef0eaa18b2976c5` | `0.2.1` |
| legacy mesh | `audunarn/ANYmesh` | `05ab5f45301c34de0ac86c1a0eb6407702d98e96` | `0.1.0` |
| current mesh | `audunarn/ANYmesh` | `979f6a88f0d81507e1ac61b854f1f56362ce5e37` | `0.2.1` |
| legacy fileIO | `audunarn/ANYfileIO` | `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` | `0.1.0` |
| current fileIO | `audunarn/ANYfileIO` | `48c6423c2aaf1f94f7bea8e7a971adf99500a91f` | `0.2.0` |

Workflow actions must use these exact reviewed commits:

- `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`
- `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
- `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
- `actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093`
- `pypa/gh-action-pypi-publish@dc37677b2e1c63e2034f94d8a5b11f265b73ba33`

Before source work, prove each ecosystem object exists as a commit in its
canonical repository and record its tree. Do not infer identity from an ambient
working tree, branch name, package directory, or installed distribution.

## Owned source paths

- `pyproject.toml`
- `README.md`
- `CHANGELOG.md`
- `.github/workflows/ci.yml`
- `.github/workflows/publish.yml`
- `tests/test_anymesher_version_compatibility.py`
- new `tests/test_anyfileio_version_compatibility.py`

All solver production modules, `tests/test_extracted_package_wiring.py`, and all
other paths are read-only. The final diff and commit must contain exactly this
allowlist or a strict subset and no generated evidence, cache, archive, wheel,
or test residue.

## Required source corrections

1. Widen only ANYsolver's direct consumer requirement from
   `ANYfileio>=0.1,<0.2` to `ANYfileio>=0.1,<0.3`. Retain all other
   dependencies, extras, package version, and the exact `<0.3` cap.
2. Align README compatibility/publication-order wording, Unreleased changelog,
   and the publish dependency gate with `ANYfileio>=0.1,<0.3`. State that the
   source/CI cells are compatibility coverage, not completed installed-wheel,
   index-resolver, or publication qualification.
3. Parse requirements with `packaging.requirements.Requirement`; require the
   normalized name `anyfileio`, no extras/marker/URL, one occurrence, and exact
   `SpecifierSet(">=0.1,<0.3")` independent of canonicalized order. Add the
   canonical-order regression `ANYfileio<0.3,>=0.1`.
4. Add a standalone public-contract probe for both fileIO endpoints. It must
   prove expected distribution/module version and origin, neutral SESAM
   document/read/write surface, CalculiX result surface consumed by ANYsolver,
   and exact ANYsolver re-export identity. Missing, unsupported, or mismatched
   symbols fail closed.
5. Add a semantic compatibility-graph assertion that reads `pyproject.toml`
   from the exact archived solver/sibling trees, normalizes every relevant
   requirement, and proves each selected package version satisfies every
   incoming constraint. Run it for both complete cells:
   - legacy: material accepted object, geometry `0.2.0`, mesh `0.1.0`, fileIO
     `0.1.0`, solver source;
   - current: material accepted object, geometry `0.2.1`, mesh `0.2.1`, fileIO
     `0.2.0`, solver source after the range edit.
   The assertion must explicitly prove a nonempty intersection for solver and
   fileIO mesh constraints and must fail if any requirement is missing,
   duplicated, unparseable, or unsatisfied. `--no-deps` installation is never
   accepted as this proof.
6. Extend the existing ANYmesher endpoint test without weakening its current
   public mesh assertions. Record and assert expected mesh, geometry, fileIO,
   solver, and module origins for each paired cell.

## Workflow corrections

1. Remove the moving `SIBLINGS` VCS URLs. In generic pytest, numba, pardiso, and
   wheel jobs, checkout material, current geometry, current mesh, and current
   fileIO at the exact immutable commits and install only their matching
   `.ecosystem` paths before ANYsolver. No default branch or ambient source may
   enter `sys.path`.
2. Pin every first-party checkout in every job and every third-party action in
   both workflows to the exact objects above. Preserve existing triggers,
   matrices, permissions, environments, and publication conditions.
3. In the ANYmesher compatibility matrix, pair legacy mesh with legacy geometry
   and legacy fileIO, and current mesh with final current geometry, final current
   mesh, and final current fileIO. Every matrix row carries all exact refs and
   expected versions; no row inherits a moving current checkout.
4. Add the corresponding two-row ANYfileIO compatibility cell using the same
   complete legacy/current graph. Build the solver wheel once per row and run
   the standalone probe from the external runner temp directory, not the source
   checkout.
5. Install each row's explicit local sibling paths together without
   `--no-deps`, then install the solver artifact and run `python -m pip check`.
   A later `--no-deps` reinstall of the already-built solver wheel is allowed
   only after the row's sibling-resolution and metadata checks pass; it cannot
   substitute for them.
6. Keep the publish workflow gated on real index availability and update only
   its fileIO range and immutable action refs. Do not claim the target index
   currently contains the required artifacts and do not dispatch publication.
7. Add source tests that reject moving action tags, missing sibling `ref` keys,
   unpinned VCS URLs, legacy pre-closeout current objects, mismatched checkout/
   install paths, broadened triggers, or altered publish permissions.

## Frozen-source LIGHT gate

After exact plan acceptance, create only the isolated solver worktree from the
registered base. Create a fresh external qualification root under
`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification`; refuse a
pre-existing target and any reparse point. Materialize each unique ecosystem
commit with `git archive` into its own child. Record commit/tree/content roots.
Never copy from or add an ambient sibling checkout to `PYTHONPATH`.

Run exactly this focused source test once from the isolated worktree. The
`PYTHONPATH` value contains no ambient repository, editable checkout, or legacy
cell. The two JSON environment values are consumed by the new focused test,
which must compare every imported module's exact version and resolved origin
before accepting the public re-export assertions:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONNOUSERSITE='1'
$env:PYTHONPATH='<isolated-solver>\src;<archive-current-material>\src;<archive-current-geometry>\src;<archive-current-mesh>\src;<archive-current-fileIO>\src'
$env:ANYSOLVER_EXPECTED_SOURCE_VERSIONS='{"anysolver":"0.2.0","anymaterial":"0.1.0","anygeometry":"0.2.1","anymesher":"0.2.1","anyfileio":"0.2.0"}'
$env:ANYSOLVER_EXPECTED_SOURCE_ROOTS='{"anysolver":"<isolated-solver>\src","anymaterial":"<archive-current-material>\src","anygeometry":"<archive-current-geometry>\src","anymesher":"<archive-current-mesh>\src","anyfileio":"<archive-current-fileIO>\src"}'
python -m pytest -p no:cacheprovider --basetemp <fresh-external-basetemp> tests/test_anymesher_version_compatibility.py tests/test_anyfileio_version_compatibility.py tests/test_extracted_package_wiring.py -q
```

The placeholders must be replaced with the exact registered absolute paths in
the accepted execution packet; they are not shell wildcards. Because
`tests/test_extracted_package_wiring.py` imports sibling modules during
collection, refuse to launch pytest unless every archive root exists, its
recorded commit/tree matches, and the complete `PYTHONPATH` string equals the
five-entry value above. The focused source test must fail if an import resolves
to site-packages, an editable install, a normal `C:\Github\<sibling>` checkout,
the wrong archive, or an unregistered path.

Then run each standalone probe once from a fresh external CWD with `PYTHONPATH`
containing only the isolated solver `src` and that cell's exact archive `src`
roots. Pass expected versions and absolute roots explicitly. Invoke the probes
in explicit `source` metadata mode: package versions and requirements come from
the exact archived/source `pyproject.toml` files, never
`importlib.metadata` from the running environment. Require every reported
origin to be beneath its matching archive/worktree root and outside normal
`C:\Github\<sibling>` checkouts. Also run the semantic graph assertion against
those same archive metadata files. Installed-distribution metadata assertions
are reserved for the workflow's built-wheel endpoint probes, which must invoke
explicit `installed` metadata mode after installation and `pip check`; source
and installed evidence may not be silently substituted for one another.

Afterward, prove both repository worktrees and the complete excluded-worktree/
ref manifest are unchanged. Remove only the owned external archive/basetemp
paths after resolving them beneath the registered qualification root and
rejecting reparse points. Require no `__pycache__`, `.pytest_cache`, basetemp,
archive, distribution, or report residue in the repository. No build, wheel,
network, broad test, performance run, or workflow execution is authorized by
this LIGHT gate.

## Review, commit, and stop gate

Submit the exact allowlisted diff, focused results, both endpoint probe records,
semantic graph ledger, module-origin ledger, immutable object/tree ledger, and
excluded-worktree/ref preservation manifest for independent review. Only after
exact-diff acceptance may this task create one non-amended direct-child commit
of `12c565899e320b2142d8b23e31f5eb19702b2486`. Require a clean isolated
worktree and unchanged primary/excluded state. Stop before merge, local-main
update, fetch, push, remote CI, tag, release, package build, or publication.
Those actions require a separate content-addressed integration plan and explicit
authority.
