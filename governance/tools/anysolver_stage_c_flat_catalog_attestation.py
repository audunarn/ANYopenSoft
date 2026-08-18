"""Flat, side-effect-free Stage-C catalog attestation orchestration.

Real Windows trust, snapshot, and contained-process operations are injected.
This module owns exact policy, ordering, validation, atomic receipts, and the
flat terminal manifest. Importing it performs no host operation.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any, Mapping, Protocol, Sequence

SCOPE_PLAN_SHA256 = "FCD071559C10AF0827E185A84F8042AD8915A16C5100C29F0A0209D76268CE9D"
IMPLEMENTATION_PLAN_SHA256 = "F7FFF227FB3167F71E433EC0E748FE1D12A2E37120F7EC1F10FDE63151B246CF"
V4_PACKET_SHA256 = "DC0E416339CCF5BB66F7EADA6C571FAEEE636129C6902D73683AEEBCBA65DA0E"
V4_EXECUTOR_SHA256 = "9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D"
D5_PLAN_SHA256 = "D5FBB6527192026CA6923751B16E96731786AAFE1CC9C37CEBCE8820C49EE88E"
WSL_PATH = r"C:\WINDOWS\system32\wsl.exe"
TRUST_E_NOSIGNATURE = 0x800B0100
TRUST_E_EXPLICIT_DISTRUST = 0x800B0111
CERT_E_UNTRUSTEDROOT = 0x800B0109
CERT_E_CHAINING = 0x800B010A
CLEAN_CATALOG_REJECTIONS = frozenset({TRUST_E_NOSIGNATURE, TRUST_E_EXPLICIT_DISTRUST, CERT_E_UNTRUSTEDROOT, CERT_E_CHAINING})
GENERIC_VERIFY_V2 = "00AAC56B-CD44-11D0-8CC2-00C04FC295EE"
WINTRUST_PROVIDER_FLAGS = 0x00000080 | 0x00001000 | 0x00002000
EXPECTED_WSL_VERSION = "2.6.1.0"
CHECK_RECEIPT_SCHEMA = "anysolver.stage_c.flat_check_receipt/1"
TERMINAL_MANIFEST_SCHEMA = "anysolver.stage_c.flat_terminal_manifest/1"
MAX_COMBINED_MEMORY_BYTES = 500 * 1024 * 1024
MAX_STREAM_BYTES = 2 * 1024 * 1024
EMBEDDED_WINTRUST_CONFIG = {
    "action_guid": GENERIC_VERIFY_V2,
    "ui_choice": "WTD_UI_NONE",
    "revocation_checks": "WTD_REVOKE_WHOLECHAIN",
    "union_choice": "WTD_CHOICE_FILE",
    "state_action": "WTD_STATEACTION_VERIFY",
    "provider_flags": WINTRUST_PROVIDER_FLAGS,
    "ui_context": "WTD_UICONTEXT_EXECUTE",
}
CATALOG_WINTRUST_CONFIG = {**EMBEDDED_WINTRUST_CONFIG, "union_choice": "WTD_CHOICE_CATALOG"}
PROVIDER_DISTROS = ("ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1", "ANYsolver-Ubuntu-24.04-82a9db28")
PROVIDER_LEAVES = (
    r"Q\wsl\ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1",
    r"Q\wsl\ANYsolver-Ubuntu-24.04-82a9db28",
    r"Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar",
    r"Q\provider\ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar.partial",
)
HELD_WSL_IDENTITY = {"canonical_path": WSL_PATH, "bytes": 278_528, "sha256": "E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126"}
ALLOWED_CRITICAL_EXTENSIONS = frozenset({"2.5.29.14", "2.5.29.15", "2.5.29.19", "2.5.29.32", "2.5.29.35", "2.5.29.37"})
CODE_SIGNING_EKU = "1.3.6.1.5.5.7.3.3"

class StageCContractError(RuntimeError):
    """A deterministic contract or operational gate failed."""

@dataclass(frozen=True, slots=True)
class CheckSpec:
    check_id: str
    argv: tuple[str, ...]
    timeout_seconds: int

CHECK_SPECS = (
    CheckSpec("C02", (WSL_PATH, "--version"), 30),
    CheckSpec("C03", (WSL_PATH, "--status"), 45),
    CheckSpec("C04", (WSL_PATH, "--list", "--verbose"), 45),
    CheckSpec("C05", (WSL_PATH, "--list", "--quiet"), 45),
)
CAMPAIGN_DEADLINE_SECONDS = 300
FINALIZATION_RESERVE_SECONDS = 60
CHECK_RECEIPT_FIELDS = frozenset({"schema", "campaign_id", "check_id", "created_utc", "input_identity", "outcome", "observation", "process", "resource", "cleanup", "primary_error", "secondary_errors"})
TERMINAL_MANIFEST_FIELDS = frozenset({"schema", "campaign_id", "created_utc", "immutable_inputs", "ordered_checks", "check_receipts", "overall_outcome", "primary_error", "secondary_errors", "retry_allowed", "cleanup_allowed"})
FILE_IDENTITY_FIELDS = frozenset({"canonical_path", "bytes", "sha256", "volume_serial", "file_id"})
SNAPSHOT_FIELDS = frozenset({"label", "captured_utc", "os_identity", "path_observations", "services", "processes", "held_identity"})
CONTAINED_FIELDS = frozenset({"argv", "timeout_seconds", "creation", "job", "events", "times", "wait", "streams", "resource"})
CONTAINMENT_EVENT_ORDER = (
    "job_created", "stdio_created", "attributes_initialized", "process_created_suspended",
    "job_membership_observed", "image_identity_observed", "thread_resumed", "process_signaled",
    "streams_drained", "process_handle_closed", "thread_handle_closed", "residual_process_query", "job_closed",
)

class TrustBoundary(Protocol):
    def open_held(self, path: str) -> object: ...
    def held_identity(self, held: object) -> Mapping[str, Any]: ...
    def embedded_verify(self, held: object, configuration: Mapping[str, Any]) -> Mapping[str, Any]: ...
    def acquire_catalog_admin(self, algorithm: str, flags: int) -> tuple[object, Mapping[str, Any]]: ...
    def catalog_hash(self, held: object, admin: object, algorithm: str) -> Mapping[str, Any]: ...
    def enumerate_catalogs(self, admin: object, member_hash: str) -> Mapping[str, Any]: ...
    def open_catalog(self, candidate: Mapping[str, Any]) -> object: ...
    def catalog_identity(self, catalog: object) -> Mapping[str, Any]: ...
    def verify_catalog(self, held: object, catalog: object, member_hash: str, configuration: Mapping[str, Any]) -> Mapping[str, Any]: ...
    def close_catalog(self, catalog: object) -> Mapping[str, Any]: ...
    def release_catalog_context(self, admin: object, candidate: Mapping[str, Any]) -> Mapping[str, Any]: ...
    def release_catalog_admin(self, admin: object) -> Mapping[str, Any]: ...
    def close_held(self, held: object) -> Mapping[str, Any]: ...

class ContainedRunner(Protocol):
    def run(self, spec: CheckSpec, held: object) -> Mapping[str, Any]: ...

class SnapshotBoundary(Protocol):
    def capture(self, label: str, held: object | None) -> Mapping[str, Any]: ...

class ReceiptStore(Protocol):
    def publish(self, relative_path: str, payload: Mapping[str, Any]) -> Mapping[str, Any]: ...
    def reopen(self, relative_path: str) -> bytes: ...

def _utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def canonical_json(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8") + b"\n"

def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()

def _error(exc: BaseException, phase: str) -> dict[str, Any]:
    return {"phase": phase, "type": type(exc).__name__, "message_sha256": _sha256(str(exc).encode("utf-8"))}

def _require_keys(value: Mapping[str, Any], expected: frozenset[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise StageCContractError(f"{label} keys differ: missing={sorted(expected - actual)!r}, extra={sorted(actual - expected)!r}")

def _parse_utc(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise StageCContractError(f"{label} is absent")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise StageCContractError(f"{label} is invalid") from exc
    if parsed.tzinfo is None:
        raise StageCContractError(f"{label} is not timezone-aware")
    return parsed.astimezone(timezone.utc)

def _normalize_identity(value: Mapping[str, Any], label: str, *, held: bool = False) -> dict[str, Any]:
    if not FILE_IDENTITY_FIELDS <= set(value):
        raise StageCContractError(f"{label} file identity is incomplete")
    path = str(value["canonical_path"])
    size = int(value["bytes"])
    sha = str(value["sha256"]).upper()
    volume = int(value["volume_serial"])
    file_id = str(value["file_id"]).upper()
    if not path or size < 0 or volume < 0 or not file_id or not re.fullmatch(r"[0-9A-F]{64}", sha):
        raise StageCContractError(f"{label} file identity is malformed")
    normalized = {"canonical_path": path, "bytes": size, "sha256": sha, "volume_serial": volume, "file_id": file_id}
    if held:
        if value.get("access") != ["FILE_READ_ATTRIBUTES", "GENERIC_READ"]:
            raise StageCContractError("held access does not prove readable identity")
        if value.get("share") != ["FILE_SHARE_READ"]:
            raise StageCContractError("held file permits write/delete replacement")
        for key, expected in HELD_WSL_IDENTITY.items():
            actual = normalized[key]
            if (key == "canonical_path" and actual.casefold() != str(expected).casefold()) or (key != "canonical_path" and actual != expected):
                raise StageCContractError(f"held wsl.exe {key} mismatch")
        normalized["access"] = list(value["access"])
        normalized["share"] = list(value["share"])
    return normalized

def _same_file(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    return all((str(left[key]).casefold() == str(right[key]).casefold()) if key == "canonical_path" else left[key] == right[key] for key in FILE_IDENTITY_FIELDS)

def _validate_api_close(row: Mapping[str, Any], api: str, label: str) -> dict[str, Any]:
    expected = {"api", "return_value", "last_error"}
    if set(row) != expected or row.get("api") != api or int(row.get("return_value", 0)) != 1 or int(row.get("last_error", -1)) != 0:
        raise StageCContractError(f"{label} cleanup failed")
    return dict(row)

def validate_microsoft_provider(provider: Mapping[str, Any], *, now: datetime | None = None) -> dict[str, Any]:
    if provider.get("provider_present") is not True or provider.get("signer_present") is not True:
        raise StageCContractError("WinTrust provider/signer is absent")
    chain = provider.get("chain")
    errors = provider.get("certificate_errors")
    if not isinstance(chain, list) or len(chain) < 2 or not isinstance(errors, list) or len(errors) != len(chain):
        raise StageCContractError("WinTrust chain evidence is incomplete")
    if int(provider.get("signer_error", -1)) != 0 or int(provider.get("chain_trust_error", -1)) != 0:
        raise StageCContractError("WinTrust signer/chain reports an error")
    if provider.get("chain_trust_info") is None or any(int(row.get("error", -1)) != 0 for row in errors):
        raise StageCContractError("WinTrust certificate error evidence failed")
    leaf, root = chain[0], chain[-1]
    if not isinstance(leaf, Mapping) or not isinstance(root, Mapping):
        raise StageCContractError("WinTrust certificate rows are malformed")
    if leaf.get("subject_o") != "Microsoft Corporation" or leaf.get("subject_cn") not in ("Microsoft Windows", "Microsoft Corporation"):
        raise StageCContractError("leaf Microsoft identity failed")
    if CODE_SIGNING_EKU not in leaf.get("ekus", []):
        raise StageCContractError("leaf lacks code-signing EKU")
    critical = leaf.get("critical_extensions")
    if not isinstance(critical, list) or set(critical) - ALLOWED_CRITICAL_EXTENSIONS:
        raise StageCContractError("leaf critical extensions failed")
    if leaf.get("test_cert") or leaf.get("provider_error") or leaf.get("revoked_reason"):
        raise StageCContractError("leaf is test, revoked, or provider-error")
    if root.get("subject_o") != "Microsoft Corporation" or not root.get("trusted_root") or not root.get("self_signed") or root.get("test_cert"):
        raise StageCContractError("root Microsoft trust failed")
    moment = datetime.now(timezone.utc) if now is None else now.astimezone(timezone.utc)
    if not (_parse_utc(leaf.get("not_before"), "leaf not_before") <= moment <= _parse_utc(leaf.get("not_after"), "leaf not_after")):
        raise StageCContractError("leaf validity failed")
    return {"leaf": dict(leaf), "root": dict(root), "chain": list(chain)}

def _validate_wintrust_row(row: Mapping[str, Any], configuration: Mapping[str, Any], label: str) -> tuple[int, dict[str, Any]]:
    if set(row) != {"configuration", "verify_call", "provider", "close_call"} or dict(row.get("configuration", {})) != dict(configuration):
        raise StageCContractError(f"{label} WinTrust configuration mismatch")
    verify = row.get("verify_call")
    close = row.get("close_call")
    if not isinstance(verify, Mapping) or set(verify) != {"api", "state_data", "status"}:
        raise StageCContractError(f"{label} VERIFY evidence malformed")
    status = int(verify.get("status", -1)) & 0xFFFFFFFF
    state_data = str(verify.get("state_data", ""))
    if verify.get("api") != "WinVerifyTrust" or not state_data:
        raise StageCContractError(f"{label} VERIFY was not performed")
    if not isinstance(close, Mapping) or set(close) != {"api", "state_action", "state_data", "status"}:
        raise StageCContractError(f"{label} CLOSE evidence malformed")
    if close.get("api") != "WinVerifyTrust" or close.get("state_action") != "WTD_STATEACTION_CLOSE" or close.get("state_data") != state_data or int(close.get("status", -1)) != 0:
        raise StageCContractError(f"{label} CLOSE failed or did not match VERIFY")
    if not isinstance(row.get("provider"), Mapping):
        raise StageCContractError(f"{label} provider evidence malformed")
    return status, dict(row["provider"])

def _validate_catalog_hash(row: Mapping[str, Any]) -> str:
    if set(row) != {"algorithm", "size_query", "fill", "position"} or row.get("algorithm") != "SHA256":
        raise StageCContractError("catalog hash call is malformed")
    if row.get("size_query") != {"api": "CryptCATAdminCalcHashFromFileHandle2", "status": 0, "required_bytes": 32}:
        raise StageCContractError("catalog hash sizing failed")
    fill = row.get("fill")
    position = row.get("position")
    if not isinstance(fill, Mapping) or set(fill) != {"api", "status", "bytes_filled", "member_hash"}:
        raise StageCContractError("catalog hash fill evidence malformed")
    member_hash = str(fill.get("member_hash", "")).upper()
    if fill.get("api") != "CryptCATAdminCalcHashFromFileHandle2" or int(fill.get("status", -1)) != 0 or int(fill.get("bytes_filled", -1)) != 32 or not re.fullmatch(r"[0-9A-F]{64}", member_hash):
        raise StageCContractError("catalog hash fill failed")
    if not isinstance(position, Mapping) or set(position) != {"before", "after"} or int(position["before"]) != int(position["after"]):
        raise StageCContractError("catalog hash file position was not restored")
    return member_hash

def _candidate_sort_key(row: Mapping[str, Any]) -> tuple[str, str]:
    path = str(row.get("path", ""))
    context = str(row.get("context_id", ""))
    if not path or not context:
        raise StageCContractError("catalog descriptor lacks path/context")
    return path.casefold(), context

def _validate_enumeration(row: Mapping[str, Any]) -> list[dict[str, Any]]:
    if set(row) != {"entries", "calls", "end"}:
        raise StageCContractError("catalog enumeration evidence malformed")
    entries, calls = row.get("entries"), row.get("calls")
    if not isinstance(entries, list) or not isinstance(calls, list) or len(calls) != len(entries) + 1:
        raise StageCContractError("catalog enumeration call count mismatch")
    previous: str | None = None
    contexts: set[str] = set()
    materialized: list[dict[str, Any]] = []
    for entry, call in zip(entries, calls[:-1], strict=True):
        if not isinstance(entry, Mapping) or not isinstance(call, Mapping):
            raise StageCContractError("catalog enumeration row malformed")
        context = str(entry.get("context_id", ""))
        if not context or context in contexts or call != {"previous_context": previous, "returned_context": context, "status": 0}:
            raise StageCContractError("catalog enumeration ownership/order failed")
        contexts.add(context)
        previous = context
        materialized.append(dict(entry))
    if row.get("end") != {"status": 1168, "symbol": "ERROR_NOT_FOUND"} or calls[-1] != {"previous_context": previous, "returned_context": None, "status": 1168}:
        raise StageCContractError("catalog enumeration did not end cleanly")
    return sorted(materialized, key=_candidate_sort_key)

def attest_catalog(boundary: TrustBoundary, held: object, held_identity: Mapping[str, Any], *, now: datetime | None = None) -> dict[str, Any]:
    initial = _normalize_identity(held_identity, "held before C01", held=True)
    events: list[dict[str, Any]] = []
    operational_errors: list[dict[str, Any]] = []
    accepted: list[dict[str, Any]] = []
    clean_rejections = 0
    admin: object | None = None
    catalog_required = False
    try:
        row = dict(boundary.embedded_verify(held, dict(EMBEDDED_WINTRUST_CONFIG)))
        status, provider = _validate_wintrust_row(row, EMBEDDED_WINTRUST_CONFIG, "embedded")
        event = {"event": "embedded", "status": status, "configuration": dict(EMBEDDED_WINTRUST_CONFIG), "verify_call": row["verify_call"], "close_call": row["close_call"], "outcome": "failure"}
        if status == 0:
            policy = validate_microsoft_provider(provider, now=now)
            event.update({"outcome": "success", "policy": policy})
            accepted.append({"mode": "embedded", "policy": policy})
        elif status == TRUST_E_NOSIGNATURE:
            event["outcome"] = "typed_rejection"
            clean_rejections += 1
            catalog_required = True
        else:
            raise StageCContractError(f"embedded non-fallback status 0x{status:08X}")
        events.append(event)
    except BaseException as exc:
        operational_errors.append(_error(exc, "embedded_verify"))
    if catalog_required and not operational_errors:
        try:
            admin, acquire = boundary.acquire_catalog_admin("SHA256", 0)
            acquire_row = dict(acquire)
            if acquire_row != {"api": "CryptCATAdminAcquireContext2", "algorithm": "SHA256", "flags": 0, "return_value": 1, "last_error": 0}:
                raise StageCContractError("catalog admin acquisition failed")
            events.append({"event": "catalog_admin_acquire", "row": acquire_row, "outcome": "success"})
            hash_row = dict(boundary.catalog_hash(held, admin, "SHA256"))
            member_hash = _validate_catalog_hash(hash_row)
            events.append({"event": "catalog_hash", "row": hash_row, "member_hash": member_hash, "outcome": "success"})
            enumeration_row = dict(boundary.enumerate_catalogs(admin, member_hash))
            candidates = _validate_enumeration(enumeration_row)
            events.append({"event": "catalog_enumeration", "row": enumeration_row, "ordered_descriptors": [{"path": item["path"], "context_id": item["context_id"]} for item in candidates], "outcome": "success" if candidates else "typed_rejection"})
            actual_ids: dict[tuple[int, str], tuple[int, str]] = {}
            for ordinal, candidate in enumerate(candidates):
                attempt: dict[str, Any] = {"event": "catalog_candidate", "ordinal": ordinal, "descriptor": {"path": candidate["path"], "context_id": candidate["context_id"]}, "before_identity": None, "after_identity": None, "verify_call": None, "close_call": None, "catalog_handle_close": None, "context_release": None, "outcome": "failure", "primary_error": None, "secondary_errors": []}
                candidate_errors: list[dict[str, Any]] = []
                catalog_handle: object | None = None
                try:
                    catalog_handle = boundary.open_catalog(candidate)
                    before = _normalize_identity(boundary.catalog_identity(catalog_handle), f"candidate {ordinal} before")
                    attempt["before_identity"] = before
                    alias_key = (before["volume_serial"], before["file_id"])
                    content = (before["bytes"], before["sha256"])
                    if alias_key in actual_ids and actual_ids[alias_key] != content:
                        raise StageCContractError("CATALOG_IDENTITY_CONFLICT")
                    actual_ids[alias_key] = content
                    verify_row = dict(boundary.verify_catalog(held, catalog_handle, member_hash, dict(CATALOG_WINTRUST_CONFIG)))
                    status, provider = _validate_wintrust_row(verify_row, CATALOG_WINTRUST_CONFIG, f"candidate {ordinal}")
                    attempt["verify_call"] = verify_row["verify_call"]
                    attempt["close_call"] = verify_row["close_call"]
                    after = _normalize_identity(boundary.catalog_identity(catalog_handle), f"candidate {ordinal} after")
                    attempt["after_identity"] = after
                    if not _same_file(before, after):
                        raise StageCContractError("catalog candidate identity drift")
                    if status == 0:
                        policy = validate_microsoft_provider(provider, now=now)
                        attempt.update({"outcome": "success", "policy": policy})
                        accepted.append({"mode": "catalog", "ordinal": ordinal, "identity": before, "policy": policy})
                    elif status in CLEAN_CATALOG_REJECTIONS:
                        attempt["outcome"] = "typed_rejection"
                        clean_rejections += 1
                    else:
                        raise StageCContractError(f"candidate operational status 0x{status:08X}")
                except BaseException as exc:
                    candidate_errors.append(_error(exc, f"candidate_{ordinal}"))
                finally:
                    if catalog_handle is not None:
                        try:
                            attempt["catalog_handle_close"] = _validate_api_close(boundary.close_catalog(catalog_handle), "CloseHandle", f"candidate {ordinal} handle")
                        except BaseException as exc:
                            candidate_errors.append(_error(exc, f"candidate_{ordinal}_handle_close"))
                    try:
                        attempt["context_release"] = _validate_api_close(boundary.release_catalog_context(admin, candidate), "CryptCATAdminReleaseCatalogContext", f"candidate {ordinal} context")
                    except BaseException as exc:
                        candidate_errors.append(_error(exc, f"candidate_{ordinal}_context_release"))
                    if candidate_errors:
                        attempt["outcome"] = "failure"
                        attempt["primary_error"] = candidate_errors[0]
                        attempt["secondary_errors"] = candidate_errors[1:]
                        operational_errors.extend(candidate_errors)
                    events.append(attempt)
        except BaseException as exc:
            operational_errors.append(_error(exc, "catalog_fallback"))
        finally:
            if admin is not None:
                try:
                    release = _validate_api_close(boundary.release_catalog_admin(admin), "CryptCATAdminReleaseContext", "catalog admin")
                    events.append({"event": "catalog_admin_release", "row": release, "outcome": "success"})
                except BaseException as exc:
                    error = _error(exc, "catalog_admin_release")
                    operational_errors.append(error)
                    events.append({"event": "catalog_admin_release", "row": None, "outcome": "failure", "primary_error": error})
    try:
        final_identity = _normalize_identity(boundary.held_identity(held), "held after C01", held=True)
        if not _same_file(initial, final_identity):
            raise StageCContractError("held wsl.exe identity drift during C01")
    except BaseException as exc:
        final_identity = None
        operational_errors.append(_error(exc, "held_identity_after_C01"))
    outcome = "failure" if operational_errors else ("success" if accepted else ("typed_rejection" if catalog_required else "failure"))
    return {"outcome": outcome, "held_identity_before": initial, "held_identity_after": final_identity, "events": events, "selected_attestation": accepted[0] if accepted and not operational_errors else None, "accepted_attestations": accepted, "clean_rejection_count": clean_rejections, "primary_error": operational_errors[0] if operational_errors else None, "secondary_errors": operational_errors[1:]}

def decode_wsl_text(data: bytes) -> str:
    if data.startswith(b"\xff\xfe"):
        text = data[2:].decode("utf-16-le", errors="strict")
    elif data.startswith(b"\xfe\xff"):
        text = data[2:].decode("utf-16-be", errors="strict")
    else:
        text = data.decode("utf-8-sig", errors="strict")
    if "\x00" in text:
        raise StageCContractError("WSL output contains NUL")
    return text.replace("\r\n", "\n").replace("\r", "\n")

def _parse_label_values(data: bytes, label: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for raw in decode_wsl_text(data).splitlines():
        line = raw.strip()
        if not line:
            continue
        if ":" not in line:
            raise StageCContractError(f"{label} row lacks colon")
        key, value = (part.strip() for part in line.split(":", 1))
        if not key or not value or key in rows:
            raise StageCContractError(f"{label} row empty/duplicated")
        rows[key] = value
    if not rows:
        raise StageCContractError(f"{label} output empty")
    return rows

def parse_c02(data: bytes) -> dict[str, Any]:
    rows = _parse_label_values(data, "C02")
    if rows.get("WSL version") != EXPECTED_WSL_VERSION:
        raise StageCContractError("C02 WSL version mismatch")
    return {"fields": rows, "wsl_version": rows["WSL version"]}

def parse_c03(data: bytes) -> dict[str, Any]:
    return {"fields": _parse_label_values(data, "C03")}

def parse_c04(data: bytes) -> dict[str, Any]:
    lines = [line.strip() for line in decode_wsl_text(data).splitlines() if line.strip()]
    if not lines or lines[0].split() != ["NAME", "STATE", "VERSION"]:
        raise StageCContractError("C04 header mismatch")
    rows: list[dict[str, Any]] = []
    names: list[str] = []
    for line in lines[1:]:
        fields = line.lstrip("* ").split()
        if len(fields) != 3 or not fields[0] or not fields[1]:
            raise StageCContractError("C04 row malformed")
        try:
            version = int(fields[2])
        except ValueError as exc:
            raise StageCContractError("C04 version malformed") from exc
        if fields[0] in names or fields[0] in PROVIDER_DISTROS:
            raise StageCContractError("C04 duplicate/provider distro")
        names.append(fields[0])
        rows.append({"name": fields[0], "state": fields[1], "version": version})
    return {"rows": rows, "names": names}

def parse_c05(data: bytes) -> dict[str, Any]:
    names = [line.strip() for line in decode_wsl_text(data).splitlines() if line.strip()]
    if len(names) != len(set(names)) or any(name in PROVIDER_DISTROS for name in names):
        raise StageCContractError("C05 duplicate/provider distro")
    return {"names": names}

def validate_contained_run(raw: Mapping[str, Any], spec: CheckSpec, held_identity: Mapping[str, Any]) -> dict[str, Any]:
    _require_keys(raw, CONTAINED_FIELDS, f"{spec.check_id} contained observation")
    if list(raw["argv"]) != list(spec.argv) or int(raw["timeout_seconds"]) != spec.timeout_seconds:
        raise StageCContractError(f"{spec.check_id} argv/timeout mismatch")
    creation, job = raw["creation"], raw["job"]
    if not isinstance(creation, Mapping) or not isinstance(job, Mapping):
        raise StageCContractError("creation/Job evidence malformed")
    pid, job_id = int(creation.get("pid", 0)), str(job.get("job_id", ""))
    if pid <= 0 or not job_id:
        raise StageCContractError("process/Job identity absent")
    if creation.get("creation_flags") != ["CREATE_SUSPENDED", "EXTENDED_STARTUPINFO_PRESENT"]:
        raise StageCContractError("process not created suspended with attributes")
    if creation.get("startup_attributes") != {"job_list": [job_id], "handle_list": ["stdin", "stdout", "stderr"]}:
        raise StageCContractError("creation-time Job/HANDLE_LIST mismatch")
    image = _normalize_identity(creation.get("image_identity", {}), "contained image")
    if not _same_file(image, held_identity):
        raise StageCContractError("contained image differs from held wsl.exe")
    if job.get("limits") != {"kill_on_close": True, "active_process_limit": 1, "job_memory_bytes": 384 * 1024 * 1024}:
        raise StageCContractError("Job limits mismatch")
    if job.get("member_pids_before_resume") != [pid] or job.get("final_member_pids") != []:
        raise StageCContractError("Job membership/residual proof failed")
    if tuple(raw["events"]) != CONTAINMENT_EVENT_ORDER:
        raise StageCContractError("containment event order mismatch")
    times = raw["times"]
    if not isinstance(times, Mapping) or set(times) != {"created_utc", "resumed_utc", "terminal_utc"}:
        raise StageCContractError("contained timestamps malformed")
    created = _parse_utc(times["created_utc"], "created_utc")
    resumed = _parse_utc(times["resumed_utc"], "resumed_utc")
    terminal = _parse_utc(times["terminal_utc"], "terminal_utc")
    elapsed = (terminal - resumed).total_seconds()
    if not created <= resumed <= terminal or elapsed < 0 or elapsed > spec.timeout_seconds:
        raise StageCContractError("contained semantic timeout/order failed")
    if raw["wait"] != {"result": "WAIT_OBJECT_0", "exit_code": 0}:
        raise StageCContractError("contained process did not terminate successfully")
    streams = raw["streams"]
    if not isinstance(streams, Mapping) or set(streams) != {"stdout", "stderr", "closed_handles"}:
        raise StageCContractError("stream evidence malformed")
    stdout, stderr = streams["stdout"], streams["stderr"]
    if not isinstance(stdout, bytes) or not isinstance(stderr, bytes) or len(stdout) > MAX_STREAM_BYTES or len(stderr) > MAX_STREAM_BYTES:
        raise StageCContractError("stream bytes invalid/over cap")
    if streams["closed_handles"] != ["stdin", "stdout", "stderr", "process", "thread", "job"]:
        raise StageCContractError("contained handles not closed exactly")
    samples = raw["resource"].get("memory_samples") if isinstance(raw["resource"], Mapping) else None
    if not isinstance(samples, list) or not samples:
        raise StageCContractError("resource samples absent")
    peak = 0
    for sample in samples:
        combined = int(sample.get("executor_bytes", -1)) + int(sample.get("job_bytes", -1))
        if combined < 0 or combined >= MAX_COMBINED_MEMORY_BYTES:
            raise StageCContractError("combined memory limit exceeded")
        peak = max(peak, combined)
    return {"pid": pid, "job_id": job_id, "image_identity": image, "start_utc": times["resumed_utc"], "end_utc": times["terminal_utc"], "stdout": stdout, "stderr": stderr, "terminal": True, "zero_pid": True, "handles_closed": True, "peak_combined_bytes": peak, "elapsed_seconds": elapsed}

def _service_map(rows: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(rows, list):
        raise StageCContractError("service inventory malformed")
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {"name", "state", "pid", "transition_utc", "activation"}:
            raise StageCContractError("service row malformed")
        name = str(row["name"])
        if not name or name in result:
            raise StageCContractError("service name empty/duplicated")
        result[name] = dict(row)
    return result

def _process_map(rows: Any) -> dict[int, dict[str, Any]]:
    if not isinstance(rows, list):
        raise StageCContractError("process inventory malformed")
    result: dict[int, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {"pid", "image_path", "start_utc", "activation"}:
            raise StageCContractError("process row malformed")
        pid = int(row["pid"])
        if pid <= 0 or pid in result or not str(row["image_path"]):
            raise StageCContractError("process row identity invalid")
        _parse_utc(row["start_utc"], "process start")
        result[pid] = dict(row)
    return result

def validate_snapshot(raw: Mapping[str, Any], *, label: str, expected_os: Mapping[str, Any] | None, held_identity: Mapping[str, Any] | None, previous: Mapping[str, Any] | None = None, trigger_check: str | None = None, trigger_process: Mapping[str, Any] | None = None, allow_query_activation: bool = False) -> dict[str, Any]:
    _require_keys(raw, SNAPSHOT_FIELDS, f"snapshot {label}")
    if raw["label"] != label:
        raise StageCContractError("snapshot label mismatch")
    _parse_utc(raw["captured_utc"], f"snapshot {label} time")
    os_identity = raw["os_identity"]
    if not isinstance(os_identity, Mapping) or set(os_identity) != {"platform", "kernel", "architecture"}:
        raise StageCContractError("snapshot OS identity malformed")
    if expected_os is not None and dict(os_identity) != dict(expected_os):
        raise StageCContractError("snapshot OS identity drift")
    if held_identity is None:
        if raw["held_identity"] is not None:
            raise StageCContractError("pre snapshot unexpectedly has held identity")
    else:
        measured = _normalize_identity(raw["held_identity"], f"snapshot {label} held", held=True)
        if not _same_file(measured, held_identity):
            raise StageCContractError("snapshot held identity drift")
    paths = raw["path_observations"]
    if not isinstance(paths, list) or {row.get("leaf") for row in paths if isinstance(row, Mapping)} != set(PROVIDER_LEAVES):
        raise StageCContractError("snapshot provider path inventory mismatch")
    for row in paths:
        if set(row) != {"leaf", "exists", "ancestors"} or row["exists"] is not False or not isinstance(row["ancestors"], list) or not row["ancestors"]:
            raise StageCContractError("provider leaf absence not proved")
        for ancestor in row["ancestors"]:
            if set(ancestor) != {"path", "exists", "kind", "reparse"} or ancestor["exists"] is not True or ancestor["kind"] != "directory" or ancestor["reparse"] is not False:
                raise StageCContractError("provider ancestor is absent/reparse/non-directory")
    services = _service_map(raw["services"])
    processes = _process_map(raw["processes"])
    if previous is not None:
        old_services, old_processes = _service_map(previous["services"]), _process_map(previous["processes"])
        if set(old_services) - set(services) or set(old_processes) - set(processes):
            raise StageCContractError("snapshot contains unattributed removal")
        service_changes = [row for name, row in services.items() if old_services.get(name) != row]
        process_changes = [row for pid, row in processes.items() if old_processes.get(pid) != row]
        if service_changes or process_changes:
            if not allow_query_activation or trigger_check not in {"C02", "C03"} or trigger_process is None:
                raise StageCContractError("snapshot contains forbidden host delta")
            pid = int(trigger_process["pid"])
            start = _parse_utc(trigger_process["start_utc"], "trigger start")
            end = _parse_utc(trigger_process["end_utc"], "trigger end")
            for row in service_changes + process_changes:
                activation = row.get("activation")
                if not isinstance(activation, Mapping) or activation.get("trigger_check") != trigger_check or int(activation.get("trigger_pid", -1)) != pid:
                    raise StageCContractError("host delta lacks concrete query attribution")
                observed = _parse_utc(activation.get("observed_utc"), "activation observed")
                if not start <= observed <= end:
                    raise StageCContractError("host delta outside query interval")
    if label == "post_C03" and services.get("WslService", {}).get("state") != "Running":
        raise StageCContractError("C03 did not prove running WslService")
    return dict(raw)

def make_check_receipt(*, campaign_id: str, check_id: str, input_identity: Mapping[str, Any], outcome: str, observation: Mapping[str, Any], process: Mapping[str, Any] | None, resource: Mapping[str, Any] | None, cleanup: Mapping[str, Any], primary_error: Mapping[str, Any] | None, secondary_errors: Sequence[Mapping[str, Any]] = ()) -> dict[str, Any]:
    if not re.fullmatch(r"[0-9a-f]{64}", campaign_id) or check_id not in {"C01", "C02", "C03", "C04", "C05"} or outcome not in {"success", "typed_rejection", "failure"}:
        raise StageCContractError("receipt campaign/check/outcome invalid")
    payload = {"schema": CHECK_RECEIPT_SCHEMA, "campaign_id": campaign_id, "check_id": check_id, "created_utc": _utc(), "input_identity": dict(input_identity), "outcome": outcome, "observation": dict(observation), "process": None if process is None else dict(process), "resource": None if resource is None else dict(resource), "cleanup": dict(cleanup), "primary_error": None if primary_error is None else dict(primary_error), "secondary_errors": [dict(row) for row in secondary_errors]}
    _require_keys(payload, CHECK_RECEIPT_FIELDS, "check receipt")
    return payload

def _validate_receipt_bytes(data: bytes, expected: Mapping[str, Any], path: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if data != canonical_json(expected):
        raise StageCContractError(f"receipt reopen bytes differ at {path}")
    try:
        decoded = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StageCContractError("receipt reopen JSON invalid") from exc
    if not isinstance(decoded, dict):
        raise StageCContractError("receipt reopen object invalid")
    _require_keys(decoded, CHECK_RECEIPT_FIELDS, "reopened check receipt")
    if decoded != dict(expected) or decoded["schema"] != CHECK_RECEIPT_SCHEMA:
        raise StageCContractError("receipt reopen semantic mismatch")
    return decoded, {"path": path, "bytes": len(data), "sha256": _sha256(data)}

def _publish_receipt(store: ReceiptStore, check_id: str, payload: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    path = f"checks/{check_id}/receipt.json"
    claimed = dict(store.publish(path, payload))
    decoded, identity = _validate_receipt_bytes(store.reopen(path), payload, path)
    if claimed != identity:
        raise StageCContractError("store publication identity differs from reopened receipt")
    return decoded, identity

def _validate_manifest_bytes(data: bytes, expected: Mapping[str, Any]) -> dict[str, Any]:
    if data != canonical_json(expected):
        raise StageCContractError("terminal manifest reopen bytes differ")
    decoded = json.loads(data.decode("utf-8"))
    if not isinstance(decoded, dict):
        raise StageCContractError("terminal manifest reopen object invalid")
    _require_keys(decoded, TERMINAL_MANIFEST_FIELDS, "terminal manifest")
    if decoded != dict(expected) or decoded["schema"] != TERMINAL_MANIFEST_SCHEMA:
        raise StageCContractError("terminal manifest semantic mismatch")
    return decoded

def _parse_observation(check_id: str, stdout: bytes) -> dict[str, Any]:
    return {"C02": parse_c02, "C03": parse_c03, "C04": parse_c04, "C05": parse_c05}[check_id](stdout)

def run_flat_campaign(*, campaign_id: str, trust: TrustBoundary, runner: ContainedRunner, snapshots: SnapshotBoundary, store: ReceiptStore, allow_query_activation: bool, now: datetime | None = None) -> dict[str, Any]:
    if not re.fullmatch(r"[0-9a-f]{64}", campaign_id):
        raise StageCContractError("campaign_id must be 64 lowercase hex")
    pre = validate_snapshot(dict(snapshots.capture("pre", None)), label="pre", expected_os=None, held_identity=None)
    expected_os = dict(pre["os_identity"])
    current_snapshot = pre
    held: object | None = None
    held_identity: dict[str, Any] | None = None
    drafts: dict[str, dict[str, Any]] = {}
    campaign_errors: list[dict[str, Any]] = []
    parsed_c04: dict[str, Any] | None = None
    c01_observation: dict[str, Any] | None = None
    held_close: dict[str, Any] | None = None
    stop = False
    try:
        held = trust.open_held(WSL_PATH)
        held_identity = _normalize_identity(trust.held_identity(held), "campaign held", held=True)
        c01_observation = attest_catalog(trust, held, held_identity, now=now)
        current_snapshot = validate_snapshot(dict(snapshots.capture("post_C01", held)), label="post_C01", expected_os=expected_os, held_identity=held_identity, previous=current_snapshot, allow_query_activation=allow_query_activation)
        stop = c01_observation["outcome"] != "success"
        for spec in CHECK_SPECS:
            if stop:
                break
            try:
                before = _normalize_identity(trust.held_identity(held), f"held before {spec.check_id}", held=True)
                if not _same_file(before, held_identity):
                    raise StageCContractError("held identity changed before contained run")
                contained = validate_contained_run(dict(runner.run(spec, held)), spec, held_identity)
                after = _normalize_identity(trust.held_identity(held), f"held after {spec.check_id}", held=True)
                if not _same_file(after, held_identity):
                    raise StageCContractError("held identity changed after contained run")
                current_snapshot = validate_snapshot(dict(snapshots.capture(f"post_{spec.check_id}", held)), label=f"post_{spec.check_id}", expected_os=expected_os, held_identity=held_identity, previous=current_snapshot, trigger_check=spec.check_id, trigger_process=contained, allow_query_activation=allow_query_activation)
                observation = _parse_observation(spec.check_id, contained["stdout"])
                if spec.check_id == "C04":
                    parsed_c04 = observation
                if spec.check_id == "C05" and (parsed_c04 is None or observation["names"] != parsed_c04["names"]):
                    raise StageCContractError("C04/C05 ordinal distro arrays differ")
                drafts[spec.check_id] = make_check_receipt(campaign_id=campaign_id, check_id=spec.check_id, input_identity=held_identity, outcome="success", observation=observation, process={key: value for key, value in contained.items() if key not in {"stdout", "stderr", "peak_combined_bytes"}}, resource={"peak_combined_bytes": contained["peak_combined_bytes"]}, cleanup={"zero_pid": contained["zero_pid"], "handles_closed": contained["handles_closed"]}, primary_error=None)
            except BaseException as exc:
                error = _error(exc, spec.check_id)
                campaign_errors.append(error)
                drafts[spec.check_id] = make_check_receipt(campaign_id=campaign_id, check_id=spec.check_id, input_identity=held_identity, outcome="failure", observation={}, process=None, resource=None, cleanup={}, primary_error=error)
                stop = True
        try:
            current_snapshot = validate_snapshot(dict(snapshots.capture("final", held)), label="final", expected_os=expected_os, held_identity=held_identity, previous=current_snapshot, allow_query_activation=allow_query_activation)
        except BaseException as exc:
            campaign_errors.append(_error(exc, "final_snapshot"))
    except BaseException as exc:
        campaign_errors.append(_error(exc, "campaign"))
    finally:
        if held is not None:
            try:
                held_close = _validate_api_close(trust.close_held(held), "CloseHandle", "campaign held")
            except BaseException as exc:
                error = _error(exc, "held_close")
                campaign_errors.append(error)
                held_close = {"error": error}
    if held_identity is None:
        raise StageCContractError("campaign never acquired a valid held identity")
    if c01_observation is None:
        error = campaign_errors[0] if campaign_errors else _error(StageCContractError("C01 absent"), "C01")
        c01_observation = {"outcome": "failure", "events": [], "primary_error": error, "secondary_errors": []}
    c01_observation = dict(c01_observation)
    c01_observation["held_handle_close"] = held_close
    c01_outcome = c01_observation["outcome"] if held_close is not None and "error" not in held_close else "failure"
    drafts["C01"] = make_check_receipt(campaign_id=campaign_id, check_id="C01", input_identity=held_identity, outcome=c01_outcome, observation=c01_observation, process=None, resource=None, cleanup={"held_handle_close": held_close}, primary_error=c01_observation.get("primary_error"), secondary_errors=c01_observation.get("secondary_errors", []))
    validated: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for check_id in ("C01", "C02", "C03", "C04", "C05"):
        if check_id in drafts:
            validated[check_id] = _publish_receipt(store, check_id, drafts[check_id])
    rows: list[dict[str, Any]] = []
    for check_id in ("C01", "C02", "C03", "C04", "C05"):
        if check_id not in validated:
            rows.append({"check_id": check_id, "path": None, "bytes": None, "sha256": None, "outcome": None})
            continue
        receipt, identity = validated[check_id]
        checked, actual_identity = _validate_receipt_bytes(store.reopen(identity["path"]), receipt, identity["path"])
        if actual_identity != identity:
            raise StageCContractError("receipt changed before manifest")
        rows.append({"check_id": check_id, **identity, "outcome": checked["outcome"]})
    success = not campaign_errors and len(validated) == 5 and all(row["outcome"] == "success" for row in rows)
    manifest = {
        "schema": TERMINAL_MANIFEST_SCHEMA,
        "campaign_id": campaign_id,
        "created_utc": _utc(),
        "immutable_inputs": {"scope_plan_sha256": SCOPE_PLAN_SHA256, "implementation_plan_sha256": IMPLEMENTATION_PLAN_SHA256, "v4_packet_sha256": V4_PACKET_SHA256, "v4_executor_sha256": V4_EXECUTOR_SHA256, "d5_plan_sha256": D5_PLAN_SHA256},
        "ordered_checks": ["C01", "C02", "C03", "C04", "C05"],
        "check_receipts": rows,
        "overall_outcome": "success" if success else "failure",
        "primary_error": campaign_errors[0] if campaign_errors else None,
        "secondary_errors": campaign_errors[1:],
        "retry_allowed": False,
        "cleanup_allowed": False,
    }
    _require_keys(manifest, TERMINAL_MANIFEST_FIELDS, "terminal manifest")
    claimed = dict(store.publish("terminal_manifest.json", manifest))
    reopened_manifest = store.reopen("terminal_manifest.json")
    decoded_manifest = _validate_manifest_bytes(reopened_manifest, manifest)
    actual_manifest_identity = {"path": "terminal_manifest.json", "bytes": len(reopened_manifest), "sha256": _sha256(reopened_manifest)}
    if claimed != actual_manifest_identity:
        raise StageCContractError("manifest publication identity mismatch")
    return {"manifest": decoded_manifest, "manifest_identity": actual_manifest_identity, "receipts": {key: value[0] for key, value in validated.items()}, "receipt_identities": {key: value[1] for key, value in validated.items()}}

class LocalAtomicStore:
    """Fresh-path, preserve-on-failure atomic store; no cleanup is attempted."""
    def __init__(self, root: Path) -> None:
        self.root = root
    def _paths(self, relative_path: str) -> tuple[Path, Path]:
        relative = Path(relative_path)
        if relative.is_absolute() or ".." in relative.parts:
            raise StageCContractError("receipt path escapes root")
        final = self.root / relative
        return final, final.with_name(final.name + ".partial")
    def publish(self, relative_path: str, payload: Mapping[str, Any]) -> dict[str, Any]:
        final, partial = self._paths(relative_path)
        if final.exists() or partial.exists():
            raise StageCContractError("receipt final/partial is not fresh")
        final.parent.mkdir(parents=True, exist_ok=True)
        data = canonical_json(payload)
        descriptor = os.open(partial, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(partial, final)
        return {"path": relative_path, "bytes": len(data), "sha256": _sha256(data)}
    def reopen(self, relative_path: str) -> bytes:
        final, _ = self._paths(relative_path)
        return final.read_bytes()
