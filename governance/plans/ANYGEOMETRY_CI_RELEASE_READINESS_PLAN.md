# ANYgeometry CI and Release-Readiness Workflow Plan

## Objective and authority

Review the currently untracked ANYgeometry GitHub Actions workflows as a bounded release-readiness source against accepted `main` tip `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`. Correct only material defects within the two authorized workflow files, obtain independent review, and—only if accepted—commit and publish the workflows to `main` through a fast-forward-only integration.

## Repository and accepted baseline

- Repository: `C:\Github\ANYgeometry`
- Accepted local and remote `main`: `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa`
- Active checkout at plan registration: `native_hybrid_mesher` at the same tip

## Exact owned paths

- `C:\Github\ANYgeometry\.github\workflows\ci.yml`
- `C:\Github\ANYgeometry\.github\workflows\publish.yml`
- This governance plan only: `C:\Github\ANYopenSoft\governance\plans\ANYGEOMETRY_CI_RELEASE_READINESS_PLAN.md`

## Excluded and protected state

- `C:\Github\ANYgeometry\.idea\vcs.xml` must remain byte-exact.
- `C:\Github\ANYgeometry\dist_gap_closure\` must remain byte-exact.
- No source, test, package metadata, documentation, artifact, tag, release, or package registry mutation.
- No force push, rebase, reset, broad build, benchmark, package publication, or release creation.

## Review criteria

The workflows must:

1. Parse as YAML and use valid GitHub Actions structure, triggers, permissions, jobs, matrices, and expression syntax.
2. Match the actual Python/package contract in `pyproject.toml`, including supported Python versions, optional test dependencies, build backend, package version, and `py.typed` expectations.
3. Pin third-party actions to coherent maintained major versions and use least-privilege permissions.
4. Keep CI deterministic and appropriately scoped to pushes/PRs without publishing.
5. Make publishing explicitly gated by a version tag, build from the checked-out tag, verify artifacts, use trusted publishing/least privilege, and avoid silently publishing stale or mismatched versions.
6. Preserve fail-closed behavior when checks, build, or publication prerequisites are invalid.

## Procedure

1. Record exact Git refs, porcelain inventory, tracked/index diffs, and SHA-256 for protected IDE/generated paths.
2. Inspect only the two workflow files plus read-only package/config files needed to validate commands.
3. Run static YAML/action/package consistency checks only; no broad build without an explicit performance lease.
4. If material defects exist, edit only the two workflows and rerun static checks.
5. Obtain an independent read-only review of the final workflow diff and validation evidence.
6. If accepted, explicitly stage only the two workflows, commit them on a dedicated workflow branch, fast-forward local `main`, and push only the accepted workflow branch/main refs required by the chosen integration path. No tag, release, or package publication.
7. Verify remote `main`, final diff scope, and protected-state hashes.

## Definition of done

- Both workflows are coherent release-readiness source and pass static validation.
- Independent review reports no blocking defect.
- Only the two workflow files are committed in ANYgeometry.
- Protected `.idea/vcs.xml` and `dist_gap_closure/` hashes remain unchanged.
- Accepted changes are integrated and pushed by ordinary fast-forward only, or a precise blocker is reported without publication.
- No package, release, or tag is published.

