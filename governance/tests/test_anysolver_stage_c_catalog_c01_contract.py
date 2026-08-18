"""AST-only contract checks for the blocked Stage-C V6 executor.

The executor is never imported or executed by this module.
"""

from __future__ import annotations

import ast
from pathlib import Path


GOVERNANCE = Path(__file__).resolve().parents[1]
EXECUTOR = GOVERNANCE / "tools" / "anysolver_no_numba_residual_stage_c_host_executor.py"
PACKET = GOVERNANCE / "plans" / (
    "ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V6.md"
)
V4_MANIFEST = GOVERNANCE / "evidence" / (
    "ANYSOLVER_STAGE_C_V4_IMMUTABLE_EVIDENCE_MANIFEST_D58E8106.json"
)
IDENTITY_LEDGER = GOVERNANCE / "evidence" / (
    "ANYSOLVER_STAGE_C_CATALOG_C01_ACCEPTED_IDENTITY_LEDGER.json"
)

V4_ENTRIES_FIXTURE = tuple(
    {"relative_path": f"d{index}", "kind": "directory"}
    for index in range(8)
) + tuple(
    {"relative_path": name, "kind": "file"}
    for name in (
        "campaign_intent.json",
        "snapshots/preflight.json",
        "stage_c_failure.json",
    )
)
HISTORICAL_ATTESTATIONS_FIXTURE = (
    {"row_id": "v4_executor", "receipt_relative_path": "campaign_intent.json"},
    {"row_id": "v4_held_member", "receipt_relative_path": "snapshots/preflight.json"},
)
LEDGER_ROWS_FIXTURE = (
    "correction_plan",
    "packet_v6",
    "executor_v6",
    "focused_catalog_contract_v2",
    "v4_manifest",
    "interpreter_receipt",
)


def _source() -> str:
    return EXECUTOR.read_text(encoding="utf-8")


def _tree() -> ast.Module:
    return ast.parse(_source(), filename=str(EXECUTOR))


def _top_level_function(name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in _tree().body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    assert len(matches) == 1, name
    return matches[0]


def _method(class_name: str, method_name: str) -> ast.FunctionDef:
    classes = [
        node
        for node in _tree().body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    ]
    assert len(classes) == 1, class_name
    matches = [
        node
        for node in classes[0].body
        if isinstance(node, ast.FunctionDef) and node.name == method_name
    ]
    assert len(matches) == 1, method_name
    return matches[0]


def _call_name(call: ast.Call) -> str | None:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return None


def _calls(node: ast.AST, name: str) -> list[ast.Call]:
    return [
        child
        for child in ast.walk(node)
        if isinstance(child, ast.Call) and _call_name(child) == name
    ]


def _literal_dict_keys(node: ast.AST) -> set[str]:
    keys: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Dict):
            keys.update(
                key.value
                for key in child.keys
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            )
    return keys


def test_packet_freezes_absent_inputs_and_no_action_boundary() -> None:
    text = PACKET.read_text(encoding="utf-8")
    assert "currently absent" in text
    assert "11/8/3" in text
    assert "grants no Stage-C execution" in text
    assert not V4_MANIFEST.exists()
    assert not IDENTITY_LEDGER.exists()


def test_raw_buffer_is_removed_only_after_promotion_and_reopen() -> None:
    node = _top_level_function("_v5_c01_emit")
    atomic_lines = [call.lineno for call in _calls(node, "_atomic_json")]
    reopen_lines = [call.lineno for call in _calls(node, "_v5_receipt_from_final")]
    deletes = [child for child in ast.walk(node) if isinstance(child, ast.Delete)]
    assert len(atomic_lines) == len(reopen_lines) == len(deletes) == 1
    assert atomic_lines[0] < reopen_lines[0] < deletes[0].lineno
    names = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
    assert "is_failure" in names


def test_candidate_results_are_emitted_after_handle_and_context_close() -> None:
    node = _top_level_function("_v5_catalog_authenticode_identity")
    finals = [child for child in ast.walk(node) if isinstance(child, ast.Try) and child.finalbody]
    containing = []
    for child in finals:
        body = ast.Module(body=child.finalbody, type_ignores=[])
        if _calls(body, "_v5_close_held_file") and _calls(body, "_v5_record_c01_event"):
            containing.append(body)
    assert len(containing) == 1
    close_line = min(call.lineno for call in _calls(containing[0], "_v5_close_held_file"))
    emit_line = min(call.lineno for call in _calls(containing[0], "_v5_record_c01_event"))
    assert close_line < emit_line
    assert {"candidate_handle_close", "catalog_context_release"} <= _literal_dict_keys(node)


def test_embedded_attempt_has_raw_verify_and_close_proof() -> None:
    attempt = _top_level_function("_v5_wintrust_attempt")
    identity = _top_level_function("_authenticode_identity")
    assert {"verify_call", "close_proof", "provider_error"} <= _literal_dict_keys(attempt)
    validate_lines = [call.lineno for call in _calls(identity, "_v5_validate_microsoft_provider")]
    emit_lines = [call.lineno for call in _calls(identity, "_v5_record_c01_event")]
    assert len(validate_lines) == 1
    assert any(line > validate_lines[0] for line in emit_lines)


def test_consumer_binding_precedes_reopen_and_lanes_are_explicit() -> None:
    register = _method("_GlobalReceiptChain", "register")
    binding_lines = [
        child.lineno
        for child in ast.walk(register)
        if isinstance(child, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "consumer_binding"
            for target in child.targets
        )
    ]
    reopen_lines = [call.lineno for call in _calls(register, "_v5_receipt_from_final")]
    assert len(binding_lines) == 1 and reopen_lines
    assert binding_lines[0] < min(reopen_lines)
    finalize = _top_level_function("_v5_finalize_run_consumers")
    assert "failure_final_count" in [arg.arg for arg in finalize.args.kwonlyargs]
    constants = {child.value for child in ast.walk(finalize) if isinstance(child, ast.Constant)}
    assert {0, 1, 2, "c05_success", "postprocess_failure"} <= constants


def test_fatal_frames_retain_mandatory_truth_in_all_forms() -> None:
    mandatory = {
        "attempt_id",
        "run_id",
        "attempted_consumer_id",
        "promoted_receipt",
        "prior_receipt",
        "durable_head",
        "primary_error_type",
        "primary_message_sha256",
        "containment_owner",
        "containment_terminal",
        "containment_zero_pid",
        "stage_c_failure_published",
        "success_report_published",
        "retry_allowed",
        "cleanup_allowed",
    }
    assert mandatory <= _literal_dict_keys(_top_level_function("_v5_fatal_frame_body"))
    assert mandatory <= _literal_dict_keys(_top_level_function("_v5_fatal_frame"))


def test_v4_fixture_and_historical_attestation_are_label_specific() -> None:
    assert len(V4_ENTRIES_FIXTURE) == 11
    assert sum(row["kind"] == "directory" for row in V4_ENTRIES_FIXTURE) == 8
    assert sum(row["kind"] == "file" for row in V4_ENTRIES_FIXTURE) == 3
    assert tuple(row["row_id"] for row in HISTORICAL_ATTESTATIONS_FIXTURE) == (
        "v4_executor",
        "v4_held_member",
    )
    attest = _top_level_function("_v4_receipts_attest_historical_identity")
    assert [arg.arg for arg in attest.args.args] == ["row", "entries", "attestation"]
    assert len(_calls(attest, "_json_pointer_get")) == 1
    assert not _calls(attest, "_v4_receipts_attest_historical_identity")
    validate = _top_level_function("_validate_v4_manifest")
    assert {"historical_attestations", "snapshot_bytes", "snapshot_sha256"} <= _literal_dict_keys(validate)


def test_external_ledger_uses_exact_v6_labels() -> None:
    node = _top_level_function("_validate_external_identity_ledger")
    constants = {
        child.value
        for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    }
    assert set(LEDGER_ROWS_FIXTURE) <= constants


def test_executor_and_contract_source_parse_without_import() -> None:
    executor_tree = _tree()
    compile(executor_tree, str(EXECUTOR), "exec", dont_inherit=True, optimize=0)
    this_source = Path(__file__).read_text(encoding="utf-8")
    this_tree = ast.parse(this_source, filename=__file__)
    compile(this_tree, __file__, "exec", dont_inherit=True, optimize=0)
