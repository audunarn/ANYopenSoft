# ANY Ecosystem Boss Home

This directory is the durable governance home for the ANY engineering ecosystem.
It is owned by the ecosystem Boss task and contains architecture philosophy,
task-governance rules, active state, and the long-term roadmap. It does not own
implementation code from any ANY package.

## Canonical documents

- `ECOSYSTEM_PHILOSOPHY.md` — stable architectural doctrine and qualification principles.
- `BOSS_PROTOCOL.md` — registration, reporting, performance-lease, and closeout rules.
- `ECOSYSTEM_LEDGER.md` — compact current state and material decisions.
- `ROADMAP.md` — cross-repository sequencing, debt, and future qualification work.

## Ownership and authority boundary

The user has granted the Boss standing authority to direct and approve work
throughout ANYopenSoft and the ANY ecosystem repositories, subject to the
ecosystem philosophy and registered ownership/evidence gates. Package tasks
continue to own their repositories and implementation; the Boss automation
itself edits governance material, delegates implementation, and independently
reviews evidence rather than silently fixing another task's code.

The portal files at the ANYopenSoft repository root are outside this governance
scope. Existing user changes there must remain untouched.

## Operating conventions

- Every engineering task and editing subagent registers an absolute `.md` plan path.
- Only material milestones, blockers, contract changes, plan deviations,
  performance leases, and completion reviews are reported.
- One exclusive performance-test lease covers the whole ecosystem.
- No task is approved to close until the Boss sends exactly
  `ECOSYSTEM CLOSEOUT: OK` after independent review.
- New Boss subagents use Norwegian mythology names and Norwegian spellings.

The former Codex visualization ledger remains a runtime/history mirror during
the transition. This directory is the canonical durable home from 2026-08-12.
