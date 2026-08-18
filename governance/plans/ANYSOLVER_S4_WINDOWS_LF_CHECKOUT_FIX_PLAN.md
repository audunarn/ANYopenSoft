# ANYsolver S4 Windows LF checkout fix plan

Status: executable under the user's transferred task authority.

## Frozen input and evidence

- Repository: `C:\Github\ANYsolver`.
- Base commit: `790c1e08da8dfdabd83d2e8a955ee873411a1b9e`.
- Base tree: `d021a102025e9a39388ba2ac0960d666d3d40987`.
- Hosted run: `31836338308`, exact head above, attempt 1.
- Failed Windows jobs inspected: `pytest (windows-latest, 3.13)` job
  `94883343877` and `pytest (windows-latest, 3.14)` job `94883343908`.
- Exact failed node in both jobs:
  `tests/test_s4_nullspace_semantics_proof.py::test_clean_process_proof_worker`.

The accepted case fixture Git blob is canonical LF text with Git blob ID
`9cabb4e46ec760beb61a0d02767ec3185bba98f9` and raw SHA-256
`223C0E1A1F03D30AA5EFBB13E8ECD8F64E5F7F0865E6F11274577D15C6691ABF`.
The repository has no `.gitattributes` rule for the path, so Git for Windows
checks it out as CRLF under the runner's line-ending policy. The proof oracle
correctly rejects that noncanonical checkout with `cases JSON must use LF
newlines only`. Ubuntu checks out LF and passes this gate.

## Owned correction

Odin is sole editor of exactly one path:

- `.gitattributes` (new).

Add exactly one path-specific rule:

`docs/reference_cases/s4_nullspace_semantics_cases.json text eol=lf`

This is a checkout transport correction only. Do not edit or renormalize the
fixture blob, oracle, proof test, cases, equations, thresholds, operators,
production source, workflow, release policy, dependencies, or tolerances. Do
not add a global line-ending rule.

## Verification and delivery

1. Require `git check-attr text eol --
   docs/reference_cases/s4_nullspace_semantics_cases.json` to report
   `text: set` and `eol: lf`.
2. Re-check out the fixture in the correction worktree and require its raw
   SHA-256 to equal the accepted `223C...91ABF`, with no CR bytes.
3. Run the focused proof wrapper; both pytest-facing tests must pass.
4. Require `git diff --check` and an exact one-path cached extent.
5. Commit only `.gitattributes`, fast-forward main, and make one ordinary
   non-force push after run `31836338308` is terminal. Do not rerun or cancel
   that run.
6. Verify the new push's attempt-1 24-job matrix reaches terminal success.

Cleanup remains deferred until terminal hosted verification.
