# ANYfileIO M2 Governance Allowlist Addendum

Status: M2-scoped governance classification; not CAD implementation authority

Date: 2026-08-12 (Europe/Oslo)

Parent M1 manifest:
`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_M1_CONSEQUENCE_MANIFEST.md`

Accepted parent SHA-256:
`732FD118FC94BC5846FFEBD90EC44329AC8994A282CFF5858DE35EC74807EFF4`

Accepted M2 source commit:
`0d2c7f8ef1b17f42f667d6183125e51cb650a70d`

The accepted content-addressed M1 manifest remains immutable. This companion
record replaces the obsolete allowlist for the earlier CAD baseline-addendum
candidate and classifies the final revised governance file:

`C:\Github\ANYopenSoft\governance\plans\ANYFILEIO_OCCT_CAD_PIPELINE_BASELINE_ADDENDUM.md`

Verified SHA-256:
`9249191E78C746A81A2B7D80B8ADA543AD45FCAE9CA41F5CAB04E169D68796A1`

Verified extent: 641 lines; 32,068 bytes.

Allowed identity occurrences in that exact file, hash, and extent are:

- canonical repository `ANYfileIO`: **21 occurrences** on lines 1, 50, 61, 99,
  189, 192, 220, 253, 294, 299, 304, 305, 307, 323, 351, 355, 415, 416,
  492, 587, and 600;
- distribution/product `ANYfileio`, including distinct `ANYfileio-occt`:
  **25 occurrences** on lines 51, 62, 179, 199, 203, 208, 210, 223, 257,
  258, 262, 266, 361, 417, 418, 501, 502, 504 (two occurrences), 507, 508,
  538, 541, 588, and 601;
- import-package identities `anyfileio` and `anyfileio_occt`: **18
  occurrences** on lines 50, 62, 231, 232, 238, 243, 245, 247, 295, 518,
  520, 538, 539, 542, 545, 546 (two occurrences), and 548;
- former repository `ANYio`: **one occurrence** on line 60, allowed only because
  it explicitly states that `C:\Github\ANYio` is frozen and never an
  implementation source;
- third-party lowercase `anyio`: **zero occurrences**.

The counts use case-sensitive identity boundaries; a line listed as two
occurrences contributes twice to the stated total. The exception is valid only
while the governed file's hash, line count, byte count, and classified counts
all match. Any edit requires a new content hash and a fully regenerated count,
not a line-number-only adjustment.

This allowlist does not permit former-repository text in canonical package
metadata, current documentation, source, CI, consumer configuration, or another
governance file. It grants no dependency, version, implementation, release,
publication, external-service, or destructive action.
