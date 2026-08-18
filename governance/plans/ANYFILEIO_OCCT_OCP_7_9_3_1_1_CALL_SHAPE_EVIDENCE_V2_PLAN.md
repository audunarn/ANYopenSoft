# ANYfileio-occt OCP 7.9.3.1.1 call-shape inventory v2 plan

Status: **registration candidate**. This content-addressed plan grants no probe
write, subprocess, download, environment, install, OCP import/call, evidence
write, repository edit, merge, push, or publication authority until the
ecosystem Boss registers its exact path/hash and explicitly releases the next
stage. This is a replacement plan, not authority to rerun the retired
controller.

Date: 2026-08-13 (Europe/Oslo)

Proposed evidence owner: one direct child
`/root/nanna_anyfileio_ocp_callshape_inventory_v2`; no nested writer.

## 1. Objective, identity, and immutable predecessor

On the exact Windows/CPython cell in section 2, acquire and verify only the
three pinned wheels below, install them into a disposable isolated environment,
import only `OCP`, call only the stub-qualified
`OCP.Standard.Standard_Version_Complete_s()` once, and inventory the exact 105
symbols in section 5. The result is evidence for a later, separately registered
native lifecycle probe. It is not native-reader correctness or provider
capability evidence.

Authoritative ancestry:

- original pipeline plan SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- baseline addendum SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- lightweight-core handoff SHA-256
  `739EE860455966EC157BB029FD806EB3B42500562EC06D9F4C430AC85E3AC15F`;
- accepted core `5513881827cdee9fd337497a2730a5912d8ea751`;
- native-foundation plan SHA-256
  `6C2ECD0CCA7A34F8632F29B522A1A0EAB81F6D80BE0CA78D771FABD53DD12DED`;
- read-only provider tip `23b441c3fcabb5bf4cf077daca882b984f978b42`,
  tree `a996a21a31c775660eb9dac3d491160231ba8cc1`.

The retired plan and accepted receipt are immutable inputs:

- retired plan
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CALL_SHAPE_EVIDENCE_PLAN.md`,
  SHA-256 `CA9543A84316051156471C41A71656303EBCF25426199C8D3F3744C1C203DF84`,
  23,150 bytes/433 LF/0 CR;
- accepted receipt
  `C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY.pending`,
  exactly seven regular non-reparse files/134,002 bytes;
- receipt `SHA256SUMS.txt` SHA-256
  `5AB56F7750DAA11650FECF698F108435A08B0083E0525A43106BFB3414E5A7F5`;
- receipt `OUTCOME.json` SHA-256
  `D996AEAF89B7A6248601B7B00E8393664A874883AF753E9EEF0EEB3608EFBAB7`;
- retired final root is absent. Neither the retired task root nor receipt may be
  cleaned, renamed, promoted, rewritten, or reused.

The v2 `OUTCOME.json` is attempt `3` and records an immutable predecessor
reference with the paths/hashes above plus:

1. attempt 1: probe
   `90856D3347DC4728DA9BD4C715F3ED515784C29115554027A3F15C8F2BEA7677`,
   exit 1/~0.6 s, evidence-staging `FileNotFoundError`/WinError 3, with zero
   GETs, wheels, environment, install, OCP import, pending/final, or residual
   task process;
2. attempt 2: probe
   `AE22C292CC9E9FE03BFB57E46653E6D34314876009F7C98994D421DB5C5AA44F`,
   exit 2/0.111471 s, first failure `resource: foundation-identity left an
   unexpected descendant`; wheel/API stages `NOT_RUN`, empty streams, zero
   GET/environment/install/OCP import, and no residual task process.

## 2. Exact host and three artifacts

Preflight must observe exactly:

```text
C:\Python\Python313\python.exe
CPython 3.13.9 final, Windows 11 AMD64, 64-bit
host OCP import spec absent
cadquery-ocp-novtk/proxy/stubs host distributions absent
provider checkout at the exact clean commit/tree in section 1
```

Only three written-order, one-shot, direct HTTPS GETs are eligible for a later
network grant. Require status 200, no redirects, no proxy/index/resolver,
hostname `files.pythonhosted.org`, exact byte count and SHA-256, 120 seconds per
GET, one MiB bounded reads with exact remaining-plus-one overflow detection,
and no retry or alternate URL.

| Distribution artifact | Exact URL | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | `https://files.pythonhosted.org/packages/57/48/4595c22b0ae1b4759f209a13d21dadd229db6c374d9b0a95afa7ed0c4714/cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | 46,364,506 | `3390be6d8199a50b01ae0137a60f56d0cfecd8753dbee08532bbbeb8b7169682` |
| `cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | `https://files.pythonhosted.org/packages/30/c0/04e9363a99fee892de2776820e3dcf04f8825b6edc9580efe3416c9465a7/cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | 3,322 | `ca4164ec4b54956d9fc3e68c67d555b5486cb963c2f71e18df005ba16b921c91` |
| `cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | `https://files.pythonhosted.org/packages/6c/de/2a93a7cd47226bdd802674e8a040235ef1a1a4433bbf4d220e21253fe31e/cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | 2,899,849 | `5ecba090df1ada12c558ff4a1b49c61d5155edc8cb3411067a785e3b43f4b359` |

Before install, inspect without execution and require one safe
`.dist-info/{METADATA,WHEEL,RECORD}` set per archive. Freeze:

| Name | Version | Requires-Python | Requires-Dist | Tag |
| --- | --- | --- | --- | --- |
| `cadquery-ocp-novtk` | `7.9.3.1.1` | `<3.15,>=3.10` | one unversioned `cadquery-ocp-proxy` | `cp313-cp313-win_amd64` |
| `cadquery-ocp-proxy` | `7.9.3.1.1` | `>=3.10` | empty | `py3-none-any` |
| `cadquery-ocp-stubs` | `7.9.3.1.1` | `<3.15,>=3.10` | empty | `py3-none-win_amd64` |

Record ordered raw `METADATA`/`WHEEL` bytes, fields, sizes and hashes plus every
`RECORD` row. The stubs PEP-658 metadata SHA is
`514e4d3a8d0f6072ab94d766649a675a591bbcb55294faf28c01e546a8b8eec7`.
Every safe member occurs once in `RECORD`; every non-`RECORD` hash/size matches;
only `RECORD` has empty self hash/size. Unsafe/duplicate/missing/extra members,
sdists, VTK/CadQuery wheels, metadata drift, or source fallback are `BLOCKED`.

## 3. Distinct v2 ownership and canonical evidence

This plan file is the registration candidate. The task/final/pending paths
below must be absent at registration and immediately before their separately
authorized source/run stages:

```text
plan:    C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CALL_SHAPE_EVIDENCE_V2_PLAN.md
task:    C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v2
final:   C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2
pending: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2.pending
sentry-temp: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2.staging-sentry.tmp
sentry:      C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2.staging-sentry
```

The plan path becomes this registered file; task/final/pending remain absent
until separately released. Task-owned children are only `probe.py`,
`wheelhouse\`, `venv\`, `tmp\`, and draft streams/JSON. Reject symlink,
junction, reparse, escape, unexpected entry, and less than one GiB free disk.

Before the first GET, require the existing common evidence parent to be a
normal non-reparse directory and v2 final/pending/both named sentries absent.
Create the exact `sentry-temp` file with a frozen short payload, fsync/close it,
no-replace rename it to exact `sentry`, reopen/hash it, delete it, and verify
both sentry paths absent afterward. Failure is a pre-download `BLOCKED`
outcome.

Terminal evidence is exactly seven regular non-reparse files:

1. `PROBE.py` (exact executed bytes);
2. `WHEELS.json`;
3. `API_INVENTORY.json`;
4. `OUTCOME.json` (attempt 3 plus predecessor history);
5. `STDOUT.txt`;
6. `STDERR.txt`;
7. `SHA256SUMS.txt` (lower-case SHA-256/bytes for the preceding six, sorted).

`first_failure` is write-once. Later cleanup/staging/validation facts append to
ordered `secondary_failures` and never replace it. `NOT_RUN` means no attempt:
result arrays and streams are empty. Attempted failure remains `BLOCKED` with
the first captured streams. Stage pending by owned same-directory temporaries,
fsync/close/atomic file rename, and create sums last.

A separate `-I -B`, stdlib-only, no-OCP validator reopens pending and enforces
the exact seven-file inventory, canonical JSON/schema/depth/caps, attempt
history, exact targets/wheels/install proofs, streams, and all six hashes/sizes.
It never renames. After its exit, pipe EOF and worker quiescence, close the empty
worker job; the controller then rechecks pending identity/hashes and uses one
same-volume `MoveFileExW(MOVEFILE_WRITE_THROUGH)`, without replace, to final.
If this final directory rename fails, leave validated pending byte-exact and
report the rename error separately; never rewrite or retry it.

## 4. Minimal worker containment (no asynchronous policing)

The controller is never assigned to a task Job Object. Omit the retired
self-supervisor Job Object, CPU affinity, controller memory ceiling, completion
port association, asynchronous job messages, and message-derived resource
classification.

Before any GET, create exactly one controller-owned worker Job Object with:

- `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`;
- `JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 3`;
- per-process memory `536,870,912` bytes;
- job memory `805,306,368` bytes;
- no silent/breakaway flags on that worker job.

Every external git/venv/pip/inventory/validator root is created suspended and
no-window (using the already-proven outer-job breakaway creation flag), assigned
to the worker job, verified with `IsProcessInJob`, given bounded non-inheritable
pipe ownership, then resumed. Assignment/resume failure terminates the still
suspended root; no child runs unassigned. Before every root, synchronously
require `JobObjectBasicAccountingInformation.ActiveProcesses == 0`.

After the direct root handle signals and stdout/stderr reach EOF, poll that
same accounting value every 100 ms for at most
`ACTIVE_PROCESS_ZERO_GRACE_SECONDS = 10.0`; the stage/global deadline wins.
Transient nonzero accounting during this grace is not failure. Only expiry
without root exit, both pipe EOFs, and confirmed zero is
`resource.residual_process`. Do not call this an
`JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO` notification; no completion port exists.

On timeout, stream/disk cap, nonzero child exit, accounting error, or residual
process, preserve the first failure. If nonempty, call `TerminateJobObject`
once and poll for zero for at most another 10 seconds bounded by global time;
close root/thread/pipe handles. Cleanup problems are secondary facts. If zero
cannot be confirmed, close the kill-on-close job, publish no PASS/final root,
preserve task/pending diagnostics, and stop. A setup/configuration failure is
pre-download `BLOCKED`. The job is reused only while confirmed empty and closes
after the independent validator. No resource-limit provenance beyond enforced
caps/observed exits is claimed.

## 5. Exact finite inventory

For each ordered target, record segment existence, runtime qualified type,
callable/class flags, `inspect.signature` or exact error, `__text_signature__`,
`__doc__`, matching installed-stub AST declarations/provenance/line ranges, and
one conclusion `AGREE|AMBIGUOUS|MISSING|CONFLICT`. Never infer a call shape.

The ordered 105-target tuple is exactly:

```text
OCP.Standard.Standard_Version_s
OCP.Standard.Standard_Version
OCP.Standard.Standard_Version_Complete_s
OCP.Standard.Standard_Version_Complete
OCP.Standard.Standard_Version_String_s
OCP.Standard.Standard_Version_String
OCP.XCAFApp.XCAFApp_Application.GetApplication_s
OCP.XCAFApp.XCAFApp_Application.NewDocument
OCP.XCAFApp.XCAFApp_Application.InitDocument
OCP.XCAFApp.XCAFApp_Application.Close
OCP.TDocStd.TDocStd_Document
OCP.TDocStd.TDocStd_Document.Main
OCP.TCollection.TCollection_ExtendedString
OCP.XCAFDoc.XCAFDoc_DocumentTool.ShapeTool_s
OCP.XCAFDoc.XCAFDoc_DocumentTool.ColorTool_s
OCP.XCAFDoc.XCAFDoc_DocumentTool.LayerTool_s
OCP.STEPCAFControl.STEPCAFControl_Reader
OCP.STEPCAFControl.STEPCAFControl_Reader.SetColorMode
OCP.STEPCAFControl.STEPCAFControl_Reader.SetNameMode
OCP.STEPCAFControl.STEPCAFControl_Reader.SetLayerMode
OCP.STEPCAFControl.STEPCAFControl_Reader.SetPropsMode
OCP.STEPCAFControl.STEPCAFControl_Reader.ReadFile
OCP.STEPCAFControl.STEPCAFControl_Reader.Transfer
OCP.STEPCAFControl.STEPCAFControl_Reader.Reader
OCP.STEPCAFControl.STEPCAFControl_Reader.ChangeReader
OCP.IGESCAFControl.IGESCAFControl_Reader
OCP.IGESCAFControl.IGESCAFControl_Reader.SetColorMode
OCP.IGESCAFControl.IGESCAFControl_Reader.SetNameMode
OCP.IGESCAFControl.IGESCAFControl_Reader.SetLayerMode
OCP.IGESCAFControl.IGESCAFControl_Reader.SetPropsMode
OCP.IGESCAFControl.IGESCAFControl_Reader.ReadFile
OCP.IGESCAFControl.IGESCAFControl_Reader.Transfer
OCP.IGESCAFControl.IGESCAFControl_Reader.Reader
OCP.IGESCAFControl.IGESCAFControl_Reader.ChangeReader
OCP.IFSelect.IFSelect_ReturnStatus
OCP.IFSelect.IFSelect_RetDone
OCP.XSControl.XSControl_Reader.PrintCheckLoad
OCP.XSControl.XSControl_Reader.PrintCheckTransfer
OCP.XSControl.XSControl_Reader.GetStatsTransfer
OCP.STEPControl.STEPControl_Reader.FileUnits
OCP.STEPControl.STEPControl_Reader.SystemLengthUnit
OCP.STEPControl.STEPControl_Reader.SetSystemLengthUnit
OCP.IGESControl.IGESControl_Reader.IGESModel
OCP.IGESControl.IGESControl_Reader.SystemLengthUnit
OCP.IGESControl.IGESControl_Reader.SetSystemLengthUnit
OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFiles
OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFile
OCP.TDF.TDF_Label
OCP.TDF.TDF_LabelSequence
OCP.TDF.TDF_Tool
OCP.TDF.TDF_LabelSequence.Length
OCP.TDF.TDF_LabelSequence.Value
OCP.TDF.TDF_LabelSequence.Append
OCP.TDF.TDF_Tool.Entry_s
OCP.XCAFDoc.XCAFDoc_ShapeTool
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetFreeShapes
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetComponents
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetUsers
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetSubShapes
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetReferredShape
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetLocation
OCP.XCAFDoc.XCAFDoc_ShapeTool.GetShape
OCP.XCAFDoc.XCAFDoc_ShapeTool.IsAssembly
OCP.XCAFDoc.XCAFDoc_ShapeTool.IsComponent
OCP.XCAFDoc.XCAFDoc_ShapeTool.IsReference
OCP.XCAFDoc.XCAFDoc_ColorTool
OCP.XCAFDoc.XCAFDoc_ColorTool.GetColor
OCP.XCAFDoc.XCAFDoc_ColorTool.GetColors
OCP.XCAFDoc.XCAFDoc_ColorTool.IsSet
OCP.XCAFDoc.XCAFDoc_ColorTool.IsVisible
OCP.XCAFDoc.XCAFDoc_LayerTool
OCP.XCAFDoc.XCAFDoc_LayerTool.GetLayers
OCP.XCAFDoc.XCAFDoc_LayerTool.GetLayer
OCP.XCAFDoc.XCAFDoc_LayerTool.IsSet
OCP.XCAFDoc.XCAFDoc_LayerTool.IsVisible
OCP.TDataStd.TDataStd_Name.GetID_s
OCP.TDF.TDF_Label.FindAttribute
OCP.TopExp.TopExp.MapShapes_s
OCP.TopExp.TopExp_Explorer
OCP.TopExp.TopExp_Explorer.More
OCP.TopExp.TopExp_Explorer.Next
OCP.TopExp.TopExp_Explorer.Current
OCP.TopTools.TopTools_IndexedMapOfShape
OCP.TopTools.TopTools_IndexedMapOfShape.Extent
OCP.TopTools.TopTools_IndexedMapOfShape.FindKey
OCP.TopTools.TopTools_IndexedMapOfShape.Add
OCP.TopLoc.TopLoc_Location.Transformation
OCP.gp.gp_Trsf
OCP.gp.gp_Trsf.Value
OCP.gp.gp_Trsf.TranslationPart
OCP.gp.gp_Trsf.VectorialPart
OCP.gp.gp_Trsf.IsNegative
OCP.gp.gp_Trsf.Inverted
OCP.gp.gp_Trsf.Multiplied
OCP.gp.gp_Trsf.Multiply
OCP.gp.gp_Trsf.PreMultiply
OCP.gp.gp_Trsf.Form
OCP.gp.gp_Trsf.ScaleFactor
OCP.Interface.Interface_Static.IsPresent_s
OCP.Interface.Interface_Static.CVal_s
OCP.Interface.Interface_Static.IVal_s
OCP.Interface.Interface_Static.RVal_s
OCP.Interface.Interface_Static.SetCVal_s
OCP.Interface.Interface_Static.SetIVal_s
OCP.Interface.Interface_Static.SetRVal_s
```

The sole native call is exactly
`OCP.Standard.Standard_Version_Complete_s()` once, only after exactly one
installed-stub declaration proves `() -> str`. No fallback target is called.
Require a `str` whose leading numeric triple is exactly `7.9.3`; record runtime
OCCT version separately from distribution version. All other targets are
inventory-only. Candidate global-setting keys are recorded but never queried:
`read.precision.mode`, `read.precision.val`, `read.step.product.mode`,
`read.step.assembly.level`, `xstep.cascade.unit`, `write.step.unit`,
`write.step.schema`, `read.iges.onlyvisible`, `write.iges.unit`.

## 6. Installation, isolation, and finite limits

Create CPython's venv with copies, remove only task-owned baseline ensurepip
bytecode through bounded, resolved non-reparse paths, then snapshot baseline
site-packages. Install locally with exact verified wheel paths and
`--no-index --no-deps --no-cache-dir --no-compile`. The installed delta is
exactly the three distributions. Reconcile every installed file to wheel
payload or the allowed pip-created `INSTALLER`, empty `REQUESTED`, canonical
`direct_url.json`, and rewritten `RECORD`; reject every other/missing/changed
file. Repeat this exact file/distribution/no-`.pyc` audit after inventory.

Inventory runs as `venv\Scripts\python.exe -I -B probe.py --inventory`, with
empty `PYTHONPATH`, no user site, and repository sources absent. Only the
isolated `OCP` origin is allowed; `cadquery`, VTK, ANYgeometry and consumer
modules remain absent. The controller and validator never import OCP.

Inclusive limits:

- global wall 600 s; each GET 120 s; venv 180 s; pip 180 s; inventory 120 s;
  validator plus publication 30 s; every smaller stage yields to global time;
- task-owned disk 1 GiB; staged evidence 32 MiB; stdout/stderr 8 MiB each;
  response headers 64 KiB; network/hash chunks 1 MiB;
- 4,096 archive members, 4,096 installed files, 128 `.pyi` files, 16 MiB per
  `.pyi`, 128 MiB aggregate stubs, 256 declarations, 16,384 UTF-8 bytes per
  doc/signature field, 2 MiB aggregate captured text, JSON depth 32 and 8 MiB
  per JSON.

Check sizes/counts before allocation/parse, stream hashes, suppress bytecode,
and stop on limit plus one. No profiler, benchmark, build, broad suite, or
performance claim is in scope; Boss separately classifies the future run.

## 7. Freeze, single-run gate, and definition of done

After registration and explicit source authority, create only the v2 task root
and one stdlib-only multi-mode `probe.py`. Static review must prove exact wheel
constants/105 targets, exactly one version-call site, forbidden native-call
absence, bounded source/symbol inventory, and no retired-path mutation. Stream
hash the probe, report its path/SHA/bytes/LF count, obtain independent review,
then externally stream-compare that SHA immediately before the exact controller
command. Changed bytes never run.

Execution requires a later explicit network grant for the exact three GETs and
one controller invocation. Preserve its first result; no retry. PASS requires
all three verified downloads/archives, both exact install audits, one valid
version call, all 105 result records, clean streams, confirmed empty worker job,
validated canonical seven-file final bundle, and no residual process. Missing,
ambiguous, or conflicting call shapes remain truthful per-target evidence and
block any later native call that needs them.

Explicit exclusions: all retired task/evidence mutations; repository or
foundation edits; application/document/reader/tool/setting construction or
calls; CAD files; public capabilities; tessellation/translation/write; BREP;
ANYgeometry/consumers; builds, index/resolution, source installs, retry,
benchmark; branch/worktree/commit/merge/push/tag/PR/package publication. Any
need to cross this boundary requires a new content-addressed plan.
