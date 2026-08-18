# ANYai Commercial Feasibility and Buckling Wedge Plan

Date: 2026-08-14 (Europe/Oslo)

Status: **REVIEW REQUESTED — planning only; independent acceptance required before any execution**

Registered path:
`C:\Github\ANYopenSoft\governance\plans\ANYAI_COMMERCIAL_FEASIBILITY_AND_BUCKLING_WEDGE_PLAN.md`

## 1. Objective and authority

This plan converts the ANY ecosystem monetization proposal into a gated commercial-feasibility and architecture program. It does not implement the product. Its objectives are to:

1. determine a legally and operationally coherent open/commercial boundary;
2. preserve canonical engineering ownership across the ANY repositories;
3. define an open headless tool, safety, and audit contract;
4. bound the first commercial wedge to traceable panel and cylindrical-shell buckling;
5. establish model, installer, update, privacy, and evidence security requirements;
6. preregister customer and pricing discovery; and
7. state the independent gates that must pass before product implementation.

### 1.1 Governing source

The only product source for this milestone is:

- path: `C:\Users\AudunArnesenNyhus\Downloads\ANY_Ecosystem_Monetization_AI_Interface.md`
- observed bytes: `15,915`
- SHA-256: `424592AFB73122197ADBD6C43F1B9B66202E5523BD6F7BA4680B4A710B772157`

The hash was reverified locally before planning. The unrelated TradingSystem document and its review are explicitly out of scope.

Applicable ecosystem governance is:

- `C:\Github\AGENTS.md` — ecosystem-wide performance serialization;
- `C:\Github\ANYopenSoft\governance\ECOSYSTEM_PHILOSOPHY.md` — ownership, contract, evidence, and qualification doctrine;
- `C:\Github\ANYopenSoft\governance\BOSS_PROTOCOL.md` — registration, reporting, evidence, and closeout gates; and
- `C:\Github\ANYopenSoft\governance\ROADMAP.md` — current ecosystem sequencing and the existing ANYai planning context.

### 1.2 Licensing authority clarification

Current repository licences are not immutable. The ecosystem owner may select a new coherent licensing model for code whose copyright and inbound obligations permit it. This authority does not waive:

- contributor or copyright ownership;
- inbound licence obligations;
- third-party dependency terms;
- notice, attribution, corresponding-source, or source-offer duties;
- model, standards, dataset, trademark, or vendor-SDK rights;
- compatibility and migration duties; or
- specialist legal review before commercial distribution.

No licence file is edited under this plan.

## 2. Repository, base, owned path, and exclusions

### 2.1 Planning repository state

| Field | Registered value |
|---|---|
| Repository | `C:\Github\ANYopenSoft` |
| Current branch | `main` |
| Observed HEAD | `7d29eaef1c899fc56681a723184c97e2ed04abb0` |
| Worktree condition | Pre-existing dirty primary checkout; unrelated portal and governance changes are present |
| Exact owned path | `governance/plans/ANYAI_COMMERCIAL_FEASIBILITY_AND_BUCKLING_WEDGE_PLAN.md` |
| Branch/worktree action | None authorized or performed |
| Commit/push/PR action | None authorized or performed |

Only the registered plan file is owned by this planning task. Every other modified, untracked, staged, or committed path belongs to its existing owner and must remain untouched.

The observed HEAD is an audit anchor, not an implementation base. Every later editing plan must select and reverify a clean accepted base SHA for each repository, use disjoint ownership, and state its branch/worktree explicitly. No future implementation may infer authority from this dirty primary checkout.

### 2.2 No-action boundary

Until this plan is independently accepted, it authorizes none of the following:

- product or engineering-package implementation;
- licence-file changes or relicensing;
- creation of an ANYai runtime repository;
- GUI work or GUIexpert review;
- cloud, remote-compute, or data-egress work;
- marketplace or third-party pack onboarding;
- installer, updater, licensing-service, packaging, signing, or publication work;
- acquisition or redistribution of customer data, licensed standards, proprietary templates, models, or vendor content;
- customer outreach, interviews, price testing, offers, billing, build/service distribution, customer-data handling, or paid pilots without a separate explicit user authorization for that exact external action;
- model or runtime downloads;
- package builds, native builds, releases, deployment, or performance work; or
- claims of certification, approval, qualification beyond recorded evidence, or production readiness.

This plan cannot itself open an implementation gate. Acceptance permits only the next separately registered milestone stated in section 16.

### 2.3 Read-only ecosystem snapshot

These observed identities bound this audit only. They are not approved implementation bases.

| Repository | Branch | Observed HEAD | Worktree note |
|---|---|---|---|
| ANYgeometry | `main` | `939e047f19177692c861a68eaef0eaa18b2976c5` | Existing unrelated dirty entries |
| ANYmesh | `main` | `979f6a88f0d81507e1ac61b854f1f56362ce5e37` | Observed clean |
| ANYmaterial | `main` | `4626887667f4c251479d26f321b9e73b046a2783` | Observed clean |
| ANYfileIO | `codex/anyfileio-repository-rename` | `0d2c7f8ef1b17f42f667d6183125e51cb650a70d` | Observed clean; not default-branch authority |
| ANYfileio-occt | `main` | `23b441c3fcabb5bf4cf077daca882b984f978b42` | Observed clean |
| ANYsolver | `main` | `3cdb51efcdded232054225ea0eb9cc16dc79dde9` | Observed clean |
| ANYfem | `main` | `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2` | Existing unrelated UI/test changes |
| ANYbuckling | `main` | `3fe06c9ea126fcd59f2cd0ce825a029540b479e9` | Existing unrelated IDE entry |
| ANYstructure | `clean-up-after-external` | `4a79b860739c2f0b24f61314d4c13d943886bdd3` | Existing unrelated entry; not default-branch authority |
| ANYtk3D | `main` | `0f49efc53670c601bbabc012d856cc8ca18dcc9b` | Existing unrelated source/test changes |
| ANYintelligent | `move_solver` | `a1f58f3488e6a250fa0ce5b189fbfc8f658415ff` | Heavily dirty research checkout; not an implementation base |
| ANYtimeseries | `main` | `c578e910fd9d1ea481b4fae144a75bd66549beaf` | Existing unrelated changes |

Any drift or proposed consumption requires a new snapshot and a separately accepted plan. No branch, index, worktree, or repository state was changed by this audit.

## 3. Product thesis and first commercial decision

The commercial thesis is accepted provisionally:

> Commercial value comes from a private, reliable engineering workflow with deterministic authority, validated capability packs, traceable evidence, installation and compatibility management, and support—not from generic access to a language model.

The target experience remains a local-first Windows engineering workbench with no user-managed Python, Docker, CUDA tooling, model files, ports, or command line. “No Python” means **no customer-managed Python**; it does not require rewriting qualified Python kernels. A controlled and signed internal runtime remains an implementation option.

The broad `CAD → validation → mesh → solve → results → report` vision is a later product direction. It is not the first wedge because arbitrary CAD repair, broad meshing, and general nonlinear qualification are not yet one bounded, commercially supportable capability.

The first wedge is instead:

> **A private, traceable buckling-assessment workbench for supported stiffened flat panels and circular cylindrical shells.**

## 4. Current licence, copyright, and dependency feasibility

### 4.1 Verified repository-licence snapshot

The following is a planning snapshot, not a complete legal audit:

| Repository | Current root/package licence evidence | Initial commercial classification |
|---|---|---|
| ANYopenSoft | GPL-3.0-or-later | Governance/product-portal repository; no runtime role and no relicensing assumption |
| ANYgeometry | GPL-3.0-or-later | Relicensing/dual-licensing candidate after provenance audit |
| ANYmesh / `ANYmesher` distribution | GPL-3.0-or-later | Relicensing/dual-licensing candidate after provenance audit |
| ANYmaterial | GPL-3.0-or-later | Relicensing/dual-licensing candidate after provenance audit |
| ANYfileIO / `ANYfileio` distribution | GPL-3.0-or-later | Relicensing/dual-licensing candidate after provenance audit |
| ANYfileio-occt | GPL-3.0-or-later | Candidate only after contributor and OCCT/provider dependency review |
| ANYsolver | GPL-3.0-or-later | Relicensing/dual-licensing candidate after provenance audit |
| ANYfem | GPL-3.0-or-later | Relicensing/dual-licensing candidate; intended workflow authority |
| ANYbuckling | GPL-3.0-or-later | Relicensing/dual-licensing candidate; first-wedge engine |
| ANYstructure | GPL-3.0-or-later | Keep GPL and outside proprietary runtime unless full legacy provenance is cleared |
| ANYtk3D | GPL-3.0-or-later | Candidate after provenance and GUI dependency review; not needed for the headless wedge |
| ANYintelligent | No root licence found in the observed checkout | Research/history only; exclude from product until ownership and licence are resolved |
| ANYtimeseries | MIT | May remain permissive; not a canonical FEM or product-workflow owner |

The common GPL text observed in the principal repositories has SHA-256 `230184F60BAE2FEAF244F10A8BAC053C8FF33A183BCC365B4D8B876D2B7F4809`; ANYstructure has a project-specific GPL header. Package metadata was also checked where present. A root licence and metadata statement are evidence, but neither proves complete copyright ownership or dependency compatibility.

### 4.2 Copyright and inbound-code audit

Git history shows mostly Audun Arnesen Nyhus identities in the newer owner packages, but that is not sufficient evidence of sole copyright. Material exceptions requiring file- and commit-level review include:

- multiple named contributors in ANYstructure;
- multiple local agent identities in ANYfileio-occt;
- a generated-agent identity in ANYintelligent;
- code transferred or extracted from ANYstructure into ANYbuckling or other packages;
- copied formulas, tables, fixtures, examples, model outputs, and reference data;
- generated code whose applicable service terms and human modification history must be retained; and
- dependencies or vendored files not governed by the repository's root licence.

Material audit findings that must be resolved rather than inferred are:

- ANYstructure changed from MIT to GPL in commit `83cdadf`; pre-change third-party code may retain a usable MIT grant, but its original copyright and permission notices survive and it cannot be represented as exclusively owned without evidence.
- ANYintelligent has no observed root licence, CLA, DCO, NOTICE, or contributor policy, and contains substantial agent-attributed material. Treat all of it as rights-unresolved and exclude it from the product.
- current ANYfileio-occt implementation/test history is attributed to local agent identities `Eir` and `Liv`; record the model/service terms, commissioning party, human review, and source provenance.
- the migration documents in ANYgeometry, ANYmesh, ANYmaterial, ANYfileIO, and ANYsolver, plus the ANYbuckling and ANYtk3D histories, describe curated transfers. New-repository blame cannot substitute for the original source-range history.
- ANYtimeseries is MIT, but bundles upstream QATS-derived material whose original MIT notice and authorship must be restored and preserved.
- ANYmaterial contains standards-derived data and ANYbuckling documents equations/limits drawn from locally held standards/manuals. ANYstructure also contains PULS-derived trained assets. Quarantine these tables, manuals, sheets, models, datasets, and labelled fixtures until their reproduction and derivative-data rights are cleared.

The mandatory audit deliverable for every candidate repository is a file-level provenance ledger containing:

```text
path
blob/content identity
origin repository and commit
authors/contributors
copyright claimant
inbound licence or agreement
third-party or generated status
relicensing authority
required notice/source offer
commercial-use restrictions
decision and reviewer
```

Commit shortlogs are discovery aids only. They cannot establish authorship, employment assignment, or relicensing authority. Any unresolved file remains under its existing licence and cannot enter a differently licensed commercial distribution.

### 4.3 Dependency and content audit

The next audit must produce SPDX-compatible software bills of materials and a manual rights matrix for:

- direct, optional, build, test, native, GUI, and transitive dependencies;
- CPython and bundled runtime components;
- NumPy, SciPy, HDF5-related components, OCP/OCCT, Qt/PySide, and platform runtimes;
- local-model runtimes such as llama.cpp or Ollama;
- every model file, tokenizer, prompt template, embedding model, and document indexer;
- standards-derived formulas, tables, terminology, examples, and report language;
- OrcaFlex, PULS, Excel, vendor SDK, and licensed-sheet integrations;
- fonts, icons, installers, update frameworks, and code-signing tools; and
- test data, benchmark data, customer files, and generated reports.

Each row records source, exact version/hash, SPDX expression, copyright, redistribution, modification, attribution, source-offer, patent, trademark, field-of-use, data-use, export, and end-user obligations. A model licence is independent of the runtime licence. A standards-based calculation does not authorize redistribution of standards text or proprietary tables.

Known dependency gates include:

- the `ANYmesh[gmsh]` extra: the GPL Gmsh build is excluded from a closed distribution unless an accepted commercial or otherwise compatible route exists ([Gmsh licensing](https://gmsh.info/));
- PySide6/Qt: select and document either a compliant LGPL route or a commercial Qt route; community wheels cannot be treated as obligation-free ([Qt for Python commercial-use guidance](https://doc.qt.io/qtforpython-6.10/commercial/index.html));
- OCP/OCCT: preserve the binding and native-library licences and complete the currently blocked wheel-record/redistribution evidence ([CadQuery OCP](https://github.com/cadquery/OCP), [OCCT](https://github.com/Open-Cascade-SAS/OCCT));
- pypardiso/MKL, xlwings/Pro features, ReportLab fonts, and similar optional assets: exclude from the wedge until exact-wheel and content review passes; and
- NumPy, SciPy, CPython, and other permissive components: keep exact version-locked SBOM and notice evidence even where proprietary use is allowed.

The checked-out package graph is not currently a distributable lock: ANYfileIO and ANYfileio-occt declare incompatible core ranges, and current ANYstructure ranges lag current geometry/mesher versions. Packaging remains blocked until one compatible source/wheel matrix is independently accepted.

The current ANYopenSoft public statement that the whole ecosystem is GPL also conflicts with ANYtimeseries being MIT and ANYintelligent having no observed licence. Public messaging must be corrected only after the target model is accepted. The existing ANYstructure trademark policy should be expanded through a later reviewed ecosystem policy covering `ANY`, `ANYopenSoft`, `ANYai`, logos, and referential use of third-party marks.

### 4.4 Target licensing models

| Model | Description | Advantages | Principal blockers |
|---|---|---|---|
| A. Entirely GPL desktop | ANYai and workers remain GPL; revenue comes from verified builds, support, packs where separable, compute, and enterprise services | Lowest internal GPL-integration risk; maximally open | Weakest proprietary differentiation; pack separability and standards rights still unresolved |
| B. Proprietary client plus arm's-length GPL workers | Closed workbench communicates with independently distributed GPL applications | Preserves existing GPL packages | Separation is legally fact-specific; intimate model/protocol exchange may form a combined work; deployment/support complexity |
| C. Permissive open core plus proprietary product | Relicense selected packages permissively; close orchestration and premium packs | Easy third-party adoption | Gives competitors broad commercial rights; every contributor must permit relicensing |
| D. Dual-licensed engineering core plus proprietary workbench | Keep public GPL editions and offer a commercial licence for qualified proprietary integration; open protocol/safety contracts remain permissive | Preserves open access while funding an integrated product; clean local deployment | Requires consolidated copyright/provenance, contributor policy, dependency compatibility, and legal administration |
| E. Explicit linkage exception | GPL packages add a narrowly drafted commercial/interface exception | Can preserve copyleft while enabling one integration pattern | Hard to draft and maintain; still requires all relevant copyright authority |

The distinction between separate programs and one combined work depends on actual coupling and communication semantics, not merely the use of IPC. Specialist counsel must review any GPL/proprietary boundary. Relevant background includes the [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html).

### 4.5 Recommended migration path

Recommend **Model D: a dual-licensed open engineering core with an open protocol/safety foundation and a proprietary ANYai workbench**, subject to the following gates:

1. Freeze all licence changes until file-level provenance and dependency audits finish.
2. Classify each repository/file as `CLEAR_FOR_DUAL`, `KEEP_EXISTING`, `REPLACE_CLEANLY`, or `EXCLUDE`.
3. Keep ANYstructure and ANYintelligent outside the proprietary runtime unless their legacy provenance is independently cleared. Consume only stable exported data or cleanly owned APIs; do not transplant uncertain code.
4. Dual-license only owner packages for which all material copyright is controlled or separately licensed. Preserve every historical GPL tag and source release unchanged.
5. Create the tool schemas, reference types, compatibility manifest, and generic receipt verifier as a new open, neutral foundation under a permissive licence chosen after counsel review; Apache-2.0 is the initial candidate because of its explicit patent grant. Draft it cleanly from the accepted contract without copying GPL implementation code.
6. Place proprietary UX, conversation state, orchestration experience, entitlement, update/model management, and enterprise administration in a new ANYai repository only after the legal and architecture gates pass.
7. Adopt a contributor agreement or equivalent inbound policy granting the rights needed for both public GPL and commercial licensing. A DCO alone may not grant relicensing authority.
8. Maintain separate GPL and commercial release manifests, notices, licence texts, source/source-offer obligations, SBOMs, and compatibility evidence.
9. Treat a licensing change as an explicit release/migration event with user-facing documentation; never rewrite old history or silently change existing entitlements.
10. Obtain specialist software-licensing approval before any closed build, packaging, price publication, or commercial pilot.

Fallback: if sufficient rights cannot be consolidated, use Model A for the affected combined work and monetize verified distributions, support, onboarding, hosted compute where separately lawful, and consulting. Do not use IPC structure as an unreviewed workaround.

This recommendation is a planning conclusion, not legal advice and not licence-change authority.

## 5. Canonical ownership and dependency direction

| Owner | Canonical responsibility in the program |
|---|---|
| ANYgeometry | Geometry, topology, persistent identity, tolerance, intersections, and geometry audit truth |
| ANYmesh | Discretization, mapped-mesh policy, refinement, conformity, and mesh-quality truth |
| ANYmaterial | Material definitions, validation, units, and constitutive conventions |
| ANYfileIO | Neutral interchange semantics and backend-neutral imported-artifact contracts |
| ANYfileio-occt | Optional native CAD provider behind ANYfileIO contracts; currently a zero-capability refusing shell and not part of the first wedge |
| ANYsolver | FE physics, numerical state, convergence, result provenance, and exact qualification scope |
| ANYbuckling | Prescriptive and semi-analytical panel/cylinder buckling calculations and their applicability truth |
| ANYfem | Canonical project state, analysis intent, application workflow, job coordination, project persistence, postprocessing, and report context |
| ANYstructure | Specialized/legacy structural application and migration source; not a second general workflow authority and not imported by the first wedge |
| ANYtk3D | Rendering and interaction primitives only; never project or engineering truth |
| ANYtimeseries | Generic time-series utility only where a narrow headless contract is demonstrated |
| ANYintelligent | Research/history and experiments; no production runtime authority until separately audited |
| Open protocol/safety foundation | Versioned capability, action, artifact, compatibility, permission-class, and receipt schemas plus generic verification |
| ANYopenSoft governance | Cross-repository plans, qualification evidence, compatibility decisions, and independent closeout; no runtime implementation |
| Proprietary ANYai Desktop | UX, conversation and proposal orchestration, entitlement, model/runtime/update management, diagnostics, and enterprise administration |
| Capability pack | Versioned recipes, policies, validators, templates, reference cases, qualification evidence, and declared legal scope |

The dependency direction is:

```text
domain owners -> ANYfem workflow composition -> owner adapters
              -> open protocol/safety boundary -> ANYai client
```

ANYai never owns FEM state, geometry, mesh, materials, solver results, or buckling truth. It proposes typed operations against a pinned project revision. The owning package validates and executes; ANYfem coordinates project state; the safety boundary authorizes; the audit layer records.

No owner imports ANYai. No owner gains a dependency on an LLM runtime. Existing standalone and scripted workflows remain independently useful.

### 5.1 Readiness constraints

The current repositories support a narrow headless program, but not a general commercial claim:

- ANYfem already has canonical project/document revisions, command/session semantics, job and artifact records, checksum-verified results, and deterministic reporting. It remains the project/artifact authority; ANYai must not create a competing database.
- ANYbuckling exposes callable panel and cylinder prescriptive APIs, but there is no committed clause-level qualification packet establishing a commercial envelope. Regression to current outputs is not independent validation.
- ANYbuckling S3/U3 describes itself as a reduced first physics milestone and does not establish PULS parity. Its licensed-sheet path and manual-derived evidence are excluded.
- ANYsolver exposes genuine eigen-buckling and capacity workflows, but the currently inspected evidence does not establish a full externally referenced cylindrical-shell commercial qualification. FE results are excluded from v0.1.
- ANYfem has a headless stiffened-panel FE acceptance workflow, but no equivalent accepted cylinder-buckling reference. That makes an FE-first two-template wedge premature.
- ANYmaterial, ANYgeometry, ANYmesh, and ANYsolver use SI conventions, while legacy ANYbuckling setters use mixed millimetre/MPa engineering units. A named, audited adapter must accept canonical SI, perform one explicit conversion, and retain both the SI input and exact owner-call payload.
- ANYfem's current job completion state can describe callable completion without independently proving engineering validity. The safety wrapper must keep execution status, numerical validity, applicability, and qualification as separate fields.
- the current package-version constraints are not one compatible installed product graph; no installer or distribution claim is allowed before a clean locked matrix passes.
- ANYfem's documented migration gate remains closed. API completeness must not be reported as ecosystem replacement or release readiness.

The smallest defensible wedge therefore uses ANYmaterial validation, ANYbuckling prescriptive calculations, and ANYfem project/revision/artifact/report authority without CAD, meshing, or FE execution.

## 6. Open protocol, safety, and audit v0.1

### 6.1 Protocol design

Protocol v0.1 is transport-neutral. An MCP adapter may expose it to a model, but MCP is not the engineering safety boundary. The normative contracts are typed, versioned, unit-aware, deterministic, and executable without an LLM.

Required records:

| Record | Mandatory semantics |
|---|---|
| `CapabilityDescriptor` | Namespaced capability/version, provider/package identity, input/output schemas, units, qualification scope, resource estimate, mutation class, reversibility, egress/network need, compatibility range |
| `ArtifactRef` | Stable ID, role, media/schema type, byte length, SHA-256, owner, creation receipt, confidentiality class; no arbitrary path authority |
| `ProjectRevision` | Project/model identity, revision, parent/content hash, schema version, dirty/stale state |
| `OperationPlan` | Capability, canonical inputs, expected outputs and mutations, preconditions, cost/resource budget, deadline, idempotency key, operation hash |
| `ValidationReceipt` | Schema/unit/identity/applicability/qualification checks, warnings, typed refusal, provider and validator versions |
| `ApprovalRequest` / `ApprovalReceipt` | Human-readable preview, exact operation hash and project revision, permission class, expiry, one-use token, approver identity |
| `ExecutionReceipt` | Start/end, exact implementation/environment identities, status, diagnostics, consumed/produced artifacts, resource use, warnings, cancellation/recovery state |
| `EvidenceManifest` | Ordered hash-addressed chain from instruction and proposal through approval, results, overrides, report, and sign-off |
| `CompatibilityManifest` | Protocol, package, project-schema, capability-pack, runtime/model, and report-schema ranges plus known exclusions |

The wedge also freezes these domain compositions without creating a second project model:

- `ProjectRef`: ANYfem project/document UUID, sequence, document hash, and model hash.
- `CaseRevision`: case UUID/type/schema, parent hash, canonical SI input hash, method/edition reference, material/source references, assumptions, and approval events.
- `RunSubmission`: job UUID, frozen case hash, operation/adapter/owner versions, settings/config hash, environment, deterministic resource policy, and approval.
- `EvidenceBundle`: proposal, approval, canonical SI input, exact owner payload, validation/domain report, raw and normalized results, diagnostics/refusals, evidence class, producer versions, rendered report, append-only audit events, and SHA-256 manifest.

Artifact references use scoped relative locations plus byte length and SHA-256; a protocol request never grants arbitrary filesystem access. A changed revision makes an earlier run stale rather than silently current.

Lifecycle:

```text
discover -> plan -> validate -> approve when required
         -> execute/commit atomically -> validate outputs
         -> publish artifacts and append receipt -> explain
```

No output becomes authoritative before output validation and atomic receipt publication. Partial, cancelled, unsupported, unqualified, stale, incompatible, resource-exceeded, provider-unavailable, execution-failed, and verification-failed states remain explicit non-successes.

Protocol invariants:

- SI internally; conversion occurs exactly once at ingestion/display and is recorded.
- Capability discovery and version handshake precede use.
- Every mutating action supports dry-run and lists its expected mutation set.
- Approval is bound to one operation hash and one current project revision; project drift invalidates it.
- Idempotency prevents retry-created duplicate work.
- Deadlines, cancellation, CPU/RAM/GPU/disk budgets, and expected duration are explicit.
- Read-only, reversible, expensive, irreversible, external-integration, and data-egress classes are distinct.
- Provider-specific objects never cross the public boundary.
- Receipts are append-only and content-addressed; report facts trace to receipts.
- Unsupported or unqualified work fails closed and cannot be rewritten as a warning-only success.
- Execution status and evidence status are orthogonal. A completed process may still produce `invalid`, `refused`, `out_of_scope`, or `unqualified_computation` evidence.

### 6.2 Safety authority

The open safety foundation owns generic authorization and receipt invariants. Domain owners retain engineering validation. ANYai and the LLM own neither.

| Class | v0.1 policy |
|---|---|
| S0 — Inspect/validate | Read-only and journalled; no approval needed after schema/revision/confidentiality checks |
| S1 — Reversible draft mutation | Compare-and-swap against the expected revision, dry-run, explicit approval, atomic rollback |
| S2 — Engineering run/report | Explicit approval bound to the frozen case revision and resource estimate; cancellation/recovery required |
| S3 — Export/overwrite/authoritative release | Prohibited in v0.1; later requires separate engineer acknowledgement and plan |
| S4 — Network/cloud/install/publish/licensed external effect | Prohibited in the wedge and requires separate authority |

The model sidecar receives only approved context and has no direct filesystem, package, network, credential, shell, or Python authority. AI explanations must cite recorded facts. AI prose is visibly distinct from verified numerical output and cannot upgrade `unsupported`, `not executed`, `failed`, or `unqualified`.

### 6.3 First-wedge capability surface

The contract-freeze milestone should consider only the following logical operations; final names and schemas are frozen there, not here:

```text
system.capabilities.get
project.create
project.revision.get
buckling.case.propose
buckling.case.validate
buckling.case.commit
buckling.assessment.run
buckling.assessment.get
artifact.verify
report.render
audit.manifest.verify
```

Every operation descriptor records its owner/version, schemas, canonical unit profile, side-effect and risk classes, approval policy, idempotency/reversibility, determinism, domain predicate, resource estimate, cancellation/timeout, artifact types, and qualification level. Every invocation records project/case revision hashes, canonical input and exact adapter-payload hashes, approval event, environment, timestamps, typed diagnostics, output artifacts, and evidence classification.

Execution status is one of `succeeded`, `refused`, `invalid`, `failed`, or `cancelled`. Evidence is separately classified as `unqualified_computation`, `internally_verified`, `qualified_for_named_envelope`, or `out_of_scope/refused`. Nothing in the orchestration layer may promote evidence classification.

An ANYsolver comparison may be added only as a separately qualified later capability with exact supported geometry, elements, loads, boundary conditions, and interpretation. It is excluded from v0.1.

## 7. Bounded buckling wedge

### 7.1 Included product hypothesis

The wedge serves engineers who repeatedly assess supported stiffened flat panels or circular cylindrical shells and need local privacy, checking, reproducibility, and a reviewable report. It is one workbench with two deliberately narrow synthetic/manually authored case templates:

| Template | Bounded v0.1 candidate envelope |
|---|---|
| A — Panel | Regular isotropic-steel flat stiffened panel; stress input; ULS; DNV-RP-C201 prescriptive path; one fixed supported T-bar profile family; no girder |
| B — Cylinder | Isotropic-steel longitudinally stiffened circular cylindrical shell; stress input; ULS; DNV-RP-C202 prescriptive path; no rings, orthogonal stiffening, cones, or force-input mode |

ANYmaterial validates the steel definition and source metadata. A named ANYbuckling adapter accepts canonical SI only, performs audited SI-to-legacy-unit conversion, and retains normalized SI plus the exact owner-call payload. ANYbuckling owns applicability and calculation truth. ANYfem owns case/project revision, run/job, immutable artifact, evidence, and report records.

M2 must freeze the remaining envelope before implementation: exact rights-cleared standard edition references; accepted stress components, signs, gradients, and combinations; boundary/support conventions; geometry, slenderness, material, and profile ranges; partial/material factors; applicability predicates; tolerances; and typed refusals. The SI-to-legacy conversion adapter is owned and versioned by ANYbuckling because only the calculation owner may define its input semantics. The open protocol carries canonical SI; ANYfem composes the case and records both payloads; ANYai owns neither conversion nor applicability.

No geometry, mesh, CAD, or FE execution is required for v0.1. Inputs are synthetic or manually authored; existing ANYstructure projects and customer models are not imported. Both templates remain feasibility/verification-only until independent reference calculations establish the exact supported envelope.

The exact scope is defined by the owning code and accepted qualification evidence, not by marketing language. PULS Excel/sheets, ML predictors, licensed inputs, and S3/U3 as a governing result are excluded.

### 7.2 Deterministic workflow

```text
create a supported parameterized case in canonical ANYfem project records
  -> snapshot identity and revision
  -> validate geometry, material, units, loads/stresses and applicability
  -> preview selected method and limitations
  -> approve exact assessment
  -> run owner calculation
  -> validate result/status and preserve warnings
  -> build evidence manifest and engineer-reviewable report
  -> named engineer/checker sign-off outside AI authority
```

Required output includes canonical SI inputs, the exact converted owner payload, selected method/edition/scope, raw owner result, normalized utilization/check list, controlling check where supported, assumptions and limitations, applicability checks, warnings, typed non-success, package/adapter/environment identities, content hashes, timestamps, approvals, overrides, and report provenance. Missing or invalid values never become zero or a plausible estimate.

### 7.3 Explicit exclusions

- arbitrary STEP/IGES repair or CAD healing;
- general CAD preparation or solid-to-shell conversion;
- any CAD/file import, geometry, meshing, or OCCT provider use;
- unrestricted FEM model generation or modification;
- ANYsolver FE/eigen/capacity as a governing result;
- S3/U3 as a governing result;
- deep post-buckling, fatigue, thermal, contact, optimization, batch, or parameter-study automation;
- PULS sheets, standards text/tables, proprietary templates, or vendor data;
- ANYstructure runtime/import and all ML/trained assets;
- non-steel, orthotropic, composite, unstiffened, girder, ring-stiffened, orthogonally stiffened, or conical domains;
- force-input mode, ALS, automatic corrosion allowance, or automatic standards lookup;
- cloud inference, remote compute, marketplace, or third-party packs;
- autonomous execution, arbitrary scripting, or direct model mutation;
- certification, class approval, or substitution for engineer/checker responsibility; and
- PDF signing, overwrite/export authority, installation, GUI/ANYtk3D, licensing, or commercial-release implementation under this plan.

### 7.4 Headless-wedge definition of done

The later headless wedge is complete only when all of the following pass under separately accepted implementation plans:

- versioned schemas with explicit units exist for at least one accepted panel case and one accepted cylinder case;
- deterministic synthetic/reference fixtures cover success, boundary, unsupported, malformed, stale-revision, cancellation, and recovery cases;
- exact input, package, environment, and configuration identities reproduce authoritative numerical results within predeclared tolerances;
- owner-package qualification scope is quoted without broadening;
- protocol negotiation, idempotency, approval binding, rollback, and receipt verification pass;
- every numerical report statement reconciles to a recorded result field and evidence hash;
- failures and unsupported conditions cannot generate a pass-like report;
- no LLM is required for the reference execution;
- an independent engineering validator reproduces and accepts the results and limitations; and
- reports state that engineering review/sign-off remains required and do not claim certification.
- clause-level independent hand calculations or accepted external references validate every reported governing quantity; matching today's implementation is not sufficient;
- malformed, non-finite, unit-mismatched, out-of-domain, revision-race, approval-replay, path-traversal, and corrupt-artifact cases refuse deterministically; and
- the dependency lock and installed-wheel matrix are mutually compatible and accepted before any packaged prototype.

## 8. Model, installer, and update threat model

Security baselines for downstream design include [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final), [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), and the OWASP guidance on [prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/).

| Trust boundary | Principal threats | Required controls | Later evidence |
|---|---|---|---|
| Imported files/text/metadata | Indirect prompt injection, malformed parser input, path traversal, deceptive units | Treat all content as data; sandbox parsers; type/size/path limits; hashes; explicit units; no active content | Injection/malformed corpus and path/size/unit rejection tests |
| Local model sidecar | Compromised model/runtime, parser exploit, exfiltration, resource exhaustion | Unprivileged isolated process; no network/credentials/packages; staged read-only context; memory/time/disk quotas; watchdog | Network-denial, boundary, timeout, OOM, crash and recovery tests |
| Protocol/orchestrator | Excessive agency, schema confusion, replay, stale approval/TOCTOU | Allowlist; strict schemas; version handshake; idempotency; action hash plus project revision; fail closed | Unauthorized-tool, replay, stale-token, forged-response and mismatch tests |
| ANY executors/project | Corruption, partial writes, version drift, fabricated success | Scoped workspace; atomic checkpoints/publication; pinned versions; output validation; deterministic envelopes | Crash recovery, rollback, reproducibility and result-validation tests |
| Model/runtime/update supply chain | Substitution, incompatible licence, signing-key compromise, downgrade/freeze | Signed allowlisted manifests with origin, licence, hash, bytes, compatibility, expiry/revocation; separated keys/roles; rollback protection | Tamper, revoked/expired key, wrong-model, downgrade and freeze tests |
| Installer/updater/repair | Privilege escalation, DLL hijack, partial update, data loss | Per-user install where possible; no persistent privileged service; restricted temp/search paths; atomic rollback; signed/timestamped binaries; SBOM | Clean-image, non-admin, signature, interruption, repair and uninstall tests |
| Licence/telemetry/diagnostics | Project disclosure, invasive fingerprint, client signing secret, clock rollback | Signed entitlements; server-side private keys; privacy-preserving device ID; no/opt-in telemetry; diagnostic preview/redaction; customer-file access preserved | Offline, expiry/revocation, clock-change, packet-capture and redaction tests |
| Audit/report | Evidence tampering, secrets in logs, prose mistaken for approval | Append-only/hash-chained records; redaction; immutable manifest; explicit overrides; engineer/checker sign-off | Mutation, omission, source reconciliation and restore tests |

Downloaded models and runtimes require a per-artifact licence/security manifest. Model files are untrusted inputs. Later update design should evaluate [The Update Framework](https://theupdateframework.io/docs/security/) for rollback/freeze-resistant metadata, Windows [code-signing options](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options), and [AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation) or an equivalent restricted-process boundary.

Legal review must assess applicable product-security, vulnerability-handling, privacy, export, and liability obligations, including the [EU Cyber Resilience Act legal text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847) and current official manufacturer guidance. No exemption is assumed.

## 9. Customer and pricing discovery

### 9.1 Target hypotheses

Initial target organisations are small and mid-sized offshore, marine, and structural-engineering teams performing repeated panel/cylinder buckling assessments on Windows with confidentiality and checking requirements.

Sample these roles separately:

- analyst/user;
- independent checker or technical authority;
- IT/security approver; and
- budget owner/procurement decision maker.

Discovery begins only after M2 contract acceptance, through the separately registered M2D discovery milestone in section 12, **and after the user explicitly authorizes the exact external-contact scope**. That user gate must name the target segment or organisations, contact method, approved interview/price-testing script, information to be collected, storage/retention, privacy handling, responsible owner, and stop conditions. Boss standing authority alone cannot open this gate. Discovery uses synthetic cases only and acquires no customer models, standards, or proprietary templates.

Sequence:

1. Preregister interview questions, segments, thresholds, price cells, and evidence format.
2. Conduct 15–20 problem interviews across at least ten organisations without leading with product features or prices.
3. Observe at least six reconstructions of the current workflow using synthetic inputs.
4. Measure task frequency, analyst/checker time, rework, audit burden, confidentiality constraints, support expectations, budget source, and purchase authority.
5. Test concept and price cells with qualified budget owners; randomize cells and retain refusals.
6. Seek three to five fixed-scope paid design-partner pilots only after the headless, legal, security, and GUI gates.

Provisional go/no-go thresholds:

- at least 10 of 15 qualified organisations confirm recurring workflow and checking/reporting pain;
- at least five budget owners identify a credible budget and purchase route;
- at least three organisations accept a paid pilot at a tested price;
- at least two of three completed pilots reduce measured preparation/reporting time by at least 30% without reducing checker acceptance or traceability; and
- no pilot depends on an excluded broad CAD, cloud, licensed-content, or unsafe automation feature.

Stop or rescope if three paid pilots cannot be secured after 20 qualified opportunities, demand is dominated by excluded capabilities, local confidentiality cannot be met, or verified savings cannot support delivery and support costs.

### 9.2 Pricing hypotheses only

No price is approved for publication or sale.

| Research cell | Hypothesis | Purpose |
|---|---:|---|
| Open ecosystem | €0 | Existing packages, documentation, and manual workflows |
| Source-plan Local anchor | €190–290/year | Detect consumer-AI price anchoring and support-cost mismatch |
| Source-plan Engineering anchor | €490–790/year | Test the source proposal, not endorse it |
| Buckling Professional challenger | €1,500–4,000/named user/year | Test value of traceable workflow, evidence, and maintained qualification |
| Paid design-partner pilot | €3,000–8,000/organisation for 8–12 weeks | Fixed synthetic/reference cases, onboarding, and measured non-production evaluation |
| Enterprise Offline challenger | €10,000–40,000/organisation/year | Test air-gap/LTS/policy/support value |
| Custom integration/validation | Separate quote | Prevent hidden subsidy through seat pricing |

All cells exclude VAT, cloud, licensed third-party content, and custom validation. Test annual entitlement that preserves access to the last licensed version against subscription-only access. Select no tier until measured support cost, conversion, value, and renewal evidence exist.

## 10. GUIexpert advisory gates

GUIexpert is advisory and cannot waive engineering, legal, security, or independent-validation findings.

| Gate | Earliest trigger | Advisory scope | Required exit |
|---|---|---|---|
| GUX-0 Contract comprehension | Headless protocol/safety/audit v0.1 frozen and model-free synthetic wedge accepted | Task/state model, proposed-versus-executed distinction, units, provenance, failure taxonomy | Severity-ranked memo; every P0/P1 finding assigned |
| GUX-1 Safety wireframe | Threat model and approval semantics accepted | Approval previews, reversibility, warnings, evidence navigation, prohibited cloud boundary | No ambiguous modifying action or hidden data boundary |
| GUX-2 Workflow usability | Independently verified headless wedge | Low-fidelity panel/cylinder workflow with synthetic fixtures | At least 4/5 representative users finish uncoached; 5/5 distinguish proposal from verified result and locate provenance |
| GUX-3 Install/repair usability | Installer security design accepted and packaging separately authorized | Clean install, CPU fallback, model choice, update/repair, disk/error messaging | No command-line dependency; recovery understood; no silent privilege/network action |
| GUX-4 Pilot readiness | Legal, security, engineering, and signed-build pilot gates satisfied | Accessibility, recovery, report comprehension, limitations and sign-off | No unresolved P0/P1; accountable owners record decision |

No GUI milestone precedes GUX-0. Kill, recovery, verification, and evidence access must remain available through headless mechanisms.

## 11. Migration and compatibility policy

- Historical licence grants, releases, tags, and notices remain intact.
- Protocol, project, capability-pack, artifact, receipt, and report schemas use explicit semantic versions.
- A compatibility manifest pins exact supported ranges and known exclusions across repositories, runtime/model, and packs.
- Breaking schema or ownership changes require a new major version and deterministic migration or explicit refusal.
- ANYfem owns project migrations; domain packages own their schema migrations; ANYai does not rewrite either independently.
- Receipts preserve the original schema and implementation identities; migration creates a new linked artifact rather than rewriting evidence.
- Standalone package APIs/CLIs remain useful without ANYai.
- No reverse dependency from owner packages to ANYai or its proprietary models is permitted.
- A capability pack declares required protocol/package/project ranges, evidence version, licences, standards/vendor rights, hardware support, and revocation state.
- Revoked/incompatible packs and models fail closed; there is no silent downgrade or cloud fallback.
- Current dirty worktrees are never implementation bases. Downstream plans freeze accepted SHAs and isolate changes in branches/worktrees.

## 12. Milestones and gates

| Milestone | Deliverable | Exit gate | Newly permitted work |
|---|---|---|---|
| M0 — This planning artifact | Complete registered plan and exact identity | Independent `ACCEPT` by ecosystem Boss | Separately planned audits only |
| M1 — Rights and dependency feasibility | File-level copyright/inbound ledger, dependency/model/content matrix, legal decision on target licensing model | Specialist review plus independent ecosystem acceptance | Licence migration plan may be drafted; no licence edit yet |
| M2 — Ownership and contract freeze | Canonical dependency ADR, protocol/safety/audit v0.1 schemas, compatibility policy, exact wedge contract | Owner-package and independent architecture/security acceptance | Model-free reference implementation may be separately planned |
| M2D — Problem and pricing discovery | **Pre-start user gate:** explicit authority for exact customer contact, interview/price-testing scope, script, data handling, owner, and stop conditions. Then preregistered interviews, synthetic workflow observations, randomized price cells, retained refusals and go/no-go evidence | User authorization plus independent commercial-evidence review; no customer files or production promise | Commercial hypothesis may be refined; no product authority |
| M3 — Model-free headless reference | Deterministic panel/cylinder workflow, synthetic fixtures, receipts, report, failure preservation | Independent engineering/security verification | Capability-pack qualification may be planned |
| M4 — Qualified buckling pack | Scope statement, reference/negative cases, evidence/report schema, limitations and rights record | Independent qualification acceptance | Local-model evaluation may be planned |
| M5 — Local-model evaluation | Frozen models/prompts, proposal/explanation metrics, hardware hypotheses, abuse evidence | Safety/engineering acceptance | GUIexpert GUX-0 may begin |
| M6 — UX/installer design | GUIexpert reviews plus accepted installer/security design | GUX-0 through GUX-3 and separate packaging authority | Prototype packaging may be planned |
| M7 — Paid design-partner pilot | **Pre-start user gate:** explicit authority for named offer scope, price/billing, build/service distribution, contracts, customer-data handling, support owner, and stop/withdrawal terms. Then an approved signed non-production build, synthetic/reference scope, and measured ROI/support | Explicit user authorization plus legal/security/engineering/GUX-4 acceptance | Only the exact authorized pilot; no broader sale or release |
| M8 — Commercial decision | Evidence-based tier, entitlement, support, LTS, liability, and go/no-go | Explicit user authority | Separate release/cloud/enterprise plans as applicable |

No milestone may be skipped because a demo appears successful. Every transition records exact artifact hashes, accepted limitations, and the reviewer independent of its author.

M2D and M7 are external-action gates, not ordinary internal milestones. Neither may start under ecosystem Boss standing authority alone. M8 remains the separate explicit user decision for any final commercial release, published offering, or broader distribution.

## 13. Verification and evidence program

### 13.1 Allowed planning verification now

Only read-only inventory, source/hash checks, document consistency checks, and final file-identity measurement are allowed. No test, import, build, download, network service, package, solver, or performance execution is required for this plan.

### 13.2 Future light verification categories

Exact commands, repositories, accepted SHAs, environments, and output locations must be frozen in downstream plans. Expected light checks include:

- schema validation and canonical serialization;
- unit and property tests for units, revisions, operation hashes, idempotency, approvals, and receipts;
- synthetic positive/negative wedge cases;
- deterministic report-to-result reconciliation;
- compatibility/version refusal tests;
- prompt-injection and unauthorized-capability tests using bounded fixtures;
- crash/rollback/audit-tamper tests that are not resource-heavy; and
- licence/SBOM/notice consistency checks.

The first failure is preserved. No retry, tolerance widening, output rewriting, or qualification broadening is inferred.

### 13.3 Anticipated PERF register — not authorized or executed

Every run below requires a separate exact plan and request through `C:\Github\.resource-manager\request-test.ps1`, an approval entry in `C:\Github\.resource-manager\ledger.md`, exclusive acquisition through `acquire-test.ps1`, execution of only the approved command/scope, and release in a `finally` path through `release-test.ps1`.

| PERF ID | Later purpose and measurements |
|---|---|
| PERF-01 | CPU-only and approved-GPU model profiles: cold load, first-token latency, throughput, peak RAM/VRAM, and fallback |
| PERF-02 | Context/resource sweep: latency, memory growth, truncation, cancellation, and OOM recovery with synthetic content |
| PERF-03 | Small/medium/large synthetic panel and cylinder wedge: stage/end-to-end wall time, peak RAM/disk, deterministic variance |
| PERF-04 | Proposed 8-hour or 100-cycle local soak: leaks, crashes, orphan processes, throttling, cancellation, and restart |
| PERF-05 | Installer/update/repair matrix: clean/upgrade/interrupted/disk-full/rollback/repair time, bandwidth, temporary disk, recoverability |
| PERF-06 | Serialized Windows hardware/backend matrix: driver/runtime identity, compatibility, CPU fallback, and diagnostic quality |
| PERF-07 | Enterprise concurrency, deferred until separately accepted enterprise scope: bounded throughput and isolation |

No command, dataset size, hardware claim, threshold, or ETA is approved by this inventory. Those values are preregistered with the later lease request.

## 14. Risks and stop conditions

| Risk | Severity | Blocking mitigation/exit |
|---|---|---|
| Copyright or dependency rights prevent the recommended dual licence | Critical | Complete file-level audit and counsel approval; otherwise use fallback model or exclude code |
| Incorrect engineering result or fabricated explanation | Critical | Deterministic owner authority, evidence-bound reports, independent validation, sign-off |
| AI prompt injection/excessive agency mutates project | Critical | Untrusted-model boundary, capability allowlist, revision-bound one-use approval, abuse tests |
| Model/runtime/update supply-chain compromise | Critical | Signed provenance manifests, separated keys, expiry/revocation, rollback/freeze protection |
| Confidential data leaves workstation | Critical | Network-denied Local Private mode, packet-capture evidence, diagnostic redaction; cloud remains a separate plan |
| Report is mistaken for certification | Critical | Explicit limitations, evidence manifest, named engineer/checker sign-off, no AI approval |
| Standards/model/vendor content is unlicensed | High | Per-artifact rights record; exclude until approved; never acquire under this plan |
| Package/protocol/project drift breaks reproducibility | High | Compatibility handshake, pinned versions, fail-closed mismatch, immutable receipts |
| Windows/hardware fragmentation defeats one-click use | High | Supported matrix, CPU fallback, installer/repair gates and later serialized PERF |
| Price is too low for support burden or too high for demand | High | Preregistered price cells, paid pilots, support/unit-economics evidence before publication |
| Demand requires broad CAD or general FEA | High | Enforce wedge exclusions; rescope or stop rather than silently expand |
| Product-security/privacy/liability duties are misclassified | High | Current specialist review before pilot and each release |
| Ecosystem worktrees drift during the program | High | Re-freeze clean accepted SHAs in each downstream plan; never consume dirty state silently |
| Key-person dependency | Medium | Recorded ownership, release/recovery runbooks, independent review, contributor policy |

Immediate stop conditions are unresolved proprietary rights, inability to reproduce the owner result, any LLM bypass of deterministic controls, customer value dependent on excluded content, local privacy failure, or an unsupported certification expectation.

## 15. Definition of done for this planning milestone

This plan is ready for independent review only when:

- the exact source path, bytes, and SHA-256 are recorded and match;
- the registered plan path, repository state, owned path, and exclusions are explicit;
- current licence evidence, audit limitations, target models, recommendation, fallback, and migration gates are stated;
- canonical repository ownership and dependency direction are unambiguous;
- protocol/safety/audit v0.1 records, lifecycle, permissions, and first-wedge surface are specified;
- the panel/cylinder wedge has exact inclusions, exclusions, flow, and downstream DoD;
- model/installer/update threats, abuse cases, controls, and future evidence are defined;
- customer segments, discovery method, price hypotheses, thresholds, and stop rules are preregistered;
- GUIexpert appears only after headless contract freeze;
- migration/compatibility, verification, risks, and anticipated PERF work are explicit;
- no prohibited implementation or external action occurred; and
- an independent reviewer receives the exact final bytes/LF/CR/BOM/SHA-256 identity and returns `ACCEPT` or material bounded changes.

## 16. Acceptance packet and next authorized milestone

The completion request must report only:

1. registered absolute path;
2. exact bytes, LF count, CR count, BOM state, and SHA-256;
3. source identity;
4. planning repository branch/base and dirty-state preservation;
5. the recommended licensing path and unresolved legal gates;
6. canonical ownership and protocol/safety boundary;
7. wedge scope and DoD;
8. migration/compatibility and verification gates;
9. highest risks and stop conditions;
10. anticipated PERF inventory and confirmation that none ran; and
11. confirmation that no product, licence, GUI, cloud, marketplace, packaging, publication, licensed-content, customer, model-download, or commercial action occurred.

After independent acceptance, the next authorized milestone is **M1 planning and read-only rights/dependency audit only**. It requires its own exact registered plan, disjoint ownership, clean base identities, specialist review questions, and completion packet. This document grants no authority to change licences or implement the product.
