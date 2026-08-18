# ANYai M1 Specialist Review Questions

Date: 2026-08-14 (Europe/Oslo)

Status: **QUESTION PACKET ONLY — no specialist or external party contacted**

## 1. Use of this packet

These are bounded decisions required before later commercial execution. They do not ask the reviewer to approve a repository in the abstract. Each answer must identify:

- the exact repository, commit, path/range, dependency artifact, or content edition reviewed;
- relied-on documentary evidence and assumptions;
- permitted and prohibited distribution models;
- surviving notices, attribution, source/source-offer, relinking, patent, trademark, data-use, export, and end-user obligations;
- required remediation; and
- the reviewer, date, scope, and expiry/revisit condition.

References use natural keys from the two M1 CSVs, for example `RP[ANYbuckling:prescriptive/plates.py]` and the `DM[PROGRAM:standards_content]` row.

No question has been sent and no external contact is authorized by M1.

## 2. Software copyright and licensing counsel — P0

1. **Identity and authority.** Do `audunarn@gmail.com`, `audun@pm.me`, and historical `root <q1w2e3>` represent the same legal rights holder, and what assignment/employment/commissioning documents establish authority over each surviving range? Evidence: `RP[ANYstructure:42 full committed files selected by exact q1w2e3 blame predicate; 23 text-like files and 19 image/icon files]`, all newer-repository shortlogs.

2. **Named third-party contributions.** What rights and notice obligations govern the 88 surviving `theScriptingEngineer` lines contributed while ANYstructure displayed MIT terms, and are separate permissions needed for commercial licensing? Evidence: `RP[ANYstructure:anystruct/main_application.py listed 88 lines]`, commits `9f1e5a1…`, `40a6ac0…`.

3. **Historical licence sequence.** How must ANYstructure's GPL-to-MIT-to-GPL history be represented per file/range, and which prior MIT grants, copyright notices, and permission notices survive? Evidence: `RP[ANYstructure:LICENSE]`, commit `83cdadf7…` and parent.

4. **Local agent identities.** Who legally supplied and owns the Eir and Liv ranges, under which service/account terms, and may those exact ranges be offered under both GPL and a commercial licence? Evidence: the two `RP[ANYfileio-occt:…]` agent rows and commits `76706335…`, `c569b0ac…`, `23b441c3…`.

5. **Vibe contribution.** What Mistral/Vibe terms applied to the 15 `Vibe Nuage Agent <vibe@mistral.ai>` commits on their generation dates; what human contribution and review occurred; and who may license those outputs? Evidence: `RP[ANYintelligent:19 full committed files selected by Vibe author/blame predicate]` and `M1_EVIDENCE_REPORT.md` section 5.3.

6. **Claude, GPT, and Codex assistance.** For each Claude co-author trailer, GPT-labelled sweep, and deterministic Codex-associated history set, what service/account terms, human authorship, commissioning, attribution, and disclosure evidence is needed before commercial licensing? Evidence: agent-associated rows for ANYsolver, ANYbuckling, ANYstructure, ANYtk3D, ANYtimeseries, and ANYgeometry.

7. **Curated transfers.** Is the documented file mapping in the migration notes sufficient when combined with original histories, and what exact additional evidence is required to offer transferred ANYgeometry, ANYmesh, ANYmaterial, ANYfileIO, ANYsolver, ANYbuckling, and ANYtk3D ranges commercially? Evidence: every `RP` migration/source-tree row.

8. **ANYfem authority.** What affirmative documents are needed to move `RP[ANYfem:src/anyfem/**]` from `CONDITIONAL` to a commercial grant when Git discovery shows only Audun aliases but there is no CLA/assignment ledger?

9. **Dual-licence mechanics.** For each cleared owner package, may unchanged code be offered simultaneously under public GPL and a separate commercial licence; who must consent; and what release manifest must bind a customer to the exact commercially licensed bytes?

10. **Public GPL preservation.** What notices and access commitments are required to ensure historical tags/releases and existing recipients' GPL rights remain unaffected by future dual licensing?

11. **Contributor policy.** What CLA or equivalent inbound agreement should grant both GPL-publication and commercial-licensing authority, address patents and moral rights where applicable, and record AI assistance? Is a DCO useful but insufficient for this target?

12. **Clean replacement.** What process and evidence would make a later replacement sufficiently independent from uncleared GPL/agent-generated implementation, while respecting standards access, patents, trade secrets, and interoperability rights? Evidence: all `REPLACE_CLEANLY` alternatives in the classification report.

13. **Process boundary.** For the exact future protocol semantics, deployment, installation, data structures, and lifecycle, would proprietary ANYai plus GPL workers likely be separate programs or one combined work? Which coupling changes the answer? No conclusion may rely solely on IPC.

14. **Root GPL application.** Does the plain GPLv3 text used by ANYopenSoft and ANYfileio-occt adequately state the project grant/version option, or is a project application notice required before another distribution? Evidence: their `LICENSE` and package metadata rows.

15. **No-root-licence repository.** Confirm that ANYintelligent cannot be distributed or used as an inbound source without separate authority, and define the evidence required even for a clean migration reference.

## 3. Standards, technical content, and data counsel — P0

16. **Governing prescriptive calculations.** For the exact ranges `ANYbuckling:prescriptive/plates.py` and `cylinders.py`, what material citing DNV-RP-C201/C202, DNV-OS-C101/DNVGL-OS-C101, DNVGL-RU-SHIP Pt.3 Ch.3 (July 2017), and unspecified DNVGL sheets may be implemented and distributed commercially—including formulas, coefficient tables, sheet-derived factors, labels, applicability language, edition references, examples, and report wording? Evidence: `RP[ANYbuckling:prescriptive/plates.py; cylinders.py]`, `DM[PROGRAM:standards_content]`.

17. **Edition and sheet control.** What standard edition/corrigenda identifiers, exact DNVGL-sheet provenance, and customer access assumptions must be recorded so a supported envelope is reproducible without redistributing protected standards or sheets?

18. **C208 table.** May the 17 rows in `dnv_rp_c208.json` be reproduced in software; if so under what licence, attribution, access control, and update rules? Evidence: `RP[ANYmaterial:dnv_rp_c208.json]`.

19. **Mixed material library.** For each source range in `materials.json`, distinguish public facts, copyrightable selection/expression, licensed supplier/NCAMP content, calculated values, and CC-BY-4.0 derivatives. What may be shipped and what attribution/change record is required? Evidence: the three `RP[ANYmaterial:materials.json]` rows, including the separately classified NCAMP attribution at line 488.

20. **Section-profile table.** Identify the source and rights for `bulb_anglebar_tbar_flatbar.csv`. May it be distributed, or must the wedge accept explicit user-entered section properties instead? Evidence: `RP[ANYbuckling:…csv]`.

21. **PULS/CSR material.** Confirm that PULS workbook/manual-derived logic, S3/U3 governing claims, CSR coefficients, training CSVs, and locally referenced manuals remain excluded absent explicit licences. Define whether any non-expressive compatibility behavior may be retained. Evidence: PULS/S3-U3 rows in both ledgers.

22. **Customer/company-labelled paths.** Do OKEA-labelled paths or hard-coded project/location data create confidentiality, personal-data, or trade-secret concerns even when the referenced files are absent? What source-code remediation is required before any later publication? Evidence: `DM[ANYbuckling:three OKEA OneDrive inputs]`, `DM[ANYtimeseries:asset_data_set]`.

23. **Reference cases and outputs.** What rights apply to analytical values, benchmark baselines, generated reports, and optional CalculiX example sources? How must independent qualification evidence avoid redistributing protected examples? Evidence: ANYsolver and ANYintelligent reference/evidence rows.

24. **QATS bundle.** Identify the exact QATS upstream version/commit, licence, contributors, NOTICE, modification history, and DNV/QATS mark obligations for `ANYtimeseries:anyqats/**`. May any range remain under the root MIT notice as presently packaged?

25. **Model/training lineage.** What permissions, consent, documentation, and reproducibility evidence would be required for the 56 ANYstructure pickle models and absent PULS/CSR training data? Confirm exclusion is sufficient for the first wedge.

## 4. Open-source dependency and distribution counsel — P0/P1

26. **Exact-artifact method.** What fields and evidence must the later wheel/native SBOM contain to support a Windows offline installer: hashes, SPDX expressions, copyright, notices, source correspondence, source offers, relinking/install information, patents, ABI, and platform provenance?

27. **Internal graph.** After engineering selects compatible package versions, what licence/notice evidence must accompany each local wheel, and can CI `--no-deps` installs be used only as development evidence rather than resolver compatibility? Evidence: the five conflicts in `RELICENSING_CLASSIFICATION.md` section 5.3.

28. **Gmsh.** For an exact selected Gmsh artifact, which GPL or commercial route would permit the proposed closed distribution and what source/notice obligations would apply? Confirm exclusion avoids this question for the first wedge.

29. **OCP/OCCT.** For an exact `cadquery-ocp-novtk` wheel, enumerate binding and native OCCT licences, exceptions, notices, source/relinking duties, and supported platforms. Evidence: `DM[ANYfileio-occt:cadquery-ocp-novtk]`.

30. **Qt/PySide.** For any later GUI, compare a compliant LGPL route with commercial Qt licensing, including relinking, installation information, QtWebEngine/Chromium notices, and platform libraries. Confirm PySide/Qt remains outside the headless wedge.

31. **Numerical/native stack.** For the exact future CPython, NumPy, SciPy, BLAS/LAPACK/OpenMP, HDF5/h5py, Shapely/GEOS, Numba/LLVM, and platform runtime builds, which notices, source terms, patents, and redistributables apply?

32. **PARDISO/MKL.** What Intel MKL and pypardiso terms apply to an exact artifact, and is exclusion the safest first-wedge decision? Evidence: `DM[ANYsolver:pypardiso]`.

33. **IfcConvert/IfcOpenShell.** Identify the exact bundled executable version/build, upstream licence, notices, source correspondence and source-offer duties. Confirm that the current unversioned binary must not be redistributed. Evidence: `DM[ANYstructure:IfcConvert.exe]`.

34. **xlwings/Excel.** Distinguish open and Pro features, Excel prerequisites, automation rights, and redistribution constraints for exact future artifacts. Confirm no xlwings/Excel/PULS path enters the first wedge.

35. **Fonts, icons, and marks.** What licences and local notices apply to any selected fonts/icons? Confirm the current remote Google Fonts service should not be a dependency of an offline product.

36. **Source-offer model.** If any GPL component is distributed alongside a proprietary application, what exact corresponding source, written offer, installation information, relinking facility, and notice package is required for the selected distribution model?

## 5. Trademark specialist — P1

37. Who owns or may register `ANY`, `ANYopenSoft`, `ANYai`, package names, logos, and ANYstructure marks, and what evidence is required before commercial branding?

38. What wording permits referential use of DNV, PULS, QATS, OrcaFlex, SESAM, CalculiX, OCCT/OCP, Qt, Excel, and other third-party marks without implying certification, affiliation, endorsement, or equivalence?

39. Which product/result statements are prohibited or need qualification, including “DNV certified”, “PULS equivalent”, “qualified”, and general buckling claims outside the named envelope?

## 6. Security, model, privacy, and product specialists — P1

40. **Local model/runtime.** Before selection, what licence, training-data, acceptable-use, telemetry, vulnerability, export-control, model-card, tokenizer, and commercial-use fields must a per-artifact manifest contain? Evidence: `DM[PROGRAM:local LLM runtime]` and `DM[PROGRAM:LLM model and tokenizer]`.

41. **Supply chain.** What signing, key separation, revocation, rollback/freeze protection, sandboxing, update metadata, vulnerability disclosure, and incident response are required for an offline Windows model/runtime/update chain?

42. **Untrusted artifacts.** Confirm security controls for model files, HDF5/JSON/project files, relative artifact paths, reports, and any future plugin/provider. Confirm pickle models and arbitrary Python/shell dispatch remain prohibited.

43. **Customer data.** Before any separately authorized pilot, what lawful basis, contract, retention/deletion, access control, encryption, support-log, subprocess, incident, cross-border, and data-subject provisions are required? Evidence: `DM[PROGRAM:customer files,projects,reports,telemetry]`.

44. **Engineering product liability.** What disclaimers, professional-review gates, limitation-of-liability terms, evidence retention, qualification labels, and jurisdiction-specific duties are required for a buckling assessment workbench?

45. **Export and sanctions.** Do local AI models, encryption, engineering analysis, standards content, or customer jurisdictions trigger export-control, sanctions, or end-use restrictions?

## 7. Tax and commercial specialists — P1 before external activity

46. Before interviews or price tests, which research consent, confidentiality, incentive, recordkeeping, and competition/marketing rules apply? External contact requires a fresh explicit user gate.

47. Before a pilot offer or billing, which entity, VAT/sales-tax, merchant-of-record, invoicing, refund, warranty, consumer-versus-enterprise, subscription/entitlement, and accounting rules apply? Pilot offers, billing, build distribution, and customer-data handling require a separate explicit user gate.

48. What contract structure preserves access to the last licensed version, distinguishes software entitlement from support/updates, and states third-party/licensed-content exclusions?

## 8. Required answer format and stop rule

Each answer must be recorded against the relevant ledger natural key and must result in one controlled disposition:

- `CLEAR_FOR_DUAL` only with affirmative documentary evidence and specialist scope;
- `CONDITIONAL` with named remaining evidence;
- `KEEP_EXISTING` with surviving obligations;
- `REPLACE_CLEANLY` with an accepted clean-process record;
- `EXCLUDE`;
- `NEEDS_SPECIALIST`; or
- `UNKNOWN` with no distribution decision permitted.

Silence, missing evidence, Git dominance, package metadata, or an AI provider's general marketing statement cannot promote a row. Until answers are received under separate authority, the M1 classifications remain fail-closed.
