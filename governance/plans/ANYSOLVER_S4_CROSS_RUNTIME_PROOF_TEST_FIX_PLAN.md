# ANYsolver S4 cross-runtime proof-test fix plan

Status: executable under the user's transferred task authority.

## Frozen input and evidence

- Repository: `C:\Github\ANYsolver`.
- Base commit: `df03dc897d550b4ea2a3ffd3c8a92d5f021a3bb5`.
- Base tree: `64d0600c993b60d2a4f7251a9a2b57d9b9bcfef8`.
- Hosted run: `31834729157`, exact head above, attempt 1.
- Failed job: `pytest (ubuntu-latest, 3.11)`, job `94878357940`.
- Exact failed node: `tests/test_s4_nullspace_semantics_proof.py::test_clean_process_proof_worker`.

The worker reaches `_check_environment_manifest_and_same_environment_snapshots`
and unconditionally compares `digest` with the registered Windows/Python-3.13
manifest digest. On the unsupported Ubuntu runtime, the oracle correctly returns
`(None, None)`, as required by the accepted proof plan. The test therefore
contradicts its governing cross-runtime contract.

## Owned correction

Odin is sole editor of exactly one path:

- `tests/test_s4_nullspace_semantics_proof.py`.

Update only `_check_environment_manifest_and_same_environment_snapshots`:

1. Call `environment_manifest()` twice and require stable object/digest results.
2. When the runtime is outside the registered little-endian Windows CPython
   snapshot domain, require exactly `(None, None)` and return. Scientific proof
   checks elsewhere in the same worker continue to enforce ranks, dimensions,
   projectors, residuals, topology, constraints, and repeatability.
3. On a supported snapshot runtime, validate the manifest schema and fields,
   require a lowercase 64-hex digest, recompute the digest from canonical JSON,
   and retain same-manifest snapshot repeatability and environment separation.
4. Do not require every supported Windows runtime to equal the historical
   `8ec3966b...` digest. That identity belongs only to the recorded environment.

No oracle, cases, proof equations, thresholds, operators, production source,
release policy, workflow, dependency, or tolerance may change. No test may be
skipped or xfailed.

## Verification and delivery

Run the exact worker locally under the registered Windows environment, plus a
small clean subprocess or monkeypatched unit discriminator for the unavailable
manifest branch. Run `git diff --check`, commit the one path, fast-forward main,
and make one ordinary non-force push. Do not cancel or rerun attempt 1. Let it
reach terminal for evidence, then verify the new push's attempt-1 24-job matrix.

Cleanup remains deferred until terminal hosted verification.
