# ANYsolver Stage-C Catalog Attestation Scope-Reduction Plan

Date: 2026-08-14 (Europe/Oslo)

Status: **PLAN-ONLY SUPERSESSION; INDEPENDENT ACCEPTANCE REQUIRED BEFORE ANY
IMPLEMENTATION OR EXECUTION.**

Registered path:
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_ATTESTATION_SCOPE_REDUCTION_PLAN.md`

## 1. Decision and immutable history

The user selected **simplify and replace**. The V7 design is retired as
immutable rejected evidence. It must not be patched, renamed, overwritten,
deleted, imported, tested, or executed:

- accepted V7 amendment SHA-256
  `90D911524C5158B8994810F6A906B4600D2F333CA38CDD1A764405B80A76BFFA`;
- V7 packet SHA-256
  `3F668EE66CD826BDFBE95015432F325A3E2F0CB1CDFEF9E4ADEA33815EC6280F`;
- final rejected V7 executor SHA-256
  `507D351F0FD781F3C10974816021170C7D0A33DA674B8A17FBA277E83FF7E94F`;
- final rejected V7 focused-test SHA-256
  `AA4A40228A69CCE23D145FF1CB7F29AC74073C103174B4406A66A6503A5B057B`.

The accepted contained V4 C02-C05 process behavior remains the downstream
behavioral baseline. This plan does not rewrite V4 evidence or reopen V4
qualification.

## 2. Replacement scope

The replacement has four components only:

1. a small catalog-aware C01 attestation that reports embedded-signature and
   Microsoft catalog evidence for the held `wsl.exe` identity;
2. the already accepted contained V4 C02-C05 behavior, consumed without a new
   cross-check receipt protocol;
3. one atomic receipt per check, with no receipt-to-receipt registration; and
4. one flat terminal manifest listing the exact final receipts and outcome.

The replacement explicitly excludes:

- a global receipt DAG or mutable global head;
- run-consumer state machines, proof-consumer prefixes, or terminal marks;
- registration-loss and containment-proof-loss fatal ladders;
- reduced/emergency fatal-frame encodings;
- source-spelling, substring, or mutation-based AST qualification gates;
- V7 schemas, paths, identity ledger, executor, test, and evidence root;
- any V8 or repair of the rejected V7 implementation.

## 3. C01 behavioral contract

C01 opens and holds the target executable against replacement, records its
canonical path, size, SHA-256, file identity, and handle-close outcome, then:

1. performs one embedded WinVerifyTrust attempt;
2. accepts embedded success only when the frozen Microsoft policy passes;
3. falls back to catalog lookup only for exact `TRUST_E_NOSIGNATURE`;
4. records every catalog hash/enumeration/candidate/VERIFY/CLOSE attempt in
   ordinal order, including returned-context and cleanup evidence;
5. accepts one or more valid Microsoft catalog candidates deterministically;
6. treats malformed provider data, API failure, identity drift, VERIFY/CLOSE
   failure, or cleanup failure as operational failure; and
7. treats clean exhaustive no-acceptance as typed rejection.

The C01 receipt is one canonical JSON object promoted atomically after all
handles and catalog contexts reach their recorded terminal state. It contains
the input identity, ordered raw attempts, selected attestation, cleanup truth,
outcome (`success`, `typed_rejection`, or `failure`), and primary/secondary
errors. No intermediate C01 JSON file is a final.

## 4. C02-C05 and flat evidence

C02-C05 retain the accepted V4 commands, creation-time containment, timeout,
resource, process-tree, stream, and residual-process behavior. Each check owns
exactly one atomic final receipt. A failed check may preserve owned raw stream
partials but cannot promote a success receipt.

After C01-C05 stop, the coordinator writes one flat terminal manifest containing:

- schema/version and campaign identity;
- immutable input identities;
- ordered check IDs C01-C05;
- for each check: outcome, final-receipt path/bytes/SHA-256, or truthful absence;
- process/resource/residual summaries already proven by that check;
- first error plus secondary errors;
- overall outcome and retry/cleanup permissions.

The manifest reopens and validates every listed receipt before atomic promotion.
It does not register receipts, mutate another file, or claim success unless all
five required checks succeeded. Promotion/reopen failure is an ordinary
campaign failure reported by the caller and preserved console/process evidence;
there is no second fatal publication mechanism.

## 5. Behavioral fixture gate

Before host execution, a separately accepted implementation plan must register
small deterministic behavioral fixtures that call isolated pure helpers or
mocked OS/API boundaries. They must prove:

- embedded success, exact no-signature fallback, and non-fallback rejection;
- zero, one, repeated, malformed, and operationally failing catalog candidates;
- returned-context, VERIFY/CLOSE, held-handle, and catalog-context cleanup truth;
- identity drift and duplicate/alias ordering;
- atomic receipt success, pre-promotion failure, reopen failure, and no stale final;
- C02-C05 success/failure receipt presence without consumer-state machinery;
- flat-manifest success, typed rejection, operational failure, and missing receipt.

Tests assert public behavior and canonical JSON values. Static syntax checking
may prove parseability only; it cannot substitute for behavioral assertions.
No fixture may invoke real WinTrust, WSL, network, or the immutable V4 root.

## 6. Sequencing and gates

1. Independently accept this scope reduction.
2. Register one bounded implementation plan with fresh semantically named paths,
   exact source/test allowlists, immutable V4 inputs, and absent evidence root.
3. Implement the small C01 adapter, per-check receipts, flat manifest, and
   behavioral fixtures only.
4. Run the focused behavioral gate only after separate authority.
5. Request an exclusive PERF lease before any real C01/WSL Stage-C campaign.

Any recurrence of cross-receipt ordering, custom fatal transport, or source-text
qualification is out of scope and stops implementation for explicit review.

## 7. Current no-action boundary

This plan authorizes no source, packet, test, executor, fixture, manifest,
ledger, or evidence-root creation beyond this Markdown file. It authorizes no
import, test, WinTrust/catalog API, WSL, process, network, PERF, Git, cleanup,
build, publication, Defender exception, or mutation of old artifacts.
