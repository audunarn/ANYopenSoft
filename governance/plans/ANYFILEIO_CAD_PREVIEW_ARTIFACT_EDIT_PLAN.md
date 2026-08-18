# Editing-agent plan — ANYfileIO OCP-free CAD preview artifacts

**Status:** proposed for ecosystem-Boss registration. This file grants no edit,
branch, worktree, test, build, resolver, merge, push, or publication authority
until its exact absolute path, byte extent, line count, and SHA-256 are accepted.

## 1. Objective and frozen authority

One logical editor, **Sigrid** (`/root/sigrid_anyfileio_cad_artifact`), will
implement schema-1 preview persistence in the NumPy-only ANYfileIO core. The
slice owns deterministic ZIP/NPY writing, strict OCP-free opening, eager
manifest and occurrence validation, one-shot lazy prototype loading, optional
retained-source snapshotting, atomic publication, and focused synthetic tests.

It implements the exact public calls frozen by the accepted contract:

```python
def write_preview_artifact(
    document: CadDocument,
    destination: str | os.PathLike[str],
    *,
    tessellation: CadTessellationResult | None = None,
    cancellation: CancellationCheck = None,
) -> str: ...

def open_preview_artifact(
    artifact: str | os.PathLike[str],
    *,
    retained_source: str | os.PathLike[str] | None = None,
) -> CadDocument: ...
```

The writer returns the lower-case SHA-256 of the committed artifact. The
reader constructs a closed, session-free `CadDocument` and imports neither a
backend nor OCP. The module `__all__` contains exactly the two functions. Both
are additively re-exported from `anyfileio.__init__` because every accepted
public CAD-neutral type and operation already uses that facade.

Authoritative inputs:

- source plan
  `C:\Users\AudunArnesenNyhus\Downloads\ANYfileIO_OCCT_CAD_pipeline_Codex_Sol_Ultra_plan.md`,
  SHA-256
  `473523BD3BD28FC88487A961C29BF7B640592F415B981236C558FA963AF1E414`;
- registered baseline addendum
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`,
  SHA-256
  `9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`;
- registered M2 allowlist
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M2_GOVERNANCE_ALLOWLIST_ADDENDUM.md`,
  SHA-256
  `87A30E18F4DCF6D7CE194AC4CE05909BC149027128A8F2CE5EFB421310185697`;
- accepted frozen contract commit
  `5f605d0bcd63de9e45230588abf7f8b211a23b20`;
- accepted CAD public-types chain ending at
  `a01c9a81ef5690873c802d9832c672ec77c6a474`;
- accepted semantic-runtime commit
  `1f0b5780df7f025fc786fd3db2cba9da2104fb5c`;
- registered operations plan
  `C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_CAD_OPERATIONS_EDIT_PLAN.md`,
  SHA-256
  `5EF3F06E58D70EEA029E6BF74C2469F2AA735E5FED706B1221A6DE9EB966D452`;
- Boss-accepted operations chain ending at the exact base in section 2.

Any change to schema name/version, member set/order, JSON key set, NPY rules,
cache-key properties, public signatures, artifact error semantics, core record
meaning, or merge order is a `PUBLIC CONTRACT CHANGE` / `PLAN DEVIATION` and
stops implementation.

## 2. Repository, exact base, branch, and isolated worktree

```text
repository:        C:\Github\ANYfileIO
remote identity:   https://github.com/audunarn/ANYfileIO.git
accepted base:     da8fd8dd562dfd266124a222973e43d65f7db064
base tree:         1c101bd525f858f8ac3f560db575d720dff51e45
sole base parent:  7e7538e76a847cf700fee2535cdeae5c1c046c78
source branch:     codex/anyfileio-cad-operations
new branch:        codex/anyfileio-cad-artifact
branch upstream:   none
isolated worktree: C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact
```

At plan creation the source worktree is clean with no upstream; the proposed
branch and worktree do not exist. After registration, create exactly that
branch/worktree directly from the full base, without fetch, pull, merge,
rebase, or precursor commit. Primary checkout and every earlier worktree are
read-only comparison paths.

Produce one coherent direct-child commit with subject:

```text
feat: add OCP-free CAD preview artifacts
```

No nested writer, delegated hunk, fixup commit, merge, push, tag, PR, or
publication is authorized. Before worktree creation and again before commit,
verify the full base/tree/parent, remote, clean state, absent upstream,
protected digests/blobs, and exact path ownership.

## 3. Protected ancestry and evidence

Frozen order:

```text
0d2c7f8ef1b17f42f667d6183125e51cb650a70d  Forseti M2
5f605d0bcd63de9e45230588abf7f8b211a23b20  contract freeze
085e92c5ff144fb0f9f96db4afc68c4d2dc7f099  CAD public types
a01c9a81ef5690873c802d9832c672ec77c6a474  discovery correction
1f0b5780df7f025fc786fd3db2cba9da2104fb5c  semantics runtime
7e7538e76a847cf700fee2535cdeae5c1c046c78  CAD operations
da8fd8dd562dfd266124a222973e43d65f7db064  ownership correction / base
```

Reproduce these raw binary-diff proofs with the same argument order and hash
the raw stdout bytes, never terminal-rendered or CRLF-transcoded text:

| Slice | Raw bytes | Insertions/deletions | SHA-256 |
| --- | ---: | ---: | --- |
| M2 | 3,380 | 15 / 7 | `4B2763FC72F0F1FA53E808E28E3D6DEBE0973DD6DE0B2D50E0C0F6A6FA229068` |
| Contract | 107,797 | 2,172 / 0 | `39139AB6DCD18787232F0ECBA0F9535B9D2C0EDC8AE8CAC07CF50DD90222047E` |
| CAD types | 99,478 | 2,425 / 5 | `AFAADC1DFEE6B8717DF596ABA36D6709999110517858CF59A3827568FBD89B94` |
| Semantics runtime | 42,266 | 644 / 83 | `8C18B315CF3745CA18EDC96D43E32983EEFC922E2F64D5BA58E9150C4D4EF7B6` |
| CAD operations, `1f0b5780df7f025fc786fd3db2cba9da2104fb5c` through `da8fd8dd562dfd266124a222973e43d65f7db064`, exact seven paths | 74,252 | 1,699 / 7 | `BD411A6480DCD81AD828A72A46A3CDCC849C4F9E91B6CC17A49618F4F7F559AC` |

Exact proof commands and path order are inherited from the registered
operations plan for M2/contract/types/runtime. The operations proof uses:

```text
git diff --binary 1f0b5780df7f025fc786fd3db2cba9da2104fb5c da8fd8dd562dfd266124a222973e43d65f7db064 -- src/anyfileio/__init__.py src/anyfileio/cad_operations.py src/anyfileio/formats.py tests/test_backends.py tests/test_cad_operations.py tests/test_formats_and_cli.py tests/test_layering.py
```

Frozen contract files:

| Path | Git blob | SHA-256 of blob bytes |
| --- | --- | --- |
| `docs/CAD_BACKEND_CONTRACT.md` | `f4ecd214cdd2ae448c91a6e8d46d4101b34a4ddb` | `723FE2EF33E582F3AE9A3A60A77AB1DCD709F4C838D27F0E1C8B73134D9FF374` |
| `docs/ANYGEOMETRY_0_2_ADAPTER.md` | `f828cc4a0ab6c1c93cb569c45af5191dfd723e34` | `9E79744135C83FC10DE4C8EB231CC57B29B79AB967DF7C5468F19168448D1AA8` |
| `DEPENDENCY_MATRIX.md` | `ed53d6d8fc5d315c3c5e31139032fea4353c8e60` | `BB2E28A41BD2DB773E1A501113B54E9936F0708C34F21C452C2235C48091D2E3` |

Consumed implementation files are protected from edits:

| Path | Git blob |
| --- | --- |
| `src/anyfileio/cad.py` | `baa7a5fde9db1da0951def9ff0abe1cd46626c7d` |
| `src/anyfileio/cad_backend.py` | `fca05afc5f2daa7d4cdd5677d774628e67de7980` |
| `src/anyfileio/cad_operations.py` | `4e9d5585d3e19da4b4a97b504466e5550b7ee845` |
| `tests/test_cad_contract.py` | `d9420623a2fcaf9ed61d47a44ca13587cf9fb31c` |

The implementation may consume private integration boundaries already frozen
for the codec, including `cad._source_identity_for_manifest`,
`cad._bind_tessellation`, `CadDocument._from_preview_artifact`, and the
accepted source/temporary ownership, cancellation, hashing, and drift helpers
in `cad_operations`. For retained source, consume the accepted private
`_copy_source_snapshot(..., expected_sha256=...)` companion so the codec
receives the path, computed digest, and creation-time dev/ino identity; do not
re-adopt ownership through a later pathname stat. It does not edit or duplicate
their record validation, provider SPI, or operations behavior.

## 4. Exact four-path ownership

Every edit target resolves beneath the registered isolated worktree. Equivalent
paths elsewhere are not edit targets. No glob ownership exists.

### 4.1 New whole module

```text
src/anyfileio/cad_artifact.py
C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src\anyfileio\cad_artifact.py
```

The path is absent at the base. Sigrid owns the complete new file and only the
schema-1 codec described here.

### 4.2 Additive facade hunk

```text
src/anyfileio/__init__.py
C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\src\anyfileio\__init__.py
```

Starting blob `4d1a1ba22c8a5c56c8c63de6cbcd67eb36b97aa2`, 5,007 bytes.

Add exactly one import after the existing `cad_operations` import and exactly
two matching `__all__` entries:

```python
from .cad_artifact import open_preview_artifact, write_preview_artifact
```

Do not reorder, delete, or alter any accepted CAD type/operation, semantic
facade, format, diagnostics, version, or other export.

### 4.3 New focused test module

```text
tests/test_cad_artifact.py
C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\tests\test_cad_artifact.py
```

The path is absent at the base. It owns synthetic, tiny, provider-free codec
tests only. It must not add committed ZIP/NPY fixtures or large generated data.

### 4.4 Exact layering tuple hunk

```text
tests/test_layering.py
C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-cad-artifact\tests\test_layering.py
```

Starting blob `aa75e3174611a20ecfe07aea8ea5a7d27af2c9f5`, 6,523 bytes. Change only
`CAD_NEUTRAL_MODULES` to include `"cad_artifact.py"`, preserving every other
allowlist, test, semantic rule, and optional-import rule byte-for-byte.

The final combined diff is exactly these four paths: two additions and two
bounded modifications.

## 5. Schema constants, cache identity, and projections

Module constants are exact:

```text
schema name:     anyfileio.cad-preview
schema version:  1
protocol:        1
MIME intent:     application/vnd.anyfileio.cad-preview+zip
cache prefix:    cad-preview-key-v1:
```

Before deriving a cache id, recompute the manifest source identity through the
accepted core helper and require equality with the selected
`CadTessellationResult.source_identity`.

The cache-id hash input is canonical UTF-8 JSON of exactly these long contract
property names:

```text
source_sha256
source_name
source_format
effective_source_length_unit
normalized_read_options
backend_id
backend_version
backend_compatibility_version
binding_distribution
binding_version
occt_version
source_identity
normalized_tessellation_options
preview_artifact_schema_name
preview_artifact_schema_version
```

Use sorted keys, compact separators, `ensure_ascii=False`, and
`allow_nan=False`. The id is the prefix plus lower-case SHA-256. The serialized
`cache_key` projection instead uses the separately frozen names
`read_options`, `tessellation_options`, `artifact_schema`, and
`artifact_version`; all component values and the id must match the long-name
identity. No label from input JSON is trusted.

`manifest.json` is raw canonical UTF-8 JSON. Decode with duplicate-key and
non-finite-number rejection; re-encode canonically and require byte equality.
Its top-level object has exactly:

```text
schema, version, protocol_version, backend, cache_key, document, meshes, entries
```

Require exact recursive key sets for backend; cache key; read and tessellation
options; document; prototype, occurrence-projection, and shape records; entity
references; diagnostics; meshes; and each arrays map. Every required nullable
value is present as JSON null. Reject unknown/missing keys, unknown enums,
duplicate logical ids, noncanonical numbers/strings, and inconsistent repeated
source/backend/options/schema values.

The `document` projection has exactly the contract fields. Prototype and shape
records use exact public field names. Occurrence JSON has only `id`, `cad_ref`,
`array_row`, `world_bounds_m`, and `name`; it never duplicates the five
array-backed values. Rows follow strictly ascending occurrence id and
`array_row` is exactly `0..n-1`.

`CadEntityRef`, `CadDiagnostic`, bounds, topology counts, immutable details,
colors, layers, roots, foreign keys, and public records are reconstructed
strictly through accepted core constructors. JSON-only positive integer ids
remain Python integers. Only ids encoded in occurrence NPY arrays—prototype,
occurrence, and parent ids—must preflight as fitting unsigned 64-bit. Root
parent is zero. Choose uint32 only if the maximum encoded value fits; otherwise
use uint64. An encoded id above uint64 fails closed before temporary creation.

## 6. Exact deterministic ZIP/NPY envelope

Required global members:

```text
manifest.json
occurrences/prototype_ids.npy
occurrences/parent_ids.npy
occurrences/local_transforms.npy
occurrences/accumulated_transforms.npy
occurrences/visibility.npy
```

For each positive prototype id, rendered as canonical decimal without leading
zeroes:

```text
prototypes/<id>/origin.npy
prototypes/<id>/positions.npy
prototypes/<id>/triangles.npy
prototypes/<id>/face_offsets.npy
prototypes/<id>/edge_offsets.npy
```

`normals.npy` and `edge_indices.npy` occur exactly when the corresponding
array is non-null. `manifest.json` is first; every other member follows in
ascending ASCII-byte order. Names are unique, UTF-8, relative, slash-separated,
and contain no empty, `.`, or `..` component.

Each `ZipInfo` is exact:

```text
compress_type=ZIP_STORED
date_time=(1980,1,1,0,0,0)
create_system=3
create_version=20
extract_version=20
flag_bits=0
internal_attr=0
external_attr=(0o100600 << 16)
extra=b""
comment=b""
```

The archive comment is empty. No encryption, data descriptor, extra field,
ZIP64 member/EOCD/locator, duplicate central entry, noncanonical local/central
header, or trailing bytes are accepted. Writer uses `allowZip64=False` and
preflights ordinary ZIP member-count, member-size, offset, and total-size
limits; `LargeZipFile`, overflow, or a would-be ZIP64 value becomes
`CadArtifactError` without target replacement. Reader rejects ZIP64 rather
than allowing `zipfile` to normalize it away.

All NPY member bytes are produced with:

```python
numpy.lib.format.write_array(
    stream,
    normalized_array,
    version=(2, 0),
    allow_pickle=False,
)
```

Reader checks magic/version/header before allocating and rejects object dtype,
Fortran order, non-native byte order, wrong dtype/shape, trailing bytes,
declared/data-length mismatch, and excessive allocation. Reads use
`allow_pickle=False`.

### 6.1 Frozen local reader-resource policy

Schema 1 remains an interchange schema, not a promise that every conforming
archive fits every machine. This implementation freezes the following finite
integer **local reader-policy** caps. Exceeding one may leave an artifact
schema-1-valid, but this reader and its self-validating writer fail closed with
`CadArtifactError` code `cad.preview.resource_limit` and immutable diagnostic
details `resource`, `limit`, and `observed`. These values are not serialized,
do not participate in the cache key, and do not narrow schema-1 validity.

| Resource | Inclusive cap |
| --- | ---: |
| complete artifact bytes | `1_073_741_824` |
| `manifest.json` bytes | `8_388_608` |
| one NPY header bytes | `65_536` |
| one stored non-manifest member bytes | `268_435_456` |
| aggregate stored non-manifest member bytes | `805_306_368` |
| one decoded ndarray data bytes | `268_435_456` |
| aggregate decoded ndarray data bytes | `805_306_368` |
| archive member count, including `manifest.json` | `16_384` |
| one decoded ndarray element count | `67_108_864` |
| aggregate decoded ndarray element count | `134_217_728` |
| JSON nesting depth, with the top-level object at depth 1 | `64` |

Apply the policy before material allocation or unbounded decode. Check the
artifact's regular-file size before ZIP opening; check central-directory member
count, each declared stored size, and overflow-safe aggregate stored size before
reading a member. Read the manifest through an inclusive cap plus one byte and
reject before JSON decode. Parse only the fixed NPY prefix/header-length fields
first, reject a header above its cap, then validate dtype and every non-negative
shape dimension. Compute element count and data bytes with Python integers and
checked multiplication (`value > limit // factor` before multiplying), and
compute aggregates with checked addition before allocating or calling a NumPy
array reader. On first prototype access, preflight every lazy array header and
the complete lazy aggregate before publishing any array.

Hash the complete artifact and every stored member incrementally in bounded
chunks; never use an unbounded `read()` or create a second whole-member copy
merely to hash it. A hashing reader may feed the validated NPY decoder, but its
byte count must equal the preflight size and the digest must match before the
array is published. The writer applies the same policy before temporary-file
creation because its mandatory self-open must be locally readable. Policy
boundary tests exercise every table row at exactly `limit` and `limit + 1`
through synthetic counters/headers, without allocating limit-sized fixtures.

Occurrence arrays share canonical id dtype: prototype and parent ids uint32 or
uint64 as above; transforms native float64 `(n,4,4)`; visibility bool. Parent
zero maps only to `None`. Roots must exactly equal zero-parent rows. Validate
affine and accumulated transforms through `CadManifest` construction.

Prototype arrays use section-4.3 dtype, shape, C-contiguity, finiteness, index,
owner, and offset rules. Indices use canonical uint32 unless their vertex
domain requires uint64; offsets are int64. Mesh descriptors are ascending and
cover every manifest prototype once. Bounds equal their prototype bounds;
owners are known shapes in that prototype; diagnostics belong to the document;
optional JSON-null/member presence agrees.

`entries` maps every non-manifest member, and no other member, to the lower-case
SHA-256 of its complete stored bytes. Occurrence member hashes are checked
eagerly; prototype member hashes are checked during lazy loading.

## 7. OCP-free opening, lazy loading, and retained source

Initial open follows this exact ownership sequence:

1. normalize the caller artifact to an absolute path without adopting it;
2. open one read handle and verify regular-file status plus same-view path and
   handle drift, following the accepted Windows rule: all five stat fields are
   compared within pathname views and within handle views, while the initial
   pathname-to-handle anchor compares dev/ino/size/mtime only;
3. validate the complete ordinary-ZIP envelope and exact inventory;
4. read canonical `manifest.json`, then hash/validate only the five compact
   occurrence members required to construct the complete `CadManifest`;
5. capture immutable expected manifest bytes, exact inventory/metadata,
   entries hashes, cache identity, and absolute caller-owned artifact path;
6. close the archive and handle; and
7. install one loader through `CadDocument._from_preview_artifact`.

No `ZipFile`, stream, or descriptor remains open after initial return. The
loader never adopts, deletes, or rewrites the artifact. On first mesh access it
reopens the same path, repeats within-read drift and full envelope/inventory
checks, requires identical canonical manifest bytes/cache identity, then reads
and hash-validates every prototype member before returning one complete tuple.
Byte-equivalent path replacement is safe only because all canonical metadata,
inventory, and hashes still match; anything else fails before publication.
The core factory owns thread-safe one-shot execution, cached success/failure,
core validation, and read-only publication.

Lazy invalidation semantics are exact:

- classification uses the document's **currently usable owned snapshot at the
  failure linearization point**, never the `retained_source` argument supplied
  at open time;
- if release has completed or `_release_requested` was set before first
  prototype access linearizes, invalid or changed lazy data raises
  `CadArtifactError` code `cad.preview.invalid_without_source`;
- if the owned snapshot is still present and not release-requested when failure
  linearizes, the loader raises generic `CadArtifactError`, preserves that
  snapshot for explicit later `tessellate_cad`, and never regenerates; and
- the core's cached first lazy failure retains the classification selected at
  that linearization point even if source release occurs later.

`CadDocument._ensure_preview_loaded` holds the document condition across the
one-shot loader. Source release linearizes when it sets `_release_requested`
under that same condition; lazy failure classification occurs under the same
condition before the loader returns. Thus release-first deterministically
selects `cad.preview.invalid_without_source`, while load-first with a usable
snapshot deterministically selects generic artifact failure; a release caller
that has not yet acquired the condition has not linearized. The codec loader
captures the constructed document only after factory success and consults its
current source state while classifying. It does not add a second lock or infer
availability from a pathname.

When `retained_source` is supplied, use the accepted hardened source-copy/hash
boundary with `expected_sha256=manifest.source_sha256`. Attach only its returned
task-owned snapshot. Never attach, rename, modify, or delete the caller source.
If factory construction fails, remove only the recorded owned snapshot; a
cleanup failure is a note and never replaces the first exception. Without a
source, `source_available=False`.

## 8. Writer validation, atomicity, and cancellation

Before destination coercion or filesystem interaction, require `document` to
be `CadDocument`, require an explicit result to be `CadTessellationResult`, and
validate the cancellation callable. Use the explicit result when supplied;
otherwise access `document.tessellation`. Absence raises exact code
`cad.preview.tessellation_required`.

Before temporary creation:

- recompute and compare source identity;
- core-bind the result against the exact manifest/options;
- require one mesh per prototype and validate ids, owners, bounds,
  diagnostics, arrays, and producer/source identity;
- preflight occurrence uint64 and ordinary ZIP limits;
- normalize and hash every NPY member; and
- build canonical manifest bytes and exact inventory.

Publication sequence:

1. require the destination parent already exists; do not create directories;
2. create one same-directory task-owned temporary and record dev/ino through
   `fstat` before closing its exclusive creation handle;
3. write deterministic ZIP bytes, close, flush/fsync, and revalidate regular,
   non-symlink identity;
4. reopen through the codec with OCP/provider imports blocked, force the lazy
   result, and compare manifest, options, records, and every normalized array;
5. hash the complete artifact;
6. perform the final cancellation and identity checks; and
7. perform exactly one `os.replace(temporary, destination)` and return the hash.

No fallible processing or cancellation check follows successful replace. Any
earlier failure/cancellation preserves an existing destination and removes only
the still-matching owned temporary. Substitution fails closed and is not
unlinked. Cleanup failure is attached as a note. Two writes of identical
normalized input are byte-identical and return the same hash.

Cancellation uses accepted codes `cad.operation.cancelled` and
`cad.cancellation_check.failed`, preserves callback causes, and is checked
before work and between bounded member/write/validation stages. No native call
is made or claimed interruptible.

## 9. Exact focused tests and static proof

`tests/test_cad_artifact.py` owns synthetic core records and small arrays only.
Its exact nodes are:

```text
test_public_artifact_signatures_and_facade_exports
test_write_is_byte_deterministic_and_returns_committed_sha256
test_zip_envelope_is_canonical_stored_and_non_zip64
test_manifest_json_and_entry_hashes_are_canonical
test_npy_members_are_version_two_native_c_contiguous_and_pickle_free
test_occurrence_ids_choose_uint32_or_uint64_and_reject_overflow
test_open_reconstructs_occurrences_instancing_and_read_only_arrays
test_open_is_metadata_eager_and_prototype_lazy_once
test_lazy_failure_is_cached_without_partial_publication
test_writer_accepts_explicit_or_document_tessellation
test_writer_requires_tessellation_with_frozen_code
test_writer_rejects_source_options_backend_and_mesh_mismatches
test_reader_rejects_unknown_missing_duplicate_or_noncanonical_json
test_reader_rejects_extra_missing_duplicate_or_unsafe_zip_members
test_reader_rejects_zip_metadata_descriptor_zip64_and_trailing_data
test_reader_rejects_entry_hash_and_npy_corruption
test_reader_policy_limits_accept_exact_limit_and_reject_limit_plus_one
test_reader_policy_preflight_is_overflow_safe_and_hashes_streaming
test_retained_source_is_snapshotted_hash_bound_and_releasable
test_lazy_artifact_replacement_fails_closed_with_or_without_source
test_release_before_first_access_selects_without_source_failure
test_release_and_lazy_load_have_deterministic_linearization
test_writer_preserves_destination_and_cleans_only_owned_temporary
test_cancellation_preserves_destination_with_frozen_codes
test_write_open_and_lazy_load_import_no_optional_cad_packages
test_writer_self_validation_forces_lazy_round_trip
```

Those nodes must cover:

- exact public signatures, facade identity, and no optional/heavy imports;
- deterministic byte-identical double write and returned SHA;
- exact archive order, local/central metadata, ordinary EOCD, no descriptors,
  ZIP64, extras, encryption, or trailing data;
- canonical JSON, duplicate/non-finite rejection, exact recursive key sets,
  cache/source identity, and complete member hashes;
- NPY 2.0, native C-contiguous non-object arrays, exact dtype/shape, and no
  trailing bytes;
- uint32 and sparse/large-id uint64 occurrence paths plus uint64 overflow;
- occurrence reconstruction, roots/transforms/visibility, instancing, and
  read-only publication;
- metadata open without prototype reads, first-access lazy read, shared
  one-shot success, and cached first failure;
- explicit detached-result and `document.tessellation` writer paths;
- missing tessellation exact diagnostic;
- source/options/backend/prototype/bounds/owner/diagnostic mismatch rejection;
- missing/extra/duplicate/unsafe members and JSON/logical ids;
- compression/metadata/descriptor/ZIP64/hash/NPY/dtype/shape/order/index/offset
  corruption;
- every frozen reader-policy byte/count/depth cap at its exact inclusive limit
  and at limit plus one, overflow-safe pre-allocation rejection, and streaming
  rather than unbounded member hashing;
- retained-source match/mismatch, separate ownership, caller-path preservation,
  release behavior, and factory-failure cleanup;
- lazy artifact replacement/corruption with and without retained source;
- release completed before first lazy access versus load-first/release-waits
  ordering, exact failure-code selection, cached first classification, snapshot
  preservation at generic failure, and no automatic regeneration;
- existing-destination preservation, identity-substitution refusal,
  cancellation, owned-temp cleanup, and one atomic success; and
- no OCP, CadQuery, provider, geometry, mesher, or material import during
  module import, write, metadata open, or lazy load.

The one proposed LIGHT/non-lease command, subject to registration, is:

```text
python -m pytest -q tests/test_cad_artifact.py tests/test_cad_contract.py::test_preview_factory_loads_once_and_caches_first_failure tests/test_layering.py::test_third_party_imports_are_declared tests/test_layering.py::test_base_third_party_allowlist_is_numpy_only tests/test_layering.py::test_cad_neutral_modules_do_not_import_heavy_or_geometry_packages
```

Run it once after source review. Preserve the first result. Do not broaden,
install, tune, or retry without a Boss ruling. All archive/provider behavior is
local and synthetic; no real CAD, OCP, entry point, network, build, or resolver
is used.

Always-allowed static completion proof:

- `git diff --check`;
- AST parse of the four owned Python paths;
- exact changed-path equality to section 4;
- base/direct-parent, worktree, branch, and absent-upstream checks;
- protected M2/contract/types/runtime/operations diff and blob reproduction;
- source scan proving only stdlib, NumPy, and core imports; and
- no provider, ANYgeometry, consumer, metadata, or release implementation.

## 10. Definition of done

- Exact four-path diff and one direct-child commit.
- Public signatures/facade exports match section 1.
- Deterministic schema-1 ZIP/NPY bytes and strict ordinary-ZIP validation.
- Complete eager envelope/manifest/occurrence validation.
- Complete one-shot lazy prototype validation without retained handles.
- Frozen bounded reader policy, overflow-safe pre-allocation checks, and
  streaming hashes; every cap has exact limit/limit-plus-one proof.
- Cache/source identity and every member hash are recomputed.
- Caller artifact/source paths are never adopted, modified, or deleted.
- Retained source is separately snapshotted, hash-bound, and releasable.
- Writer self-validates OCP-free and publishes through one owned atomic replace.
- Focused command passes once if authorized.
- Worktree is clean, branch has no upstream, protected evidence reproduces.
- No claim is made about provider, consumer, wheel, resolver, performance,
  publication, or real-CAD qualification.

## 11. Explicit exclusions

No edit, generated fixture, formatting rewrite, or transferred hunk in:

- `src/anyfileio/cad.py`, `cad_backend.py`, `cad_operations.py`, `formats.py`,
  `__main__.py`, GUI, diagnostics, or semantic modules;
- any existing CAD test except the one exact layering tuple hunk;
- `pyproject.toml`, README, CHANGELOG, packaging tests, workflows, version,
  dependency ranges, build metadata, or release files;
- the three frozen contract documents;
- ANYfileio-occt, OCP/provider code, ANYgeometry adapter, ANYfem V7, UI, solver,
  structure, mesh, material, renderer, or any other repository;
- benchmarks, profilers, scaling/stress, large fixtures, reports, wheels,
  resolver environments, install tests, publication, merge, push, or PR.

This source slice makes no resolver/wheel qualification claim. Heavy or broad
tests, builds, installs, clean environments, timing/RSS, benchmarks, or
profiling require a fresh exact `PERF LEASE REQUEST` and `PERF LEASE GRANTED`.

## 12. Merge order and handoff

Frozen linear order:

```text
... -> 1f0b578 semantics runtime
    -> 7e7538e CAD operations
    -> da8fd8d ownership correction / exact base
    -> this one accepted artifact commit
    -> combined NumPy-only lightweight-core handoff
    -> separately registered ANYfileio-occt provider slices
    -> owner-gated ANYfem V7 persistence and offline preview
```

A metadata/resolver commit cannot interleave without an explicit registered
rebase/merge order and protected-M2/contract/types/runtime/operations/artifact
diff proof. This editor does not merge, cherry-pick, rebase, push, publish, or
create a PR.

Completion evidence reports:

- this plan path/hash/bytes/lines and Sigrid identity;
- branch/worktree/upstream and exact base/tree/parent;
- commit/tree/sole parent/subject;
- exact four-path diff/stat/final blobs;
- focused-test first outcome if authorized plus static checks;
- protected diff/blob reproduction;
- deterministic artifact hashes, lazy/ownership/atomic behavior, and clean
  worktree; and
- exclusions, deferred qualification, and next registered owner.

Any need to touch a fifth path, change a protected file, add a dependency,
alter a public call/schema/key/error/provider boundary, run real provider or
consumer work, or reorder merges stops work and requires a revised
content-addressed plan and Boss registration.
