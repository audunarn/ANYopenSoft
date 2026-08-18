# ANYfileio-occt OCP 7.9.3.1.1 call-shape inventory V3 recovery plan

Date: 2026-08-13 (Europe/Oslo)

Status: registration candidate and source-freeze contract. The V2 blocker ruling
authorizes creation and static review of this plan and one corrected stdlib-only
V3 `probe.py`. It does not authorize the controller, wheel reuse/copy, venv,
install, OCP import/call, evidence staging, provider edits, or publication.

## 1. Objective and exact ancestry

Run one offline recovery attempt for the registered OCP 7.9.3.1.1 call-shape
inventory. Reuse the three already downloaded, pinned V2 wheel bytes after
streaming hash/size verification. Correct only the Wheel/RECORD interpretation:
an explicit safe empty ZIP directory entry is not an installed file and need
not have a RECORD row. Every non-directory member retains the exact V2 RECORD,
hash, size, metadata, isolation, resource, and independent-validation gates.

Governing inputs:

- release-clearance program SHA-256
  `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`;
- V2 plan SHA-256
  `89EA6939C477A22E18A84ECD4805B298DDD601ADCE24661A47F2E9C31BC2CE07`;
- V2 frozen probe SHA-256
  `3A86FB437E804A0CB0ED205C1A41FF536B61300F38AE4F08945BFEF7B0C3EED6`,
  139,062 bytes/3,238 LF/0 CR;
- accepted core `5513881827cdee9fd337497a2730a5912d8ea751`;
- native-foundation provider tip
  `23b441c3fcabb5bf4cf077daca882b984f978b42`, tree
  `a996a21a31c775660eb9dac3d491160231ba8cc1`.

V3 uses attempt `4`. Its immutable history is exact attempts 1 and 2 from V2
plus attempt 3:

- status `BLOCKED`, exit `2`, elapsed `6.254012` seconds;
- plan/probe identities exactly V2 above;
- first failure stage `wheel`, message
  `directory member not represented in RECORD: cadquery_ocp_novtk.libs/`;
- the three exact GETs each completed once with status 200;
- installation, OCP import/version call, and 105-target inventory were `NOT_RUN`;
- no secondary failure; canonical V2 final bundle published.

## 2. Immutable V2 inputs and distinct V3 ownership

V2 inputs are read-only and never cleaned, renamed, rewritten, or installed
from directly:

```text
V2 task:  C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v2
V2 final: C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2
```

Require V2 final to contain exactly seven regular non-reparse files/145,235
bytes. Protect `OUTCOME.json` SHA-256
`A65E85D0A4F0CA01020E0C9EAA76B6683BF29AFE7289B4F55B1CDED839821042`
and `SHA256SUMS.txt` SHA-256
`F4CAD6876D537DD905A7AAECB4FE896A87D225B5ED06D2E54C97CB5155A3A993`;
revalidate all six listed payloads. Preserve the older accepted pending receipt
and its already frozen hashes as required by V2.

V3 owns only these distinct paths:

```text
plan:    C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CALL_SHAPE_EVIDENCE_V3_RECOVERY_PLAN.md
task:    C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v3
final:   C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3
pending: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.pending
sentry-temp: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.staging-sentry.tmp
sentry:      C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.staging-sentry
```

At source freeze the V3 task contains only `probe.py`; final, pending, and both
sentries are absent. At execution the controller may create only task-owned
`wheelhouse`, `venv`, `tmp`, and draft streams/JSON, then the canonical evidence.

## 3. Exact offline wheel reuse

No network API or network fallback exists in the V3 probe. Remove the V2
WinHTTP/download implementation and prove statically that controller execution
has no HTTP client, URL-open, socket, pip index, retry, or resolver path.

Read only these V2 wheelhouse files, in this order:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | 46,364,506 | `3390BE6D8199A50B01AE0137A60F56D0CFECD8753DBEE08532BBBEB8B7169682` |
| `cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | 3,322 | `CA4164EC4B54956D9FC3E68C67D555B5486CB963C2F71E18DF005BA16B921C91` |
| `cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | 2,899,849 | `5ECBA090DF1ADA12C558FF4A1B49C61D5155EDC8CB3411067A785E3B43F4B359` |

Preflight requires the V2 wheelhouse to be normal/non-reparse with exactly
these three regular non-link files and the V2 task to contain only its frozen
probe, empty normal `tmp`, and that wheelhouse. Stream-hash each source with
one-MiB bounded reads before use. Copy it once to an exclusive `.part` under
the V3 wheelhouse, fsync/close, no-replace rename, then independently rehash
the V3 copy. Never modify or delete a V2 byte. Pip consumes only V3 copies with
`--no-index --no-deps --no-cache-dir --no-compile`.

Compute one inclusive local-reuse deadline as
`min(operation_deadline, reuse_started + 120 seconds)` immediately before the
three-wheel loop. That one deadline covers all three source hashes, copies,
fsync/renames, source stability rechecks, and destination rehashes; it is never
renewed per wheel.

`WHEELS.json` records three ordered `LOCAL_REUSE` inputs, exact source paths,
source/destination hashes and sizes, with no HTTP/download claim. PASS requires
all three local-reuse and archive records `VERIFIED`.
For a BLOCKED receipt, independent validation permits a verified ordered reuse
prefix plus at most one terminal `BLOCKED` reuse record. That record contains
the exact same typed stage/message as `OUTCOME.first_failure`; no later reuse
record exists. A failure after reuse may instead retain all three VERIFIED
records. `STARTED`, a nonterminal BLOCKED record, or erased attempt is invalid.

## 4. Corrected explicit-directory contract

For every ZIP member, before RECORD comparison:

1. reject NUL, backslash, colon, absolute paths, empty/`.`/`..` segments,
   normalization changes, duplicate exact names, or case-fold collisions;
2. classify a directory only when its name has exactly one terminal `/`, its
   logical name is otherwise canonical, `ZipInfo.is_dir()` is true, and the
   exact pinned create-system/mode/flag/compression attributes below prove
   Unix `S_IFDIR` and not `S_IFLNK`;
3. permit low DOS attributes only `0` or directory bit `0x10`, reject every
   attribute tuple outside the exact pinned per-wheel set, and record it;
4. require `file_size == 0`, `compress_size == 0`, `CRC == 0`, and a bounded
   archive read that returns immediate EOF; reject encrypted/unsupported flags;
5. include the safe directory in the total-member and expanded-size caps and
   in ordered evidence, but exclude it from the RECORD-required file set.

Every non-directory member must have exactly one RECORD row and must match the
exact pinned regular-file attribute tuple/count below, including
`stat.S_ISREG`, create system, full external attributes, UTF-8 flag, and deflate
compression. Require `set(RECORD rows) == set(non-directory members)`; a
directory RECORD row is extra and fails. Retain empty hash/size only for RECORD
self; stream-verify SHA-256 and exact size for every other file.

Freeze and independently validate these observed counts:

| Wheel | Total | Files/RECORD rows | Safe explicit directories |
| --- | ---: | ---: | ---: |
| novtk | 720 | 398 | 322 |
| proxy | 7 | 5 | 2 |
| stubs | 329 | 329 | 0 |

Exact directory tuples `(create_system, external_attr, flag_bits,
compress_type, count)` are novtk `(0, 0x41FF0010, 0, STORED, 322)` and proxy
`(3, 0x41ED0000, 0x800, STORED, 2)`; stubs has none. Exact regular-file tuples
are novtk `(0, 0x81B60000, 0, DEFLATED, 398)`, proxy
`(3, 0x81A40000, 0x800, DEFLATED, 5)`, and stubs
`(0, 0x81B60000, 0, DEFLATED, 328)` plus its RECORD self
`(0, 0x81B40000, 0, DEFLATED, 1)`. The DOS directory bit is optional only as
frozen by these tuples. No other Wheel/RECORD rule is relaxed.

## 5. Retained V2 execution and evidence gates

Except for V3 paths, attempt/history, offline local reuse, and section 4, retain
the V2 probe behavior byte-for-semantics:

- exact CPython 3.13.9 final / Windows 11 AMD64 / 64-bit host and absent host
  OCP and cadquery distributions;
- exact clean foundation commit/tree and process-contained worker job;
- exact wheel METADATA/WHEEL fields, raw bytes, RECORD rows, archive/member,
  installed-file, no-bytecode, task/evidence/JSON/text/stub limits;
- copied venv, exact three-distribution install delta, and identical post-call
  installed-file/no-`.pyc` audit;
- isolated `OCP` import, sole qualified call
  `OCP.Standard.Standard_Version_Complete_s()` once after one installed stub
  proves `() -> str`, requiring leading runtime triple `7.9.3`;
- exact ordered 105-target inventory and truthful per-target conclusions;
- one worker Job Object, suspended assignment, bounded streams/deadlines/disk,
  synchronous `ActiveProcesses == 0` grace, and no residual process;
- exactly seven canonical evidence files, independent `-I -B` no-OCP validator,
  fsync/hash recheck, and one no-replace same-volume final rename.

Global wall remains 600 seconds; all three local reuses share one inclusive
120-second stage; venv/install/inventory remain 180/180/120 seconds; validator plus
publication remains 30 seconds. Existing 1 GiB task, 32 MiB evidence, 8 MiB
per stream/JSON, one-MiB chunk, member/file/stub/depth, worker process and memory
caps remain exact. First failure is write-once; cleanup facts are ordered
secondary failures. Preserve the first result and never retry.

V3 `OUTCOME.json` is attempt 4, includes exact attempts 1-3 and immutable V2
bundle reference, and truthfully distinguishes local reuse from downloads.
PASS requires all archive/install/API/105-target/validator/publication gates;
otherwise publish a canonical BLOCKED receipt when safe.

## 6. Source freeze, review, and separate execution gate

Under the V2 blocker ruling, create only the V3 task root and corrected
stdlib-only `probe.py`. The probe embeds this plan's final SHA-256. Static review
must prove:

- exact V2/V3 paths, wheel identities, attempt history, 105 targets, and sole
  native call;
- no network implementation or call site;
- only the directory exception in section 4; exact RECORD checks for files;
- exact local-copy ownership, resource/containment, canonical validation, and
  immutable V2 checks;
- successful inert AST parse and no non-stdlib static dependency.

Stream-hash and report the plan and probe path/SHA/bytes/LF/CR extents. One
independent read-only audit must return CLEAN before requesting one-shot
execution authority. Immediately before any later invocation, externally
rehash both identities and require V3 evidence paths absent. No execution is
authorized by this plan's preparation.

Explicit exclusions: network; V2 mutation; provider/repository/source edits;
application/document/reader/tool/setting construction or calls; CAD fixtures;
public capabilities; geometry/consumers; builds; tests/benchmarks; branch,
commit, merge, push, tag, PR, wheel/package publication, or release creation.
