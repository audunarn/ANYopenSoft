"""Behavioral contract tests using synthetic boundaries only."""
from __future__ import annotations
from copy import deepcopy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tools" / "anysolver_stage_c_flat_catalog_attestation.py"
FIXTURE = Path(__file__).with_name("fixtures") / "anysolver_stage_c_flat_catalog_attestation_v1" / "contract_cases.json"
SPEC = importlib.util.spec_from_file_location("anysolver_stage_c_flat_catalog_attestation", SOURCE)
assert SPEC is not None and SPEC.loader is not None
stage_c = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = stage_c
SPEC.loader.exec_module(stage_c)

def _fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))

def _lookup(root: dict, dotted: str):
    value = root
    for component in dotted.split("."):
        value = value[component]
    return value

def _resolve(value, root: dict):
    if isinstance(value, dict):
        if set(value) == {"$ref"}:
            return _resolve(deepcopy(_lookup(root, value["$ref"])), root)
        return {key: _resolve(item, root) for key, item in value.items()}
    if isinstance(value, list):
        return [_resolve(item, root) for item in value]
    return deepcopy(value)

def _case(name: str) -> dict:
    root = _fixture()
    return _resolve(root["attestation_cases"][name], root)

def _set_path(value, path: list, replacement) -> None:
    target = value
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = replacement

class FakeTrust:
    def __init__(self, case: dict) -> None:
        self.case = case
        self.held = object()
        self.admin = object()
        self.catalogs: dict[object, dict] = {}
        self.calls: list[tuple] = []
        self.identity_calls = 0
    def open_held(self, path: str):
        self.calls.append(("open_held", path))
        return self.held
    def held_identity(self, held: object) -> dict:
        assert held is self.held
        self.calls.append(("held_identity", self.identity_calls))
        sequence = self.case.get("held_identity_sequence", [self.case["held_identity"]])
        row = sequence[min(self.identity_calls, len(sequence) - 1)]
        self.identity_calls += 1
        return deepcopy(row)
    def embedded_verify(self, held: object, configuration: dict) -> dict:
        assert held is self.held
        self.calls.append(("embedded_verify", deepcopy(configuration)))
        return deepcopy(self.case["embedded"])
    def acquire_catalog_admin(self, algorithm: str, flags: int):
        self.calls.append(("acquire_catalog_admin", algorithm, flags))
        return self.admin, deepcopy(self.case["catalog_acquire"])
    def catalog_hash(self, held: object, admin: object, algorithm: str) -> dict:
        assert held is self.held and admin is self.admin
        self.calls.append(("catalog_hash", algorithm))
        return deepcopy(self.case["catalog_hash"])
    def enumerate_catalogs(self, admin: object, member_hash: str) -> dict:
        assert admin is self.admin
        self.calls.append(("enumerate_catalogs", member_hash))
        entries = [{"path": row["path"], "context_id": row["context_id"]} for row in self.case.get("candidates", [])]
        previous = None
        calls = []
        for entry in entries:
            calls.append({"previous_context": previous, "returned_context": entry["context_id"], "status": 0})
            previous = entry["context_id"]
        calls.append({"previous_context": previous, "returned_context": None, "status": 1168})
        row = {"entries": entries, "calls": calls, "end": {"status": 1168, "symbol": "ERROR_NOT_FOUND"}}
        return deepcopy(self.case.get("enumeration_override", row))
    def open_catalog(self, candidate: dict):
        match = next(row for row in self.case["candidates"] if row["context_id"] == candidate["context_id"])
        token = object()
        self.catalogs[token] = match
        self.calls.append(("open_catalog", match["path"]))
        return token
    def catalog_identity(self, catalog: object) -> dict:
        row = self.catalogs[catalog]
        count = sum(1 for call in self.calls if call[:2] == ("catalog_identity", row["path"]))
        self.calls.append(("catalog_identity", row["path"]))
        return deepcopy(row["before_identity"] if count == 0 else row.get("after_identity", row["before_identity"]))
    def verify_catalog(self, held: object, catalog: object, member_hash: str, configuration: dict) -> dict:
        assert held is self.held
        row = self.catalogs[catalog]
        self.calls.append(("verify_catalog", row["path"], deepcopy(configuration), member_hash))
        if "raise_verify" in row:
            raise RuntimeError(row["raise_verify"])
        return deepcopy(row["verify"])
    def close_catalog(self, catalog: object) -> dict:
        row = self.catalogs[catalog]
        self.calls.append(("close_catalog", row["path"]))
        return deepcopy(row.get("handle_close", {"api": "CloseHandle", "return_value": 1, "last_error": 0}))
    def release_catalog_context(self, admin: object, candidate: dict) -> dict:
        assert admin is self.admin
        self.calls.append(("release_catalog_context", candidate["context_id"]))
        row = next(item for item in self.case["candidates"] if item["context_id"] == candidate["context_id"])
        return deepcopy(row.get("context_release", {"api": "CryptCATAdminReleaseCatalogContext", "return_value": 1, "last_error": 0}))
    def release_catalog_admin(self, admin: object) -> dict:
        assert admin is self.admin
        self.calls.append(("release_catalog_admin",))
        return deepcopy(self.case.get("admin_release", {"api": "CryptCATAdminReleaseContext", "return_value": 1, "last_error": 0}))
    def close_held(self, held: object) -> dict:
        assert held is self.held
        self.calls.append(("close_held",))
        return deepcopy(self.case.get("held_close", {"api": "CloseHandle", "return_value": 1, "last_error": 0}))

def _run_observation(spec, held_identity: dict, output: str, mutation: dict | None = None) -> dict:
    pid = 7000 + int(spec.check_id[1:])
    job_id = f"job-{spec.check_id}"
    raw = {
        "argv": list(spec.argv), "timeout_seconds": spec.timeout_seconds,
        "creation": {"pid": pid, "creation_flags": ["CREATE_SUSPENDED", "EXTENDED_STARTUPINFO_PRESENT"], "startup_attributes": {"job_list": [job_id], "handle_list": ["stdin", "stdout", "stderr"]}, "image_identity": deepcopy(held_identity)},
        "job": {"job_id": job_id, "limits": {"kill_on_close": True, "active_process_limit": 1, "job_memory_bytes": 384 * 1024 * 1024}, "member_pids_before_resume": [pid], "final_member_pids": []},
        "events": list(stage_c.CONTAINMENT_EVENT_ORDER),
        "times": {"created_utc": "2026-08-14T10:00:00Z", "resumed_utc": "2026-08-14T10:00:01Z", "terminal_utc": "2026-08-14T10:00:02Z"},
        "wait": {"result": "WAIT_OBJECT_0", "exit_code": 0},
        "streams": {"stdout": output.encode("utf-8"), "stderr": b"", "closed_handles": ["stdin", "stdout", "stderr", "process", "thread", "job"]},
        "resource": {"memory_samples": [{"executor_bytes": 32 * 1024 * 1024, "job_bytes": 64 * 1024 * 1024}]},
    }
    if mutation:
        _set_path(raw, mutation["path"], deepcopy(mutation["value"]))
    return raw

class FakeRunner:
    def __init__(self, root: dict, held_identity: dict, mutation: dict | None = None) -> None:
        self.root, self.held_identity, self.mutation = root, held_identity, mutation
        self.calls: list[str] = []
    def run(self, spec, held: object) -> dict:
        self.calls.append(spec.check_id)
        mutation = self.mutation if self.mutation and self.mutation["check_id"] == spec.check_id else None
        return _run_observation(spec, self.held_identity, self.root["outputs"][spec.check_id], mutation)

def _path_rows() -> list[dict]:
    return [{"leaf": leaf, "exists": False, "ancestors": [{"path": "Q", "exists": True, "kind": "directory", "reparse": False}, {"path": "Q\\wsl" if "\\wsl\\" in leaf else "Q\\provider", "exists": True, "kind": "directory", "reparse": False}]} for leaf in stage_c.PROVIDER_LEAVES]

class FakeSnapshots:
    def __init__(self, root: dict, held_identity: dict, mutation: dict | None = None) -> None:
        self.root, self.held_identity, self.mutation = root, held_identity, mutation
        self.labels: list[str] = []
    def capture(self, label: str, held: object | None) -> dict:
        self.labels.append(label)
        state = "Running" if label in {"post_C03", "post_C04", "post_C05", "final"} else "Stopped"
        activation = None
        transition = "2026-08-14T09:59:00Z"
        if label == "post_C03":
            activation = {"trigger_check": "C03", "trigger_pid": 7003, "observed_utc": "2026-08-14T10:00:01.500000Z"}
            transition = activation["observed_utc"]
        raw = {"label": label, "captured_utc": "2026-08-14T10:00:03Z", "os_identity": deepcopy(self.root["os_identity"]), "path_observations": _path_rows(), "services": [{"name": "WslService", "state": state, "pid": 4000 if state == "Running" else None, "transition_utc": transition, "activation": activation}], "processes": [], "held_identity": None if held is None else deepcopy(self.held_identity)}
        if self.mutation and self.mutation["label"] == label:
            _set_path(raw, self.mutation["path"], deepcopy(self.mutation["value"]))
        return raw

class MemoryStore:
    def __init__(self, fault: str | None = None, target: str | None = None) -> None:
        self.values: dict[str, bytes] = {}
        self.partials: dict[str, bytes] = {}
        self.fault, self.target = fault, target
        self.reopen_counts: dict[str, int] = {}
    def publish(self, relative_path: str, payload: dict) -> dict:
        partial = relative_path + ".partial"
        if relative_path in self.values or partial in self.partials:
            raise stage_c.StageCContractError("not fresh")
        data = stage_c.canonical_json(payload)
        self.partials[partial] = data
        if self.fault == "pre_promotion" and self.target == relative_path:
            raise OSError("synthetic pre-promotion failure")
        self.values[relative_path] = self.partials.pop(partial)
        identity = {"path": relative_path, "bytes": len(data), "sha256": stage_c._sha256(data)}
        if self.fault == "claimed_identity" and self.target == relative_path:
            identity["bytes"] += 1
        return identity
    def reopen(self, relative_path: str) -> bytes:
        self.reopen_counts[relative_path] = self.reopen_counts.get(relative_path, 0) + 1
        if self.fault == "reopen_missing" and self.target == relative_path:
            raise FileNotFoundError(relative_path)
        data = self.values[relative_path]
        if self.fault == "reopen_tamper" and self.target == relative_path:
            return data + b" "
        if self.fault == "second_reopen_tamper" and self.target == relative_path and self.reopen_counts[relative_path] >= 2:
            return data + b" "
        return data

def test_frozen_constants_configs_and_check_table() -> None:
    root = _fixture()
    assert stage_c.IMPLEMENTATION_PLAN_SHA256 == root["implementation_plan_sha256"]
    assert stage_c.EMBEDDED_WINTRUST_CONFIG == root["wintrust_configs"]["embedded"]
    assert stage_c.CATALOG_WINTRUST_CONFIG == root["wintrust_configs"]["catalog"]
    assert [[row.check_id, list(row.argv), row.timeout_seconds] for row in stage_c.CHECK_SPECS] == root["check_specs"]

def test_microsoft_policy_positive_and_every_registered_negative() -> None:
    root = _fixture()
    now = datetime(2026, 8, 14, tzinfo=timezone.utc)
    stage_c.validate_microsoft_provider(root["provider_valid"], now=now)
    for mutation in root["provider_mutations"]:
        provider = deepcopy(root["provider_valid"])
        _set_path(provider, mutation["path"], mutation["value"])
        with pytest.raises(stage_c.StageCContractError, match=mutation["error"]):
            stage_c.validate_microsoft_provider(provider, now=now)

@pytest.mark.parametrize("name,expected", [("embedded_success", "success"), ("catalog_success", "success"), ("no_catalog_candidates", "typed_rejection"), ("nonfallback_failure", "failure"), ("candidate_operational_failure", "failure"), ("candidate_identity_drift", "failure"), ("candidate_close_failure", "failure")])
def test_concrete_attestation_outcomes_and_cleanup(name: str, expected: str) -> None:
    case = _case(name)
    trust = FakeTrust(case)
    outcome = stage_c.attest_catalog(trust, trust.held, case["held_identity"], now=datetime(2026, 8, 14, tzinfo=timezone.utc))
    assert outcome["outcome"] == expected
    assert trust.calls[0][0] == "embedded_verify"
    if any(call[0] == "open_catalog" for call in trust.calls):
        assert sum(call[0] == "close_catalog" for call in trust.calls) == len(case["candidates"])
        assert sum(call[0] == "release_catalog_context" for call in trust.calls) == len(case["candidates"])

def test_all_candidates_attempted_in_deterministic_order_despite_failure() -> None:
    case = _case("repeated_candidates")
    trust = FakeTrust(case)
    result = stage_c.attest_catalog(trust, trust.held, case["held_identity"], now=datetime(2026, 8, 14, tzinfo=timezone.utc))
    assert result["outcome"] == "failure"
    attempted = [call[1] for call in trust.calls if call[0] == "open_catalog"]
    assert attempted == sorted(attempted, key=str.casefold) and len(attempted) == 3

def test_only_exact_embedded_nosignature_falls_back() -> None:
    for name, fallback in (("no_catalog_candidates", True), ("nonfallback_failure", False)):
        case = _case(name)
        trust = FakeTrust(case)
        stage_c.attest_catalog(trust, trust.held, case["held_identity"], now=datetime(2026, 8, 14, tzinfo=timezone.utc))
        assert any(call[0] == "acquire_catalog_admin" for call in trust.calls) is fallback

def test_contained_run_positive_and_every_registered_negative() -> None:
    root = _fixture()
    spec = stage_c.CHECK_SPECS[0]
    valid = _run_observation(spec, root["held_identity"], root["outputs"]["C02"])
    summary = stage_c.validate_contained_run(valid, spec, root["held_identity"])
    assert summary["terminal"] and summary["zero_pid"] and summary["handles_closed"]
    for mutation in root["contained_negative_mutations"]:
        raw = deepcopy(valid)
        _set_path(raw, mutation["path"], mutation["value"])
        with pytest.raises(stage_c.StageCContractError, match=mutation["error"]):
            stage_c.validate_contained_run(raw, spec, root["held_identity"])

def test_snapshot_positive_activation_and_every_registered_negative() -> None:
    root = _fixture()
    snapshots = FakeSnapshots(root, root["held_identity"])
    pre = stage_c.validate_snapshot(snapshots.capture("pre", None), label="pre", expected_os=None, held_identity=None)
    post = stage_c.validate_snapshot(snapshots.capture("post_C01", object()), label="post_C01", expected_os=root["os_identity"], held_identity=root["held_identity"], previous=pre)
    trigger = {"pid": 7003, "start_utc": "2026-08-14T10:00:01Z", "end_utc": "2026-08-14T10:00:02Z"}
    stage_c.validate_snapshot(snapshots.capture("post_C03", object()), label="post_C03", expected_os=root["os_identity"], held_identity=root["held_identity"], previous=post, trigger_check="C03", trigger_process=trigger, allow_query_activation=True)
    for mutation in root["snapshot_negative_mutations"]:
        fake = FakeSnapshots(root, root["held_identity"], {"label": "post_C01", "path": mutation["path"], "value": mutation["value"]})
        with pytest.raises(stage_c.StageCContractError, match=mutation["error"]):
            stage_c.validate_snapshot(fake.capture("post_C01", object()), label="post_C01", expected_os=root["os_identity"], held_identity=root["held_identity"], previous=pre)

def test_exact_c02_c05_parsing_and_negative_observations() -> None:
    root = _fixture()
    assert stage_c.parse_c02(root["outputs"]["C02"].encode())["wsl_version"] == "2.6.1.0"
    assert stage_c.parse_c03(root["outputs"]["C03"].encode())["fields"]["Default Version"] == "2"
    assert stage_c.parse_c04(root["outputs"]["C04"].encode())["names"] == stage_c.parse_c05(root["outputs"]["C05"].encode())["names"]
    for case in root["parser_negative_cases"]:
        with pytest.raises(stage_c.StageCContractError, match=case["error"]):
            getattr(stage_c, f"parse_{case['check_id'].lower()}")(case["text"].encode())

def test_flat_campaign_pre_snapshot_held_cleanup_reopen_and_manifest() -> None:
    root, case = _fixture(), _case("embedded_success")
    trust = FakeTrust(case)
    runner = FakeRunner(root, case["held_identity"])
    snapshots = FakeSnapshots(root, case["held_identity"])
    store = MemoryStore()
    result = stage_c.run_flat_campaign(campaign_id="a" * 64, trust=trust, runner=runner, snapshots=snapshots, store=store, allow_query_activation=True, now=datetime(2026, 8, 14, tzinfo=timezone.utc))
    assert result["manifest"]["overall_outcome"] == "success"
    assert snapshots.labels == ["pre", "post_C01", "post_C02", "post_C03", "post_C04", "post_C05", "final"]
    assert trust.calls[0] == ("open_held", stage_c.WSL_PATH) and trust.calls[-1] == ("close_held",)
    assert runner.calls == ["C02", "C03", "C04", "C05"]
    assert all(store.reopen_counts[f"checks/{check}/receipt.json"] >= 2 for check in ("C01", "C02", "C03", "C04", "C05"))
    assert list(store.values)[-1] == "terminal_manifest.json"

@pytest.mark.parametrize("fault", ["pre_promotion", "reopen_missing", "reopen_tamper", "claimed_identity", "second_reopen_tamper"])
def test_receipt_and_manifest_negative_lifecycle_blocks_terminal_manifest(fault: str) -> None:
    root, case = _fixture(), _case("embedded_success")
    store = MemoryStore(fault, "checks/C01/receipt.json")
    with pytest.raises((stage_c.StageCContractError, OSError, FileNotFoundError)):
        stage_c.run_flat_campaign(campaign_id="b" * 64, trust=FakeTrust(case), runner=FakeRunner(root, case["held_identity"]), snapshots=FakeSnapshots(root, case["held_identity"]), store=store, allow_query_activation=True, now=datetime(2026, 8, 14, tzinfo=timezone.utc))
    assert "terminal_manifest.json" not in store.values
    if fault == "pre_promotion":
        assert "checks/C01/receipt.json.partial" in store.partials

def test_manifest_publication_reopen_failure_is_terminal() -> None:
    root, case = _fixture(), _case("embedded_success")
    store = MemoryStore("reopen_tamper", "terminal_manifest.json")
    with pytest.raises(stage_c.StageCContractError, match="manifest reopen"):
        stage_c.run_flat_campaign(campaign_id="c" * 64, trust=FakeTrust(case), runner=FakeRunner(root, case["held_identity"]), snapshots=FakeSnapshots(root, case["held_identity"]), store=store, allow_query_activation=True, now=datetime(2026, 8, 14, tzinfo=timezone.utc))

def test_stale_final_and_partial_are_rejected_without_cleanup() -> None:
    payload = stage_c.make_check_receipt(campaign_id="d" * 64, check_id="C01", input_identity=_fixture()["held_identity"], outcome="success", observation={}, process=None, resource=None, cleanup={}, primary_error=None)
    for stale in ("final", "partial"):
        store = MemoryStore()
        path = "checks/C01/receipt.json"
        if stale == "final":
            store.values[path] = b"stale"
        else:
            store.partials[path + ".partial"] = b"stale"
        with pytest.raises(stage_c.StageCContractError, match="not fresh"):
            store.publish(path, payload)
