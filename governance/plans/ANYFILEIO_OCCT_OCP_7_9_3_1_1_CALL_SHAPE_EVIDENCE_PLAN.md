# ANYfileio-occt OCP 7.9.3.1.1 call-shape inventory plan

Status: **registration candidate**. This content-addressed file grants no
download, environment creation, installation, OCP import/execution, evidence
write, build, resolver, repository edit, merge, push, or publication authority
until the ecosystem Boss registers its exact path/hash and classifies the run.

Date: 2026-08-13 (Europe/Oslo)

Evidence owner: one direct child only, proposed identity
`/root/nanna_anyfileio_ocp_callshape_inventory`; no nested agent.

## 1. Objective and hard boundary

Acquire exactly the published CPython 3.13 Windows AMD64
`cadquery-ocp-novtk==7.9.3.1.1` wheel, its exact proxy, and the separate exact
`cadquery-ocp-stubs==7.9.3.1.1` Windows wheel into a disposable environment.
Verify all three artifacts before installation. Import exact namespace `OCP`,
call only the preselected, stub-qualified
`OCP.Standard.Standard_Version_Complete_s()` once, and capture a finite, named
inventory of the separate stub declarations plus runtime presence/type/signature
and documentation metadata needed to write a subsequent safe native
lifecycle/probe plan without guessing pybind call forms.

This task does **not** instantiate an XDE application/document, reader, label,
shape, transform, or setting object; call `NewDocument`, `InitDocument`,
`Close`, `ReadFile`, `Transfer`, a traversal/tool method, or an
`Interface_Static` getter/setter; create/read/write a CAD file; or change a
process-global setting. It performs no repository source/metadata edit or capability
activation. The next content-addressed evidence plan must derive its exact
application-owned `NewDocument`/close lifecycle and safe native calls from this
inventory before reader implementation begins.

Authoritative inputs:

- original pipeline plan SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- baseline addendum SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- lightweight-core handoff SHA-256
  `739EE860455966EC157BB029FD806EB3B42500562EC06D9F4C430AC85E3AC15F`;
- accepted core `5513881827cdee9fd337497a2730a5912d8ea751`;
- registered native-foundation plan SHA-256
  `6C2ECD0CCA7A34F8632F29B522A1A0EAB81F6D80BE0CA78D771FABD53DD12DED`;
- closed provider chain
  `571231dc4c7d8b4131daac6b719a6b93125a20b4 ->
  76706335af1e1bfcf0900e6824692da0058308a5 ->
  c569b0ace92305d33957b021edbf31112333a271 ->
  23b441c3fcabb5bf4cf077daca882b984f978b42`;
- foundation tree `a996a21a31c775660eb9dac3d491160231ba8cc1`.

The foundation checkout remains clean/read-only. This plan creates no branch or
worktree and changes no tracked Git content; its only durable output is the
separately owned governance evidence bundle specified below.

## 2. Exact host cell and artifacts

Preflight must match:

```text
interpreter: C:\Python\Python313\python.exe
Python:      CPython 3.13.9 final, 64-bit
platform:    Windows-11 AMD64
host OCP:    import spec absent
host dists:  cadquery-ocp-novtk, cadquery-ocp-proxy, and
             cadquery-ocp-stubs absent
```

Any drift stops before network/environment creation. Only these direct HTTPS
files are allowed; all redirects fail:

| Artifact | Exact URL | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | `https://files.pythonhosted.org/packages/57/48/4595c22b0ae1b4759f209a13d21dadd229db6c374d9b0a95afa7ed0c4714/cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | 46,364,506 | `3390be6d8199a50b01ae0137a60f56d0cfecd8753dbee08532bbbeb8b7169682` |
| `cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | `https://files.pythonhosted.org/packages/30/c0/04e9363a99fee892de2776820e3dcf04f8825b6edc9580efe3416c9465a7/cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | 3,322 | `ca4164ec4b54956d9fc3e68c67d555b5486cb963c2f71e18df005ba16b921c91` |
| `cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | `https://files.pythonhosted.org/packages/6c/de/2a93a7cd47226bdd802674e8a040235ef1a1a4433bbf4d220e21253fe31e/cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | 2,899,849 | `5ecba090df1ada12c558ff4a1b49c61d5155edc8cb3411067a785e3b43f4b359` |

After filename/size/SHA validation, inspect all three archives without executing
them. Accept exactly one matching `.dist-info/{METADATA,WHEEL,RECORD}` set in
each. `WHEELS.json` records the complete ordered raw `METADATA` and `WHEEL`
header field/value sequences, their raw bytes/hashes/sizes, and every parsed
`RECORD` row. The frozen critical metadata is:

| Distribution | Name | Version | Requires-Python | Requires-Dist multiset | Wheel tag |
| --- | --- | --- | --- | --- | --- |
| novtk | `cadquery-ocp-novtk` | `7.9.3.1.1` | `<3.15,>=3.10` | exactly one unversioned `cadquery-ocp-proxy` | `cp313-cp313-win_amd64` |
| proxy | `cadquery-ocp-proxy` | `7.9.3.1.1` | `>=3.10` | empty | `py3-none-any` |
| stubs | `cadquery-ocp-stubs` | `7.9.3.1.1` | `<3.15,>=3.10` | empty | `py3-none-win_amd64` |

The stubs wheel's published PEP-658 metadata SHA-256 is
`514e4d3a8d0f6072ab94d766649a675a591bbcb55294faf28c01e546a8b8eec7`;
the downloaded wheel's embedded METADATA must agree field-for-field with the
frozen values above. The unversioned novtk dependency does not relax this task's
separate exact proxy filename/version/hash requirement.

Every safe archive member must occur exactly once in `RECORD`; every row other
than the wheel's own `RECORD` must have the exact URL-safe base64 SHA-256 and
decimal size of its payload, and `RECORD` alone must have empty hash/size.
Installed non-`RECORD` files must equal those payloads plus only pip-created
`.dist-info/INSTALLER` (`pip` plus LF), empty `.dist-info/REQUESTED`, and one
canonical `.dist-info/direct_url.json` naming that exact local verified wheel.
The installed rewritten `RECORD` must enumerate that exact set once with valid
hashes/sizes; `--no-compile` forbids installed `.pyc` files. Any additional,
missing, duplicate, unsafe, or changed file is `BLOCKED`.

The first filename/size/hash/tag/metadata mismatch, additional archive, unsafe
archive path, source distribution, redirect/host/status mismatch, or
RECORD/WHEEL inconsistency stops before venv creation. No `cadquery-ocp`,
`cadquery`, VTK, source build, mirror, alternate index, retry, resolution, or
unpinned dependency is permitted.

## 3. Exact task/evidence ownership

Disposable root, required absent initially:

`C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory`

Owned children only: `wheelhouse\`, `venv\`, `tmp\`, `probe.py`, `STDOUT.txt`,
`STDERR.txt`, and draft JSON. Resolve every create/cleanup target and refuse any
path outside this root. `probe.py` is one reviewed stdlib-only source with
separate controller and inventory modes; controller mode does not import OCP,
and inventory mode is the sole OCP-importing process.

Preserved evidence root, also required absent initially:

`C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY`

Exact same-volume pending sibling, also required absent initially:

`C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY.pending`

Exact new files:

1. `PROBE.py` — exact executed bytes;
2. `WHEELS.json` — URLs/final URLs/names/bytes/SHA/tags and bounded
   WHEEL/METADATA/RECORD inventory;
3. `API_INVENTORY.json` — exact target results and stub provenance;
4. `OUTCOME.json` — host, commands, timestamps, exits, first failure,
   PASS/BLOCKED and nonclaims;
5. `STDOUT.txt` and `STDERR.txt` — exact first probe streams;
6. `SHA256SUMS.txt` — lower-case SHA-256 and bytes for the preceding six files,
   sorted by relative POSIX path.

Every terminal first outcome after controller invocation, including a
pre-download `BLOCKED`, produces this canonical seven-file shape. A read-only
registration/preflight drift before controller invocation prevents the run and
is reported to the Boss without pretending that evidence exists. For a stage
that did not run, `WHEELS.json` and `API_INVENTORY.json` retain their complete
schema with status `NOT_RUN` and empty result arrays, and the corresponding
stream file is empty; no evidence is invented.

Stage all seven files only under the exact pending sibling. Write each through
a same-directory owned temporary, flush/close it, and atomically rename it into
place. Create `SHA256SUMS.txt` last. A separate stdlib validator process that
never imports OCP reopens the pending directory, requires exactly seven regular
non-link files, validates schemas/caps and the six listed hashes/sizes, and
rejects every extra entry. After every handle closes, recheck pending identity
and that the final root is absent, then call Windows `MoveFileExW` once with
`MOVEFILE_WRITE_THROUGH` and without `MOVEFILE_REPLACE_EXISTING` to rename the
pending directory to the final root on the same volume. Never create or mutate
the final root before that rename, and never mutate it afterward. Publication
failure leaves the final root absent and the pending bundle retained for Boss
review; there is no retry or overwrite.

Do not preserve wheels, venv/DLL/PYD, caches, environment dumps, or CAD data in
governance. Leave the task root until Boss closeout; later cleanup requires an
exact resolved-root check.

## 4. Exact finite inventory

`probe.py` itself imports only the standard library except that its isolated
inventory mode imports the exact target namespace `OCP`. It is reviewed and
content-frozen before download. It emits canonical UTF-8 JSON
(`sort_keys=True`, compact separators, `ensure_ascii=False`,
`allow_nan=False`). For every exact target below it records:

- module + qualified name and whether each path segment exists;
- runtime object's qualified type, callable/class flag;
- `inspect.signature` value or exact exception;
- `__text_signature__` and `__doc__` (each at most 16,384 UTF-8 bytes,
  recording original byte count/SHA and truncation);
- matching declarations/overloads AST-extracted from the installed stubs-wheel `.pyi`
  files, with exact relative file, file SHA-256 and line numbers;
- a conclusion `AGREE`, `AMBIGUOUS`, `MISSING`, or `CONFLICT`, never an
  inferred call form.

Caps are reader policy, not wheel validity: at most 4,096 wheel members per
archive, 4,096 installed distribution files, 128 `.pyi` files, 16 MiB per
`.pyi`, 128 MiB aggregate `.pyi`, 256 target declarations/overloads, 2 MiB
aggregate captured docs/signatures, JSON nesting depth 32, and 8 MiB per output
JSON. Check counts/sizes before allocation/AST parse; exceeding a cap is
`BLOCKED`. SHA hashing is streamed in 1 MiB chunks.

The exact target set is:

### 4.1 Identity/version

- `OCP.Standard.Standard_Version_s`
- `OCP.Standard.Standard_Version`
- `OCP.Standard.Standard_Version_Complete_s`
- `OCP.Standard.Standard_Version_Complete`
- `OCP.Standard.Standard_Version_String_s`
- `OCP.Standard.Standard_Version_String`

The sole permitted native call is exactly
`OCP.Standard.Standard_Version_Complete_s()` once. Before calling, the installed
stubs wheel must unambiguously declare that exact target as a zero-argument call
returning `str`; otherwise the run is `BLOCKED` without a version call. A
missing runtime target, call exception, non-`str` result, or value whose leading
numeric triple is not exactly `7.9.3` is `BLOCKED`. No alternate version target
is called after any outcome. The other five symbols are inventory-only.
Distribution version `7.9.3.1.1` is recorded separately and is never inferred
to be the runtime OCCT version.

### 4.2 Application/document/tools

- `OCP.XCAFApp.XCAFApp_Application.GetApplication_s`
- `OCP.XCAFApp.XCAFApp_Application.NewDocument`
- `OCP.XCAFApp.XCAFApp_Application.InitDocument`
- `OCP.XCAFApp.XCAFApp_Application.Close`
- `OCP.TDocStd.TDocStd_Document`
- `OCP.TDocStd.TDocStd_Document.Main`
- `OCP.TCollection.TCollection_ExtendedString`
- `OCP.XCAFDoc.XCAFDoc_DocumentTool.ShapeTool_s`
- `OCP.XCAFDoc.XCAFDoc_DocumentTool.ColorTool_s`
- `OCP.XCAFDoc.XCAFDoc_DocumentTool.LayerTool_s`

### 4.3 STEP/IGES readers and status

For each class `OCP.STEPCAFControl.STEPCAFControl_Reader` and
`OCP.IGESCAFControl.IGESCAFControl_Reader`, inventory the class plus exact
members `SetColorMode`, `SetNameMode`, `SetLayerMode`, `SetPropsMode`,
`ReadFile`, `Transfer`, `Reader`, and `ChangeReader`.

Also inventory:

- `OCP.IFSelect.IFSelect_ReturnStatus`
- `OCP.IFSelect.IFSelect_RetDone`
- `OCP.XSControl.XSControl_Reader.PrintCheckLoad`
- `OCP.XSControl.XSControl_Reader.PrintCheckTransfer`
- `OCP.XSControl.XSControl_Reader.GetStatsTransfer`
- `OCP.STEPControl.STEPControl_Reader.FileUnits`
- `OCP.STEPControl.STEPControl_Reader.SystemLengthUnit`
- `OCP.STEPControl.STEPControl_Reader.SetSystemLengthUnit`
- `OCP.IGESControl.IGESControl_Reader.IGESModel`
- `OCP.IGESControl.IGESControl_Reader.SystemLengthUnit`
- `OCP.IGESControl.IGESControl_Reader.SetSystemLengthUnit`
- `OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFiles`
- `OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFile`

### 4.4 Labels, shape/color/layer tools

- classes `OCP.TDF.TDF_Label`, `OCP.TDF.TDF_LabelSequence`,
  `OCP.TDF.TDF_Tool`, and members `TDF_LabelSequence.Length`, `Value`,
  `Append`, `TDF_Tool.Entry_s`;
- `OCP.XCAFDoc.XCAFDoc_ShapeTool` members `GetFreeShapes`, `GetComponents`,
  `GetUsers`, `GetSubShapes`, `GetReferredShape`, `GetLocation`, `GetShape`,
  `IsAssembly`, `IsComponent`, `IsReference`;
- `OCP.XCAFDoc.XCAFDoc_ColorTool` members `GetColor`, `GetColors`, `IsSet`,
  `IsVisible`;
- `OCP.XCAFDoc.XCAFDoc_LayerTool` members `GetLayers`, `GetLayer`, `IsSet`,
  `IsVisible`;
- `OCP.TDataStd.TDataStd_Name.GetID_s` and
  `OCP.TDF.TDF_Label.FindAttribute`.

### 4.5 Topology/location/transform

- `OCP.TopExp.TopExp.MapShapes_s`
- class `OCP.TopExp.TopExp_Explorer` and members `More`, `Next`, `Current`;
- class `OCP.TopTools.TopTools_IndexedMapOfShape` and members `Extent`,
  `FindKey`, `Add`;
- `OCP.TopLoc.TopLoc_Location.Transformation`;
- class `OCP.gp.gp_Trsf` and members `Value`, `TranslationPart`,
  `VectorialPart`, `IsNegative`, `Inverted`, `Multiplied`, `Multiply`,
  `PreMultiply`, `Form`, `ScaleFactor`.

### 4.6 Process-global settings

- `OCP.Interface.Interface_Static.IsPresent_s`
- `CVal_s`, `IVal_s`, `RVal_s`, `SetCVal_s`, `SetIVal_s`, and `SetRVal_s` on
  that same class.

Candidate key strings are evidence metadata only and are **not queried** here:
`read.precision.mode`, `read.precision.val`, `read.step.product.mode`,
`read.step.assembly.level`, `xstep.cascade.unit`, `write.step.unit`,
`write.step.schema`, `read.iges.onlyvisible`, `write.iges.unit`.

No `dir()`-derived name becomes a target. Exact installed filenames/modules
may be enumerated only within the numeric caps; arbitrary object state is never
walked or serialized.

## 5. Exact execution

After registration only:

1. Revalidate foundation tip/tree/clean state, host cell, absent host OCP/dists,
   absent task/final/pending roots, >=1 GiB free disk, and the exact registered
   network authority. Drift prevents controller invocation and is reported to
   the Boss; it creates no filesystem or evidence claim.
2. Create the task root and exact dual-mode `probe.py`. Parent and one bounded
   independent reviewer inspect its imports, exact target tuple, caps, sole
   version call, outputs, and absence of every forbidden constructor/method
   call. Freeze its lower-case SHA-256 as `probe_sha256` before network. The
   controller streams and compares that hash immediately before every child
   launch, immediately after the inventory child exits, and against the exact
   bytes staged as `PROBE.py`; any drift is `BLOCKED` and no changed bytes run.
3. Run the frozen file once in controller mode under exact host Python. At
   The coordinator first uses a separate reviewed stdlib one-liner to stream
   `probe.py` in 1 MiB chunks and compare it to the frozen `probe_sha256`
   immediately before the exact command below. A mismatch aborts before any
   probe byte executes and creates no evidence claim. With a match, controller
   startup establishes the hard limits in section 6 or blocks before its first
   GET. It makes exactly three written-order HTTPS GETs to the frozen URLs, each
   once: status must be 200, final URL/host must be unchanged, and redirects are
   disabled. Preserve the first network outcome; no retry or fallback.

```powershell
& 'C:\Python\Python313\python.exe' -I $inventoryProbe --controller
```
4. Before venv creation verify all three names, exact sizes, streamed hashes,
   wheel tags, archive path safety, caps, complete METADATA/WHEEL/RECORD data,
   frozen requirements, and RECORD payload hashes/sizes.
5. Create `venv --copies` using exact host Python. Set `PYTHONNOUSERSITE=1`,
   `PYTHONDONTWRITEBYTECODE=1`, empty `PYTHONPATH`, and exact task-owned
   `TEMP`, `TMP`, and `PIP_CACHE_DIR`. Record baseline distributions.
6. Install only the three local verified wheels:

```powershell
& $inventoryVenvPython -m pip install --disable-pip-version-check --no-index --no-deps --no-cache-dir --no-compile $inventoryProxyWheel $inventoryOcpWheel $inventoryStubsWheel
```

   PASS requires the installed-distribution delta to be exactly
   `cadquery-ocp-proxy==7.9.3.1.1` and
   `cadquery-ocp-novtk==7.9.3.1.1` and
   `cadquery-ocp-stubs==7.9.3.1.1`; installed files must match the verified
   wheel payloads plus only the explicitly allowed pip-added files in section
   2. No third-party distribution may appear.
7. The controller runs inventory mode once from the task root:

```powershell
& $inventoryVenvPython -I -B $inventoryProbe --inventory
```

   The controller captures its stdout/stderr through bounded binary pipes into
   the exact stream files; shell redirection is not used. Immediately after the
   child exits and before PASS publication, re-enumerate all three installed
   distributions and verify the exact installed-file contract from section 2,
   including an explicit recursive rejection of every `.pyc` and `__pycache__`
   path. Any drift or bytecode file is `BLOCKED`.
8. Launch the separate no-OCP validator, stage and atomically publish the exact
   seven-file bundle as section 3 specifies, and stop. A failed stage records
   only the first failure in `OUTCOME.json`; no later native stage or retry
   follows. Validation after the inventory process is explicitly performed in
   a distinct process that has never imported OCP.

No shell glob selects install/cleanup targets. No command runs from a repo.

## 6. Resource, lease, and network authority

This evidence run has hard, inclusive ceilings rather than estimates:

- 600 seconds total wall time from controller invocation through final
  publication; 120 seconds per HTTPS GET, 180 seconds each for venv creation
  and pip install, 120 seconds for the inventory child, and 30 seconds for the
  validator/publication stage; the global deadline always wins;
- four simultaneously active processes in the controller's process tree,
  affinity to one logical processor, a 268,435,456-byte controller ceiling,
  536,870,912 bytes per worker, and 1,073,741,824 bytes for the whole tree;
- 1,073,741,824 bytes total beneath the resolved task root, including wheels,
  venv, pip temp/cache, streams, and drafts;
- exactly 46,364,506, 3,322, and 2,899,849 response-body bytes respectively,
  64 KiB response headers per GET, 1 MiB network/hash chunks, 8 MiB each for
  stdout and stderr, the section-4 documentation/signature and JSON caps, and
  32 MiB total staged evidence bytes.

At controller startup, before network, stdlib `ctypes` creates two Windows Job
Objects. A supervisor job has active-process limit one, contains only the
controller, permits breakaway, fixes the one-CPU affinity, and caps its
committed memory at 268,435,456 bytes. A worker job enables kill-on-close, caps
active descendants at three, fixes the
same one-CPU affinity, caps each worker at 536,870,912 bytes and all workers at
805,306,368 bytes. The resulting whole tree is at most four live processes and
1,073,741,824 committed bytes. Assignment/configuration failure is `BLOCKED`
before network. Each external command is created suspended with breakaway,
assigned to the worker job, verified as a member, and only then resumed; its own
descendants inherit that job. The supervisor never imports OCP and remains able
to close the worker job, preserve the first failure, and publish a `BLOCKED`
bundle after a child-stage limit.

The controller enforces stage/global deadlines, closes the worker job on a
deadline, memory/process-limit notification, or unexpected descendant, and
waits for confirmed process exit. It measures the resolved task-root tree before
and after every stage and at 250 ms while a child runs; downloads also check it
after every 1 MiB chunk. Every HTTP/body and child-stream reader stops before
accepting limit+1 bytes. A limit event is the first `BLOCKED` outcome, all
handles/processes are closed or killed, and no retry follows.

No GPU is used; ETA is 3–8 minutes. This is one native wheel import plus bounded
introspection, not a build, suite, resolver matrix, benchmark, profiler, stress,
or scaling run. The Boss classifies it as normal functional evidence: no
performance lease is required. After superseding registration, network
authority is limited to exactly the three one-shot pinned HTTPS GETs above,
status 200, no redirect, finite deadlines, and no index/retry/resolution. No
action begins merely because this plan exists.

Excluded: builds, general pip resolution/index access, editable/source install,
repo tests, CAD fixtures/operations, document/reader/tool/setting construction
or calls (other than the single version function), consumer work, merge,
rebase, push, tag, PR, and publication.

## 7. Acceptance, nonclaims, and next gate

PASS requires all three exact wheels/origins and the exact three-distribution
delta, isolated OCP import with no `cadquery`, VTK,
ANYgeometry, ANYfem, or repo source path, independently returned OCCT
version whose leading numeric triple is exactly `7.9.3`, one result for every
exact target, caps respected, complete stub hashes/declarations, and canonical
evidence hashes.

Missing/conflicting/ambiguous targets are recorded individually. Any ambiguity
in the application-owned `NewDocument`/close lifecycle, required reader forms,
or global setting access makes the next native-call gate `BLOCKED`; it never
authorizes guessing. PASS here proves only inventory on this one host cell. It
does not prove any lifecycle, reader construction/read/transfer, global-state
restoration, CAD correctness, assemblies/metadata/units/identity/transforms,
memory safety, performance, another wheel cell, or provider capability.

Only after Boss accepts this inventory may a separately content-addressed safe
native lifecycle/call evidence plan select exact observed call forms and invoke
them. Only after that evidence closes may a capability-zero STEP+IGES XDE
reader implementation plan be registered. Tessellation, translation/write,
integrated activation, optional BREP, qualification, geometry, and consumers
retain the frozen order.
