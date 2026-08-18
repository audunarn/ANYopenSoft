# ANYfileIO Repository Rename and Ecosystem Migration Plan

Status: **initial plan; implementation blocked pending Boss registration**  
Owner: Forseti (administrative migration owner)  
Date: 2026-08-12  
Governing directive: the user states that repository `ANYio` has been renamed to
canonical `ANYfileIO`, that the latter name is available on PyPI, and that
`ANYio` will be void.

## 1. Objective and authority

Make `ANYfileIO` the sole active repository identity for the ecosystem's neutral
file interchange project, map every consequence of retiring the former
repository identity `ANYio`, and update administrative references without
changing file-format behavior or accidentally claiming the third-party `anyio`
Python namespace.

Authority is limited to the user's 2026-08-12 rename/void directive and the
ecosystem governance contract in `C:\Github\ANYopenSoft\governance`. Repository
metadata, code, remotes, CI configuration, local checkout names, external service
settings, releases, and publications remain unchanged until this plan is
registered by the Boss and the relevant write ownership is confirmed.

The initial read-only inventory establishes these facts:

- `C:\Github\ANYio` is clean on `main` at
  `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa`, tracking `origin/main`, with
  `origin=https://github.com/audunarn/ANYio.git`.
- `C:\Github\ANYfileIO` is clean on `main` at the identical commit, tracking
  `origin/main`, with
  `origin=https://github.com/audunarn/ANYfileIO.git`.
- The source package already uses distribution name `ANYfileio` and import
  package `anyfileio`; it deliberately coexists with the unrelated third-party
  distribution/import `anyio`.
- Actionable former-repository references remain in the primary repository and
  in ANYsolver, ANYfem, ANYstructure, ANYmesh, and ANYopenSoft. Historical
  evidence also contains old paths and must not be rewritten as if rerun.

## 2. Canonical identity contract

These are distinct identifiers and must never be handled as blind
case-insensitive search-and-replace:

| Identity kind | Canonical value | Migration rule |
| --- | --- | --- |
| GitHub repository | `audunarn/ANYfileIO` | Replaces active links and checkout targets for `audunarn/ANYio`. |
| Repository display name | `ANYfileIO` | Exact casing: `ANY` + `file` + `IO`. |
| Canonical local checkout | `C:\Github\ANYfileIO` | Used by new workspace, editable-install, and `PYTHONPATH` instructions. |
| Former repository/check-out | `ANYio` / `C:\Github\ANYio` | Void/read-only compatibility reference only; no active development or release. |
| PyPI distribution metadata | `ANYfileio` (current contract) | Preserve until an explicit public-metadata decision changes display casing; package indexes normalize lookup to `anyfileio`. |
| Python import package | `anyfileio` | No change. |
| Console scripts | `anyfileio`, `anyfileio-gui` | No change. |
| Unrelated async distribution/import | `anyio` | Never rename, shadow, vendor, deprecate, or replace. Coexistence tests remain. |

The repository rename does not by itself authorize a distribution rename,
version bump, import rename, module shim, CLI rename, or file-format/API change.
Before publication, the owner and Boss must decide whether future uploaded
metadata should display `ANYfileIO` or retain current `ANYfileio`; because PyPI
name matching is normalized, that is a presentation/release-metadata decision,
not a second namespace. Existing dependency declarations using `ANYfileio`
remain valid unless that separate decision is approved.

## 3. Repositories, remotes, branches, and bases

Initial affected working state (read-only snapshot; revalidate immediately before
each edit because other tasks are active):

| Repository | Current branch / HEAD | Upstream base | Initial consequence |
| --- | --- | --- | --- |
| `C:\Github\ANYfileIO` | `main` / `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | `origin/main`; new origin | Canonical source of future rename edits. |
| `C:\Github\ANYio` | `main` / same SHA | `origin/main`; old origin | Freeze as void/read-only; do not develop both copies. |
| `C:\Github\ANYopenSoft` | `main` / `7d29eaef1c899fc56681a723184c97e2ed04abb0` | `origin/main` | Governance and portal references; worktree already has unrelated/user changes. |
| `C:\Github\ANYsolver` | `native_hybrid_mesher` / `7daa6e8c61954cfc1bc4469457fef0db154d3375` | `origin/main` | VCS checkout URL, local install docs, environment evidence paths. |
| `C:\Github\ANYfem` | `native_hybrid_mesher` / `b17f1d47ba79e5c04692301e96d23dd5ac5627cb` | `origin/main` | CI checkout/path, GUI sibling path, docs, migration-path test. |
| `C:\Github\ANYstructure` | `clean-up-after-external` / `4a79b860739c2f0b24f61314d4c13d943886bdd3` | `origin/master` | CI/readthedocs checkout/path, GUI sibling path, docs and contract tests. |
| `C:\Github\ANYmesh` | `native_hybrid_mesher` / `97058e0a1213ba7f0da506ff1a00d4ef10093d20` | `origin/main` | Canonical link plus historical command/evidence paths; active resolver-conflict handoff. |

Other initially scanned ecosystem repositories had no actionable former-repo
reference, or only a semantic mention of the unrelated `anyio`; they remain in
the validation scan but outside the initial edit set. `ANYfileio-occt` is a
distinct repository and is not renamed by this plan.

No force-push, history rewrite, default-branch change, tag move, release move, or
mass remote rewrite is authorized. Each consumer change must land on a branch and
base agreed with that repository's active owner. GitHub-side repository rename,
redirect health, default branch, branch protection, releases/tags, issues/PRs,
Actions permissions, Pages, deploy keys, webhooks, and environments require an
administrative verification checklist rather than assumptions based on redirects.

## 4. Owned and excluded paths

### Owned before registration

- Only this plan:
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_REPOSITORY_RENAME_PLAN.md`.

### Proposed owned paths after registration and repository-owner coordination

- Canonical repository administrative surfaces under
  `C:\Github\ANYfileIO`: `pyproject.toml`, `README.md`, packaging identity tests,
  `.github/workflows/**`, repository-local docs that state the former repository
  name/path, and any badge/link configuration found by the complete inventory.
- Consumer administrative surfaces that contain an active former URL or checkout
  path: relevant workflow files, Read the Docs configuration, install/development
  docs, sibling-source launchers, and path-contract tests in ANYsolver, ANYfem,
  ANYstructure, ANYmesh, and ANYopenSoft.
- A small migration guard/allowlist may be added in the canonical repository or
  governance tooling if approved, to reject newly introduced active
  `audunarn/ANYio` and `C:\Github\ANYio` references while permitting clearly
  labelled history and the unrelated lowercase `anyio` package.

Every file is re-read and its working-tree diff checked before patching. Existing
user changes, especially the dirty ANYopenSoft portal files, are preserved; if a
relevant hunk overlaps, the task stops and requests coordination.

### Excluded without separate authority

- Runtime/file-format implementation under `src/**`; neutral models, parsers,
  serializers, solver or mesher behavior; public Python APIs.
- Renaming `src/anyfileio`, creating `src/anyio`, or publishing an `ANYio` shim.
- Source history rewrites, tags, releases, artifacts, generated distributions,
  wheels, caches, build outputs, virtual environments, and IDE state.
- Historical performance/qualification reports and JSON snapshots. Old absolute
  paths remain truthful historical provenance and may only receive an adjacent
  explanatory note, never silent textual rewriting.
- The distinct `ANYfileio-occt` repository and all unrelated uses of the async
  `anyio` package.
- Deleting or renaming either checkout; pushing; publishing to TestPyPI/PyPI;
  changing external service settings, secrets, trusted publishers, DNS, or
  redirects without explicit authority.

## 5. Consequence map

### Repository and developer workspaces

- Update canonical clone URLs, local editable-install paths, sibling-source
  discovery (`run_gui.py` and equivalent), `PYTHONPATH` examples, task scripts,
  IDE/workspace references, and contributor instructions to `ANYfileIO`.
- Ensure the canonical checkout is the only writable/development copy. Mark the
  old checkout void/read-only until closeout; do not rely indefinitely on two
  directories containing the same commit.
- Audit all local remotes, submodules, worktrees, repository dispatch inputs,
  reusable workflows, and automation configuration. Redirect success is only a
  compatibility aid, not the canonical result.

### Packaging, dependencies, versions, and locks

- Preserve `project.name = "ANYfileio"`, import `anyfileio`, entry points, and
  dependency specifiers during the repository-only phase.
- Update `project.urls` and equivalent source/homepage/issues/changelog metadata
  to `https://github.com/audunarn/ANYfileIO`.
- Inventory `pyproject.toml`, `setup.py/setup.cfg`, requirements files,
  constraints, lock files, editable/VCS dependencies, package metadata tests,
  SBOM/provenance inputs, and cache keys across all consumers.
- Do not bump a package version merely for a repository redirect. If shipped
  metadata must expose corrected URLs, record that in the next normal release's
  changelog; require a version decision only if a release is actually cut.
- Verify both source/editable and index resolution. Do not change dependency
  bounds to make a resolver pass unless the owning package approves a public
  dependency contract change.

### CI, documentation, badges, and URLs

- Change active `actions/checkout` repositories and checkout directory names
  from `ANYio` to `ANYfileIO`, then change every matching install path in the
  same job atomically.
- Update VCS install URLs, Read the Docs configuration, documentation links,
  portal cards/tabs/copy commands, workflow/release/status badges, issue links,
  source links, coverage/code-quality dashboards, and generated-doc source URLs.
- Audit case-sensitive Linux paths as well as case-insensitive Windows paths.
  Validate YAML, TOML, RST, Markdown, HTML, and JavaScript consumers after edits.
- Preserve lowercase `anyio` coexistence workflow/job names and assertions where
  they refer to the external async library.

### Release and external administration

- Confirm GitHub rename/redirect behavior, canonical clone URL, default branch,
  branch protection/rulesets, Actions access, environments, release/tag
  continuity, Pages, webhooks, deploy keys, issue/PR links, and repository topics.
- Confirm TestPyPI/PyPI project ownership and name normalization. Review OIDC
  trusted-publisher bindings because they may name a GitHub owner/repository,
  workflow filename, and environment. A successful old URL redirect does not
  prove trusted publishing is configured for the new repository identity.
- Confirm Read the Docs, coverage, code scanning, dependency bots, and any other
  installed integrations point to the canonical repository.
- No publish step occurs in this administrative migration unless separately
  authorized after clean-build evidence and dependency availability gates.

## 6. Compatibility and deprecation strategy for void `ANYio`

1. `ANYfileIO` becomes the only active repository name immediately after the
   migration cutover; new documentation and automation must use it.
2. `ANYio` is not a deprecated Python package alias. No top-level `anyio` module
   or distribution is created because that name belongs to the established async
   ecosystem package and shadowing it is an architectural defect.
3. GitHub's old-repository redirect may be retained as a passive compatibility
   bridge. It is tested but not used by canonical CI or documentation.
4. `C:\Github\ANYio` remains untouched and read-only during migration. After all
   active consumers use `C:\Github\ANYfileIO`, its disposition (archive marker,
   move, or deletion) requires a separate explicit, recoverable action. This plan
   does not delete it.
5. Add a narrow regression check that distinguishes forbidden old repository
   URLs/paths from allowed historical records and valid lowercase `anyio`
   coexistence tests.
6. Record the repository rename in the canonical changelog/migration notes
   without implying a runtime API, format, or performance change.

## 7. Milestones and definition of done

### M0 — Register and freeze

- Boss registers this plan and its SHA-256.
- Confirm canonical spelling and identity table; confirm per-repository write
  ownership and branch/base with active task owners.
- Keep both source checkouts unchanged until registration.

### M1 — Complete consequence inventory

- Classify every hit as active repository identity, distribution name, import
  name, third-party `anyio`, or immutable historical evidence.
- Produce the exact edit/allowlist manifest and external-administration checklist.
- Revalidate clean/diff state and commit identities before edits.

### M2 — Canonical repository metadata

- Work only from `C:\Github\ANYfileIO`.
- Correct repository URLs, local-path documentation, packaging assertions, badges,
  and repository-facing CI/docs; preserve runtime names and behavior.
- Document that `C:\Github\ANYio` is void without modifying/deleting it.

### M3 — Consumer migration

- Coordinate and patch active checkout URLs/paths and docs in ANYsolver, ANYfem,
  ANYstructure, ANYmesh, and ANYopenSoft on owner-approved branches.
- Preserve historical evidence and unrelated dirty changes.
- Complete active-task handoffs and merge-order notes.

### M4 — External service and release readiness

- Owner verifies GitHub and connected-service settings, including trusted
  publishers, using the external checklist.
- Resolve or explicitly defer the ANYmesher package-version/index conflict; do
  not conceal it with relaxed constraints or skipped dependency resolution.
- Decide PyPI display capitalization before any next release.

### M5 — Validation and closeout

Definition of done:

- `audunarn/ANYfileIO` and `C:\Github\ANYfileIO` are the sole active repository
  URL/path in source metadata, current workflows, workspace instructions, and
  current documentation.
- Former `ANYio` references are absent from active surfaces or explicitly
  allowlisted as historical/redirect/third-party evidence.
- Distribution `ANYfileio`, import `anyfileio`, and the unrelated `anyio` coexist
  without namespace collision.
- Focused packaging, metadata, consumer wiring, Linux/Windows path, and clean-wheel
  checks pass with no skips that erase required evidence.
- Resolver status is reported truthfully; publication remains blocked if sibling
  distributions cannot resolve on the target index.
- All external checklist items have evidence or named owner/deferment.
- Repositories, branches, final SHAs, changed paths, commands/results, limits, and
  rollback state are reported to the Boss, which issues the only closeout verdict.

## 8. Validation plan

Light/focused checks (run after edits, preserving the first failure):

- `git diff --check` and per-repository `git status --short --branch`.
- Targeted `rg` inventory for `audunarn/ANYio`, `C:\Github\ANYio`, `.ecosystem/ANYio`,
  and semantic/case variants, with a reviewed allowlist for history and async
  `anyio`.
- Parse the canonical `pyproject.toml` and assert repository URLs, distribution
  name, package discovery, entry points, and version remain internally coherent.
- Canonical-repository focused packaging/coexistence tests, including
  `tests/test_packaging.py`, `tests/test_layering.py`, and the existing async
  `anyio` coexistence contract.
- Focused consumer path/wiring tests in ANYfem and ANYstructure plus import smoke
  from the canonical checkout.
- Validate current workflow checkout paths and VCS URLs as matched pairs; validate
  docs/portal links and commands without rewriting historical reports.

Network/external checks require appropriate approval and credentials: canonical
GitHub redirect/clone resolution, linked documentation/status services, and
TestPyPI/PyPI trusted-publisher configuration. A URL redirect check is not publish
authority.

### Anticipated heavy runs requiring a Boss performance lease

No benchmark, scaling, profiler, or performance claim belongs to this task. If
needed for final qualification, request the exclusive lease before each exact
registered command for:

- the canonical repository's full multi-version/full-platform test matrix;
- clean sdist/wheel build, isolated wheel install, and `twine check`;
- full affected-consumer suites across ANYsolver, ANYfem, and ANYstructure;
- a clean-environment dependency-resolver matrix against TestPyPI/PyPI and VCS
  siblings.

Lease requests must state exact commands, resource envelope, ETA, and preserve the
first failure without retry/tuning. The rename task will not overlap the active
ANYmesher MSVC lease.

## 9. Dependencies, risks, and rollback

Dependencies:

- Boss plan registration and per-repository ownership/branch coordination.
- GitHub repository administrator access and external-integration access.
- A decision on future PyPI metadata display casing.
- Compatible released/index-visible ANYmaterial and ANYmesher distributions for
  isolated resolver and publish gates.

Principal risks and mitigations:

- **Split-brain edits:** two clean checkouts currently share a commit but point at
  different remotes. Mitigation: edit only the canonical checkout after
  registration; freeze the old checkout and record SHA/remotes at every gate.
- **Namespace collision:** blind replacement could turn valid async `anyio` uses
  into project imports or create a shadow package. Mitigation: identity-aware
  classification and coexistence tests; never create an `anyio` shim.
- **Case/normalization confusion:** GitHub/path casing and PyPI normalization have
  different rules. Mitigation: use the identity table and validate on Windows and
  Linux.
- **Broken CI pairs:** changing checkout repository but not checkout/install path
  breaks jobs. Mitigation: patch and test each pair atomically.
- **External publishing failure:** trusted-publisher bindings may still name the
  former repository. Mitigation: explicit admin verification before publication.
- **Evidence corruption:** replacing paths in historical reports would falsify
  provenance. Mitigation: exclude reports or append clearly dated annotations.
- **Active-branch conflicts:** ANYmesh/ANYsolver/ANYfem/ANYstructure contain
  ongoing task work. Mitigation: owner handoffs, disjoint hunks, agreed merge
  order, and no opportunistic rebases.

Rollback is commit-scoped and non-destructive: revert the administrative commits
in reverse dependency order, restore prior URLs/checkout paths as a matched set,
and retain both local checkouts and GitHub redirect until verification completes.
Do not reset hard, delete a checkout, move tags, or publish a duplicate
distribution. If an external setting fails, keep releases blocked, restore its
previous binding where safe, and record the failed state. Reverting the GitHub
repository name itself is an owner-admin decision and is not automatic rollback,
because the user explicitly declared `ANYio` void.

## 10. Cross-task handoffs

- **ANYmesher native-hybrid owner:** current `ANYfileio` metadata requires
  `ANYmesher>=0.1,<0.2`, while the ecosystem ledger records an unresolved resolver
  metadata conflict. The rename must not relax that bound, fake index
  availability, use a stale wheel, or report source-path tests as installed-wheel
  resolution. ANYmesher owns its version/release contract; this task owns only
  replacing former repository URLs/paths after the owner identifies the compatible
  release or accepted VCS-source gate. Its compiled-build blocker and performance
  evidence remain separate from this administrative rename.
- **ANYsolver and ANYfem native-hybrid owners:** coordinate edits on their active
  `native_hybrid_mesher` branches and ensure path-only changes neither consume nor
  overwrite native-hybrid handoffs.
- **ANYstructure owner:** its default base is `origin/master` and active branch is
  `clean-up-after-external`; coordinate CI, Read the Docs, launcher, docs, and
  contract-test edits as one path migration.
- **ANYopenSoft/Boss:** governance may register evidence, while dirty portal files
  remain user-owned. Portal changes require overlap review and a separate
  owner-approved hunk set.
- **Release administrator:** verify GitHub redirects/settings, PyPI/TestPyPI
  ownership and trusted publishers, environments, and connected services; no task
  agent infers success from source edits.

Any proposed runtime API, distribution dependency/version, publication, or scope
change is a public-contract change or plan improvement and must be reported to the
Boss before implementation.
