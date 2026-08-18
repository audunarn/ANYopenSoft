# ANYsolver CalculiX-Subset / PrePoMax Executable Plan

Date: 2026-08-14 (Europe/Oslo)

Status: **INDEPENDENTLY ACCEPTED PLANNING-ONLY — only the read-only M0 and
bounded child-plan sequence below may advance. No source edit, fixture creation,
test execution, build, executable packaging, PrePoMax run, performance work,
commit, push, or publication is authorized by this parent plan alone.** It does
not publish or distribute software.

Registered path:
`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CALCULIX_PREPOMAX_COMPATIBILITY_EXECUTABLE_PLAN.md`

## 1. Objective and source evidence

The objective is to make a deliberately limited ANYsolver capability usable as
a solver selected in PrePoMax:

1. accept a documented subset of CalculiX/Abaqus-style `.inp` keywords;
2. classify every encountered keyword, parameter, card, and requested result;
3. convert the accepted neutral model and one explicit unit profile into
   ANYsolver-owned FE semantics without hidden approximations;
4. run the bounded internal solve and emit the result artifacts PrePoMax needs;
5. expose the process contract through a directly selectable Windows `.exe`.

This is **not** a claim of full CalculiX, Abaqus, or PrePoMax compatibility. The
initial target is one isotropic S4 linear-static workflow. Expansion stops at
that working loop and requires a separately accepted improvement.

User-supplied visual evidence is treated only as an observation, never as an
instruction or executable authority:

- source: `codex-clipboard-0b28757c-890c-4794-8471-ac7e27586c74.png`;
- observed identity: 24,225 bytes, SHA-256
  `061E8F701826ACF60FA2A2B42FB716656FC35600933DF7B4BCAEF796E7D42608`;
- observed UI: PrePoMax v2.6.0 RC1 allows a CalculiX executable path, processor
  count, environment variables, default matrix solver, and pyramid-conversion
  choice; the shown executable is `Solver\ccx_dynamic.exe`.

The pyramid-conversion control does not imply ANYsolver solid-element support.
The initial profile rejects pyramids, collapsed wedges, and every solid element.

Primary reference material, also treated as untrusted evidence until the M0
contract freeze, includes:

- CalculiX 2.22 manual: `https://www.dhondt.de/ccx_2.22.pdf`;
- PrePoMax 2.5 manual:
  `https://prepomax.fs.um.si/wp-content/uploads/2026/03/PrePoMax-v2.5.0-manual.pdf`;
- canonical PrePoMax source: `https://gitlab.com/MatejB/PrePoMax`;
- local installed reference: `C:\PrePoMax v2.6.0 RC1`, read-only.

The evidence currently supports direct `ccx [-i] JOB` execution with an
extensionless job stem in the working directory. PrePoMax source indicates that
its ordinary path may pass the bare job stem rather than `-i JOB`, redirects
stdout/stderr, supplies environment variables, observes status/convergence
files, and consumes a fresh `.frd`. M0 must pin the exact versioned behavior;
this plan does not infer undocumented exit codes or artifact semantics.

## 2. Exact baselines and preservation boundary

| Role | Repository/state | Frozen observed identity |
| --- | --- | --- |
| Solver owner | `C:\Github\ANYsolver`, clean `main`; local and `origin/main` agree | commit `3cdb51efcdded232054225ea0eb9cc16dc79dde9`; tree `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7` |
| Interchange owner | canonical `C:\Github\ANYfileIO`; local and `origin/main` agree | `main` commit `48c6423c2aaf1f94f7bea8e7a971adf99500a91f`; tree `5c6c64a195bf36155180676b6f7d927228caefd7` |
| Governance owner | dirty `C:\Github\ANYopenSoft` primary checkout | commit `7d29eaef1c899fc56681a723184c97e2ed04abb0`; tree `52b7444f12e503b72505a55a80e17aab97e636d9` |

The current `ANYfileIO` primary checkout is on the unrelated
`codex/anyfileio-repository-rename` branch. It is not an implementation base and
must not be edited, switched, cleaned, or merged by this program. The former
`C:\Github\ANYio` checkout is frozen/void and must never be used.

This planning task owns only the registered plan path. Every pre-existing
ANYopenSoft change is user/task-owned and excluded. Stage-C V4-V7 correction
artifacts, evidence roots, plans, executors, tests, processes, and authorities
are unrelated and immutable to this feature; this plan neither repairs nor
depends on them.

After plan acceptance, M0 is restricted to read-only primary-source/manual and
installed-file inspection plus one in-place amendment of this plan. It may not
create a fixture/evidence path, execute PrePoMax/CalculiX/ANYsolver, or read a
private user model. After the amended M0 contract is independently accepted,
the repository tasks must register no more than two child plans before editing:

1. an ANYfileIO contract/result-codec plan based on the exact accepted canonical
   main object then current; and
2. an ANYsolver adapter/CLI/executable plan based on the exact accepted solver
   main object then current and the accepted ANYfileIO contract commit.

Each child plan freezes its own branch, isolated worktree, exact path allowlist,
tests, dependency objects, and stop gate. Suggested branch names are
`codex/calculix-prepomax-profile-v1` and
`codex/calculix-prepomax-executable-v1`. Moving branch names and ambient sibling
checkouts are never dependency evidence.

The ANYfileIO child plan also freezes whether the new public records/encoders are
backward-compatible additive `0.2.x` work or require a new minor version. If a
new minor is required, it must define migration and compatibility behavior
before source edits. The ANYsolver child plan then binds the exact accepted
ANYfileIO commit, version, dependency range, resolver graph, and source/wheel
compatibility tests. Current ANYsolver metadata is `ANYfileio>=0.1,<0.3`; it may
not consume an `ANYfileio>=0.3` contract without an explicitly accepted range
and migration change.

## 3. Canonical ownership and dependency direction

### ANYfileIO owns syntax and external artifact encoding

ANYfileIO exclusively owns:

- byte decoding, line/continuation/comment handling and keyword tokenization;
- normalized keyword/parameter/card records with original source spans;
- deterministic diagnostic locations and loss-awareness;
- the single-file CalculiX input document contract;
- neutral FRD, DAT, and any accepted STA serialization needed by the profile;
- lexical/schema tests and format fixtures.

The current `anyfileio.calculix.inp` reader only summarizes nodes and element
counts. It is not a semantic parser and must not be presented as one. V1 may
recognize `*INCLUDE`, but must refuse it without opening the referenced file.
An include graph is deferred.

### ANYsolver owns engineering meaning and execution

ANYsolver exclusively owns:

- the named compatibility profile and version;
- keyword-capability admission after ANYfileIO parsing;
- exact unit-profile resolution and conversion to internal SI;
- neutral document to `FEModel` mapping;
- analysis dispatch, resource limits, cancellation safe points, and physics;
- result recovery/projection into neutral output records;
- CLI/process behavior, exit classification, execution receipts, and the
  Windows executable entry point.

The proposed compatibility manager is therefore a semantic admission and
conversion layer, **not** a second parser. It must consume public ANYfileIO
records and must not inspect raw keyword lines.

### Other owners

- ANYmaterial continues to own material definitions and validation.
- ANYmesh continues to own neutral mesh topology, numbering, and quality.
- ANYfem remains unchanged in V1 and owns no new syntax or executable behavior.
- ANYopenSoft governance records build provenance, SBOM/notices, signing gates,
  and release decisions; it does not own solver or format implementation.
- PrePoMax is an external consumer. No ANY package imports or embeds PrePoMax.
- GUIexpert advises only the later PrePoMax GUI acceptance milestone, after the
  headless process/artifact contracts are frozen. GUI advice cannot change
  solver semantics or format ownership.

Dependency direction is:

```text
ANYmaterial / ANYmesh -> ANYfileIO neutral records -> ANYsolver compatibility
ANYsolver result records -> ANYfileIO encoders -> PrePoMax files
PrePoMax -> direct ANYsolver executable process
```

No reverse dependency, shared implementation copy, implicit ambient import, or
raw syntax parsing in ANYsolver is allowed.

## 4. Versioned compatibility contract

The public working name is `anysolver.prepomax-calculix-s4-static/1`. Before
implementation, the child plans may improve the spelling once, but the profile
must remain explicitly versioned and must appear in every compatibility report,
result, banner, and build manifest.

### 4.1 Dispositions

Every keyword and each of its parameters/cards receives exactly one disposition:

- `supported` — mapped without semantic loss inside the qualified profile;
- `metadata_only` — retained and reported, mechanically inactive by an exact
  frozen rule (initially limited to heading/comments);
- `unsupported` — known but outside V1;
- `invalid` — malformed, contradictory, duplicated, non-finite, or out of range;
- `ambiguous` — meaning or unit interpretation cannot be proven.

`unsupported`, `invalid`, and `ambiguous` are fatal before model construction or
solve. There is no silent ignore, nearest-keyword substitution, warning-only
fallback, unknown-option acceptance, empirical gate tuning, or result fabrication.
`metadata_only` cannot be expanded merely because an observed deck happens to
solve without the card.

### 4.2 Initial supported engineering slice

M0 must freeze the exact spelling, option/card grammar, aliases, ordering rules,
and PrePoMax-generated fixture. The maximum V1 semantic scope is:

- one input file and one extensionless job stem;
- comments and one heading as reported metadata;
- `*NODE` with finite 3-D coordinates and stable positive identifiers;
- `*ELEMENT, TYPE=S4` only, with four valid nodes and stable identifiers;
- explicit `*NSET` / `*ELSET`, plus `GENERATE` only if the M0 fixture and
  ANYfileIO contract prove exact semantics;
- one isotropic `*MATERIAL` with linear `*ELASTIC`; optional positive `*DENSITY`;
- one homogeneous `*SHELL SECTION` with positive thickness;
- zero-valued `*BOUNDARY` restraints on supported shell degrees of freedom;
- bounded `*CLOAD` forces/moments and/or uniform `*DLOAD` pressure or gravity
  only where the existing qualified solver path has matching semantics;
- exactly one `*STEP` / linear `*STATIC` / `*END STEP` sequence;
- only the exact nodal/element output request forms frozen in M0 for coordinates,
  displacement, reaction force, and stress required by PrePoMax V1;
- one explicitly named PrePoMax unit profile, converted exactly to SI and back.

The unit profile is not guessed from magnitude. M0 must freeze the authoritative
deck marker or explicit extra argument and the complete dimensional factor
table. Missing, duplicated, conflicting, or unknown unit evidence is fatal. No
unitless default is accepted.

### 4.3 Initial exclusions

V1 explicitly excludes:

- C3D or other solids, wedges, pyramids, collapsed elements, S3/S6/S8, and beams;
- more than one material, section, step, or analysis case unless M0 proves that
  a mechanically inactive repeated metadata form is unavoidable;
- prescribed nonzero displacement, equations/MPCs, couplings, ties, rigid
  bodies, contact, connectors, submodels, and initial fields;
- plasticity, damage, nonlinear geometry, arc length, post-buckling, dynamics,
  modal/frequency, buckling, thermal or coupled analysis;
- amplitudes, distributions, complex numbers, user subroutines, restart,
  include files, generated code, and raw keyword passthrough;
- arbitrary Abaqus compatibility or reuse of the existing one-way exporter as
  proof that inbound semantics are supported;
- CAD, geometry repair, meshing, PrePoMax project files, or GUI changes.

The existing ANYfileIO exporter supports a wider set (including other shells,
beams, frequency, and buckling). That does not widen this inbound V1 profile.

## 5. Process and executable contract

The first public executable name is `anysolver_ccx.exe`. It is a referential
compatibility name, not a CalculiX binary or claim of affiliation. The program
banner and documentation must say `ANYsolver CalculiX-subset compatibility
profile`, never `CalculiX CrunchiX`. Trademark wording receives review before
distribution.

The headless source CLI is implemented and qualified before packaging. V1 must:

1. accept both `anysolver_ccx.exe JOB` and `anysolver_ccx.exe -i JOB`;
2. accept `--version` without model execution;
3. reject unknown flags, response files, duplicate job arguments, extensions,
   absolute paths, separators, traversal, shell metacharacters, empty names,
   and out-of-policy length/Unicode forms;
4. use the inherited working directory and read exactly `JOB.inp` there;
5. launch no shell, child solver, network request, installer, updater, model
   download, plugin, or arbitrary script;
6. accept only a frozen environment/resource allowlist, including a bounded
   positive processor count mapped to ANYsolver `ResourceConfig`;
7. print bounded line-oriented progress and diagnostics suitable for PrePoMax's
   redirected stdout/stderr monitor;
8. establish cancellation safe points and ensure termination cannot promote a
   successful result;
9. record executable/profile/version/build identity, argv, cwd identity, input
   hash, effective environment/resources, timing, compatibility report hash,
   output identities, exit class, and first error.

M0 freezes the exact exit-code table after comparing CalculiX and PrePoMax
behavior. At minimum, success, CLI misuse, syntax/input error, unsupported
profile, invalid engineering model, solve failure, result-encoding failure,
resource refusal, and cancellation remain distinguishable internally. Do not
invent a `check-only` flag from PrePoMax's UI without primary-source proof.

### Output lifecycle

M0 freezes artifact expectations per accepted deck/output request. V1 success
requires exit success **and** all required fresh artifacts to parse and reconcile;
file existence alone is never success. The likely surface is:

- `JOB.frd`: required atomic final with stable node/element IDs and requested
  displacement, reaction, and stress fields;
- `JOB.dat`: emitted only with the exact required/requested diagnostic semantics;
- `JOB.sta`: only if the versioned PrePoMax contract proves a needed grammar;
- `JOB.cvg` and `JOB.eig`: unsupported/absent unless separately proven;
- `JOB.anysolver-compat.json`: deterministic sidecar with the full admission,
  conversion, solve, and output receipt; ignored safely by PrePoMax.

M0 classifies every artifact as either a terminal final or a live observational
stream. Terminal artifacts (including `.frd`, the compatibility receipt, and
any terminal-only DAT/STA form) use sibling partials and atomic promotion; a
partial is never a final. If PrePoMax requires `.sta`, `.cvg`, or another file to
advance during execution, that file is a bounded append-only live stream with
the exact versioned grammar. It is never success evidence, is closed before the
terminal decision, and remains explicitly `evidence_limited` after failure or
cancellation. Its final byte identity is recorded separately. V1 refuses a
working directory containing a pre-existing recognized final unless M0 proves
PrePoMax performs a safe deletion/replacement handshake. It never accepts stale
output after a failed or cancelled run. First semantic/solve error is preserved;
cleanup/encoding errors are secondary and cannot turn failure into success.

## 6. Windows artifact and licensing boundary

The required deliverable is a directly selectable Windows AMD64 executable,
not merely a Python command shim. The first qualified package is a transparent
one-folder portable layout containing `anysolver_ccx.exe` and its exact runtime
dependencies. A single-file self-extractor, installer, PATH mutation, registry
write, service, auto-update, code signing, and public release are deferred.

The packaging child plan must choose and justify the smallest auditable method
(for example an embedded CPython launcher, PyInstaller one-folder, or a compiled
launcher) after a bounded source-CLI prototype. It must freeze:

- exact Python/toolchain/wheel/native-library inputs and hashes;
- offline/reproducible build command and isolated build root;
- dependency and DLL search policy with no ambient-machine fallback;
- SBOM, licences, copyright notices, source correspondence/source-offer duties,
  and build provenance;
- clean-machine operation without a separately installed Python;
- Windows paths with spaces, approved non-ASCII and length boundaries;
- antivirus/signing observations as evidence-limited facts, not release claims.

ANYsolver and ANYfileIO currently declare GPL-3.0-or-later. The first artifact
therefore remains GPL-compatible with complete corresponding-source/notices
evidence. It must not bundle CalculiX, PrePoMax, MKL, Pardiso, sample-model, or
other third-party binaries/content merely because they are present locally.
Relicensing, trademark approval, signing, installer work, and distribution are
separate user/legal/governance gates.

## 7. Milestones and stop gates

### M0 — exact external contract freeze

- Read-only inspect and pin the PrePoMax version/source object and CalculiX
  manual/build reference. Do not launch an executable or inspect private Temp
  model content.
- Specify, but do not yet create, one synthetic/manual S4 linear-static fixture
  with no private user model, licensed standard content, or copied vendor example.
- Freeze argv, cwd, environment, unit marker/profile, stdout/stderr behavior,
  keyword/options/cards, expected fields/files, status monitoring, cancellation,
  and stale-output behavior.
- Add the exact compatibility matrix, expected result schema, registered future
  fixture/evidence paths, and bounded future launch commands to one in-place
  amendment of this plan and obtain independent acceptance.

Stop if the fixture requires solids, nonlinear behavior, contact, unsupported
materials, unverifiable units, or an undocumented process/result behavior.

### M1 — ANYfileIO owner contract

- Register and accept the ANYfileIO child plan.
- Create the registered synthetic fixture as the first owned artifact; do not
  run PrePoMax or a solver in this milestone.
- Implement the single-file typed input records, source diagnostics, explicit
  dispositions, and neutral FRD/DAT/accepted-STA writers.
- Prove parser/encoder determinism, strict limits, no reverse dependency, and
  negative behavior for every excluded feature.
- Freeze and verify the additive/new-minor version decision, migration contract,
  public exports, and old/new reader compatibility.

Stop before ANYsolver work until the public ANYfileIO contract and focused tests
are independently accepted.

### M2 — ANYsolver admission, conversion, and physics

- Register and accept the ANYsolver child plan pinned to the accepted ANYfileIO
  object.
- Bind the exact ANYfileIO distribution version/range and prove source plus
  installed-wheel compatibility without an ambient checkout.
- Implement the compatibility profile, unit conversion, FEModel adapter,
  linear-static dispatch, recovery, and compatibility receipt.
- Verify the S4 model against independent analytical or first-principles oracles.

M2 must use the accepted/default S4 implementation present on the exact solver
base and may not alter element formulation, integration, rank/gauge policy,
stiffness, or qualification gates. The dormant restricted-S4 proof/integration
line is excluded and may not be merged, enabled, copied, or used as evidence by
this compatibility feature.

Stop if a card cannot be mapped without approximation, the exact output field
cannot be recovered, or the source solver regime is outside current qualification.

### M3 — source CLI and fault containment

- Add the direct source entry point and exact process/exit contract.
- Qualify argv, cwd, resources, progress, cancellation, partials, stale finals,
  failure precedence, and deterministic evidence.
- Exercise it without PrePoMax before any executable build.

### M4 — headless artifact loop

- Run the synthetic deck through the source CLI.
- Reparse every output with ANYfileIO and independently reconcile identifiers,
  units, requested fields, equilibrium, and analytical results.
- Compare the same model with a separately identified CalculiX build as an
  independent reference, never as the sole truth oracle.

### M5 — Windows executable

- Build the one-folder AMD64 package in an isolated, content-addressed build.
- Verify hashes, SBOM/notices/source correspondence, DLL closure, no Python
  prerequisite, no network, and no ambient dependency resolution.
- Exercise the same source-CLI fixture and failure matrix through the `.exe`.

Native packaging/build qualification and hardware/startup matrices require an
exclusive PERF lease with exact command, resources, and ETA.

### M6 — PrePoMax end-to-end and review stop

- With GUIexpert advising only the GUI acceptance observations, configure the
  exact executable path in the pinned PrePoMax version and run only the synthetic
  fixture.
- Verify process monitor behavior, result import/visualization, IDs, units,
  displacement/reaction/stress values, failure display, and cancellation.
- Submit the completion packet and stop. No second element, analysis, unit
  profile, keyword family, installer, signing, or publication is implied.

## 8. Verification and definition of done

The child plans freeze exact commands, but the final evidence must include:

1. exact source/build/dependency identities and clean isolated worktrees;
2. ANYfileIO positive and mutation/negative fixtures for every accepted and
   refused lexical/encoding rule;
3. an exact keyword/parameter/card compatibility matrix with source locations;
4. ANYsolver unit-profile, admission, adapter, solve, recovery, and failure tests;
5. first-principles S4 checks for rigid-body/preflight, load/equilibrium,
   displacement, reaction, stress, and unit round-trip;
6. direct source-CLI and packaged-executable contract/fault tests;
7. actual PrePoMax end-to-end evidence on the single synthetic fixture;
8. comparison to a separately identified CalculiX executable with declared
   tolerances fixed before results are observed;
9. exact output hashes/schemas plus proof that failed/unsupported/cancelled runs
   cannot leave an admissible success final;
10. docs stating supported profile, exclusions, installation layout, invocation,
    units, diagnostics, licences, and lack of CalculiX/PrePoMax affiliation;
11. independent engineering, format-contract, security/process, packaging, and
    ecosystem review.

The milestone is done only when a user can point the pinned PrePoMax version to
the packaged `anysolver_ccx.exe`, run the single admitted S4 static fixture, and
obtain correctly scaled, independently validated results in PrePoMax—while all
out-of-profile cases fail before solving with precise diagnostics.

## 9. Performance register

LIGHT work not requiring a lease: parser/adapter unit tests, tiny analytical
models, source-CLI argument/failure tests, and static packaging metadata review.

Lease-required anticipated work:

- native/standalone executable builds used for qualification;
- broad solver or repository suites;
- clean-machine/hardware/startup matrices;
- repeated scaling, stress, soak, memory, profiler, or large-model runs;
- antivirus/package scanning if resource intensive.

Performance is subordinate to correctness. No keyword support, tolerance,
algorithm, or solver setting may be tuned merely to pass PrePoMax or CalculiX
comparisons.

## 10. Risks, dependencies, and anti-sprawl rules

Material risks are semantic mismatch disguised as syntax compatibility, unit
ambiguity, PrePoMax/CalculiX version drift, FRD dialect mismatch, stale results,
partial promotion, subprocess/path injection, uncontrolled native threading,
runtime/DLL ambiguity, GPL/notice/source duties, and misleading compatibility or
trademark claims.

Controls:

- one parent plan and at most the two named repository child plans;
- no new `V2` plan: correct this plan by one accepted amendment if necessary;
- at most two bounded implementation correction rounds per child milestone;
  recurring defects trigger scope reduction or architectural stop, not another
  widening attempt;
- every new keyword family requires a source fixture, semantic mapping, negative
  test, unit rule, independent numerical evidence, and accepted plan improvement;
- every nice-to-have is deferred unless required for the one S4 end-to-end loop;
- stop after the first working loop for ecosystem review;
- do not modify public APIs, dependency ranges, versions, licences, workflows,
  packaging, or other repositories outside accepted child-plan allowlists;
- do not use private user models, standards-derived models, or locally bundled
  vendor samples as redistributable fixtures;
- preserve dirty and unrelated worktrees byte-for-byte.

## 11. Completion and integration boundary

Each repository task submits its exact diff, source/test/build identities,
commands, raw results, compatibility matrix, limitations, and downstream effects
for independent review. Planning acceptance, an M0 contract, a source pass, and
an executable build are distinct gates and cannot substitute for one another.

No completion packet may claim general CalculiX/Abaqus compatibility, solver
parity, certification, publication readiness, or commercial readiness. Only
after exact implementation closeout may a separate integration plan authorize
commits, default-branch updates, pushes/PRs, signing, installer creation, or
distribution as applicable. External publication remains user-gated.

## 12. M0 exact external contract freeze (2026-08-14)

### 12.1 Milestone disposition and evidence boundary

M0 is complete as a read-only contract milestone. It freezes profile `anysolver.prepomax-calculix-s4-static/1` for one isotropic S4 linear-static workflow; it does not qualify an executable or authorize implementation. Exact local reference identities are:

| Artifact | Identity |
| --- | --- |
| PrePoMax executable | `C:\PrePoMax v2.6.0 RC1\PrePoMax.exe`; 1,910,784 bytes; SHA-256 `9553387C0BAE2DC746498322FEF662F7E1AF13156547A86EFFA0007EF14F34D4`; file/product version `2.6.0` |
| Bundled solver executable | `C:\PrePoMax v2.6.0 RC1\Solver\ccx_dynamic.exe`; 48,560,044 bytes; SHA-256 `1C1F4AD9392C0A9537E9FF1D7ADAF86EA0A6193DA5916ABB2912AE541E530C10`; PE version `1,0,0,0` is not accepted as the CalculiX build version |
| Canonical PrePoMax source | GitLab commit `12398d5e72ed48a11e96a618dcc2e6653802e2e8` (`v2.6.0 RC1`, 2026-08-07) |
| Relevant source blobs | `CaeJob/AnalysisJob.cs` `97f86b697d0b92bca8c2d834ba1e567849b777b5`; `CaeJob/CalculixMonitorData.cs` `9318461992df91a7e7df91aecfe195e7108f4d3a`; `CaeJob/ExecutableJob.cs` `08cb0762601f2e94f4ad938b64c81bb1a59772ad`; `CaeJob/EnvironmentVariable.cs` `f504...` remains evidence-limited until its full blob identity is independently retained |
| CalculiX manual | Official 2.22 manual `https://www.dhondt.de/ccx_2.22.pdf`; exact bytes/page extraction are `evidence_limited` because the bounded read timed out and was not retried |

The source evidence fixes the PrePoMax call shape: direct process creation with no shell, one bare extensionless job stem as the argument, caller-selected working directory, redirected stdout/stderr, `OMP_NUM_THREADS` set from the selected CPU count, and result discovery at `<cwd>\<JOB>.frd`. PrePoMax also observes optional `<JOB>.dat`, `<JOB>.sta`, and `<JOB>.cvg`. Its existing size-only FRD heuristic is historical behavior, not an ANYsolver acceptance oracle.

### 12.2 Invocation, path, environment, and stream contract

The PrePoMax-facing invocation is exactly:

```text
anysolver_ccx.exe JOB
```

`JOB` is one extensionless ASCII stem matching `^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$`. The input is exactly `<cwd>\JOB.inp`; absolute stems, separators, drive/UNC syntax, dots, whitespace, glob characters, empty values, duplicate arguments, and symlink/reparse inputs are rejected. The direct human/CI alias `anysolver_ccx.exe -i JOB` has identical semantics but is not part of the PrePoMax GUI acceptance claim. No shell, subprocess solver, prompt, stdin protocol, network access, plugin discovery, or ambient repository import is allowed.

The working directory must be an absolute, existing, non-reparse directory supplied by the caller. Input and every output must remain its direct child. Before parsing, refuse any recognized final or partial for the stem: `.frd`, `.dat`, `.sta`, `.cvg`, `.eig`, `.anysolver.json`, or any corresponding `.partial`. This stale-output rule is fail-closed; no file is deleted or overwritten.

Accepted task environment is exactly `OMP_NUM_THREADS=<decimal 1..64>` plus `ANYSOLVER_PREPOMAX_UNIT_PROFILE=MM_N_S_V1`. The executable records both values in its sidecar. Missing or malformed values fail before output creation. Unknown `ANYSOLVER_*` variables fail; unrelated inherited OS variables have no semantic effect. Locale-sensitive numeric parsing/formatting is forbidden.

Stdout and stderr are UTF-8, line-oriented, noninteractive, and independently capped at 1,048,576 bytes. Stdout contains deterministic phase records only; stderr contains diagnostics only. Truncation, undecodable output, or a write failure is an execution failure, never success with warning.

### 12.3 Unit profile `MM_N_S_V1`

The input/result profile is millimetre, newton, second, tonne, and MPa (`N/mm^2`). Internal solver-neutral values are SI. Exact conversions are:

| Quantity | External to SI | SI to external |
| --- | ---: | ---: |
| length/displacement | `1e-3` | `1e3` |
| area | `1e-6` | `1e6` |
| volume | `1e-9` | `1e9` |
| force/reaction | `1` | `1` |
| moment | `1e-3` | `1e3` |
| stress/pressure/elastic modulus | `1e6` | `1e-6` |
| mass | `1e3` | `1e-3` |
| density | `1e12` | `1e-12` |
| acceleration | `1e-3` | `1e3` |

The M0/M1 fixture deliberately excludes density, gravity, temperature, plasticity, contact, and dynamics. Their conversion rows reserve representation only and confer no supported-keyword claim.

### 12.4 Exact supported keyword matrix

The initial parser accepts keywords case-insensitively but preserves IDs/names and rejects duplicate/conflicting definitions. Only the following forms are supported:

| Keyword | Accepted subset |
| --- | --- |
| `*HEADING` and `**` comments | metadata only |
| `*NODE` | explicit unique positive integer ID and three finite coordinates |
| `*ELEMENT` | `TYPE=S4`, one explicit `ELSET`, four distinct existing node IDs, orientation retained |
| `*NSET` / `*ELSET` | one name and explicit unique IDs only; no `GENERATE` |
| `*MATERIAL` | one unique material name |
| `*ELASTIC` | exactly one isotropic `E, nu` row with finite `E>0` and `-1<nu<0.5` |
| `*SHELL SECTION` | one `ELSET`, one `MATERIAL`, one finite positive thickness |
| `*BOUNDARY` | existing node set, exact `first_dof,last_dof,value`; DOFs 1..6; finite zero value only |
| `*CLOAD` | existing node or node set, translational DOF 1..3, finite value |
| `*STEP` / `*STATIC` / `*END STEP` | exactly one non-nested linear-static step; default static controls only |
| `*NODE FILE` | exact variables `U,RF` |
| `*EL FILE` | exact variable `S` |

Every other keyword, parameter, data-row shape, continuation, include, generated set, element type, nonlinear control, or output request is typed `UNSUPPORTED_KEYWORD` or `AMBIGUOUS_INPUT`; it is never ignored, inferred, or downgraded. Duplicate IDs, missing references, nonmanifold/degenerate S4 geometry, invalid orientation, unsupported boundary/load semantics, and non-finite data fail before solving.

### 12.5 Frozen synthetic fixture contract

The future fixture is a 100 mm by 20 mm membrane strip with six nodes and two S4 elements: nodes `(1..6)` at `(0,0,0)`, `(50,0,0)`, `(100,0,0)`, `(0,20,0)`, `(50,20,0)`, `(100,20,0)` mm; elements `(1,2,5,4)` and `(2,3,6,5)`; isotropic `E=210000 MPa`, `nu=0.3`; thickness `1 mm`; nodes 1 and 4 fixed in DOFs 1..6; nodes 3 and 6 each loaded `+10 N` in DOF 1. Requested results are `U`, `RF`, and `S`.

The first-principles ledger freezes total applied `Fx=20 N`, equilibrium `sum(RFx)=-20 N`, nominal axial stress `1 MPa`, and nominal free-edge axial displacement `0.0004761904761904762 mm`. The ANYfileIO child plan must freeze discretization-aware tolerances before any fixture execution; M0 does not silently choose or tune tolerances.

### 12.6 Results, artifacts, status, cancellation, and stale-output truth

Successful output requires all of:

- `<JOB>.frd` promoted atomically from a fresh same-directory partial, larger than 300 bytes, parseable, and containing the exact input node/element IDs plus semantic datasets `DISP`, `FORC`, and `STRESS` mapped to displacement, reaction force, and stress.
- `<JOB>.anysolver.json` promoted atomically after FRD reopen/validation. It records schema/profile, input/output hashes, unit profile, thread count, phases, exit status, elapsed time, field/component mapping, warnings (empty for qualification), and optional-file inventory.
- Optional `.dat`, `.sta`, `.cvg`, and `.eig` are inventoried and hashed if created. Their absence is permitted for this static fixture. An unexpected recognized file, unregistered dataset, missing ID, duplicate row, partial result, or stale timestamp/hash fails qualification.

No final is published until parse, solve, result conversion, reopen, and validation succeed. A failed or cancelled run may leave owned `.partial` evidence but must not create/replace finals.

Exact exit codes are: `0` success; `2` CLI/path/environment misuse; `3` syntax; `4` unsupported or ambiguous contract; `5` invalid model/units; `6` resource refusal; `7` solve/result failure; `8` encoding or durable-I/O failure; `9` cancellation; `10` internal invariant failure. Nonzero is always failure. PrePoMax may forcibly terminate the process tree; therefore correctness relies on publish-last finals, not a cleanup promise. No automatic retry, fallback backend, healing, coordinate inference, or stale-result reuse is allowed.

### 12.7 Exact child-plan order and frozen future paths

The next child is exclusively the ANYfileIO contract/result-codec plan:

`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_CALCULIX_PREPOMAX_S4_CONTRACT_PLAN.md`

It owns future paths under canonical ANYfileIO only, including:

`C:\Github\ANYfileIO\tests\fixtures\calculix\prepomax_s4_static_v1.inp`

`C:\Github\ANYfileIO\tests\fixtures\calculix\prepomax_s4_static_v1.frd`

`C:\Github\ANYfileIO\tests\test_calculix_prepomax_s4_contract.py`

Its later focused command is frozen as:

```text
python -B -m pytest -p no:cacheprovider tests/test_calculix_prepomax_s4_contract.py -q
```

Only after an independently accepted ANYfileIO commit may the solver child be registered:

`C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_CALCULIX_PREPOMAX_S4_ADAPTER_EXECUTABLE_PLAN.md`

Its prospective owned paths and commands must be frozen in that child; none are authorized here. PrePoMax GUI execution/acceptance remains downstream M6 work and requires GUIexpert review after the headless contracts are green. GUI behavior cannot alter parsing, units, status, cancellation, or result semantics.

M0 therefore closes with a bounded dependency decision: register and review the ANYfileIO child first; do not register or implement the ANYsolver child yet. No executable, fixture, test, build, PERF run, Git mutation, publication, or GUI action was performed by M0.
