# ANYfileIO M1 Classified Consequence Manifest

Status: **M1 inventory only; no implementation/metadata edit authorized by this artifact**  
Parent plan: `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_REPOSITORY_RENAME_PLAN.md`  
Registered parent-plan SHA-256: `BCC54B83774C2ED90775026183BE189A06E15411D178C9E3029F066ABE9A9A4C`  
Inventory owner: Forseti  
Snapshot date: 2026-08-12 (Europe/Oslo)

## 1. Scope, method, and classification rules

This is the exact M1 edit/allowlist manifest requested by the ecosystem Boss. It
does not change package source, repository metadata, remotes, CI, documentation,
or external services.

The scan covered all Git-tracked text in these repositories, using the current
worktree for tracked files so existing uncommitted user content was not hidden:

`ANYfileIO`, `ANYio`, `ANYopenSoft`, `ANYsolver`, `ANYfem`, `ANYstructure`,
`ANYmesh`, `ANYmaterial`, `ANYgeometry`, `ANYbuckling`, `ANYintelligent`,
`ANYtimeseries`, `ANYtk3D`, `ANY3dView`, and `ANYfileio-occt`.

It also covered the untracked-but-governing files under
`C:\Github\ANYopenSoft\governance`. A broad separator/case scan found no missed
hyphenated, underscored, dotted, spaced, or `I/O` spelling variant. `.git/**`,
build outputs, caches, bytecode, environments, and unrelated generated/untracked
data are not source inventory. A text scan of 1,435 untracked candidate files in
the listed repositories found no additional hit outside the six governance
files; the two governance source files and registered parent plan are classified
below. This manifest itself is necessarily excluded from its own input snapshot.

Each occurrence has exactly one classification:

- **R — active repository identity:** canonical `ANYfileIO`, former `ANYio`, an
  old/current repository URL or checkout path, or a portal-internal repository
  key. R may be either preserve (canonical/intentional governance record) or edit
  (former active identity).
- **D — PyPI distribution/product identity:** exact `ANYfileio`; preserve during
  this repository-only migration.
- **I — Python import/CLI identity:** exact `anyfileio`, including source package
  paths, module imports, console scripts, and lowercase package keys; preserve.
- **T — unrelated third-party async `anyio`:** exact lowercase `anyio` only where
  context proves the external package/collision contract; preserve.
- **H — immutable historical evidence:** a naming occurrence inside a completed
  performance/qualification report whose original path/name is provenance;
  preserve without textual rewriting. H overrides the token's ordinary R/D/I
  classification inside the named evidence file.

Lowercase spelling alone is not classification. In particular, `anyio` in the
ANYopenSoft portal is an R internal repository key and must not be mistaken for T.

## 2. Repository and overlap snapshot

Revalidate every row immediately before any later edit; active tasks may advance
branches after this snapshot.

| Repository | Branch / HEAD | Base / origin | Relevant state and risk |
| --- | --- | --- | --- |
| `C:\Github\ANYfileIO` | `main` / `82a0f5f110361fcd902cd3aac5d4c6beeaa187fa` | `origin/main`; `https://github.com/audunarn/ANYfileIO.git` | Clean, 37 tracked files, no untracked/ignored files. Canonical M2 source. CRLF files require hunk-minimal patching. |
| `C:\Github\ANYio` | `main` / same HEAD and tree `e8cfb6f37cc1ca0231f9c45cb3967fa62f54422b` | `origin/main`; `https://github.com/audunarn/ANYio.git` | Clean tracked tree and normalized content identical to canonical; frozen/void. It has 42 ignored IDE/bytecode artifacts and checkout EOL differences. Never edit or validate from this copy. |
| `C:\Github\ANYopenSoft` | `main` / `7d29eaef1c899fc56681a723184c97e2ed04abb0` | `origin/main` | Dirty relevant files: `README.md`, `app.js`, `index.html`; also dirty `styles.css`, `.idea/ANYopenSoft.iml`, untracked `assets/` and governance. **Direct overlap risk is high**; portal owner/user must approve exact hunks. |
| `C:\Github\ANYsolver` | `native_hybrid_mesher` / `7daa6e8c61954cfc1bc4469457fef0db154d3375` | `origin/main` | Clean, but branch belongs to active native-hybrid work. Path-only patch waits for owner handoff/integration tip. |
| `C:\Github\ANYfem` | `native_hybrid_mesher` / `b17f1d47ba79e5c04692301e96d23dd5ac5627cb` | `origin/main` | Dirty implementation/tests from active work. Proposed rename targets are clean; `src/anyfem/ui/app.py` is dirty but contains only preserved D/I hits and must not be touched. |
| `C:\Github\ANYstructure` | `clean-up-after-external` / `4a79b860739c2f0b24f61314d4c13d943886bdd3` | `origin/master` | Only untracked `.claude/`; proposed target files are clean. Base is `master`, unlike the other consumers. Coordinate with owner. |
| `C:\Github\ANYmesh` | `native_hybrid_mesher` / `97058e0a1213ba7f0da506ff1a00d4ef10093d20` | `origin/main` | Heavily dirty active compiled/native work, including `setup.py`; the sole active rename target `README.md` is clean. Historical reports are H. Resolver/version work is owner-controlled and excluded. |
| `C:\Github\ANYmaterial` | `main` / `4626887667f4c251479d26f321b9e73b046a2783` | `origin/main` | Clean; no edit proposed. |
| `C:\Github\ANYgeometry` | `native_hybrid_mesher` / `37234b7bc6b6c3f2e02cf1c53acb875245d9c3aa` | `origin/main` | Dirty/untracked but zero tracked naming hits; no edit. |
| `C:\Github\ANYbuckling` | `main` / `3fe06c9ea126fcd59f2cd0ce825a029540b479e9` | `origin/main` | Untracked IDE state; zero tracked hits; no edit. |
| `C:\Github\ANYintelligent` | `move_solver` / `a1f58f3488e6a250fa0ce5b189fbfc8f658415ff` | `origin/main` | Large unrelated untracked archive/data state; zero tracked hits and zero untracked text hits; no edit. |
| `C:\Github\ANYtimeseries` | `main` / `c578e910fd9d1ea481b4fae144a75bd66549beaf` | `origin/main` | Unrelated dirty state; zero tracked/untracked text hits; no edit. |
| `C:\Github\ANYtk3D` | `main` / `0f49efc53670c601bbabc012d856cc8ca18dcc9b` | `origin/main` | Unrelated dirty state; zero tracked/untracked text hits; no edit. |
| `C:\Github\ANY3dView` | `main` / `cd2098dd55f12a60ea7ccbe9379989ef84933ae5` | `origin/main` | Clean; zero hits; no edit. |
| `C:\Github\ANYfileio-occt` | `main` / `571231dc4c7d8b4131daac6b719a6b93125a20b4` | `origin/main` | Clean, zero hits, distinct repository; explicitly excluded. |

ANYsolver also has 24 registered secondary worktrees (`analysis-session`,
`baseline`, `corotational`, `damage-matrix`, `docs`, `functional-merge`, `hill48`,
`impact`, `impact-reduced`, `integration`, `numerical-baseline`, three
`qualification-*` trees, `recovery`, `s4-baseline-61e2f45`, four active S4 trees,
`shell-batches`, `state-storage`, `thread-scaling`, and `verification`). They
contain inherited copies of the same active URL/path references. They are not 24
independent edit targets: land one owner-approved migration commit and merge or
cherry-pick it only into surviving branches. Captured JSON/report paths and
registered S4 plan/addendum/proposal content remain immutable evidence.

## 3. Exact proposed edit manifest

Line numbers describe the snapshot above. Each later patch must match content,
not assume a line number still applies.

### 3.1 Canonical `ANYfileIO` — Forseti, proposed branch
`codex/anyfileio-repository-rename` from registered `main`

| File:line | Class | Exact proposed edit |
| --- | --- | --- |
| `pyproject.toml:6` | R | `The repository is ANYio` -> `The repository is ANYfileIO`; preserve the adjacent third-party `anyio` rationale. |
| `pyproject.toml:57` | R | Homepage URL -> `https://github.com/audunarn/ANYfileIO`. |
| `pyproject.toml:58` | R | Repository URL -> `https://github.com/audunarn/ANYfileIO`. |
| `pyproject.toml:59` | R | Issues URL -> `https://github.com/audunarn/ANYfileIO/issues`. |
| `README.md:11` | R | Repository display -> `ANYfileIO`; preserve lowercase external `anyio`. |
| `README.md:137` | R | Editable path -> `C:\Github\ANYfileIO[dev]`. |
| `tests/test_packaging.py:44` | R | Comment repository display -> `ANYfileIO`; preserve lowercase external `anyio`. |

Proposed same-owner enforcement (new line, not an existing hit): extend
`tests/test_packaging.py` to assert the three canonical project URLs exactly.
This is a metadata guard, not a runtime/API change.

### 3.2 `ANYopenSoft` portal/governance — portal owner plus Boss; current dirty
`main` only after exact-hunk overlap approval

| File:line(s) | Class | Exact proposed edit |
| --- | --- | --- |
| `README.md:27` | R | Link label `ANYio` -> repository display `ANYfileIO`; URL -> `https://github.com/audunarn/ANYfileIO`. |
| `app.js:258,524,543` | R | Internal portal key/id/edge `anyio` -> `anyfileio` as an atomic internal-key migration. |
| `app.js:259,525` | R | Repository title/label `ANYio` -> `ANYfileIO`. |
| `index.html:91,422` | R | `data-pkg="anyio"` -> `data-pkg="anyfileio"`; update matching tab label at line 91 to `ANYfileIO`. |
| `index.html:421,424` | R | Comment/title `ANYio` -> `ANYfileIO`. |
| `index.html:437` | R -> D | Incorrect `pip install ANYio` -> distribution command `pip install ANYfileio`; this must not become `pip install ANYfileIO` until the separate display-casing decision. |
| `index.html:438` | R | Link -> `https://github.com/audunarn/ANYfileIO`. |
| `index.html:648,660` | R | Local path `C:\Github\ANYio` -> `C:\Github\ANYfileIO` in both copy payload and visible command. |
| `governance/ECOSYSTEM_PHILOSOPHY.md:11` | R + D | Former repository half `ANYio/ANYfileio` -> `ANYfileIO/ANYfileio`; distribution half remains unchanged. Boss-owned governance edit. |

Do not patch these dirty portal files without the user/portal owner: current diffs
are substantial (`README.md` +13/-12, `app.js` +281/-126, `index.html`
+278/-264), and all target hunks lie inside those user changes.

### 3.3 `ANYsolver` — repository owner/Forseti handoff; current active branch
`native_hybrid_mesher`, eventual isolated rename branch from the accepted
integration tip

| File:line(s) | Class | Exact proposed edit |
| --- | --- | --- |
| `.github/workflows/ci.yml:15` | R | VCS sibling URL -> `git+https://github.com/audunarn/ANYfileIO`. |
| `.github/workflows/ci.yml:59-60` | R | Checkout pair -> `repository: audunarn/ANYfileIO`, `path: .ecosystem/ANYfileIO`. |
| `.github/workflows/ci.yml:75` | R | Matching clean-wheel target path -> `.ecosystem/ANYfileIO`. |
| `README.md:21` | R | Editable path -> `C:\Github\ANYfileIO`. |

All four workflow replacements land atomically so checkout and install paths
cannot diverge. The canonical R occurrence at `tests/test_sesam_fem.py:1`
(`ANYfileIO-to-ANYsolver`) is already correct and is preserved.

### 3.4 `ANYfem` — repository owner/Forseti handoff; current active branch
`native_hybrid_mesher`, eventual isolated rename branch from the accepted
integration tip

| File:line(s) | Class | Exact proposed edit |
| --- | --- | --- |
| `.github/workflows/tests.yml:42-43,113-114` | R | Both checkout pairs -> `audunarn/ANYfileIO` and `.ecosystem/ANYfileIO`. |
| `.github/workflows/tests.yml:59,141` | R | Both install paths -> `.ecosystem/ANYfileIO`. |
| `README.md:16` | R + D | Preserve label `ANYfileio`; change only URL -> `https://github.com/audunarn/ANYfileIO`. |
| `README.md:99` | R | Editable path -> `C:\Github\ANYfileIO`. |
| `run_gui.py:17` | R | Sibling source directory -> `"ANYfileIO"`. |
| `tests/test_migration.py:106` | R | Clean-interpreter sibling source directory -> `"ANYfileIO"`. |

The checkout/path edits are atomic across both jobs. `src/anyfem/ui/app.py` is
dirty but its lines 1829/1831 are valid D/I and receive no rename patch.

### 3.5 `ANYstructure` — repository owner/Forseti handoff; active branch
`clean-up-after-external`, base `origin/master`

| File:line(s) | Class | Exact proposed edit |
| --- | --- | --- |
| `.github/workflows/tests.yml:43-44,118-119` | R | Both checkout pairs -> `audunarn/ANYfileIO` and `.ecosystem/ANYfileIO`. |
| `.github/workflows/tests.yml:61,136,157` | R | All corresponding editable/clean-wheel paths -> `.ecosystem/ANYfileIO`. |
| `.readthedocs.yaml:19` | R | VCS URL -> `git+https://github.com/audunarn/ANYfileIO.git`. |
| `README.md:70` | R | Editable path -> `C:\Github\ANYfileIO`. |
| `README.md:79` | R | Repository list member `ANYio` -> `ANYfileIO`; preserve distribution wording on adjacent line. |
| `docs/install.rst:23` | R | Editable path -> `C:\Github\ANYfileIO`. |
| `run_gui.py:17` | R | Sibling source directory -> `"ANYfileIO"`. |
| `tests/test_ecosystem_integration.py:266` | R | Workflow assertion -> `repository: audunarn/ANYfileIO`. |

### 3.6 `ANYmesh` — native-hybrid owner/Forseti handoff; active branch
`native_hybrid_mesher`, no resolver or compiled-source edit

| File:line | Class | Exact proposed edit |
| --- | --- | --- |
| `README.md:167` | R + D | Preserve link label `ANYfileio`; change only URL -> `https://github.com/audunarn/ANYfileIO`. |

No other package/implementation/release file in ANYmesh is a rename target.

## 4. Exact preserve inventory (every non-H tracked hit)

Comma-separated numbers are exact snapshot line numbers. A line can contain more
than one occurrence; the category is per occurrence. The canonical and old
checkouts have identical normalized tracked content, so section 4.1 classifies
both by a one-to-one path mapping. The old checkout is not a second edit target.

### 4.1 Canonical `ANYfileIO` and frozen mirror `ANYio`

There are 109 occurrences per checkout: 7 R edit occurrences (section 3.1),
26 D, 65 I, and 11 T. No H.

**D — preserve `ANYfileio` (26):**

| File | Lines |
| --- | --- |
| `.github/workflows/publish.yml` | 47, 65 |
| `CHANGELOG.md` | 91 |
| `MIGRATION.md` | 1, 3, 48, 114 |
| `README.md` | 1, 8, 14, 120, 142 |
| `docs/ARCHITECTURE.md` | 7, 13 |
| `pyproject.toml` | 9, 10, 40 |
| `run_gui.py` | 2 |
| `src/anyfileio/calculix/deck.py` | 434 |
| `src/anyfileio/gui.py` | 431, 452 |
| `tests/test_calculix.py` | 423, 427 |
| `tests/test_layering.py` | 3, 84 |
| `tests/test_packaging.py` | 49 |

**I — preserve `anyfileio` (65):**

| File | Lines |
| --- | --- |
| `.github/workflows/ci.yml` | 34, 53 (two occurrences), 54, 73, 74 |
| `CHANGELOG.md` | 40, 41, 61 |
| `MIGRATION.md` | 13-24, 110, 120-127 |
| `README.md` | 14, 19, 62, 70, 78 |
| `pyproject.toml` | 9, 50 (two), 54 (two), 66 |
| `run_gui.py` | 34 |
| `src/anyfileio/__init__.py` | 22 |
| `src/anyfileio/__main__.py` | 3 (two), 185 |
| `src/anyfileio/gui.py` | 13 |
| `src/anyfileio/sesam/__init__.py` | 3, 5, 6 |
| `tests/test_calculix.py` | 11, 23 |
| `tests/test_formats_and_cli.py` | 9, 18 |
| `tests/test_gui.py` | 61, 209, 223 |
| `tests/test_layering.py` | 21 |
| `tests/test_packaging.py` | 14, 40, 50, 82 |
| `tests/test_sesam.py` | 8 |

All 19 tracked paths under `src/anyfileio/**` are also I path identity and remain
unchanged.

**T — preserve external async `anyio` (11):**

| File | Lines and role |
| --- | --- |
| `.github/workflows/ci.yml` | 39, 42, 52, 53 (two), 54 (two): coexistence job/install/import/negative assertion. |
| `pyproject.toml` | 6: collision rationale. |
| `README.md` | 11: collision rationale. |
| `tests/test_packaging.py` | 44, 51: collision rationale and absence of `src/anyio`. |

The line-6/11/44 R text on the same lines is still edited as specified; the T
substrings remain byte-for-byte.

### 4.2 `ANYopenSoft` and governance

All 16 tracked portal occurrences are R and are listed in section 3.2; none is T.
The following governing occurrences are intentional and preserved/allowlisted:

| File | R | D | I | T | Treatment |
| --- | --- | --- | --- | --- | --- |
| `governance/ECOSYSTEM_LEDGER.md` | lines 12-13 (canonical), line 12 (former void name) | 12 | 12 | none | Preserve as active transition state/source authority. |
| `governance/plans/ANYFILEIO_REPOSITORY_RENAME_PLAN.md` | canonical: 1,7,12,29,31,46-48,58,70,100,138,151,165,191,199,226,250; former: 6,8,14,26,28,46,49,71,109,120,165,189,193,198,229,253,270,342 | 32,50,58,60,80,126,148,255,346 | 33,50-52,120,148,255 | 15,34,53,79,110,120,127,172,193,203,220,255,272,277,319,321 | Preserve registered governing contract. Some lines carry more than one class. |
| `governance/ECOSYSTEM_PHILOSOPHY.md` | 11 former | 11 | none | none | R half is an edit target in section 3.2; D half preserved. |

### 4.3 `ANYsolver`

There are 79 tracked occurrences: 6 R (five edits plus one already-canonical
preserve), 33 D, 25 I, and 15 H.

**D — preserve (33):**

| File | Lines |
| --- | --- |
| `.github/workflows/publish.yml` | 21 |
| `CHANGELOG.md` | 28 |
| `MIGRATION.md` | 45 |
| `README.md` | 31, 37, 103, 105, 117 |
| `docs/QUALITY_CONTROL.md` | 27 |
| `pyproject.toml` | 31 |
| `scripts/benchmark_sol_ultra_performance.py` | 365, 372 |
| `scripts/compare_sol_ultra_performance.py` | 228 |
| `scripts/verify_sol_ultra_numerics.py` | 219 |
| `src/anysolver/__init__.py` | 9, 788 |
| `src/anysolver/external_references.py` | 130, 235 |
| `src/anysolver/reference_cases.py` | 209, 215, 221 |
| `src/anysolver/sesam_fem/__init__.py` | 1 |
| `src/anysolver/sesam_fem/__main__.py` | 1 |
| `src/anysolver/sesam_fem/diagnostics.py` | 1 |
| `src/anysolver/sesam_fem/document.py` | 1 |
| `src/anysolver/sesam_fem/exporter.py` | 1 |
| `src/anysolver/sesam_fem/importer.py` | 1, 37, 107 |
| `src/anysolver/sesam_fem/records.py` | 1 |
| `src/anysolver/sesam_fem/schema.py` | 1 |
| `src/anysolver/sesam_fem/sif_importer.py` | 1 |
| `src/anysolver/sesam_fem/validation.py` | 1 |

**I — preserve (25):**

| File | Lines |
| --- | --- |
| `.github/workflows/ci.yml` | 87 |
| `MIGRATION.md` | 31 |
| `scripts/benchmark_sol_ultra_performance.py` | 372 (module import/provenance key) |
| `scripts/verify_sol_ultra_numerics.py` | 219, 2400, 2596 |
| `src/anysolver/external_references.py` | 25 |
| `src/anysolver/reference_cases.py` | 28 |
| `src/anysolver/sesam_fem/diagnostics.py` | 3 |
| `src/anysolver/sesam_fem/document.py` | 3 |
| `src/anysolver/sesam_fem/exporter.py` | 3 |
| `src/anysolver/sesam_fem/importer.py` | 8, 15, 16 |
| `src/anysolver/sesam_fem/records.py` | 3 |
| `src/anysolver/sesam_fem/schema.py` | 3 |
| `src/anysolver/sesam_fem/sif_importer.py` | 3 |
| `src/anysolver/sesam_fem/validation.py` | 3 |
| `tests/test_extracted_package_wiring.py` | 5, 31-36 (line 30 is a function name containing lowercase characters but no boundary-exact import token) |

R preserve: `tests/test_sesam_fem.py:1` already says `ANYfileIO`.

### 4.4 `ANYfem`

There are 34 tracked occurrences: 10 R edits, 17 D, 7 I, no T/H.

**D — preserve (17):** `README.md:16`; `docs/ARCHITECTURE.md:13,24`;
`pyproject.toml:32`; `src/anyfem/io/decks.py:4,72,79`;
`src/anyfem/io/results.py:5`; `src/anyfem/io/sesam.py:220,498`;
`src/anyfem/parity.py:295,301,307,311`; `src/anyfem/ui/app.py:1829`;
`tests/test_interop_results.py:8`; `tests/test_io.py:461`.

**I — preserve (7):** `src/anyfem/io/results.py:263,337`;
`src/anyfem/io/sesam.py:353`; `src/anyfem/ui/app.py:1831`;
`tests/test_ecosystem_integration.py:99,101,107` (line 98 is a function name but
not a boundary-exact import token).

Ignored local governance/evidence was separately inventoried: the registered
`reports/native_hybrid/anyfem_v6_native_backend_migration_plan.md:54,74,93,112`
contains valid D/canonical R plus an intentional line-112 void-name contrast; the
ignored `reports/parity/parity.json:342,348,354,360` and
`reports/parity/parity.md:111-114` contain valid D evidence. Preserve all; they are
not tracked edit targets.

### 4.5 `ANYstructure`

There are 36 occurrences: 13 R edits, 13 D, 10 I, no T/H.

**D — preserve (13):** `.github/workflows/tests.yml:40,115`;
`README.md:43,78`; `anystruct/ecosystem_gui.py:161`;
`anystruct/main_application.py:275`; `docs/index.rst:49`;
`docs/install.rst:12`; `requirements-core.txt:3`; `requirements.txt:3`;
`setup.py:24`; `tests/test_ecosystem_integration.py:256,275`.

**I — preserve (10):** `.github/workflows/tests.yml:165`;
`anystruct/ecosystem_gui.py:163`; `anystruct/fe_plate_fields.py:576,645,674`;
`tests/test_ecosystem_integration.py:174,193,209,231,236` (line 208 is a
function name but not a boundary-exact import token).

### 4.6 `ANYmesh`

There are 12 tracked occurrences: one R edit, six D, one I, four H.

**D — preserve (6):** `MIGRATION.md:145`; `README.md:167` (label only);
`docs/ARCHITECTURE.md:18,24`; `src/anymesher/serialize.py:4`;
`tests/test_layering.py:3`.

**I — preserve (1):** `tests/test_layering.py:39`.

### 4.7 `ANYmaterial`

All three occurrences are preserved: D `docs/ARCHITECTURE.md:7`; I
`tests/test_layering.py:33`; T `tests/test_packaging.py:45`, whose lowercase
`anyio` names the already-taken third-party PyPI/import identity in packaging
rationale.

### 4.8 Confirmed zero-hit repositories

`ANYgeometry`, `ANYbuckling`, `ANYintelligent`, `ANYtimeseries`, `ANYtk3D`,
`ANY3dView`, and distinct `ANYfileio-occt` have zero tracked hits. Their scanned
untracked text also has zero hits. They receive no edit and no wildcard allowlist.

## 5. Immutable historical-evidence allowlist (H)

Only these exact tracked files/lines may retain former paths/names as evidence.
Do not use a broad `reports/**` exemption.

| Repository/file | H lines | Why immutable |
| --- | --- | --- |
| `ANYsolver/reports/performance/sol_ultra_baseline.json` | 190, 7118, 7160, 7161 | Captured import failure, package version, and source checkout path. |
| `ANYsolver/reports/performance/sol_ultra_baseline.md` | 44 | Captured missing-import result. |
| `ANYsolver/reports/performance/sol_ultra_comparison.md` | 32 | Captured package comparison. |
| `ANYsolver/reports/performance/sol_ultra_environment.json` | 40, 55, 56 | Captured package/path environment. |
| `ANYsolver/reports/performance/sol_ultra_final.json` | 8840, 8882, 8883 | Captured final package/path environment. |
| `ANYsolver/reports/performance/sol_ultra_independent_verification.md` | 26 | Captured package version. |
| `ANYsolver/reports/performance/sol_ultra_numerical_comparison.json` | 79, 130 | Captured package versions. |
| `ANYmesh/reports/native_hybrid/baseline.json` | 17 | Captured old source-tree requirement. |
| `ANYmesh/reports/native_hybrid/baseline.md` | 26 | Captured old source-tree requirement. |
| `ANYmesh/reports/native_hybrid/damage_deletion.md` | 16 | Exact historical `PYTHONPATH` command. |
| `ANYmesh/reports/native_hybrid/dynamic_remeshing.md` | 42 | Exact historical `PYTHONPATH` command. |

Ignored generated deck evidence under
`ANYsolver/reports/external_references/decks/{beam_column_buckling,cylinder_s4_pressure,orthotropic_membrane_s4,pressure_plate_s4}.inp:1`
contains valid D generator provenance and is preserved outside the tracked guard.

The registered parent plan, ecosystem ledger transition row, and this manifest
may state the former identity as governance/source authority; they are R
governance allowlist entries, not H performance evidence. `.git/**` and the entire
frozen old checkout are excluded from source guards rather than allowlisted as
current content. No canonical tracked history file presently needs an old-name H
exception.

## 6. Guard policy / exact allowlist

A later guard should scan tracked current surfaces and fail on:

- `https://github.com/audunarn/ANYio` with optional `.git`, `/issues`, or suffix;
- boundary-exact `C:\Github\ANYio` and `.ecosystem/ANYio`;
- checkout declaration `repository: audunarn/ANYio`;
- prose/display repository identity `ANYio` outside the exact governance/H
  allowlist;
- portal-internal key `anyio` in `ANYopenSoft/README.md`, `app.js`, or
  `index.html`.

The allowlist is deliberately narrow:

1. all D and I occurrences enumerated in section 4;
2. T only at the 11 canonical locations and
   `ANYmaterial/tests/test_packaging.py:45`;
3. H only at the exact files/lines in section 5;
4. registered governance/source-authority files named in sections 4.2 and 5;
5. `.git/**`, generated/cache/build/environment paths, and the frozen
   `C:\Github\ANYio` checkout are excluded from the guard input.

There is no general lowercase-`anyio`, docs, tests, reports, or JSON exemption.
Line-based allowlists must also verify expected surrounding content so line drift
cannot silently broaden an exception.

## 7. Packaging, version, lock, release, and resolver consequences

### Preserved public package contract

The canonical package remains:

- distribution `ANYfileio`, version `0.1.0`;
- import package `anyfileio`;
- scripts `anyfileio` and `anyfileio-gui`;
- dependencies `numpy>=1.26`, `ANYmesher>=0.1,<0.2`, and
  `ANYmaterial>=0.1,<0.2`.

The repository rename changes only newly built `project.urls` and active source
links/checkout paths. It does not require a version bump, lock regeneration,
module shim, CLI change, or dependency-bound change. The canonical repository has
no tracked lock, constraint, requirements, `setup.py`, or `setup.cfg`; its tracked
packaging inputs are `pyproject.toml` and `MANIFEST.in`. The scanned consumers
also have no lockfile carrying an old repository identity. ANYstructure's
requirements files contain valid D dependency declarations and remain unchanged.

Before a future publication, separately decide whether uploaded display metadata
continues to spell the normalized project `ANYfileio` or changes presentation to
`ANYfileIO`. Repository casing does not create a second resolvable PyPI namespace,
and this plan does not authorize that metadata decision.

### Exact resolver conflict and handoff

- Current canonical `ANYfileIO` requires `ANYmesher>=0.1,<0.2`.
- Current ANYsolver `0.2.0` also requires `ANYmesher>=0.1,<0.2` and
  `ANYfileio>=0.1,<0.2`.
- Current ANYfem `0.1.0` requires `ANYmesher>=0.2,<0.3` and
  `ANYfileio>=0.1,<0.2`.
- Current ANYstructure `6.1.1` requires `ANYmesher>=0.1,<0.2` and
  `ANYfileio>=0.1,<0.2` in `setup.py` and requirements files.
- The active ANYmesh source metadata is version `ANYmesher 0.2.0`.

Therefore the active 0.2 mesher source cannot satisfy the `<0.2` constraints in
ANYfileIO, ANYsolver, or ANYstructure. Existing `--no-deps` source-install jobs
can hide this incompatibility and are not resolver evidence. The canonical
publish workflow independently downloads `ANYmesher>=0.1,<0.2` and
`ANYmaterial>=0.1,<0.2` from the target index before building; index availability
was not network-verified in M1, and publication remains blocked if that gate does
not resolve.

The ANYmesher native-hybrid owner owns its release/version contract. This rename
task must not edit ANYmesh `setup.py`/`pyproject.toml`, relax dependency bounds,
use a stale wheel, or recast a `--no-deps` pass as resolution. A version-bound
repair is a separate public-contract decision and cross-task handoff.

## 8. External-administrator checklist

These are unchecked administrative obligations, not locally verified facts and
not authority to mutate an external service.

### GitHub repository

- [ ] Confirm canonical slug and HTTPS/SSH clone identity are
  `audunarn/ANYfileIO`; confirm default branch `main`.
- [ ] Verify old `audunarn/ANYio` web, API, HTTPS clone, and SSH clone redirects;
  do not recreate the old slug while redirects are needed. Redirect success is
  compatibility evidence, not permission to keep active old links.
- [ ] Verify branch protection/rulesets, required checks, Actions permissions,
  secrets/variables, environments, issue/PR continuity, releases/tags, Pages,
  deploy keys, webhooks, topics, installed GitHub Apps, code scanning, Dependabot,
  and repository-dispatch/reusable-workflow callers.
- [ ] Confirm all developer remotes/worktrees/submodules use the canonical URL.
  Freeze `C:\Github\ANYio`; its later removal/archive is a separate recoverable
  action.

### PyPI and TestPyPI (verify separately)

- [ ] Confirm ownership/maintainers for normalized project `anyfileio` on both
  indexes.
- [ ] Update/verify OIDC trusted-publisher subject exactly: GitHub owner
  `audunarn`, repository `ANYfileIO`, workflow `publish.yml`, environment
  `testpypi` on TestPyPI and `pypi` on PyPI.
- [ ] Confirm matching GitHub environments and protection rules. The workflow
  already requests `id-token: write`; no old slug occurs in its source.
- [ ] Decide future distribution display capitalization (`ANYfileio` versus
  `ANYfileIO`) before the next upload and record it as a public metadata decision.
- [ ] Do not publish until sibling dependency gates and clean artifact checks pass.

### Connected services and public surfaces

- [ ] Verify Read the Docs repository integration and the explicit ANYstructure
  VCS install after its source edit.
- [ ] Verify coverage, code-quality/security dashboards, release automation,
  webhook consumers, dependency bots, source/documentation links, badges, and
  any package-index project links. No badge or canonical-repository RTD config was
  found locally; absence in source is not external proof.
- [ ] Verify ANYopenSoft portal display, install command, internal key, dependency
  edge, link, and workspace copy command together after owner-approved patching.
- [ ] Search external workspace/IDE/task configuration for old clone paths without
  modifying unrelated user state.

## 9. Proposed ownership and merge order

1. **M2 canonical:** Forseti on a dedicated
   `codex/anyfileio-repository-rename` branch from revalidated canonical `main`;
   old checkout stays frozen.
2. **Governance/portal:** Boss owns governance; user/portal owner owns dirty portal
   files. Patch only approved exact hunks after the current portal work stabilizes.
3. **Consumer handoffs:** ANYsolver, ANYfem, and ANYmesh native-hybrid owners first
   identify accepted integration tips. ANYstructure owner identifies its
   `origin/master`-based tip. Then apply isolated path-only commits or owner
   cherry-picks; do not opportunistically modify their active engineering diffs.
4. **Resolver:** ANYmesher owner reports the accepted version/index strategy before
   any clean resolver or publication claim. Repository-path edits do not wait for
   a resolver repair, but release readiness does.
5. **External administration:** repository/release administrator verifies GitHub,
   PyPI/TestPyPI, OIDC, and integrations after source URLs are coherent and before
   publication.

## 10. M1 completion statement and limits

This manifest classifies every naming occurrence in the defined source snapshot,
identifies every active former-repository edit, gives an exact allowlist and H
evidence list, and records per-file owner/branch/overlap/resolver/external-service
consequences. No build, test suite, benchmark, profiler, native compilation,
network request, remote mutation, branch change, consumer edit, canonical metadata
edit, push, or publication was performed. Later validation/heavy runs remain
subject to the parent plan and Boss performance-lease protocol.
