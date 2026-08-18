# ANYsolver Run 31746877870 Terminal-Row Recovery Plan

## Status

Plan only. No query is authorized by this document.

The prior one-shot terminal audit established:

- run `31746877870`;
- workflow `Tests`, path `.github/workflows/ci.yml`, run number `35`;
- event `push`, branch `main`;
- head `3cdb51efcdded232054225ea0eb9cc16dc79dde9`;
- tree `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7`;
- attempt `1`, status `completed`, conclusion `failure`;
- created/started `2026-08-13T21:43:04Z`;
- updated `2026-08-13T23:26:37Z`;
- URL `https://github.com/audunarn/ANYsolver/actions/runs/31746877870`;
- jobs endpoint `total_count=24`;
- target-SHA all-workflow inventory `total_count=1`, containing only this
  `Tests` push run, hence zero target `Publish` runs.

The unfiltered jobs response exceeded the tool display boundary. All 24 rows
were returned by GitHub, but their exact compact identities were not durably
retained. Omitted job identities are `evidence_limited`. Known retained rows are:

- `94603441356`, `ANYfileio 0.2.0 compatibility`, `completed`, `failure`,
  `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441356`;
- `94603441358`, `ANYfileio 0.1.0 compatibility`, `completed`, `failure`,
  `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441358`;
- `94603441671`, `pytest (windows-latest, 3.11)`, `completed`, `failure`,
  `https://github.com/audunarn/ANYsolver/actions/runs/31746877870/job/94603441671`.

No log was read. The audit is stopped and may not be retried under its expired
authority.

## Later one-shot recovery

A later explicit grant may authorize exactly one compact, read-only request:

```text
& 'C:\Program Files\GitHub CLI\gh.exe' api 'repos/audunarn/ANYsolver/actions/runs/31746877870/jobs?per_page=100' --jq '{total_count, jobs: [.jobs[] | {id, name, status, conclusion, html_url}]}'
```

Execution requirements:

- `login=false`;
- network escalation changes sandbox context only, never command bytes;
- one request, no poll, retry, pagination replay, log query, run query, active-job
  query, rerun, cancellation, dispatch, cleanup, or mutation;
- expected `total_count` exactly `24`;
- exactly 24 unique integer IDs, unique names, and unique job URLs;
- every status exactly `completed`;
- every conclusion non-null and terminal;
- every URL belongs to run `31746877870`;
- ordinal output is preserved as returned and a second ordinal-by-ID rendering is
  included in the later immutable recovery report;
- any mismatch or display truncation remains `evidence_limited` and is not
  retried.

The later report path is frozen as:

`C:\Github\ANYopenSoft\governance\reports\ANYSOLVER_RUN_31746877870_TERMINAL_ROW_RECOVERY.md`

It must be created via `apply_patch` from the one retained compact response,
record the exact command and 24 rows, link this plan hash, and contain no
self-hash. Its hash is computed once after creation. This plan authorizes neither
the request nor the report creation now.

