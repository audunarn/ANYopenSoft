# ANYsolver S4 drill-constraint execution addendum

Status: execution-only supersession for the registered proof plan. It changes
no scientific input, equation, fixture, precision, sensitivity multiplier,
threshold, rank rule, outcome rule, owned repository path, or production scope.

## 1. Bound identities

- governing plan SHA-256:
  `90B5C4903EE6A9C06056F7E1F3AB21DAE0626C185A27627843A04BF289430E3A`;
- Tor plan SHA-256:
  `8E969863806461124510E7C31D99A3244FCCF15DD67424517320EE819439AA90`;
- cases SHA-256:
  `B4D663382302E971752F0757F6E869549A54234F485235E06DBEF74085860F38`;
- base commit/tree:
  `587fa2efabcd48ada8a258ecf7301070b47f2b32` /
  `de137d6a72548b5d5908d799b96f0586dff2ba8f`;
- execution worktree:
  `C:\Github\ANYsolver\.perf2-worktrees\s4-drill-constraint-certification`;
- oracle SHA-256 at the stopped execution boundary:
  `0112EF21FCF56672EB09DFB2FB5E179637C1BF1E026FE92D07CD919DFB91A12F`
  (142,705 bytes).

The governing plan, Tor plan, cases, oracle, test, derivation, pyproject, and
accepted historical artifacts remain byte-frozen while this addendum executes.
The cases remain bound to the registered governing/Tor hashes above; this
addendum is deliberately outside the scientific identity graph.

## 2. Preserved terminal evidence

The monolithic catalog previously exited 124 at 30 minutes with no JSON.
Under the accepted precision-shard runner:

- `set1_080.json` completed in 900.9 seconds, 393,782 bytes, SHA-256
  `321D9AE299B4D0BE5F1F5FA49F6F3B6DAA3E4CA8D1D46A766705EB715CEFABE9`;
- `set1_160.json` completed in 1,273.8 seconds, 467,206 bytes, SHA-256
  `ED3951413EA8E655B9DC521536F06F3F0F7F18CE82403B0184384CFCB69459CB`;
- `set1_320` exited 124 after 1,801.8 seconds; neither
  `set1_320.json` nor `set1_320.json.tmp` exists and no worker remains.

The two completed shards have the exact registered schema, identities,
environment manifest, cases hash, precision, and canonical-byte validation.
They remain immutable and may be used as set 1 inputs. The timed-out 320 run
contributes no scientific data and is never reused.

## 3. Sole execution change

The 80- and 160-digit shard caller deadlines remain 30 minutes. The 320-digit
shard caller deadline is increased to exactly 60 minutes for `set1_320.json`
and `set2_320.json` only. This is a runtime bound, not a numerical tolerance.
All shards still run serially with one process, no children, the complete
catalog, and all sensitivity multipliers. The safe path, exclusive temporary,
flush/fsync/atomic-place, fail-stop, preservation, and merger rules in the
governing plan remain unchanged.

Resume in this exact order:

1. run only `set1_320.json` with a 60-minute caller deadline;
2. merge the immutable set-1 80/160 shards plus the new 320 shard to the
   registered stored-output path with the unchanged five-minute deadline;
3. run `set2_080.json` and `set2_160.json` with 30-minute deadlines;
4. run `set2_320.json` with a 60-minute deadline;
5. merge set 2 to `repeat_merged.json` with the unchanged five-minute deadline;
6. require byte-for-byte and SHA-256 equality of the two merged outputs.

The remaining hard ceiling is 190 minutes: 60 + 5 + 30 + 30 + 60 + 5. On any
nonzero result, timeout, identity drift, path-safety failure, or output mismatch,
stop, confirm worker absence, inventory and preserve every artifact, and issue
no scientific classification. No source edit, retry with changed inputs,
cleanup, merge, commit, integration, or production action follows a failure.

## 4. Authority and closeout

The user removed separate performance-lease requests and transferred approval
to this task. That authority permits this bounded serial continuation only; it
does not widen the scientific or repository scope. Independent read-only audit
must accept this addendum before `set1_320` resumes. Final closeout still
requires the governing plan's deterministic output, focused regressions,
independent scientific/numerical audits, exact commit/integration identities,
green hosted CI, and task-owned cleanup inventory.
