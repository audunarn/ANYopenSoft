# ANYai M1 Rights and Dependency Feasibility Plan

Date: 2026-08-14 (Europe/Oslo)

Status: **ENGINEERING AUDIT COMPLETE — PARENT M1 EXIT BLOCKED PENDING SPECIALIST REVIEW AND LEGAL TARGET-MODEL DECISION; no M2 or implementation authority**

Registered path:
`C:\Github\ANYopenSoft\governance\plans\ANYAI_M1_RIGHTS_AND_DEPENDENCY_FEASIBILITY_PLAN.md`

## 1. Authority and objective

This M1 plan is subordinate to the independently accepted program plan:

- path: `C:\Github\ANYopenSoft\governance\plans\ANYAI_COMMERCIAL_FEASIBILITY_AND_BUCKLING_WEDGE_PLAN.md`
- accepted SHA-256: `0307B0030897A20E1F888C2E3EB3063946AA25A2BD64E1717D23D522B3677163`

M1 may only establish whether the narrow ANYai buckling program has a legally and technically coherent path to a later implementation plan. It will:

1. freeze committed source identities for every audited repository;
2. build a file/range-level copyright and inbound-rights ledger;
3. inventory declared dependencies, candidate SBOM rows, models, datasets, standards-derived material, fonts, SDKs, and other content;
4. classify relicensing feasibility without changing any licence;
5. record unresolved specialist-review questions;
6. define evidence, risks, and later verification gates; and
7. submit the M1 packet for independent ecosystem review.

M1 does not authorize M2 or product implementation. The committed-object engineering audit is complete, but the accepted parent plan's M1 exit gate is not: the 48 specialist questions have not been answered and no specialist-approved legal target-model decision exists. This packet neither waives nor splits that gate.

## 2. Planning repository and exact ownership

| Field | Registered value |
|---|---|
| Planning repository | `C:\Github\ANYopenSoft` |
| Current branch | `main` |
| Observed HEAD | `7d29eaef1c899fc56681a723184c97e2ed04abb0` |
| Observed tree | `52b7444f12e503b72505a55a80e17aab97e636d9` |
| Worktree | Pre-existing dirty primary checkout; all unrelated state is protected |
| Branch/worktree action | None authorized |
| Commit/push/PR | None authorized |

This task owns only these exact paths:

1. `C:\Github\ANYopenSoft\governance\plans\ANYAI_M1_RIGHTS_AND_DEPENDENCY_FEASIBILITY_PLAN.md`
2. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\SOURCE_BASELINE.json`
3. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\RIGHTS_AND_PROVENANCE_LEDGER.csv`
4. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\DEPENDENCY_MODEL_CONTENT_MATRIX.csv`
5. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\RELICENSING_CLASSIFICATION.md`
6. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\SPECIALIST_REVIEW_QUESTIONS.md`
7. `C:\Github\ANYopenSoft\governance\audits\anyai_m1\M1_EVIDENCE_REPORT.md`

No subagent may edit any file. The root task alone may write the seven registered artifacts. Every other path and all pre-existing changes are excluded.

## 3. Audit scope and immutable-base method

Repositories in scope:

```text
ANYopenSoft
ANYgeometry
ANYmesh
ANYmaterial
ANYfileIO
ANYfileio-occt
ANYsolver
ANYfem
ANYbuckling
ANYstructure
ANYtk3D
ANYintelligent
ANYtimeseries
```

For each repository, M1 records repository path, branch label, full commit, tree, parent, dirty status summary, remote identity where available, root licence identity, packaging manifests, and relevant migration/provenance documents.

Auditable source is the committed `HEAD` tree, read through Git object commands where a checkout is dirty. Uncommitted user work is not copied, blamed, classified, or used to support a relicensing decision. A dirty checkout may therefore have a clean committed audit base, but it is never called a clean worktree or selected as a future implementation base.

M1 uses read-only history, tree, manifest, text-search, hash, and official-source inspection. It does not import packages, run solvers/tests, install dependencies, resolve environments, build wheels, or execute repository code.

## 4. Required audit records

### 4.1 Source baseline

`SOURCE_BASELINE.json` records exact identities and whether every conclusion uses committed source, worktree state, or an external official source. It must fail closed on an unreadable repository or ambiguous identity.

### 4.2 Rights and provenance ledger

`RIGHTS_AND_PROVENANCE_LEDGER.csv` uses this minimum schema:

```text
repository,path_or_range,content_or_tree_identity,origin_repository,
origin_commit_or_source,author_or_contributor,copyright_claimant,
inbound_licence_or_agreement,generated_or_agent_status,
standards_data_or_model_status,required_notices_or_source_offer,
relicensing_authority,evidence_reference,classification,review_status,notes
```

Material source ranges are split where authorship, transfer origin, licence, generated status, or content rights differ. Repository-level rows are not allowed to conceal a known mixed range. Git shortlog/blame is discovery evidence only and never proves legal ownership.

### 4.3 Dependency, SBOM, model, and content matrix

`DEPENDENCY_MODEL_CONTENT_MATRIX.csv` uses this minimum schema:

```text
owner_repository,item_type,name,declared_version_or_range,source_manifest,
direct_optional_build_test_or_transitive,local_or_external,licence_expression,
copyright_or_provider,redistribution_or_source_terms,notice_requirements,
model_data_standard_sdk_or_trademark_terms,platform_or_extra,
included_in_wedge,verification_level,evidence_reference,classification,notes
```

The M1 matrix is a **source-declared candidate SBOM**, not a complete installed/wheel SBOM. Transitive, native-binary, exact-wheel, model-file, and installer closure remain visibly `UNRESOLVED` unless evidenced without installation or download.

### 4.4 Relicensing classifications

Every material row receives one of:

- `CLEAR_FOR_DUAL` — affirmative evidence supports public GPL plus commercial licensing, still subject to counsel;
- `CONDITIONAL` — plausible route exists but named rights/notices/dependencies remain unresolved;
- `KEEP_EXISTING` — retain the current inbound licence and obligations;
- `REPLACE_CLEANLY` — do not copy; later implement from an accepted clean contract if lawful;
- `EXCLUDE` — outside the commercial wedge;
- `NEEDS_SPECIALIST` — no engineering conclusion is adequate; and
- `UNKNOWN` — evidence is insufficient and no distribution decision is permitted.

No item is `CLEAR_FOR_DUAL` merely because the dominant Git author is the ecosystem owner.

## 5. Target decision tested by M1

M1 tests, but does not enact, the accepted target:

```text
cleared engineering packages:
  public GPL + separately granted commercial licence

new clean protocol/safety contracts:
  candidate permissive licence after specialist review

ANYai UX/orchestration/runtime administration:
  candidate proprietary repository after M2 and M3 authority

uncleared legacy/research/third-party content:
  keep existing, replace cleanly, or exclude
```

M1 must state whether this structure is `FEASIBLE`, `CONDITIONALLY FEASIBLE`, or `NOT CURRENTLY FEASIBLE`, with the exact blocking rows. It must also retain the accepted GPL/open-product fallback.

## 6. Specialist-review questions

The audit must formulate bounded questions for qualified software-licensing, copyright, standards/content, trademark, security/product, tax/commercial, and product-liability specialists. At minimum:

- Who owns each transferred or agent-generated source range, and what evidence establishes authority?
- Which contributor aliases represent the same person, employment, or commissioned work?
- Which prior permissive grants and notices survive later GPL changes?
- May each cleared owner package be offered under GPL and a commercial licence?
- What contributor agreement and AI-assistance disclosure are required for future dual licensing?
- Which source-offer, installation-information, notice, patent, and relinking duties apply to each distribution model?
- Does a proposed process boundary create separate works or one combined work under the exact protocol semantics?
- Which standards-derived formulas, tables, examples, terminology, models, and reports may be implemented or distributed?
- What model/runtime, Qt, OCCT/OCP, Gmsh, MKL, xlwings, font, and SDK terms apply to the exact future artifact?
- What trademark wording is permitted for ANY/ANYai and referential use of third-party marks?
- What product-security, privacy, vulnerability, export, product-liability, engineering-disclaimer, VAT, and merchant-of-record obligations apply before pilot or sale?

Questions record facts and alternatives; they do not solicit or fabricate legal conclusions.

## 7. Milestones

1. **M1-0 Registration:** freeze this plan and report its absolute path.
2. **M1-1 Baselines:** capture immutable repository/source identities and protected dirty state.
3. **M1-2 Rights ledger:** map material source/file ranges, transfers, contributors, agents, licences, standards/data/models, and notices.
4. **M1-3 Dependency/content matrix:** inventory declared direct/optional/build/test dependencies and non-code content; expose unresolved transitive/wheel closure.
5. **M1-4 Classification:** apply the controlled relicensing classes and state the program feasibility verdict/fallback.
6. **M1-5 Specialist packet:** issue bounded questions and explicit no-action decisions.
7. **M1-6 Evidence/QA:** cross-check schemas, identities, row counts, coverage, contradictions, and protected state.
8. **M1-7 Independent review:** freeze exact identities and submit the complete M1 packet to the ecosystem Boss.

M2 may be planned only after M1 receives `ECOSYSTEM CLOSEOUT: OK`. Product source implementation requires a separately accepted M2 and registered M3 plan.

## 8. Definition of done and evidence

M1 is ready for independent review only when:

- the accepted parent-plan identity and exact owned paths match;
- every in-scope repository has a full commit/tree identity and dirty-state classification;
- every root licence and packaging/migration manifest is accounted for or explicitly missing;
- mixed/transfer/agent/third-party/standards/model ranges are not hidden by repository summaries;
- the rights ledger and dependency/content matrix conform to their schemas and contain evidence references;
- source-declared versus installed/transitive SBOM evidence is clearly distinguished;
- every commercial-wedge item has a relicensing classification and unresolved owner;
- specialist questions correspond to actual blocking rows;
- the feasibility verdict and open fallback are explicit;
- no conclusion exceeds engineering evidence or purports to be legal advice;
- only registered paths changed and protected worktrees remain untouched;
- no prohibited action or PERF run occurred; and
- exact bytes, LF, CR, BOM, SHA-256, row counts, and cross-file references are submitted for independent review.

Allowed verification is limited to read-only Git/object inspection, hashing, CSV/JSON/UTF-8/schema consistency checks that execute no repository code, and Markdown cross-reference checks.

## 9. Risks and stop conditions

| Risk | Severity | Required response |
|---|---|---|
| Authorship history is incomplete after curated transfers | Critical | Preserve `UNKNOWN`; reconstruct source ranges or exclude |
| Agent-generated code lacks retained service/commissioning terms | Critical | `NEEDS_SPECIALIST`; no relicensing or distribution |
| Standards, PULS, CSR, customer, or trained assets have unclear rights | Critical | Quarantine and exclude |
| Root licence conflicts with file-level inbound rights/notices | Critical | Preserve original obligations; specialist review |
| Declared dependencies do not form one compatible graph | High | Block packaging; require later locked-matrix plan |
| Source manifests omit transitive/native/wheel content | High | Label M1 SBOM partial; defer exact artifact closure |
| Dirty worktree contaminates audit evidence | High | Read committed Git objects only; stop on ambiguity |
| Alias mapping incorrectly merges distinct contributors | High | Keep identities separate until documentary evidence |
| Audit is mistaken for legal approval | High | Prominent limitation and explicit specialist gates |
| Scope expands into M2 design or implementation | High | Stop, report deviation, and return to M1 evidence only |

Stop immediately on ambiguous source identity, accidental write outside registered paths, attempted licence change, customer/external contact, dependency installation/download, package import/execution, or resource-heavy work.

## 10. PERF inventory — none authorized

No M1 audit step requires PERF. The following later evidence may be resource-sensitive and is inventoried only:

| PERF ID | Deferred purpose |
|---|---|
| M1-PERF-01 | Multi-platform clean resolver and exact transitive dependency closure |
| M1-PERF-02 | Exact-wheel extraction, native-library inventory, SBOM and licence/security scanning |
| M1-PERF-03 | Reproducible source/binary correspondence across supported build cells |

Each requires a separate plan, exact commands and scope, a request through `C:\Github\.resource-manager\request-test.ps1`, explicit ledger approval, exclusive acquisition, and guaranteed release. None may run during M1.

## 11. Explicit exclusions

No licence edit, contributor agreement execution, customer contact, price test, GUI/GUIexpert work, protocol or product source implementation, branch/worktree creation, package import, dependency installation, model/runtime/content download, build, wheel, installer, cloud, marketplace, signing, publication, release, billing, licensed-content acquisition, solver/test execution, or PERF work is authorized.

The only permitted output is the registered M1 planning and audit packet.

## 12. Engineering-audit completion record and unresolved parent gate

The bounded committed-object audit completed on 2026-08-14 with:

- 13 immutable repository commit/tree baselines;
- 57 material rights/provenance ledger rows;
- 111 source-declared dependency/model/content matrix rows;
- 48 bounded specialist-review questions;
- zero `CLEAR_FOR_DUAL` source ranges;
- a verdict of `CONDITIONALLY FEASIBLE` for the recommended dual-licensed core, permissive protocol, and proprietary-workbench structure;
- explicit GPL fallback, compatibility migration, exclusions, risks, and deferred PERF inventory; and
- confirmation that no licence, product, customer, GUI, package, publication, download, external-content, test, solver, or PERF action occurred.

The corrected engineering-audit packet is frozen for independent verification. Parent M1 remains open: M2 is prohibited until the required specialist review and legal target-model decision are completed and independently accepted, unless the user explicitly accepts a new parent-plan amendment that splits those gates. This packet does not supply that review, decision, or amendment. Implementation remains prohibited until accepted M2 and a separately registered M3 plan.
