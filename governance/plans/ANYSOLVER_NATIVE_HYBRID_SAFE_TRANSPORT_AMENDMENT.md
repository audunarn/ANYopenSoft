# ANYsolver Native-Hybrid Safe Transport Amendment

Status: PLAN ONLY, BLOCKED PENDING INDEPENDENT REVIEW AND PERF AUTHORITY

This amendment supersedes only the transport and orchestration portions of the accepted ANYsolver integration plan. It does not change the accepted source commit, Git target, workflow acceptance criteria, or publication boundary.

## Governing identities

| Item | Exact identity |
|---|---|
| Governing integration plan | `C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NATIVE_HYBRID_RELEASE_BLOCKERS_INTEGRATION_MAIN_PUSH_PLAN.md` |
| Governing plan SHA-256 | `A20BF27EC97D918274822B60967BC5CD384E9A0B0A6B03E7E7E5B546EA3DEAEF` |
| Primary repository | `C:\Github\ANYsolver` |
| Accepted old main | `12c565899e320b2142d8b23e31f5eb19702b2486` |
| Accepted source commit | `3cdb51efcdded232054225ea0eb9cc16dc79dde9` |
| Accepted target tree | `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7` |
| Source worktree | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers` |
| Source branch | `refs/heads/codex/native-hybrid-release-blockers` |
| Qualification root | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28` |
| Mutation phase | `mutation_phase_A20BF27E_v4.ps1` |
| Mutation SHA-256 | `C98FA7FD90551460B33BC62510329E83101E968805A0D7F2363A79BAC1377C0E` |
| Monitor phase | `monitor_phase_A20BF27E_v3.ps1` |
| Monitor SHA-256 | `C4A0EAD700A19701F0896F47918107B110EF4BD6E8EE937078BED406EE25A541` |
| Expected handoff | `mutation_phase_A20BF27E_handoff.json` |
| PowerShell executable | `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe` |
| PowerShell SHA-256 | `7600FFE12DA441FE89D035B13801E8E91D064BC544A27B19A5CF49F6AB8B18F5` |

The source commit, phase files, and exact hashes above require independent re-verification before any execution authority. Package publication, tags, releases, and any ref other than `refs/heads/main` remain prohibited.

## Security supersession

Windows Defender detected `Trojan:Win32/PowhidSubExec.B` in giant inline PowerShell command constructions used while attempting to freeze an orchestration launcher. Defender removed the blocked command. The launcher target was not created, no phase was executed, and no Git integration or network mutation occurred.

All prior requirements for nested or crash-safe PowerShell launchers are withdrawn. The following mechanisms are prohibited:

- Large inline PowerShell `-Command` payloads.
- Here-string source generation through a shell.
- `-EncodedCommand` or equivalent encoded/compressed transport.
- Hidden-window execution.
- Nested PowerShell orchestration.
- `Start-Process` launcher chains.
- Automatic retry, fallback, cleanup, or process termination.
- Defender restore, quarantine release, allow-list, exclusion, or other security exception.

No launcher artifact is an execution input. Existing launchers and prior mutation/monitor revisions remain immutable first-failure evidence and are marked DO NOT EXECUTE.

## Preserved do-not-execute evidence

| Artifact | SHA-256 | Rule |
|---|---|---|
| `mutation_phase_A20BF27E_v1.ps1` | `DB6A95666406F2C8C3555187EF4F9F40526E926AABA8F0AF59B7E7FCB2178434` | Preserve, never execute |
| `mutation_phase_A20BF27E_v2.ps1` | `DB6A95666406F2C8C3555187EF4F9F40526E926AABA8F0AF59B7E7FCB2178434` | Preserve failed freeze, never execute |
| `mutation_phase_A20BF27E_v3.ps1` | `3600E26516D85B89658D28CE225DF4FB572BF8BC22D1585650471A980D49BE50` | Preserve, never execute |
| `monitor_phase_A20BF27E_v1.ps1` | `49E9CC6811EF8E8648D8BE66519719FAD4BE517C81D56FDDE6C6F9EE98DD278C` | Preserve, never execute |
| `monitor_phase_A20BF27E_v2.ps1` | `8ECC6CFFCACC7DE973EE602162F7722ED8EAF2D9E4D23F14597D287EED97F938` | Preserve, never execute |
| `monitor_phase_A20BF27E_v2_launcher.ps1` | `A3BF5716C0CBACEAAAE67E25FD190373A31D26184159C8C8A6094B779193950D` | Retired, never execute |
| `monitor_phase_A20BF27E_v3_launcher_v2.ps1` | Absent after Defender action | Do not recreate |

Mutation V4 and Monitor V3 are permanently retired as execution inputs by the direct-native supersession at the end of this amendment. They remain immutable evidence and must never be executed, overwritten, or deleted. No evidence or partial file may be deleted before verified closeout and a separately authorized cleanup inventory.

## Retired scripted execution model (historical, DO NOT EXECUTE)

Everything from this heading through the original completion-evidence section is retained only as the accepted transport history. Its PowerShell phase commands, handoff contract, and launcher assumptions are superseded by the direct-native plan below and grant no execution authority.

## Transparent execution model

Execution is split into two independent top-level process invocations. No command invokes another PowerShell process. Codex calls each exact command directly through the shell execution boundary with `login=false`; the app records terminal output and exit state.

One exclusive 70-minute PERF lease may cover both phases and both verification windows, but authority is checkpointed. The initial grant authorizes Phase 1 only. The lease remains held after a successful push while an independent reviewer verifies Phase 1 evidence. A distinct continuation verdict is required before Phase 2 starts. Any failure releases the lease unless the Boss explicitly directs otherwise.

### Phase 1: mutation and main-only push

Exact command, one invocation only:

```powershell
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -File C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\mutation_phase_A20BF27E_v4.ps1 -MonitorScriptPath C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\monitor_phase_A20BF27E_v3.ps1 -ExpectedMonitorSha256 C4A0EAD700A19701F0896F47918107B110EF4BD6E8EE937078BED406EE25A541
```

Phase 1 is permitted only after all preflight facts are independently exact:

- Mutation V4 and Monitor V3 are direct, non-reparse files under the direct, non-reparse qualification root and match the registered hashes.
- Primary ANYsolver is clean `main` at the old commit.
- Source worktree is clean on the accepted feature branch at the target commit and target tree.
- Local `main`, `origin/main`, and authoritative remote `refs/heads/main` are the old commit.
- The frozen 36-ref invariant, 28-worktree inventory, manifests, source path inventory, origin fetch URL, and origin push URL match the accepted plan.
- No handoff, handoff partial, V4 failure record, or V4 failure partial exists.
- No Tests or other workflow run exists for the target commit.
- No competing PERF lease or task-owned Git, gh, Python, compiler, linker, or phase process exists.

Phase 1 must terminate before any outer verification begins. A nonzero exit, shell timeout, Defender event, unexpected process, missing evidence, or state drift stops the sequence. There is no second attempt.

The caller sets a hard 5-minute tool timeout for the exact Phase 1 command. A timeout is terminal, authorizes no retry, and preserves every process, ref, file, partial, transcript, and other available state for governance review.

## Mandatory independent gate between phases

The following checks occur as separate read-only top-level operations after Phase 1 exits. Prefer direct `git.exe` and `gh.exe` calls. Do not use an inline PowerShell aggregation command.

Exact direct Git commands:

```text
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver rev-parse HEAD
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver symbolic-ref -q HEAD
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver rev-parse refs/heads/main
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver rev-parse refs/remotes/origin/main
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver status --porcelain=v1 --untracked-files=all
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver ls-remote --exit-code origin refs/heads/main
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver ls-remote --refs origin
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver ls-remote --symref origin HEAD
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver for-each-ref '--format=%(refname)%09%(objectname)'
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Github\ANYsolver -C C:\Github\ANYsolver worktree list --porcelain
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers -C C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers rev-parse HEAD
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers -C C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers symbolic-ref -q HEAD
& 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers -C C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers status --porcelain=v1 --untracked-files=all
```

Exact direct GitHub CLI commands:

```text
& 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
& 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
& 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt
```

The three GitHub CLI arrays must have exact counts `1`, `1`, and `0`, respectively. The sole Tests row and sole all-runs row must have the same `databaseId`, workflow name `Tests`, event `push`, branch `main`, and target `headSha`. No other run is allowed.

The `for-each-ref` output is canonicalized without culture-sensitive sorting. Exclude only `refs/codex/turn-diffs/*`, `refs/heads/codex/native-hybrid-release-blockers`, `refs/heads/main`, `refs/remotes/origin/main`, and symbolic `refs/remotes/origin/HEAD`. Sort the remaining complete `refname<TAB>objectname` lines with ordinal string comparison, join them with LF, append one final LF, encode UTF-8 without BOM, and require exactly 36 lines with SHA-256 `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928`.

The `worktree list --porcelain` output must contain exactly 28 path records. Compare path, HEAD, and branch or detached state by exact ordinal path identity. The 27 original records come from `pre_edit_state_manifest.json`, with the primary record phase-adjusted to clean `refs/heads/main` at the target. The 28th record is the clean source worktree at the target on `refs/heads/codex/native-hybrid-release-blockers`. The 26 other worktree statuses rely on Mutation V4's accepted full scan, the matching handoff worktree count and invariant SHA, and this fresh exact inventory; no redundant 26-worktree status command set is added. Fresh `status --porcelain=v1 --untracked-files=all` output for both primary and source must be empty.

The handoff is validated field by field. Required exact values are:

| Handoff field | Required value |
|---|---|
| `schema` | `anysolver-native-hybrid-mutation-handoff-v1` |
| `success` | `true` |
| `phase` | `reconciled` |
| `plan_sha256` | `A20BF27EC97D918274822B60967BC5CD384E9A0B0A6B03E7E7E5B546EA3DEAEF` |
| `network_preflight_sha256` | `A4FE59B2BC9966BC88D2FA01370CC3AE128671156B163AC3DE061F0898DEC935` |
| `mutation_script_sha256` | `C98FA7FD90551460B33BC62510329E83101E968805A0D7F2363A79BAC1377C0E` |
| `monitor_script_path` | Exact registered Monitor V3 path |
| `monitor_script_sha256` | `C4A0EAD700A19701F0896F47918107B110EF4BD6E8EE937078BED406EE25A541` |
| `old` | `12c565899e320b2142d8b23e31f5eb19702b2486` |
| `target` | `3cdb51efcdded232054225ea0eb9cc16dc79dde9` |
| `target_tree` | `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7` |
| `push_refspec` | `refs/heads/main:refs/heads/main` |
| `fetch_refspec` | `refs/heads/main:refs/remotes/origin/main` |
| `pre_target_tests_runs` | `0` |
| `pre_all_target_runs` | `0` |
| `invariant_ref_count` | `36` |
| `invariant_ref_sha256` | `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928` |
| `worktree_count` | `28` |
| `push_completed` | `true` |
| `post_push_fetch_completed` | `true` |

The handoff's `remote_refs_before` and `remote_refs_after` arrays must each match their declared count and canonical SHA-256 using ordinal full-line sorting, LF joining, one final LF, and UTF-8 without BOM. `remote_main_before` and `remote_head_before` must name the old commit; their after values must name the target. Removing only the main-ref line from each complete remote array must yield byte-identical non-main arrays. The direct post-push remote commands must match the handoff after arrays, counts, hashes, main, and symbolic HEAD.

Expected post-Phase-1 facts:

- Phase 1 exited zero and no phase process remains.
- The handoff exists as a direct, non-reparse file; its partial is absent.
- The handoff is valid JSON and records success, phase `reconciled`, target commit/tree, exact main-only push/fetch refspecs, Mutation V4 SHA, Monitor V3 direct path, and Monitor V3 SHA.
- The handoff records the complete remote refs before and after; only remote main changed.
- Primary HEAD, local main, local origin/main, authoritative remote main, and remote HEAD object are the target commit.
- Primary branch is `refs/heads/main`; primary and source worktrees are clean.
- The 36-ref invariant and all 28 worktrees remain exact.
- No Publish run exists and no unexpected target workflow exists.
- Mutation V4, Monitor V3, manifests, old evidence, and source commit remain byte-exact.

The reviewer records the handoff SHA-256 and exact direct-command outputs. Phase 2 is blocked until the Boss issues an explicit continuation verdict naming that handoff hash and the unchanged Monitor V3 hash.

The independent interphase gate has a hard 5-minute caller timeout. A timeout is terminal, authorizes no retry, and preserves all current state and evidence.

## Phase 2: terminal workflow monitor

Exact command, one invocation only after the independent continuation verdict:

```powershell
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -File C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\monitor_phase_A20BF27E_v3.ps1
```

Monitor V3 must consume the exact Phase 1 handoff, validate its own runtime path/hash against the handoff, and monitor only the unique push-triggered Tests run for the target commit. Acceptance remains exactly 24 terminal successful jobs, one Tests run, zero Publish runs, zero unexpected runs, unchanged local/remote/ref/worktree state, and no retry.

The caller sets a hard 55-minute tool timeout for the exact Phase 2 command. A timeout is terminal, authorizes no retry, preserves live-process truth and all available evidence, and stops for governance.

Phase 2 output is preserved directly in the terminal transcript. On failure, report the first error plus every available run ID, URL, job status, process state, and current ref state. Do not rerun, dispatch, clean, terminate, or alter evidence.

## Resource and lease envelope

| Item | Bound |
|---|---|
| Local processes | One top-level PowerShell phase process at a time |
| Local RAM | Less than 500 MB combined task-owned local usage |
| GPU | None |
| Phase 1 caller timeout | 5 minutes |
| Independent interphase gate timeout | 5 minutes |
| Phase 2 caller timeout | 55 minutes |
| Final verification timeout | 5 minutes |
| Combined lease envelope | 70 minutes |
| Remote workload | Sole push-triggered ANYsolver Tests workflow, exactly 24 expected jobs |
| Network | Exact GitHub Git/gh operations already defined by accepted phase files and direct gates |

No local build, wheel, test suite, benchmark, profiler, Publish dispatch, tag, release, package publication, or other-ref mutation is authorized.

Final verification uses the same frozen direct Git and GitHub CLI commands, exact canonical comparisons, and handoff hash. Its caller timeout is 5 minutes. Any timeout in any of the four windows is terminal, preserves state/evidence, and permits no retry.

## Completion evidence

Completion requires all of the following:

- Independent acceptance of this amendment content hash and the exact phase identities.
- Explicit Phase 1 PERF grant and exact zero-exit Phase 1 result.
- Independent handoff/ref/remote/worktree verification and explicit Phase 2 continuation.
- Exact zero-exit Phase 2 result with unique Tests run URL and 24 successful job URLs.
- Final authoritative remote main confirmation at the target commit.
- Preserved old evidence and no unauthorized artifact, process, workflow, ref, tag, release, package, Defender exception, cleanup, or retry.
- Boss terminal verdict `ECOSYSTEM CLOSEOUT: OK`.

Until all conditions are met, the accepted source milestone remains unintegrated and this task remains open.

## Direct-native transport supersession

Status: PLAN IMPROVEMENT ONLY, BLOCKED PENDING INDEPENDENT CONTENT-HASH ACCEPTANCE AND A FRESH PERF LEASE.

This section is authoritative over every scripted execution, handoff, monitor, and launcher statement above. It changes transport only. The old commit, target commit, target tree, main-only refspecs, preservation contracts, remote-CI acceptance criteria, and publication prohibitions are unchanged.

No `.ps1` file is an execution input. Mutation V4, Monitor V3, every earlier phase file, every launcher, every partial, and every first-failure artifact remains DO NOT EXECUTE and must be preserved byte-for-byte. No new script, launcher, handoff, report, partial, or cleanup artifact is created. The Codex command transcript, each direct command's raw output, exit code, wall time, and the independent review messages replace V4/V3 handoff files.

### Direct-call safety contract

Every command below is one separate `shell_command` call with `login=false`. The command field contains exactly one short native invocation using PowerShell's call operator and a quoted absolute executable path. No call contains a second command, variable, loop, conditional, pipeline, redirection, here-string, encoded content, aggregation, child shell, `powershell.exe`, `cmd.exe`, `Start-Process`, hidden window, cleanup, retry, or Defender exception.

Authoritative transport clarification: `shell_command` may internally host that exact command field in its fixed outer PowerShell `-Command` process. This implementation-owned host is allowed transport only when the command field is exactly one short literal `& 'absolute git.exe/gh.exe' ...` invocation with `login=false`; it does not authorize any task-authored PowerShell child, script, variable, loop, conditional, pipeline, redirection, aggregation, encoded content, hidden window, or launcher. The prohibition on task-authored inline PowerShell payloads and nested orchestration remains absolute, and no Defender exclusion, restore, allow-list, or other exception is permitted. Native commands that require network access use `sandbox_permissions=require_escalated` because the default sandbox blocks network; escalation changes only the sandbox context and never the accepted command bytes.

The only executable paths are:

- Git: `C:\Program Files\Git\cmd\git.exe`, 46,920 bytes, SHA-256 `7B7971DD13F0C3A284E538601F2F9770B3A87DFACCB5FB52D68141C67ED22364`, output `git version 2.55.0.windows.3`.
- GitHub CLI: `C:\Program Files\GitHub CLI\gh.exe`, 41,504,056 bytes, SHA-256 `CD79F16203F1FBE56937C4C96E2B6EADD10549418DCB241D91576AC77AF0AC8B`, output lines `gh version 2.96.0 (2026-07-02)` and `https://github.com/cli/cli/releases/tag/v2.96.0`.

Each call must finish before the next mutation call starts. Read-only calls may not conceal or compensate for a prior nonzero exit. Unless a command below explicitly states otherwise, the required exit code is zero. Raw stdout and stderr are preserved separately; native success is determined from the exit code and the subsequent state query, never from benign stderr text.

Any unexpected exit, output, ref, branch, status, worktree, remote, workflow, process, timeout, or security event stops at the named checkpoint. Only `P31`, `P44`, `P49`, `P53`, `P70`, and `P74` may mutate; each may run exactly once, in that order, with its exact registered refspec or CAS arguments. No mutating command may be replayed or retried, and no additional mutation is permitted. There is no rollback, workflow dispatch, rerun, cleanup, or fallback. Read-only failure accounting after a possibly completed push is allowed only where explicitly listed.

### Immutable comparison oracles

The following already-accepted records remain the exact comparison oracles:

| Oracle | Exact identity |
|---|---|
| Governing integration plan | `A20BF27EC97D918274822B60967BC5CD384E9A0B0A6B03E7E7E5B546EA3DEAEF` |
| Pre-edit worktree/status manifest | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\pre_edit_state_manifest.json`, SHA-256 `001F38163946A4126CC9294429C1DBB458792631476F7A6530F687ADABDE60DC` |
| Archive manifest | `C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-native-hybrid-release-blockers-7A635F28\archive_manifest.json`, SHA-256 `BA4D2E5D20CCC9A33EDE7F6F5FE142BB2152ED0FA88D3E821D1AAF3212FA5EE4` |
| Old main | `12c565899e320b2142d8b23e31f5eb19702b2486` |
| Target commit | `3cdb51efcdded232054225ea0eb9cc16dc79dde9` |
| Target tree | `7b4a2a3acda5c5bfda5cf5d7638ebd1c2e6920d7` |
| Stable-ref manifest/SPACE contract | 36 lines, SHA-256 `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928` |
| Stable-ref direct-output/TAB contract | 36 lines, SHA-256 `8C449F6DE6C0893289B59C8A3692655F3B7B6803511236F1464DA600A9E373A6` |
| Origin fetch and push URL | `https://github.com/audunarn/ANYsolver.git` |

At `P21`, `P41`, `P64`, `I11`, and `F11`, the reviewer excludes only `refs/codex/turn-diffs/*`, `refs/heads/codex/native-hybrid-release-blockers`, `refs/heads/main`, `refs/remotes/origin/main`, and symbolic `refs/remotes/origin/HEAD`. Every remaining line must be exactly `refname<TAB>objectname`, with one and only one TAB delimiter and a 40-lowercase-hex object name. Ordinal-sort the 36 complete raw lines, join with LF plus one final LF, encode UTF-8 without BOM, and require direct-output/TAB SHA-256 `8C449F6DE6C0893289B59C8A3692655F3B7B6803511236F1464DA600A9E373A6`. Then replace the one TAB in every line with one SPACE, preserving line order and all other bytes; join and encode identically; require manifest/SPACE SHA-256 `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928` and exact line-by-line equality to the immutable manifest. This comparison is performed from captured direct output, not by a shell pipeline or helper script.

The completed `P01-P23` transcript is accepted evidence under this corrected oracle: `P01-P20` matched; captured `P21` has 36 exact raw TAB lines with direct-output hash `8C449F6DE6C0893289B59C8A3692655F3B7B6803511236F1464DA600A9E373A6` and normalized manifest hash `4CDB24AFC8971CA36B6DCEF421A9E7782C3C2CBE9321637013AFD6F444AF6928`; `P22` returned exactly 28 worktrees; and every `P23/W01-W28` status matched the immutable inventory. `P01-P23` must not be replayed. The sandboxed `P24` exit is preserved as a non-authoritative transport failure before remote contact and must not be repeated. After independent acceptance of this amendment identity and a fresh PERF lease, exactly one authoritative `P24` may run with `sandbox_permissions=require_escalated`; on its success continuation begins at `P25`. No earlier `P` command or sandboxed attempt may be repeated, and no further `P24` execution is permitted.

For every `worktree list --porcelain` output, the reviewer requires exactly 28 path records. The 27 records in the pre-edit manifest remain exact except for the phase-adjusted primary HEAD; the registered source worktree is the 28th record at the target on `refs/heads/codex/native-hybrid-release-blockers`. The status block below supplies exact raw status evidence for all 28 worktrees. Each of the 26 non-primary/non-source outputs must equal its corresponding manifest `status` array byte-for-byte and in order. Primary and source output must be empty.

### Reusable all-worktree status block

`W01` through `W28` are invoked as separate calls, in this exact order, wherever the phase order names `W`. They are never placed in a loop or combined command.

```text
W01 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
W02 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\analysis-session' -C 'C:\Github\ANYsolver\.perf2-worktrees\analysis-session' status --porcelain=v1 --untracked-files=all
W03 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\baseline' -C 'C:\Github\ANYsolver\.perf2-worktrees\baseline' status --porcelain=v1 --untracked-files=all
W04 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\corotational' -C 'C:\Github\ANYsolver\.perf2-worktrees\corotational' status --porcelain=v1 --untracked-files=all
W05 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\damage-matrix' -C 'C:\Github\ANYsolver\.perf2-worktrees\damage-matrix' status --porcelain=v1 --untracked-files=all
W06 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\docs' -C 'C:\Github\ANYsolver\.perf2-worktrees\docs' status --porcelain=v1 --untracked-files=all
W07 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\functional-merge' -C 'C:\Github\ANYsolver\.perf2-worktrees\functional-merge' status --porcelain=v1 --untracked-files=all
W08 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\hill48' -C 'C:\Github\ANYsolver\.perf2-worktrees\hill48' status --porcelain=v1 --untracked-files=all
W09 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\impact' -C 'C:\Github\ANYsolver\.perf2-worktrees\impact' status --porcelain=v1 --untracked-files=all
W10 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\impact-reduced' -C 'C:\Github\ANYsolver\.perf2-worktrees\impact-reduced' status --porcelain=v1 --untracked-files=all
W11 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\integration' -C 'C:\Github\ANYsolver\.perf2-worktrees\integration' status --porcelain=v1 --untracked-files=all
W12 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\numerical-baseline' -C 'C:\Github\ANYsolver\.perf2-worktrees\numerical-baseline' status --porcelain=v1 --untracked-files=all
W13 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\qualification-39846da' -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-39846da' status --porcelain=v1 --untracked-files=all
W14 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\qualification-d596648' -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-d596648' status --porcelain=v1 --untracked-files=all
W15 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\qualification-eb41e73' -C 'C:\Github\ANYsolver\.perf2-worktrees\qualification-eb41e73' status --porcelain=v1 --untracked-files=all
W16 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\recovery' -C 'C:\Github\ANYsolver\.perf2-worktrees\recovery' status --porcelain=v1 --untracked-files=all
W17 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-baseline-61e2f45' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-baseline-61e2f45' status --porcelain=v1 --untracked-files=all
W18 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-batch-qualification' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-batch-qualification' status --porcelain=v1 --untracked-files=all
W19 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-geometry-handoff' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-geometry-handoff' status --porcelain=v1 --untracked-files=all
W20 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-improved-integration' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-improved-integration' status --porcelain=v1 --untracked-files=all
W21 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-nullspace-semantics' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-nullspace-semantics' status --porcelain=v1 --untracked-files=all
W22 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-production-integration' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-production-integration' status --porcelain=v1 --untracked-files=all
W23 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\s4-reference-core' -C 'C:\Github\ANYsolver\.perf2-worktrees\s4-reference-core' status --porcelain=v1 --untracked-files=all
W24 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\shell-batches' -C 'C:\Github\ANYsolver\.perf2-worktrees\shell-batches' status --porcelain=v1 --untracked-files=all
W25 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\state-storage' -C 'C:\Github\ANYsolver\.perf2-worktrees\state-storage' status --porcelain=v1 --untracked-files=all
W26 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\thread-scaling' -C 'C:\Github\ANYsolver\.perf2-worktrees\thread-scaling' status --porcelain=v1 --untracked-files=all
W27 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver\.perf2-worktrees\verification' -C 'C:\Github\ANYsolver\.perf2-worktrees\verification' status --porcelain=v1 --untracked-files=all
W28 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' status --porcelain=v1 --untracked-files=all
```

### Phase 1 exact order: preflight, CAS, push, and reconciliation

The Phase 1 lease authorizes only `P01` through `P75`, including the named `W` blocks. Every numbered line is a separate `shell_command` call. `R0` and `R1` name captured transcript outputs, not files or shell variables.

#### Tool, target, and local preflight

```text
P01 & 'C:\Program Files\Git\cmd\git.exe' --version
P02 & 'C:\Program Files\GitHub CLI\gh.exe' --version
P03 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
P04 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref -q HEAD
P05 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
P06 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
P07 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref refs/remotes/origin/HEAD
P08 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
P09 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
P10 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' rev-parse HEAD
P11 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' symbolic-ref -q HEAD
P12 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' status --porcelain=v1 --untracked-files=all
P13 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' cat-file -t 3cdb51efcdded232054225ea0eb9cc16dc79dde9
P14 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse '3cdb51efcdded232054225ea0eb9cc16dc79dde9^{tree}'
P15 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-list --parents -n 1 3cdb51efcdded232054225ea0eb9cc16dc79dde9
P16 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' show -s '--format=%s' 3cdb51efcdded232054225ea0eb9cc16dc79dde9
P17 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' merge-base --is-ancestor 12c565899e320b2142d8b23e31f5eb19702b2486 3cdb51efcdded232054225ea0eb9cc16dc79dde9
P18 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' diff-tree --no-commit-id --name-only -r 12c565899e320b2142d8b23e31f5eb19702b2486 3cdb51efcdded232054225ea0eb9cc16dc79dde9
P19 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' remote get-url origin
P20 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' remote get-url --push origin
P21 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' for-each-ref '--format=%(refname)%09%(objectname)'
P22 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' worktree list --porcelain
P23 W01 through W28, each as its own call
```

Expected `P01` and `P02` outputs are the two frozen version identities above. `P03`, `P05`, `P06`, and `P08` equal old main; `P04` is `refs/heads/main`; `P07` is `refs/remotes/origin/main`; `P09` and `P12` are empty; `P10` is target; `P11` is `refs/heads/codex/native-hybrid-release-blockers`; `P13` is `commit`; `P14` is target tree; `P15` is exactly `3cdb51efcdded232054225ea0eb9cc16dc79dde9 12c565899e320b2142d8b23e31f5eb19702b2486`; `P16` is `fix: widen ANYfileIO compatibility`; and `P17` exits zero with no output. `P18` returns exactly the seven registered paths in the governing plan. `P19` and `P20` each return the frozen HTTPS origin. `P21`, `P22`, and `P23` satisfy the immutable 36-ref, 28-worktree, and status contracts.

#### Authoritative remote and zero-run preflight

```text
P24 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin refs/heads/main
P25 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --refs origin
P26 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --symref origin HEAD
P27 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin HEAD
P28 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
P29 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
P30 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
```

`P24` is exactly `old<TAB>refs/heads/main`. `P25` is retained verbatim as remote inventory `R0` and is nonempty. `P26` is exactly `ref: refs/heads/main<TAB>HEAD` followed by `old<TAB>HEAD`. `P27` is exactly `old<TAB>HEAD`. `P28`, `P29`, and `P30` each return the JSON array `[]`. Any other output stops before fetch.

#### Main-only fetch and local CAS

```text
P31 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main
P32 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
P33 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
P34 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
P35 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref -q HEAD
P36 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
P37 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
P38 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref refs/remotes/origin/HEAD
P39 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
P40 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
P41 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' for-each-ref '--format=%(refname)%09%(objectname)'
P42 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' worktree list --porcelain
P43 W01 through W28, each as its own call
P44 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' switch --detach 12c565899e320b2142d8b23e31f5eb19702b2486
P45 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
P46 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' branch --show-current
P47 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
P48 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
P49 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' update-ref refs/heads/main 3cdb51efcdded232054225ea0eb9cc16dc79dde9 12c565899e320b2142d8b23e31f5eb19702b2486
P50 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
P51 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
P52 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
P53 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' switch main
P54 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
P55 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref -q HEAD
P56 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse 'HEAD^{tree}'
P57 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
```

`P31` must exit zero; its output is informational. `P32` and `P33` remain old. Before detach, `P34`, `P36`, `P37`, and `P39` are old; `P35` is `refs/heads/main`; `P38` is `refs/remotes/origin/main`; `P40` is empty; and `P41`, `P42`, and `P43` repeat the exact 36-ref, 28-worktree, and all-status preservation gates. After `P44`, `P45` is old, `P46` and `P47` are empty, and `P48` remains old. `P49` is the sole local branch mutation and must exit zero with no output. After it, `P50` remains old, `P51` is target, and `P52` is empty. After `P53`, `P54` is target, `P55` is `refs/heads/main`, `P56` is target tree, and `P57` is empty.

#### Immediate pre-push preservation gate and sole push

```text
P58 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin refs/heads/main
P59 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --refs origin
P60 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --symref origin HEAD
P61 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
P62 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
P63 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
P64 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' for-each-ref '--format=%(refname)%09%(objectname)'
P65 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' worktree list --porcelain
P66 W01 through W28, each as its own call
P67 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
P68 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref refs/remotes/origin/HEAD
P69 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
P70 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' push origin refs/heads/main:refs/heads/main
```

`P58` remains old. `P59` is byte-identical to `R0`; `P60` retains symbolic main and old HEAD. `P61`, `P62`, and `P63` are `[]`. `P64`, `P65`, and `P66` satisfy the 36-ref, phase-adjusted 28-worktree, and exact-status contracts. Immediately before the sole push, `P67` and `P69` remain old and `P68` is `refs/remotes/origin/main`. `P70` is the sole push, contains no force option, and must exit zero. Its textual progress is informational; remote queries below are authoritative.

#### Post-push authoritative reconciliation

```text
P71 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin refs/heads/main
P72 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --refs origin
P73 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --symref origin HEAD
P74 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' fetch --no-tags --no-prune origin refs/heads/main:refs/remotes/origin/main
P75 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
```

`P71` is exactly `target<TAB>refs/heads/main`. Retain `P72` verbatim as `R1`; removing only the main line from `R0` and `R1` yields byte-identical arrays, and the main line alone changes old to target. `P73` retains `ref: refs/heads/main<TAB>HEAD` and now reports `target<TAB>HEAD`. `P74` exits zero and changes at most local `origin/main`; `P75` is target. Phase 1 authority ends after `P75`. The lease remains held, but no further mutation or monitoring command is authorized until the independent interphase gate passes.

### Phase 1 partial-state stop ledger

| First failed range | Exact preserved state and permitted next action |
|---|---|
| `P01-P30` | No authorized local or remote mutation occurred. Stop and report raw output. |
| `P31-P43` | Only the main-only fetch may have touched local `origin/main`; local main remains old. Remote was last confirmed old at `P24-P27`, but its current state is not freshly proven. Any post-fetch preservation mismatch stops before detach; do not replay `P31`. |
| `P44-P48` | Primary may be detached and clean at old; local main remains old. Remote was last confirmed old at `P24-P27`, but its current state is not freshly proven. Stop; do not reattach or roll back. |
| `P49-P52` | Primary remains detached at old; local main may be target. Remote was last confirmed old at `P24-P27`, but its current state is not freshly proven. Stop; do not repeat CAS or switch. |
| `P53-P57` | Primary may be attached to target main and local `origin/main` remains old. Remote was last confirmed old at `P24-P27`, but its current state is not freshly proven. Stop; do not push. |
| `P58-P69` | Primary and local main are target. Remote is freshly queried by P58-P60; preserve actual raw outputs. Old/R0/symbolic-old is established only to the extent those commands completed successfully. Any mismatch leaves remote evidence-limited/unknown and prohibits push. |
| `P70` | Push outcome may be ambiguous. Never repeat it. Run only `P71-P73` as read-only reconciliation if the Boss explicitly permits failure accounting; otherwise stop immediately. |
| `P71-P73` | Remote may be target. Preserve `R0`, all outputs, and exact local state; no second push. |
| `P74-P75` | Remote and local main are target; `origin/main` may be old or target. Stop; no second fetch. |

### Independent interphase gate

After zero-exit `P75`, run `I01` through `I18` under the separate 5-minute checkpoint. Each line and each `W` member is a separate read-only call.

```text
I01 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
I02 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref -q HEAD
I03 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
I04 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
I05 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref refs/remotes/origin/HEAD
I06 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
I07 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
I08 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin refs/heads/main
I09 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --refs origin
I10 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --symref origin HEAD
I11 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' for-each-ref '--format=%(refname)%09%(objectname)'
I12 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' worktree list --porcelain
I13 W01 through W28, each as its own call
I14 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
I15 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
I16 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
I17 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' rev-parse HEAD
I18 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' -C 'C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\worktrees\ANYsolver-native-hybrid-release-blockers' symbolic-ref -q HEAD
```

`I01`, `I03`, `I04`, `I06`, `I08`, and `I17` are target; `I02` is `refs/heads/main`; `I05` is `refs/remotes/origin/main`; `I07` is empty; `I09` is byte-identical to `R1`; `I10` retains symbolic main and target HEAD; `I11`, `I12`, and `I13` satisfy the exact 36-ref/28-worktree/status contracts. `I14` and `I15` each contain exactly one identical row: workflow `Tests`, event `push`, branch `main`, head SHA target, and the same positive integer `databaseId`. `I16` is `[]`. `I18` is `refs/heads/codex/native-hybrid-release-blockers`.

The transcript records every `P` and `I` command string, output, exit code, and wall time plus `R0`, `R1`, the stable-ref comparison, the 28-worktree comparison, and the sole Tests run ID/URL/status. This transcript record is the direct-native handoff. No handoff JSON is read or written. Phase 2 remains prohibited until the Boss explicitly accepts this evidence and names the sole decimal run ID and unchanged target SHA in a continuation verdict.

### Exact 24-job ordinal oracle

The following list is the exact Monitor V3 oracle after ordinal sorting. `M05` and `F14` must each return 24 unique job names that equal these lines byte-for-byte and in this order after ordinal sorting; count and success alone are insufficient.

```text
ANYfileio 0.1.0 compatibility
ANYfileio 0.2.0 compatibility
ANYmesher 0.1.0 compatibility
ANYmesher 0.2.1 compatibility
Wheel smoke on ubuntu-latest
Wheel smoke on windows-latest
numba (ubuntu-latest, 3.11)
numba (ubuntu-latest, 3.12)
numba (ubuntu-latest, 3.13)
numba (ubuntu-latest, 3.14)
numba (windows-latest, 3.11)
numba (windows-latest, 3.12)
numba (windows-latest, 3.13)
numba (windows-latest, 3.14)
pardiso (ubuntu-latest, 3.11)
pardiso (windows-latest, 3.11)
pytest (ubuntu-latest, 3.11)
pytest (ubuntu-latest, 3.12)
pytest (ubuntu-latest, 3.13)
pytest (ubuntu-latest, 3.14)
pytest (windows-latest, 3.11)
pytest (windows-latest, 3.12)
pytest (windows-latest, 3.13)
pytest (windows-latest, 3.14)
```

### Phase 2 exact order: terminal Tests monitoring

`RUN_ID` below is a plan token, not a shell variable. The continuation verdict must replace it with the sole positive decimal `databaseId` from `I14`. Before execution, the exact instantiated command is shown in commentary; the actual `shell_command` contains the decimal digits literally and no angle brackets, variable, substitution, or expression.

```text
M01 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Tests --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --event push --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
M02 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
M03 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
M04 & 'C:\Program Files\GitHub CLI\gh.exe' run watch RUN_ID --repo audunarn/ANYsolver --exit-status --interval 15
M05 & 'C:\Program Files\GitHub CLI\gh.exe' run view RUN_ID --repo audunarn/ANYsolver --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt,jobs'
M06 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
M07 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
```

The shared Phase 2 deadline starts immediately before `M01` and expires 55 minutes later. `M01-M03` must complete before `M04`; `M04` has a separate hard cap of 50 minutes, leaving at least five minutes within the shared deadline for `M05-M07`. `M01` and `M02` must still identify exactly the same sole Tests push run and `M03` must be `[]`; otherwise `M04` does not start. `M04` must exit zero only when the run is terminal-successful. Either the 50-minute `M04` cap or the shared 55-minute deadline expiring is terminal and permits no retry or subsequent query without new Boss authority. If `M04` exits nonzero because the remote run reached a failed terminal state, `M05` is the sole pre-authorized read-only failure-accounting call; it is not a retry. `M05` must identify the same run, return exactly 24 unique jobs, and match the exact ordinal job-name oracle above. Success requires run conclusion `success` and all 24 job conclusions `success`, with every job ID, name, URL, timestamps, status, and conclusion retained. `M06` must contain only that run and `M07` must be `[]`.

### Final five-minute verification

After successful `M07`, run the following exact read-only sequence. Each line and each `W` member is a separate call.

```text
F01 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse HEAD
F02 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref -q HEAD
F03 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/heads/main
F04 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/main
F05 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' symbolic-ref refs/remotes/origin/HEAD
F06 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' rev-parse refs/remotes/origin/HEAD
F07 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' status --porcelain=v1 --untracked-files=all
F08 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --exit-code origin refs/heads/main
F09 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --refs origin
F10 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' ls-remote --symref origin HEAD
F11 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' for-each-ref '--format=%(refname)%09%(objectname)'
F12 & 'C:\Program Files\Git\cmd\git.exe' --no-optional-locks -c 'safe.directory=C:\Github\ANYsolver' -C 'C:\Github\ANYsolver' worktree list --porcelain
F13 W01 through W28, each as its own call
F14 & 'C:\Program Files\GitHub CLI\gh.exe' run view RUN_ID --repo audunarn/ANYsolver --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt,jobs'
F15 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
F16 & 'C:\Program Files\GitHub CLI\gh.exe' run list --repo audunarn/ANYsolver --workflow Publish --commit 3cdb51efcdded232054225ea0eb9cc16dc79dde9 --limit 100 --json 'databaseId,name,event,headBranch,headSha,status,conclusion,url,createdAt,updatedAt'
```

`F01`, `F03`, `F04`, `F06`, and `F08` are target; `F02` is `refs/heads/main`; `F05` is `refs/remotes/origin/main`; `F07` is empty; `F09` is byte-identical to `R1`; `F10` retains symbolic main and target HEAD; and `F11` through `F13` satisfy the exact stable-ref/worktree/status contracts. `F14` repeats the terminal 24-success result, requires 24 unique names, and matches the exact ordinal job-name oracle. `F15` contains only the same run and `F16` is `[]`.

### Direct-native lease and completion boundary

The existing 70-minute exclusive lease model remains exact:

| Window | Hard bound |
|---|---:|
| `P01-P75` Phase 1 | 5 minutes |
| `I01-I18` independent gate | 5 minutes |
| `M01-M07` shared terminal-monitor deadline | 55 minutes total; `M04` capped at 50 minutes |
| `F01-F16` final verification | 5 minutes |

Local usage is short-lived Git/gh processes only, less than 500 MB task-owned RAM, negligible sustained CPU, and no GPU. Remote usage is the sole push-triggered 24-job Tests matrix. No local build, test, wheel, benchmark, profiler, package operation, or workflow dispatch is authorized.

Completion requires the accepted content hash of this superseding amendment, a fresh Phase 1-only PERF grant, exact `P` and `I` evidence, an explicit Phase 2 continuation with the literal run ID, exact `M` and `F` evidence, authoritative remote main at target, all 24 jobs successful, zero Publish or unexpected runs, every old artifact preserved, no unauthorized mutation or cleanup, and the exact Boss verdict `ECOSYSTEM CLOSEOUT: OK`.
