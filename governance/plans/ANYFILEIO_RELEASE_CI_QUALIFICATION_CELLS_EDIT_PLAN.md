# ANYfileIO release CI qualification cells edit plan

Date: 2026-08-13 (Europe/Oslo)

Status: registration candidate; no worktree, branch, edit, test, build, merge,
push, or publication authority exists until this exact file identity is
accepted. This plan is disjoint from every OCP V3 task/evidence path.

## 1. Identity, owner, and objective

Owner: one writer `/root/runa_anyfileio_release_ci_cells`, no nested writer.

Exact base and sole implementation parent:
`5513881827cdee9fd337497a2730a5912d8ea751`, tree
`68d703646c5d9b556c1ecdbdb96f677a4ba9a381`. Local `main` and
`origin/main` are exact and synchronized. The primary checkout is not an edit
target; create a clean isolated worktree from this exact `main` only after
registration:

```text
branch:   codex/anyfileio-release-ci-cells
worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-release-ci-cells
upstream: none
commit:   one direct child, subject `ci: split base and semantics qualification`
```

Objective: make source CI truthfully distinguish a NumPy-only base cell from a
`[semantics]` cell, retain base coverage for neutral readers, and correct stale
dependency-ledger status/provenance. This source slice makes no installed-wheel,
resolver, release, or publication claim.

The semantics source cell has exactly three immutable external inputs; mutable
branches, tags, index resolution, abbreviated revisions, and substitutions are
forbidden:

| Install order | Repository URL | Commit | Distribution/version | Import |
| ---: | --- | --- | --- | --- |
| 1 | `https://github.com/audunarn/ANYgeometry.git` | `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa` | `ANYgeometry==0.2.1` | `anygeometry` |
| 2 | `https://github.com/audunarn/ANYmesh.git` | `e676783256833f0c17e8ff6536f0f73365998928` | `ANYmesher==0.2.1` | `anymesher` |
| 3 | `https://github.com/audunarn/ANYmaterial.git` | `4626887667f4c251479d26f321b9e73b046a2783` | `ANYmaterial==0.1.0` | `anymaterial` |

## 2. Exact seven-path ownership

Only these existing paths and bounded hunks are owned:

1. `.github/workflows/ci.yml`, starting blob
   `d1df2713126246e4d5570881e497d3b352f02297`:
   - remove workflow-global `SIBLINGS` and its stale requirement comment;
   - replace `pytest` with a `base-only` 3.11-3.14 / Windows+Ubuntu matrix;
     install only `.[dev]`, assert `ANYgeometry`, `ANYmesher`, and `ANYmaterial`
     distributions and import specs are all absent, import `anyfileio`, then
     run the full suite;
   - add a distinct `semantics` matrix and run these exact commands sequentially
     in geometry -> mesh -> material order before the project install:

     ```text
     python -m pip install --no-deps "git+https://github.com/audunarn/ANYgeometry.git@37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa"
     python -m pip install --no-deps "git+https://github.com/audunarn/ANYmesh.git@e676783256833f0c17e8ff6536f0f73365998928"
     python -m pip install --no-deps "git+https://github.com/audunarn/ANYmaterial.git@4626887667f4c251479d26f321b9e73b046a2783"
     python -m pip install -e ".[dev,semantics]"
     ```

     No owner install may omit `--no-deps`, combine into an unordered/mutable
     input, use an index, or name a branch/tag. After installation, a stdlib
     Python assertion must prove exact declared versions from the table; each
     imported module's resolved `__file__` is outside resolved
     `GITHUB_WORKSPACE` and inside the active environment's install root; and
     each distribution's parsed PEP 610 `direct_url.json` is exactly the
     canonical HTTPS repository URL plus a sole `vcs_info` object with
     `vcs == "git"` and `requested_revision == commit_id ==` its full table
     commit—no `dir_info`, `archive_info`, `subdirectory`, or extra top-level or
     VCS key. Then import `anyfileio` and run the full suite;
   - remove sibling installation from `coexists-with-anyio`; it installs only
     `.[dev]` plus `anyio` and runs the same suite;
   - remove sibling installation from `wheel`; its existing base-wheel build and
     isolated import commands otherwise stay byte-identical;
   - do not alter triggers, runner/Python matrices, action versions, or add
     caching, artifact upload, release, publish, or provider jobs.

2. `DEPENDENCY_MATRIX.md`, starting blob
   `ed53d6d8fc5d315c3c5e31139032fea4353c8e60`:
   - update only the ANYfileIO observed row to accepted source tip
     `5513881827cdee9fd337497a2730a5912d8ea751`;
   - replace the stale future metadata/runtime-owner prose with the accepted
     NumPy-only base, exact `semantics` extra, lazy SEM001/SEM002/SEM003 runtime,
     and source-CI split;
   - mark source base/semantics CI definitions as implemented, while keeping
     base installed-wheel qualification `UNRUN` and semantics installed-wheel
     qualification `BLOCKED` only on accepted hash-pinned
     ANYgeometry/ANYmesher/ANYmaterial artifacts, then `UNRUN`; record the exact
     three source-cell commits from section 1 without treating them as wheel or
     resolver evidence;
   - remove only the stale future lazy-integration dependency edge; retain the
     owner-artifacts-to-installed-wheel qualification edge and every provider,
     consumer, V7, platform, performance, publication, and nonclaim boundary.

3. `tests/test_packaging.py`, starting blob
   `7a31de16a9b270c693fe865626ca86657437c779`:
   - add stdlib-only text/regex helpers for `.github/workflows/ci.yml` and the
     dependency matrix; no YAML dependency;
   - add focused predicates proving base-only has no sibling/semantics install,
     semantics alone owns sibling plus `.[dev,semantics]` installation,
     coexists/wheel contain no sibling install, both test jobs run pytest, and
     base explicitly asserts all three optional distributions/imports absent;
   - freeze the exact three full-SHA git URLs, their geometry -> mesh -> material
     order, individual `--no-deps` commands, exact versions, outside-workspace
     origins, and PEP 610 URL/VCS/requested-revision/commit-id checks; reject
     mutable URLs, missing pins, order drift, or owner index resolution;
   - prove the matrix records accepted source state and retains truthful
     installed-wheel `UNRUN`/owner-artifact `BLOCKED` boundaries;
   - prove the four semantic-consumer test modules below have no top-level
     anymesher/anymaterial imports and contain their exact local
     `pytest.importorskip` gates.

4. `tests/test_calculix.py`, starting blob
   `3138a7ff13968a9c544cbd2d57bc4218aad69763`:
   - remove only top-level `anymesher`/`anymaterial` imports;
   - add one small local helper using `pytest.importorskip` for those two
     packages and returning `Mesh`, `simple_panel_mesh`, `MaterialSpec`,
     `IsotropicMaterial`, and `OrthotropicMaterial`;
   - call the helper only from tests that construct semantic meshes/materials
     or invoke the semantic deck writer; keep FRD, DAT, deck-reader, merge,
     summary, and geometry-classification tests active in the base cell;
   - preserve test data, assertions, production imports, and node names.

5. `tests/test_sesam.py`, starting blob
   `8d8099507a8787b2e587722f96c4510db4fd5f67`:
   - add exact local `pytest.importorskip("anymesher")` and
     `pytest.importorskip("anymaterial")` gates only to
     `test_semantics_resolves_a_neutral_mesh_and_records`,
     `test_semantics_resolves_explicit_shell_local_axes`, and
     `test_semantics_maps_gunivec_to_beam_orientation`;
   - preserve every other node, fixture, assertion, and source string.

6. `tests/test_formats_and_cli.py`, starting blob
   `d883a03c33efe143c75169160700318b27ece451`:
   - add the same two local `pytest.importorskip` gates only at the start of
     `test_summary_resolves_the_document_into_neutral_records`, whose asserted
     CLI summary intentionally exercises the real semantic resolver;
   - preserve every other CLI/format node and assertion, including missing-extra
     and neutral record behavior.

7. `tests/test_gui.py`, starting blob
   `20f66193cf44f2faed0ae884dd4d9182f002d7f0`:
   - add the same two local `pytest.importorskip` gates only at the start of
     `test_loading_a_fem_file_fills_every_panel`, whose mesh assertion
     intentionally requires real semantic enrichment;
   - preserve all neutral GUI loading/record/diagnostic coverage and every
     other node/assertion.

No whole-file formatting rewrite, glob ownership, or transferred hunk exists.

## 3. Protected state and exclusions

At handoff reproduce exactly:

- complete `src/anyfileio` tree
  `6be5f48f5df9ca1ce8bc84c06d35a022f5a2b70a`;
- complete `docs` tree
  `0c536d17b568fb2cbb2028664cec682a38600aee`;
- `pyproject.toml` `39ea8fd4e6e7554d87d42ad4382489cc68eec833`;
- `.github/workflows/publish.yml`
  `51fdef44630971bcc4b3b23eee8c318f98e90252`;
- `README.md` `c8873f0c4244a7f1603ec46915c1d3cdf37e3730`;
- `CHANGELOG.md` `f18ef6a7aeefee8f981eda4b7ce41a27bc90892c`;
- `LICENSE` `f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`;
- `MANIFEST.in` `57ae840ce4286a9c932992391ce7312a09a88d28`.

All other tests and workflows are excluded and byte-exact. No metadata,
runtime, CAD/core/artifact/provider, packaging range, README/changelog,
publication, consumer, or other repository edit is allowed.

The following namespaces are explicitly excluded from reads and writes by the
implementation agent: every
`codex-anyfileio-ocp-79311-inventory-v3` task path, V3 final/pending/sentry,
V2 task/final/receipt, and all OCP wheels/probes. This plan creates no overlap
or ordering dependency with V3.

No workflow dispatch, wheel/build, install, resolver, network, OCP/native call,
broad/full suite, performance lease, benchmark, release/tag, package upload,
push, or publication is authorized.

## 4. Focused verification and definition of done

After source review, request classification and run once only if released:

```text
python -m pytest -q tests/test_packaging.py tests/test_layering.py
```

Always perform `git diff --check`, AST-parse the five owned Python tests, and
verify exact path inventory/protected blobs. Do not run the workflow or full
suite locally; GitHub execution evidence is future post-integration CI evidence.

Definition of done:

- diff paths are exactly the seven paths above;
- base CI has no ANYgeometry/ANYmesher/ANYmaterial or semantics extra and
  retains all base-safe tests;
- semantics CI alone supplies the three exact immutable owners in frozen order,
  verifies versions/origins/PEP 610 commits, and runs the same suite;
- optional test imports are local and skip only real-owner semantic nodes;
- matrix source status is current while wheel/resolver nonclaims remain true;
- one direct-child commit, clean worktree, no upstream, independent completion
  review, and `ECOSYSTEM CLOSEOUT: OK` before any merge/push under standing
  authority.

Report plan identity, commit/tree/parent, exact seven-path diff, first focused
outcome if authorized, protected proofs, and clean/no-upstream state. Any need
to change scope, metadata, node names, V3 state, or qualification claims stops
and requires a revised plan.
