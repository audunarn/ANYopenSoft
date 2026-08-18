# ANYsolver CI Six-Failure Correction Amendment

Date: 2026-08-14 (Europe/Oslo)

Status: plan-only registration candidate. This document authorizes no worktree
creation, source edit, test, commit, integration, fetch, push, workflow action,
cleanup, cancellation, package operation, publication, or Defender action until
its exact bytes and SHA-256 are independently accepted. After acceptance, local
authority is limited to the three-path edit and LIGHT gates defined here. A
separate accepted integration addendum and PERF lease are required for any push
or new remote CI run.

## Immutable source and evidence boundary

- Repository: `C:\Github\ANYsolver`.
- Exact correction base and current accepted `main`:
  `3cdb51efcdded232054225ea0eb9cc16dc79dde9`.
- Exact base tree: `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7`.
- Base subject: `fix: widen ANYfileIO compatibility`.
- Existing accepted source branch:
  `refs/heads/codex/native-hybrid-release-blockers`, at the exact base.
- Future correction branch, create only after this plan is accepted:
  `refs/heads/codex/ci-six-failure-correction`.
- Future correction worktree, create only after this plan is accepted and only
  if the path is absent and non-reparse:
  `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-ci-six-failure-correction`.
- The correction commit must be one non-amended direct child of the exact base.
- The primary worktree, accepted source worktree, all 26 other frozen worktrees,
  every S4/performance branch, and every unrelated ref or dirty path are
  excluded and must remain byte/status exact.

The triggering workflow is run `31746877870`:
`https://github.com/audunarn/ANYsolver/actions/runs/31746877870`. The accepted
M04 evidence is an exit-124 hard timeout after 3,004 seconds. At diagnosis time
the provider reported 10 successful jobs, six failed jobs, and eight active
pytest jobs. The run was still nonterminal. This plan makes no terminal-run
claim. All timeout output, transport failures, direct-native transcripts,
qualification artifacts, and first-failure evidence remain immutable. No old
script or launcher marked DO NOT EXECUTE may be run, overwritten, restored,
cleaned, or deleted.

No push or new workflow may occur while run `31746877870` is active. Its later
terminal audit is a separate read-only authority. This correction may be edited,
LIGHT-tested, reviewed, and committed locally after plan acceptance, but must
stop before integration until the old run is terminal and a new content-
addressed integration plan is accepted.

## Exact six-job diagnosis ledger

The diagnosis queried only completed failed-job identities and immutable logs.
It did not query active-job logs, poll or cancel the run, edit source, test,
build, rerun, clean, or mutate Git state.

| Job | Job ID | URL | Exact observed failure |
| --- | ---: | --- | --- |
| ANYfileio 0.2.0 compatibility | `94603441356` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441356` | Build, endpoint installation, intended version resolution, and `pip check` succeeded; installed-origin isolation then raised `ValueError: Paths don't have the same drive` in `_is_beneath`. |
| ANYfileio 0.1.0 compatibility | `94603441358` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441358` | Same cross-drive `_is_beneath` failure after successful install and `pip check`. |
| ANYmesher 0.2.1 compatibility | `94603441380` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441380` | Same cross-drive `_is_beneath` failure after successful install and `pip check`. |
| ANYmesher 0.1.0 compatibility | `94603441479` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441479` | Same cross-drive `_is_beneath` failure after successful install and `pip check`. |
| Wheel smoke on ubuntu-latest | `94603441435` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441435` | Distribution build/check completed; isolated `python -S` import failed at `anysolver.fe_core` with `ModuleNotFoundError: No module named 'numpy'`. |
| Wheel smoke on windows-latest | `94603441454` | `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441454` | Same isolated-target missing-NumPy failure after distribution build/check. |

The four endpoint jobs ran on Windows with installed distributions on `C:` and
`GITHUB_WORKSPACE` on `D:`. `os.path.commonpath` raises `ValueError` for this
valid cross-drive non-containment case. The probes stopped before their public-
contract assertions, so endpoint behavior remains unqualified by that run.

The two wheel jobs install four local siblings plus the freshly built ANYsolver
wheel into `.wheel-smoke` using `--no-deps`, then import with `python -S`.
Consequently NumPy and other declared runtime dependencies are unavailable in
the isolated target. This is workflow composition evidence, not evidence of a
bad wheel payload or production solver import regression.

## Exact owned paths

Only these paths may change:

- `tests/test_anyfileio_version_compatibility.py`
- `tests/test_anymesher_version_compatibility.py`
- `.github/workflows/ci.yml`

All production modules, package metadata, README/changelog, Publish workflow,
other tests, reports, caches, plans, preserved dirty files, and qualification
artifacts are read-only. The final staged/committed path inventory must equal
the three lines above in ordinal order and contain no generated residue.

## Exact source corrections

### Cross-drive containment

In each owned test module, change only `_is_beneath` so it retains the existing
resolved, normalized, case-normalized `os.path.commonpath` comparison and catches
only `ValueError`, returning `False`. No other exception may be swallowed.
Same-drive containment and source-shadow rejection remain unchanged and
fail-closed.

Add exactly these portable regression node IDs:

- `tests/test_anyfileio_version_compatibility.py::test_is_beneath_treats_commonpath_value_error_as_not_beneath`
- `tests/test_anyfileio_version_compatibility.py::test_is_beneath_propagates_non_value_error`
- `tests/test_anymesher_version_compatibility.py::test_is_beneath_treats_commonpath_value_error_as_not_beneath`
- `tests/test_anymesher_version_compatibility.py::test_is_beneath_propagates_non_value_error`

Each ValueError test must monkeypatch only `os.path.commonpath` to raise
`ValueError` and require `_is_beneath(...) is False`. Each propagation test must
make the same dependency raise `RuntimeError` and require that exact exception
to escape. Do not make the tests platform-skipped, loosen origin assertions, or
special-case drive letters in production behavior.

Both files are standalone endpoint probes as well as pytest modules. Add no new
module-level import, especially no module-level `pytest` import. If a regression
uses pytest facilities, import `pytest` only inside that individual test (or use
a manual exception assertion with no new dependency). Preserve successful
module import and `--probe` execution when the dev extra and pytest are absent.

### Isolated wheel target

In the `Install wheel and pinned siblings into a clean target` step of
`.github/workflows/ci.yml`, remove only the literal `--no-deps` argument. Retain
all of the following exactly:

- `python -m pip install` as the installer;
- `--target` followed by `.wheel-smoke`;
- ordered local inputs `.ecosystem/ANYmaterial`, `.ecosystem/ANYgeometry`,
  `.ecosystem/ANYmesh`, and `.ecosystem/ANYfileIO`;
- the freshly built ANYsolver wheel from `dist/*.whl` after those four inputs;
- the subsequent import under `python -S` with `.wheel-smoke` inserted first;
- exact Windows/Ubuntu matrix, Python version, sibling commit pins, action pins,
  triggers, job inventory, and all Publish workflow behavior.

Normal pip dependency resolution must place NumPy, SciPy, threadpoolctl, and any
other declared runtime requirements into the isolated target while the explicit
local sibling candidates remain the selected first-party inputs. Do not add an
ambient site-packages fallback, remove `python -S`, add a second installation,
or weaken the import/re-export assertions.

Strengthen
`tests/test_anyfileio_version_compatibility.py::test_workflows_pin_compatibility_graph_and_actions`
to freeze the exact corrected wheel command shape: no `--no-deps` in that step,
one `--target .wheel-smoke`, the exact ordered four sibling inputs followed by
the built wheel glob, and retained `python -S`. Existing exact checkout/action,
matrix, trigger, job, Publish condition, environment, permission, and repository
URL assertions must remain and must not be relaxed.

## Exact LIGHT gate

After plan acceptance, create only the registered branch/worktree. Refuse a
pre-existing correction worktree, branch at any object other than the base, an
unclean correction worktree, or any unexpected change in the frozen state.

Use this fresh external basetemp, refusing it if it already exists or is a
reparse point:
`C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-ci-six-failure-correction-31746877870\pytest-basetemp`.

From the correction worktree, with `PYTHONDONTWRITEBYTECODE=1` and
`PYTHONNOUSERSITE=1`, run exactly once:

```text
python -m pytest -p no:cacheprovider --basetemp C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-ci-six-failure-correction-31746877870\pytest-basetemp tests/test_anyfileio_version_compatibility.py::test_is_beneath_treats_commonpath_value_error_as_not_beneath tests/test_anyfileio_version_compatibility.py::test_is_beneath_propagates_non_value_error tests/test_anymesher_version_compatibility.py::test_is_beneath_treats_commonpath_value_error_as_not_beneath tests/test_anymesher_version_compatibility.py::test_is_beneath_propagates_non_value_error tests/test_anyfileio_version_compatibility.py::test_source_declares_exact_anyfileio_compatibility_range tests/test_anymesher_version_compatibility.py::test_source_declares_exact_anymesher_compatibility_range tests/test_anyfileio_version_compatibility.py::test_workflows_pin_compatibility_graph_and_actions -q
```

These seven nodes parse both owned Python modules, test ValueError-only handling,
retain both declared compatibility ranges, and exercise the exact workflow
structural oracle without importing ambient sibling packages. No source-mode
probe may be substituted for the installed endpoint or isolated wheel evidence
that only remote CI can provide.

Then run only these static gates:

```text
git diff --check
git diff --name-only 3cdb51efcdded232054225ea0eb9cc16dc79dde9 -- .github/workflows/ci.yml tests/test_anyfileio_version_compatibility.py tests/test_anymesher_version_compatibility.py
git status --porcelain=v1 --untracked-files=all
```

Require the diff name inventory to be exactly the allowlist, the index empty
before review, and status to contain only those three unstaged files. Preserve
the fresh basetemp as task evidence until independent closeout; this plan grants
no cleanup. No broad test, build, wheel, benchmark, profiler, remote workflow,
network operation, or package action is part of the LIGHT gate.

## Worktree, ref, and evidence preservation

The 28 worktrees frozen by the accepted source/integration evidence must retain
their exact path, HEAD, branch/detached state, and porcelain status. The new
correction worktree is the only authorized 29th entry. Its branch starts at the
base and may advance only through the reviewed correction commit. The primary
worktree and accepted source worktree remain clean at the base throughout local
editing and review.

For durable ref preservation, exclude only `refs/codex/turn-diffs/*`, the
existing accepted source branch, the future correction branch, local `main`,
`origin/main`, and symbolic `origin/HEAD`. The remaining 36 ordinal-sorted
`ref<TAB>40-lowercase-hex` lines must remain byte-identical to the frozen
manifest. Their direct TAB-delimited LF-final UTF-8 SHA-256 remains
`8C449F6DE6C0893289B59C8A3692655F3B7B6803511236F1464DA600A9E373A6`;
the one-TAB-to-one-SPACE normalized manifest SHA-256 remains
`4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928`.
Volatile Codex instrumentation refs may change but may never be mutated or
deleted by this task.

Re-prove the 28 frozen worktrees, authorized 29th worktree, both stable-ref
hashes, clean primary/source worktrees, exact correction diff, and all timeout/
failure artifact identities before review and after any authorized commit. Stop
on unrelated drift. Do not clean, prune, reset, restore preserved dirty files,
remove worktrees, delete branches, or discard evidence.

## Independent review, commit, integration, and remote gate

Submit plan identity, exact three-path diff, seven-node result, static gates,
worktree/ref preservation, and immutable failure ledger for independent review.
Commit authority is withheld until an exact-diff reviewer confirms:

- `ValueError` alone maps to non-containment and `RuntimeError` propagates;
- all existing origin/version/public-contract assertions remain intact;
- only the wheel-target `--no-deps` token is removed;
- four local sibling inputs, built wheel, target isolation, `python -S`, action
  pins, triggers, matrix, and Publish behavior are exact;
- no production, metadata, publication, or evidence path changed.

After explicit commit authority, create one non-amended direct-child commit of
the base containing exactly the allowlist and stop. Do not merge, update local
main, fetch, push, or run CI under this plan.

Only after run `31746877870` is provider-terminal and separately audited may a
new content-addressed integration/main-push addendum be registered. It must use
a CAS fast-forward from exact old main `3cdb51efcdded232054225ea0eb9cc16dc79dde9`
to the reviewed correction commit, one main-only no-tags/no-prune fetch shape,
one ordinary non-force `refs/heads/main:refs/heads/main` push, authoritative
remote reconciliation, and complete worktree/ref preservation. No other ref,
tag, release, package, Publish workflow, dispatch, or publication is allowed.

Before that push, request an exclusive PERF lease for the sole push-triggered
Tests workflow. Require exactly one Tests/push/main/correction run, no Publish or
unexpected target run, and the exact 24 unique job-name oracle already frozen by
the accepted integration plan. Monitor to terminal without retry. Acceptance
requires all 24 jobs successful, including the four endpoint and two wheel jobs,
with installed origins/versions and isolated wheel imports proven on their
declared platforms. Any failure or timeout is preserved as non-accepting truth.

No cleanup occurs before independent terminal verification and Boss closeout.
Final task closure still requires the exact verdict `ECOSYSTEM CLOSEOUT: OK`.
