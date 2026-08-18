# ANYfileio-occt OCP 7.9.3.1.1 call-shape inventory V4 recovery plan

Date: 2026-08-13 (Europe/Oslo)

Status: registration candidate and recovery decision only. This file authorizes
no probe creation or edit, controller invocation, wheel copy, venv, install,
OCP import/call, evidence staging, cleanup, network, or provider work until its
exact SHA-256 and extent are accepted and a later source/execution gate is
explicitly released.

## 1. Decision and immutable provenance

Attempt 4 produced a truthful canonical `BLOCKED` receipt because its frozen
novtk `Requires-Dist` expectation was stale. The exact hash-pinned wheel is
internally authentic and declares an exact-version dependency. V4 therefore
tightens the expected value; it does not relax metadata comparison or accept a
range, normalization, alternate dependency, or fallback.

Immutable governing inputs:

- release-clearance program SHA-256
  `4487A9E12DB0CC010A30EDF8CC1DBBDA9E2B659D5681C80BBECD76F67564D0C8`;
- V3 plan SHA-256
  `DFA54CAED0897847F6E11709D5B5149F292186779ADD1F21144E3A5F1EA6F689`,
  11,240 bytes/211 LF/0 CR;
- V3 probe SHA-256
  `EE0ACDBF4F7ECBBA27C9967D46141FFC216DA5BED4075C0DECB437CE10B53CDC`,
  149,639 bytes/3,400 LF/0 CR;
- native-foundation commit
  `23b441c3fcabb5bf4cf077daca882b984f978b42`, tree
  `a996a21a31c775660eb9dac3d491160231ba8cc1`;
- accepted ANYfileIO core source `48c6423c2aaf1f94f7bea8e7a971adf99500a91f`.

The V3 final receipt is immutable at:

```text
C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3
```

It contains exactly seven regular non-reparse files/158,168 bytes. Protect:

- `OUTCOME.json` SHA-256
  `34566875ECA734F52C461E0761B7C1F54D33B25DA5F15625C4FD4BB26C339E7A`;
- `WHEELS.json` SHA-256
  `F9A4B0B529550CD5ADCB98B40E3608A9B1E7535E971A8EAFA468F1595EB670D6`;
- `SHA256SUMS.txt` SHA-256
  `C32B17148F21EFDC73C67625D53BFA3E9ADC600305FB55E227E7A71136A170BD`;
- every size/hash listed by that manifest.

Attempt 4 is appended to the exact attempts 1-3 history:

- status `BLOCKED`, exit `2`, elapsed `0.734903` seconds;
- plan/probe identities exactly V3 above;
- first failure type/stage `BLOCKED` / `wheel` with message
  `Requires-Dist mismatch for cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl`;
- all three ordered `LOCAL_REUSE` records were `VERIFIED`;
- install, OCP import/version call, and API/105-target inventory were `NOT_RUN`;
- stdout/stderr were empty and there was no secondary failure.

V4 is attempt `5`. No earlier receipt, task, probe, wheel, sentry, pending path,
or evidence byte may be deleted, cleaned, pruned, renamed, rewritten, or reused
as V4 output.

## 2. Exact expected-versus-observed correction

The frozen V2 plan and V2/V3 probes expected one parsed value:

```text
cadquery-ocp-proxy
```

Exact expected parsed bytes:

- UTF-8 length: 18 bytes;
- hex: `63616471756572792D6F63702D70726F7879`;
- SHA-256: `0CCEE1D254AAE811CFC2250016A06ABBB8738BB6887E8E11EB2C7A2FB5C24AF1`.

The corresponding expected CRLF metadata line was:

```text
Requires-Dist: cadquery-ocp-proxy\r\n
```

- length: 35 bytes;
- hex:
  `52657175697265732D446973743A2063616471756572792D6F63702D70726F78790D0A`;
- SHA-256: `55BBAE0FCBFD37E2F32799A87AAF868E6E397F252A22ACDE3EFF23A144900373`.

The authoritative cached novtk wheel is exactly:

- file `cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl`;
- 46,364,506 bytes;
- SHA-256
  `3390BE6D8199A50B01AE0137A60F56D0CFECD8753DBEE08532BBBEB8B7169682`.

Its member
`cadquery_ocp_novtk-7.9.3.1.1.dist-info/METADATA` is 910 bytes, SHA-256
`A9BAD4F8A14BBB07D3026A51D1586CA84B2EF09C59840AF5015257347B4AECE2`.
At line 10, byte offset 384, it contains exactly:

```text
Requires-Dist: cadquery-ocp-proxy==7.9.3.1.1\r\n
```

Exact observed parsed value:

- UTF-8 length: 29 bytes;
- hex:
  `63616471756572792D6F63702D70726F78793D3D372E392E332E312E31`;
- SHA-256: `3AD4310AA171A98F05E4E629F3ABE70D389F0444A503D140F0D1C258E35D1C7A`.

Exact observed CRLF line:

- length: 46 bytes;
- hex:
  `52657175697265732D446973743A2063616471756572792D6F63702D70726F78793D3D372E392E332E312E310D0A`;
- SHA-256: `6C19A0E47C85D2AE0F4AD783116E39A9D6658731AA89E575718578DA205B0CBC`.

The wheel's RECORD member is 35,131 bytes, SHA-256
`D229DE2A24A5CC22FF00ED773FA401F0CE4188A23216CF9B56D4CAD998921320`.
Its exact binding is:

```text
cadquery_ocp_novtk-7.9.3.1.1.dist-info/METADATA,sha256=qbrU-KFLuwfTAmpR0VhsqEsu8JxZhAr1AVJXNHtK7OI,910
```

Independent hashing reproduces that size and digest. The separately pinned
proxy wheel is `cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl`, 3,322 bytes,
SHA-256 `CA4164EC4B54956D9FC3E68C67D555B5486CB963C2F71E18DF005BA16B921C91`,
and its RECORD-bound metadata identifies `cadquery-ocp-proxy==7.9.3.1.1`.

Safety decision: the artifact is consistent; the expectation is defective.
V4 changes only the novtk probe constant from
`("cadquery-ocp-proxy",)` to
`("cadquery-ocp-proxy==7.9.3.1.1",)`. Both archive and independent receipt
validators continue to require exact ordered equality. This is stricter and
version-coherent with the pinned proxy artifact; it introduces no dependency
range, resolver authority, alternate artifact, or compatibility inference.

## 3. Distinct V4 ownership and offline inputs

V4 owns only these currently absent paths:

```text
plan:    C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CALL_SHAPE_EVIDENCE_V4_RECOVERY_PLAN.md
task:    C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v4
final:   C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V4
pending: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V4.pending
sentry-temp: C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V4.staging-sentry.tmp
sentry:      C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V4.staging-sentry
```

Read-only V4 sources are the three exact V3 wheelhouse files, in order:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl` | 46,364,506 | `3390BE6D8199A50B01AE0137A60F56D0CFECD8753DBEE08532BBBEB8B7169682` |
| `cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl` | 3,322 | `CA4164EC4B54956D9FC3E68C67D555B5486CB963C2F71E18DF005BA16B921C91` |
| `cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl` | 2,899,849 | `5ECBA090DF1ADA12C558FF4A1B49C61D5155EDC8CB3411067A785E3B43F4B359` |

Before any later execution, require the V3 task to contain only its exact probe,
empty normal `tmp`, and normal `wheelhouse` with those three regular non-link
files. Stream-hash sources, copy under one shared inclusive 120-second deadline
to exclusive V4 `.part` files, fsync/close, no-replace rename, independently
rehash V4 copies, and recheck source stability. Pip may consume only the V4
copies with `--no-index --no-deps --no-cache-dir --no-compile`. No network or
fallback implementation may exist.

## 4. Inherited behavior and allowed source delta

Except for the following finite bookkeeping, V4 inherits the registered V3
plan and accepted V3 probe byte-for-semantics:

1. distinct V4 task/final/pending/sentry paths and V4 plan identity;
2. attempt `5`, exact attempts 1-4 history, and immutable V3 predecessor receipt;
3. V3 wheelhouse as the read-only local-reuse source;
4. the one exact novtk `requires_dist` literal in section 2.

Retain unchanged:

- exact wheel ZIP/member/attribute/directory/RECORD/hash/metadata gates;
- exact CPython 3.13.9 Windows AMD64 host and isolated three-distribution delta;
- exact no-bytecode and installed-file audit;
- sole qualified call
  `OCP.Standard.Standard_Version_Complete_s()` once after stub proof;
- exact ordered 105 targets and truthful classifications;
- one worker Job Object, deadlines, stream/process/memory/disk/count/depth caps,
  synchronous zero-process grace, and first-failure preservation;
- canonical seven-file evidence, independent `-I -B` no-OCP validator, fsync,
  identity/hash recheck, and one no-replace publication rename;
- global 600-second wall, shared 120-second reuse, 180-second venv/install,
  120-second inventory, and 30-second validation/publication boundaries.

A source-stage reversal must show that, after substituting only the four finite
items above, the V4 probe reconstructs the accepted V3 probe. Any other semantic
delta stops and requires a superseding plan.

## 5. Staged authority and one-shot boundary

This plan's submission creates only this governance file. After its exact
identity is accepted, a separate source-stage authorization may create the V4
task root and one stdlib-only `probe.py`; it must never edit the V3 probe.
Freeze and report the new probe SHA-256/bytes/LF/CR, inert AST/no-network/static
checks, exact-delta reversal, and one independent read-only audit.

Only after a further explicit one-shot execution grant may a coordinator:

1. externally re-hash the accepted plan and V4 probe;
2. require all V4 final/pending/sentry paths absent and all V1-V3 provenance
   byte-exact;
3. invoke the exact controller once offline;
4. preserve the first canonical PASS or BLOCKED seven-file result and stop.

There is no retry, fallback, tuning, cleanup, provider work, or implied follow-on
native call. A BLOCKED outcome remains canonical evidence. Even after PASS,
task/wheel/probe/receipt/evidence/sentry/temp cleanup requires independent
terminal verification, Boss closeout, an exact inventory, and explicit deletion
authority. Canonical evidence and cached source artifacts required for provenance
are never cleanup targets.

Explicit exclusions: download/network/index/resolution; mutation or cleanup of
V1-V3 paths; installation or OCP import during planning/source freeze; provider
or repository edits; CAD data; application/document/reader/tool/setting calls;
public capability activation; geometry/consumer work; builds, broad tests,
benchmarks, branch/commit/merge/push/tag/PR, package publication, or release.
