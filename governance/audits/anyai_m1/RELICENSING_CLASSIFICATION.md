# ANYai M1 Relicensing Classification

Date: 2026-08-14 (Europe/Oslo)

Status: **ENGINEERING FEASIBILITY FINDING COMPLETE — PARENT M1 EXIT BLOCKED PENDING SPECIALIST REVIEW AND LEGAL TARGET-MODEL DECISION**

## 1. Verdict

The parent plan's recommended target model is **CONDITIONALLY FEASIBLE as an engineering hypothesis**, not legally selected or cleared for execution.

The preferred path remains a dual-licensed open engineering core, a clean permissive protocol/safety foundation, and a proprietary ANYai workbench. M1 found no basis to label any material source range `CLEAR_FOR_DUAL` today. The model remains coherent only if the program:

1. preserves every current public grant and historical release;
2. obtains affirmative documentary authority for each source range selected for commercial licensing;
3. clears or cleanly replaces agent-associated and transferred ranges;
4. clears the exact standards-derived prescriptive calculation ranges and report language;
5. removes unrelated legacy, model, GUI, CAD, licensed-sheet, customer-like, and research content from the first artifact;
6. repairs and locks the internal dependency graph before packaging; and
7. obtains qualified specialist approval for the exact future distribution boundary.

This is an engineering audit conclusion, not legal advice, a licence change, or distribution authority.

## 2. Evidence basis

The conclusion rests on:

- 13 immutable committed `HEAD`/tree baselines in `SOURCE_BASELINE.json`;
- 57 material source/range records in `RIGHTS_AND_PROVENANCE_LEDGER.csv`;
- 111 source-declared software, model, data, standards, SDK, binary, asset, and future-closure records in `DEPENDENCY_MODEL_CONTENT_MATRIX.csv`;
- committed Git objects only, with every dirty worktree excluded; and
- no package import, dependency resolution, download, build, test, solver, customer contact, publication, licence edit, or PERF run.

The repositories currently present 11 GPL-family root licences, one MIT root licence (`ANYtimeseries`), and one repository without a root licence (`ANYintelligent`). Root licence text and package author metadata establish neither copyright ownership nor commercial relicensing authority.

No committed cross-ecosystem CLA, DCO, copyright-assignment ledger, agent-assistance policy, or complete third-party NOTICE/SBOM was found. Git authorship is therefore used only to find questions, never to prove ownership.

## 3. Target-model comparison after M1

| Model | Coherent after M1? | M1 finding |
|---|---|---|
| A. Entirely GPL desktop and workers | Conditionally | Lowest proprietary-boundary risk, but it still cannot include unlicensed standards content, unknown agent/contributor ranges, unversioned binaries, models, or absent third-party notices. It is the required fallback, not a blanket clearance. |
| B. Proprietary client plus arm's-length GPL workers | Not yet | Actual process/protocol coupling is not frozen and legal separation cannot be inferred from IPC. Current package ranges are also incompatible. |
| C. Permissive open core plus proprietary product | Not currently preferred | Requires the same complete rights consolidation while surrendering broader downstream commercial exclusivity. No current range is cleared for permissive relicensing. |
| D. Dual-licensed engineering core plus permissive protocol and proprietary workbench | Conditionally; recommended | Best fit with the product thesis, but only exact affirmatively cleared ranges may receive a commercial grant. Current public GPL grants remain intact. |
| E. GPL core with linkage/interface exception | Not yet | Requires the same copyright authority as dual licensing and specialist drafting for the exact interface. It does not solve provenance or standards-content blockers. |

Recommendation: retain Model D as the preferred engineering hypothesis and Model A as the fallback for any combined work whose commercial rights cannot be consolidated. Do not plan M2 until qualified specialist review yields an accepted legal target-model decision. Do not use process separation as an unreviewed workaround.

## 4. Repository classification

| Repository / material range | Current public position | M1 class | First-wedge position | Required disposition |
|---|---|---|---|---|
| ANYopenSoft site/governance | GPL text; project application notice incomplete | `KEEP_EXISTING` / `CONDITIONAL` | No runtime role | Preserve; later correct public licence messaging only under separate publication authority. |
| ANYgeometry core | GPL-declared; migrated historical geometry with incomplete source mapping | `NEEDS_SPECIALIST` | Excluded from model-free wedge | Reconstruct source history before any commercial grant. |
| ANYmesh core | GPL-declared; curated ANYfem/ANYsolver extraction | `NEEDS_SPECIALIST` | Excluded | Reconstruct original file/range rights. Native predicates also need affirmative provenance. |
| ANYmesh Gmsh path | Wrapper plus unresolved external native route | `EXCLUDE` | Excluded | Consider only after exact compatible or commercial Gmsh route is accepted. |
| ANYmaterial source code | GPL-declared; extracted from ANYsolver/ANYfem | `NEEDS_SPECIALIST` | Candidate only after clearance | Reconstruct original ranges and authority. |
| ANYmaterial DNV/mixed data | Standards, supplier, NCAMP, Zenodo and derived values | `NEEDS_SPECIALIST`; explicit CC-BY subset `KEEP_EXISTING` | No bundled data unless each source is cleared | Preserve CC-BY attribution; isolate or replace all unclear tables. |
| ANYfileIO | GPL-declared curated extraction; non-default audited branch | `NEEDS_SPECIALIST` | Excluded | Resolve canonical branch and source history; repair version graph later. |
| ANYfileio-occt | GPL text plus Eir/Liv-authored implementation and OCP/OCCT closure | `NEEDS_SPECIALIST` | Excluded | Establish agent authority and exact native licences before any later use. |
| ANYsolver | GPL-declared transfer from ANYintelligent/ANYstructure; GPT/Claude-associated ranges | `NEEDS_SPECIALIST` | FE excluded | Resolve source and service terms; do not use current history as proof of ownership. |
| ANYfem | GPL-declared; Audun-only Git discovery but no assignment ledger | `CONDITIONAL` | Narrow project/revision contract candidate only | Establish authority; M2 must avoid importing the full incompatible FE dependency graph into the prescriptive wedge. |
| ANYbuckling prescriptive source | GPL-declared transfer from ANYstructure with Claude trailer and multiple DNV standards/sheet citations | `NEEDS_SPECIALIST` | Central blocker | Freeze exact source snapshot, contributor/agent authority, every cited source/edition, and formula/table/sheet-factor/report-language rights. |
| ANYbuckling S3/U3/PULS paths | Manual-, CSR-, training-, workbook-, and customer-path-associated | `EXCLUDE` | Excluded | No governing result, acquisition, execution, or distribution. |
| ANYbuckling section-profile CSV | Copied table of unknown provider/terms | `NEEDS_SPECIALIST` | Avoid or clear | Prefer explicit case properties if the table is unnecessary. |
| ANYstructure | Current GPL with historical MIT-era permissions/notices whose continuing scope is specialist-pending, plus multiple contributor/agent identities | `KEEP_EXISTING` / `NEEDS_SPECIALIST` | Excluded | Keep as legacy/migration source only; preserve current GPL and all potentially applicable MIT notices/permissions pending specialist determination. |
| ANYstructure models/binary/assets | 56 pickles, unversioned IfcConvert, PDF, marks, images and examples | `EXCLUDE` / `NEEDS_SPECIALIST` | Excluded | Do not package. |
| ANYtk3D | GPL-declared transfer from ANYstructure with Claude trailer | `EXCLUDE` initially | GUI excluded | Revisit only after frozen headless contracts and a separate GUI plan. |
| ANYintelligent | No root licence; Vibe-agent and standards-derived research history | `EXCLUDE` / underlying rights `UNKNOWN` | Excluded | Use only as provenance evidence; do not copy into product. |
| ANYtimeseries original code | MIT-declared mixed repository | `KEEP_EXISTING` | Excluded | Retain permissive grant only for affirmatively original/cleared ranges. |
| ANYtimeseries bundled anyqats/Codex/assets | Upstream-like QATS copy without separate notice plus large agent-associated history | `NEEDS_SPECIALIST` / `EXCLUDE` | Excluded | Restore upstream identity/notices and resolve agent/asset terms before any future distribution. |

## 5. Decisive program blockers

### 5.1 Copyright and inbound authority

The audit found material current or transferred ranges associated with:

- two Audun email identities and the unresolved `root <q1w2e3>` alias;
- named historical ANYstructure contributors;
- `theScriptingEngineer` ranges contributed during an MIT period;
- `Eir`, `Liv`, `Vibe Nuage Agent`, and `Claude Fable 5` identities;
- GPT- and Codex-labelled branches or commit subjects; and
- curated transfers whose target histories omit original blame and grants.

No inference about account control, employment, commissioning, assignment, or AI-service terms is sufficient. Documentary evidence must map the exact person/service/date/range to authority for both GPL and commercial licensing.

### 5.2 Standards, data, models, and licensed content

The first commercial hypothesis depends on prescriptive code citing DNV-RP-C201/C202, DNV-OS-C101/DNVGL-OS-C101, DNVGL-RU-SHIP Pt.3 Ch.3 (July 2017), and unspecified DNVGL sheets. Those exact ranges are transferred, agent-associated, and standards-derived. M2 cannot claim a frozen governing envelope until a specialist approves what may be implemented and distributed from every cited source, including formulas, tables, labels, sheet-derived factors, edition references, examples, applicability text, and report wording.

The following remain excluded regardless of the main code-licensing model:

- PULS workbooks/manual paths and S3/U3 as a governing result;
- CSR/PULS training CSVs and OKEA/customer-like paths;
- DNV-RP-C208 table data unless separately cleared;
- profile tables of unknown origin;
- ANYstructure pickle models and their absent training lineage;
- unversioned IfcConvert and other unclosed native binaries;
- customer files, licensed SDK data, screenshots, logos, fonts, and test fixtures without per-asset provenance.

### 5.3 Dependency and artifact closure

The committed package graph is not distributable:

1. `ANYfileio-occt 0.1.0` requires `ANYfileio>=0.2,<0.3`, while the committed provider is `ANYfileio 0.1.0`.
2. `ANYfileIO 0.1.0` requires `ANYmesher>=0.1,<0.2`, while the committed provider is `ANYmesher 0.2.1`.
3. `ANYfem 0.1.0` requires `ANYmesher>=0.2,<0.3` and `ANYfileio>=0.1,<0.2`; that file-I/O package requires the incompatible mesher 0.1 family.
4. `ANYstructure 6.1.1` requires pre-0.2 geometry and mesher providers, while both committed providers are 0.2.1.
5. `ANYsolver 0.2.0` permits multiple provider families, but no lock selects or verifies one coherent combination.

No committed lock, constraints file, installed/wheel manifest, SPDX/CycloneDX SBOM, or complete third-party notice file exists. Exact CPython, NumPy/SciPy/BLAS, HDF5, Shapely/GEOS, OCP/OCCT, Qt, Gmsh, MKL/PARDISO, model-runtime, native-library, ABI, platform, and installer closure therefore remains unresolved.

## 6. Recommended migration path

### Stage R0 — preserve and quarantine

- Leave all licence files, tags, history, releases, public grants, and repository content unchanged.
- Keep ANYstructure, ANYintelligent, ANYtimeseries, ANYfileio-occt, ANYtk3D, CAD, FE, GUI, models, PULS/S3-U3, external examples, and licensed/customer content outside the first wedge.
- Mark every unresolved range fail-closed; no plausible ownership assumption may promote it.

### Stage R1 — documentary rights resolution

- Obtain identity/assignment evidence for human contributors and aliases.
- Record the applicable AI-service, account, commissioning, and human-review evidence per generated or assisted range.
- Reconstruct every curated transfer from its original repository/commit/file ranges.
- Obtain software-licensing and standards/content opinions tied to the exact proposed artifact.
- Preserve all potentially applicable prior MIT permissions/notices pending specialist determination, confirmed CC-BY grants/notices, and every other identified inbound term without asserting a legal survival conclusion.

### Stage R2 — exact wedge source decision

For each required capability, choose one of three explicit outcomes:

1. **commercially clear the existing range** and retain its public GPL edition;
2. **replace cleanly** from an accepted behavior/contract specification, with independent provenance and without copying uncleared implementation or expressive standards text; or
3. **exclude the capability** and narrow the product claim.

A clean replacement does not waive access terms for standards, patents, trademarks, test evidence, or licensed reference content.

The minimum source decision concerns only:

- an explicit SI material specification path without uncleared bundled tables;
- the exact narrow panel and cylinder prescriptive calculations and applicability checks;
- the named SI-to-owner adapter;
- the narrow ANYfem-compatible project/revision/artifact/report contract, without pulling the full FE package graph into the wedge; and
- a new clean protocol/safety/audit contract.

### Stage R3 — new licensing surfaces, only after later authority

- Keep cleared engineering packages publicly available under GPL and offer a separately administered commercial licence only for the cleared release/ranges.
- Create the neutral protocol/safety foundation from the accepted M2 contract under a specialist-approved permissive licence; Apache-2.0 remains only a candidate.
- Create proprietary ANYai UX/orchestration/runtime administration only under an accepted M3 implementation plan.
- Adopt a contributor agreement or equivalent inbound mechanism that affirmatively grants both public-GPL and commercial-licensing rights and records AI assistance. A DCO alone must not be assumed sufficient.

### Stage R4 — release and compatibility migration, separately authorized

- Publish new major/minor release boundaries rather than rewriting old history.
- Maintain GPL and commercial licence manifests, SBOMs, notices, source/source-offer obligations, compatibility matrices, and entitlement records separately.
- Preserve old package names, data schemas, project migration paths, public APIs, and last-GPL-release access as explicitly documented compatibility commitments.
- Repair internal version ranges and independently qualify a clean source/wheel/platform matrix before packaging.
- Require explicit user authority before external interviews/price testing, and a separate explicit gate before pilot offers, billing, build distribution, or customer-data handling.

None of Stages R1-R4 is authorized by this engineering-audit packet. Parent M1 has not closed.

## 7. Fallback decisions

If rights for the exact ANYbuckling prescriptive ranges cannot be consolidated, the program must either:

- implement a separately accepted clean replacement where lawful and independently validate it;
- remove the affected method and narrow the wedge; or
- keep the combined application GPL and monetize lawful verified distributions, onboarding, support, and services.

If the protocol/proprietary boundary is not accepted by specialist counsel, use the all-GPL fallback for the combined work. If dependency closure cannot be made coherent, do not package; retain source/headless development only under later authority.

## 8. M1 stop gate

M1 does not authorize any licence edit, source replacement, dependency change, M2 design, product source, model selection, download, test, GUI, packaging, publication, customer contact, billing, or PERF work.

The next required action is qualified specialist review and an accepted legal target-model decision, or an explicit user-approved amendment to the accepted parent plan. Only after parent M1 closeout may a separate **M2 headless ownership/protocol/safety/wedge-contract plan** be registered. Product implementation remains behind accepted M2 and a registered M3 plan.
