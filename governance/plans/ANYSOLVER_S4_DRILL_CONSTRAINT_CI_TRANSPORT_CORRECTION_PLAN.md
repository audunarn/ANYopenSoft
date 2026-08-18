# ANYsolver S4 drill-constraint CI transport correction plan

## Authority and frozen base

The user authorized completion of the registered S4 drill-constraint certification
slice, transferred routine approvals to this task, and explicitly requested no Boss
communication. This bounded correction closes only the terminal hosted-CI blocker
from GitHub Actions run `31861117019`, attempt `1`.

- repository: `C:\Github\ANYsolver`
- branch: `main`
- base commit: `1621796c74a7878253d315f9aad920116cffb5d6`
- base tree: `32da692db6d3c9daea82d26ead3dd25851bc9729`
- failed run: `31861117019`, exact head above, `Tests`,
  `.github/workflows/ci.yml`, `push/main`, attempt `1`
- attempt-1 result: 16 success / 8 failure; every failure is a pytest lane

## Proven cause

All eight pytest jobs fail the same two nodes in
`tests/test_s4_drill_constraint_derivation.py` before any scientific comparison.
Windows checkouts convert the 13,917-byte drill cases JSON from its accepted LF
bytes (`B4D663382302E971752F0757F6E869549A54234F485235E06DBEF74085860F38`)
to CRLF (`52594E9A1C28B47BB9D9F35D1D92BAC94868CC26E636FF296A5C6CEF7DE24C90`).
Linux checkouts retain the accepted nullspace proof's Git LF bytes
(`64895E2B56B81C3D5FB4318D026F049CA0BD8EE3591FAA434E2CC81C20F84754`),
while the frozen drill oracle intentionally binds its historical Windows raw-CRLF
identity `713465F03BE6221119C1CCB7539301BE01324445DE54FC466D398185B7B481CD`.

A clean checkout also lacks `.s4_drill_constraint_shards/`, which is untracked,
explicitly disposable execution evidence. The current test would require those
files after the newline failures are corrected, contradicting final cleanup.

## Exact ownership and edits

Sole editor: this task. Exactly two repository paths may change:

1. `.gitattributes`
   - preserve its existing nullspace-cases LF rule;
   - force the six committed drill-certification text artifacts to LF: Tor plan,
     cases, oracle, stored output, derivation, and focused test;
   - force `docs/S4_NULLSPACE_SEMANTICS_PROOF.md` to CRLF so every checkout has
     the exact raw historical identity already frozen by the committed oracle and
     stored result.
2. `tests/test_s4_drill_constraint_derivation.py`
   - freeze and verify the committed stored-output SHA-256
     `8005C6D285263E33FF7F6D4B5138D5FBE4EFAB6A95834C401F94AF044ACD9E1B`;
   - freeze and verify its exact three recorded shard digests;
   - validate repeat/shard bytes additionally when the task-owned evidence
     directory exists, but do not require disposable untracked evidence in a
     clean checkout.

Pre-edit canonical LF SHA-256 values are `.gitattributes`
`7C657B6372DD6493E6B9015FA900F3A175120587C0B05913F65A17464C2E950A`
and focused test
`BD0728F03DAC8D63F442BDFFFDBED2F3953D7C1BB69B2E9F61706DD7BC83E474`.

## Frozen exclusions

No equation, operator, fixture JSON, oracle Python, stored output, derivation,
threshold, tolerance, precision, scientific classification, source package,
workflow, dependency, production API, selector, assembly/activity path, sibling
repository, proof history, or cleanup state may change. The outcome remains
`NO_GO_PRODUCTION_RESTRICTION_UNCHANGED`; no rerun of the multiprecision catalog
is authorized or needed.

## Verification and integration

Before commit:

1. verify exact two-path diff and `git diff --check`;
2. verify attributes with `git check-attr`;
3. use a fresh clean checkout probe to prove exact raw hashes and line endings for
   cases, oracle, output, proof, and test;
4. run the focused drill test in a clean checkout without shard evidence and in
   the preserved evidence worktree with pinned sibling origins;
5. run the unchanged five-file S4 focused gate;
6. obtain independent read-only review.

Then create one atomic two-path commit, fast-forward `main`, push ordinarily
without force, and require a new attempt-1 `Tests` run with exactly 24/24 success.
No rerun of failed run `31861117019`; the corrective push must create a new run.
No cleanup occurs until that run and terminal preservation checks are complete.
