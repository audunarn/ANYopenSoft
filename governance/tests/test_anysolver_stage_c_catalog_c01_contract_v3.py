"""AST-only contract gate for the ANYsolver Stage-C catalog-aware V7 executor.

This module never imports or executes the executor. Every assertion is derived
from frozen source or packet syntax, so the later focused gate cannot invoke
WinTrust, WSL, network, or evidence-root behavior.
"""

from __future__ import annotations

import ast
from pathlib import Path


GOVERNANCE = Path(r"C:\Github\ANYopenSoft\governance")
EXECUTOR = GOVERNANCE / "tools" / "anysolver_no_numba_residual_stage_c_host_executor_v7.py"
PACKET = GOVERNANCE / "plans" / "ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V7.md"
AMENDMENT_SHA256 = "90D911524C5158B8994810F6A906B4600D2F333CA38CDD1A764405B80A76BFFA"

MANIFEST_FIELDS = frozenset(
    {
        "schema",
        "producer_label",
        "producer_plan_path",
        "producer_plan_sha256",
        "created_utc",
        "immutable_root",
        "entries",
        "entries_sha256",
        "entry_count",
        "directory_count",
        "file_count",
        "partials",
        "identity_rows",
    }
)
MANIFEST_ENTRY_FIELDS = frozenset(
    {
        "relative_path",
        "kind",
        "attributes",
        "is_reparse",
        "is_link",
        "bytes",
        "sha256",
    }
)
LEDGER_FIELDS = frozenset(
    {"schema", "ledger_path", "created_utc", "acceptance_scope", "identity_rows"}
)
IDENTITY_ROW_FIELDS = frozenset({"row_id", "path", "bytes", "sha256"})
FATAL_COMMON_FIELDS = frozenset(
    {
        "schema",
        "event",
        "created_utc",
        "truncated",
        "fatal_kind",
        "exit_code",
        "attempt_id",
        "run_id",
        "attempted_consumer_id",
        "promoted_receipt",
        "prior_global_head",
        "durable_head",
        "durable_final_exists",
        "registered_in_global_chain",
        "primary_error",
        "secondary_errors",
        "containment_outcome",
        "job_identity",
        "pid",
        "process_creation_identity",
        "source_artifact",
        "ordinary_prejob_failure",
        "run_consumer_manifest",
        "global_receipt_chain",
        "c01_pending_raw_events",
        "campaign_wsl_hold_release_outcome",
        "stage_c_failure_published",
        "success_report_published",
        "host_successor_publication_prohibited",
        "host_successor_promotion_allowed",
        "containment_repeated",
        "raw_partials_may_have_advanced",
        "evidence_status",
        "retry_allowed",
        "cleanup_allowed",
        "registration_loss",
        "containment_proof_complete",
    }
)


def _source() -> str:
    return EXECUTOR.read_text(encoding="utf-8")


def _tree() -> ast.Module:
    return ast.parse(_source(), filename=str(EXECUTOR))


def _function(name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in ast.walk(_tree())
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    assert len(matches) == 1, (name, len(matches))
    return matches[0]


def _method(class_name: str, method_name: str) -> ast.FunctionDef:
    classes = [
        node
        for node in _tree().body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    ]
    assert len(classes) == 1
    matches = [
        node
        for node in classes[0].body
        if isinstance(node, ast.FunctionDef) and node.name == method_name
    ]
    assert len(matches) == 1
    return matches[0]


def _segment(node: ast.AST) -> str:
    value = ast.get_source_segment(_source(), node)
    assert value is not None
    return value


def _called_names(node: ast.AST) -> list[str]:
    names: list[str] = []
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if isinstance(child.func, ast.Name):
            names.append(child.func.id)
        elif isinstance(child.func, ast.Attribute):
            names.append(child.func.attr)
    return names


def _string_constants(node: ast.AST) -> set[str]:
    return {
        child.value
        for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    }


def _return_dict(function_name: str) -> ast.Dict:
    function = _function(function_name)
    dictionaries = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    assert dictionaries, function_name
    return dictionaries[-1].value


def _literal_dict_keys(node: ast.Dict) -> set[str]:
    keys: set[str] = set()
    for key in node.keys:
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            keys.add(key.value)
    return keys


def _constant_string_assignment(name: str) -> str:
    values: list[str] = []
    for node in _tree().body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or target.id != name:
            continue
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            values.append(node.value.value)
    assert len(values) == 1, (name, values)
    return values[0]


def _replace_once(source: str, old: str, new: str) -> str:
    assert source.count(old) == 1, old
    return source.replace(old, new, 1)


def _node_segment(source: str, name: str, class_name: str | None = None) -> str:
    tree = ast.parse(source)
    if class_name is None:
        matches = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and node.name == name
        ]
    else:
        matches = []
        for node in tree.body:
            if not isinstance(node, ast.ClassDef) or node.name != class_name:
                continue
            matches.extend(
                child
                for child in node.body
                if isinstance(child, ast.FunctionDef) and child.name == name
            )
    assert len(matches) == 1, (class_name, name, len(matches))
    segment = ast.get_source_segment(source, matches[0])
    assert segment is not None
    return segment


def _assignment_from_source(source: str, name: str) -> str | None:
    values: list[str] = []
    for node in ast.parse(source).body:
        target: ast.expr | None = None
        value: ast.expr | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target, value = node.targets[0], node.value
        elif isinstance(node, ast.AnnAssign):
            target, value = node.target, node.value
        if (
            isinstance(target, ast.Name)
            and target.id == name
            and isinstance(value, ast.Constant)
            and isinstance(value.value, str)
        ):
            values.append(value.value)
    return values[0] if len(values) == 1 else None


def _literal_string_collections(source: str) -> tuple[frozenset[str], ...]:
    collections: list[frozenset[str]] = []
    for node in ast.walk(ast.parse(source)):
        values: list[str]
        if isinstance(node, ast.Dict):
            if not node.keys or any(
                not isinstance(key, ast.Constant) or not isinstance(key.value, str)
                for key in node.keys
            ):
                continue
            values = [key.value for key in node.keys]
        elif isinstance(node, (ast.List, ast.Set, ast.Tuple)):
            if not node.elts or any(
                not isinstance(item, ast.Constant) or not isinstance(item.value, str)
                for item in node.elts
            ):
                continue
            values = [item.value for item in node.elts]
        else:
            continue
        collections.append(frozenset(values))
    return tuple(collections)


def _literal_collection_member(
    source: str, expected: frozenset[str], member: str
) -> ast.Constant:
    matches: list[ast.Constant] = []
    for node in ast.walk(ast.parse(source)):
        items: list[ast.AST]
        if isinstance(node, ast.Dict):
            items = [key for key in node.keys if key is not None]
        elif isinstance(node, (ast.List, ast.Set, ast.Tuple)):
            items = list(node.elts)
        else:
            continue
        if not items or any(
            not isinstance(item, ast.Constant) or not isinstance(item.value, str)
            for item in items
        ):
            continue
        values = frozenset(item.value for item in items)
        if values != expected:
            continue
        matches.extend(
            item
            for item in items
            if isinstance(item, ast.Constant) and item.value == member
        )
    assert len(matches) == 1, (member, len(matches))
    return matches[0]


def _replace_ast_node(source: str, node: ast.AST, replacement: str) -> str:
    assert hasattr(node, "lineno") and hasattr(node, "end_lineno")
    lines = source.splitlines(keepends=True)
    offsets: list[int] = []
    offset = 0
    for line in lines:
        offsets.append(offset)
        offset += len(line)
    start = offsets[node.lineno - 1] + node.col_offset
    end = offsets[node.end_lineno - 1] + node.end_col_offset
    return source[:start] + replacement + source[end:]


def _candidate_loop(source: str) -> ast.For:
    function_source = _node_segment(source, "_v5_catalog_authenticode_identity")
    function = ast.parse(function_source).body[0]
    assert isinstance(function, ast.FunctionDef)
    matches: list[ast.For] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.For) or not isinstance(node.iter, ast.Call):
            continue
        if not isinstance(node.iter.func, ast.Name) or node.iter.func.id != "enumerate":
            continue
        if not node.iter.args or not isinstance(node.iter.args[0], ast.Name):
            continue
        if node.iter.args[0].id == "candidates":
            matches.append(node)
    assert len(matches) == 1
    return matches[0]


def _assigned_dict_keys(source: str, function_name: str, target_name: str) -> set[str]:
    function_source = _node_segment(source, function_name)
    function = ast.parse(function_source).body[0]
    assert isinstance(function, ast.FunctionDef)
    matches: list[ast.Dict] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id == target_name and isinstance(
            node.value, ast.Dict
        ):
            matches.append(node.value)
    assert len(matches) == 1, (function_name, target_name, len(matches))
    return _literal_dict_keys(matches[0])


def _structural_contract_errors(source: str) -> set[str]:
    errors: set[str] = set()
    try:
        ast.parse(source)
    except SyntaxError:
        return {"syntax"}

    for name in ("SCHEMA_V4_MANIFEST", "SCHEMA_IDENTITY_LEDGER"):
        value = _assignment_from_source(source, name)
        if value is None or not value.endswith("/1") or value.endswith("/2"):
            errors.add("manifest_schema")
    if "9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D" not in source:
        errors.add("historical_pointer")

    collections = set(_literal_string_collections(source))
    for label, expected in (
        ("manifest", MANIFEST_FIELDS),
        ("manifest_entry", MANIFEST_ENTRY_FIELDS),
        ("ledger", LEDGER_FIELDS),
        ("identity_row", IDENTITY_ROW_FIELDS),
    ):
        if expected not in collections:
            errors.add(f"registered_{label}")
    pointer = _node_segment(source, "_v4_receipts_attest_historical_identity")
    pointer_contract = (
        'expected_index = {"v4_executor": 1, "v4_held_member": 5}',
        'pointer = "/executor"',
        'pointer = "/campaign_held_wsl_identity"',
        'for relative in ("campaign_intent.json", "stage_c_failure.json"):',
        "if selected_rows[0] != selected_rows[1]:",
    )
    if any(token not in pointer for token in pointer_contract):
        errors.add("historical_pointer_contract")
    for literal in (
        "E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126",
        "143_022",
        "278_528",
    ):
        if literal not in source:
            errors.add("historical_pointer_identity")

    emit = _node_segment(source, "_v5_c01_emit")
    atomic = emit.find("_atomic_json(final_path, envelope)")
    reopened = emit.find("chain.nodes[-1]")
    cleared = emit.find('del context["pending_raw_events"]')
    if min(atomic, reopened, cleared) < 0 or not atomic < reopened < cleared:
        errors.add("raw_buffer_order")

    candidate = _node_segment(source, "_v7_close_and_publish_catalog_candidate")
    close_truth = candidate.find(
        'candidate_event["handle_closed"] = close_proof["succeeded"] is True'
    )
    publication = candidate.find('candidate_event["publication_attempted"] = True')
    if close_truth < 0 or publication < 0 or close_truth >= publication:
        errors.add("candidate_publication")

    terminal = _node_segment(
        source, "mark_top_level_publication", "_GlobalReceiptChain"
    )
    if "raise _ContainmentProofLost(" not in terminal:
        errors.add("terminal_proof_loss")

    finalizer = _node_segment(source, "_v5_finalize_run_consumers")
    if "exact_failure_prefixes = [[], internal_failure[:1], internal_failure]" not in finalizer:
        errors.add("consumer_lane")
    exact_lane_tokens = (
        'outer_ids != ["result.json", "post_snapshot.json"]',
        'outer_ids not in (',
        '["result.json"],',
        '["result.json", "post_snapshot.json"],',
        'f"run:{context[\'run_id\']}:outer-result"',
        'f"run:{context[\'run_id\']}:post-check-snapshot"',
        'f"run:{context[\'run_id\']}:campaign-final-snapshot"',
        'f"run:{context[\'run_id\']}:top-level-failure-published"',
        'f"run:{context[\'run_id\']}:top-level-success-published"',
        "observed not in allowed",
        "chain.mark_contained_proof_consumed",
        "chain.freeze_contained_consumer_lane",
    )
    if any(token not in finalizer for token in exact_lane_tokens):
        errors.add("consumer_lane_matrix")

    candidate_auth = _node_segment(source, "_v5_catalog_authenticode_identity")
    candidate_loop = _candidate_loop(source)
    if any(isinstance(node, (ast.Break, ast.Return)) for node in ast.walk(candidate_loop)):
        errors.add("candidate_sequence")
    if sum(isinstance(node, ast.Continue) for node in ast.walk(candidate_loop)) < 4:
        errors.add("candidate_sequence")
    for token in (
        "candidate_operational_errors.append",
        "accepted.append",
        "if candidate_operational_errors:",
        "if not accepted:",
    ):
        if token not in candidate_auth:
            errors.add("candidate_sequence")

    catalog_paths = _node_segment(source, "_v5_catalog_paths")
    row = catalog_paths.find("calls.append(call)")
    info_failure = catalog_paths.find("if not info_ok:")
    empty_path = catalog_paths.find("if not catalog_path:")
    if min(row, info_failure, empty_path) < 0 or not row < info_failure < empty_path:
        errors.add("catalog_returned_context_row")

    authenticode = _node_segment(source, "_authenticode_identity")
    zero_start = authenticode.find('if embedded["status"] == 0:')
    fallback_start = authenticode.find(
        'if embedded["status"] != _V5_TRUST_E_NOSIGNATURE:'
    )
    if zero_start < 0 or fallback_start <= zero_start:
        errors.add("embedded_status_zero")
    else:
        status_zero = authenticode[zero_start:fallback_start]
        if (
            "classified_non_success" in status_zero
            or 'setattr(exc, "c01_clean_typed_rejection", False)' not in status_zero
            or '"outcome": "failure"' not in status_zero
        ):
            errors.add("embedded_status_zero")

    registration = _node_segment(source, "__init__", "_ReceiptRegistrationLost")
    for field in (
        "promoted_receipt",
        "prior_receipt",
        "durable_head",
        "run_id",
        "attempted_consumer_id",
        "attempt_id",
    ):
        if f"self.{field}" not in registration:
            errors.add("registration_loss_binding")
    tree = ast.parse(source)
    registration_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "_ReceiptRegistrationLost"
    ]
    if not registration_calls:
        errors.add("registration_loss_binding")
    for call in registration_calls:
        keywords = {keyword.arg for keyword in call.keywords}
        if "attempted_consumer_id" not in keywords or "run_id" not in keywords:
            errors.add("registration_loss_binding")

    fatal = _node_segment(source, "_v7_fatal_payload")
    fatal_keys = _assigned_dict_keys(source, "_v7_fatal_payload", "payload")
    if FATAL_COMMON_FIELDS - fatal_keys or '"prior_global_head": prior' not in fatal:
        errors.add("fatal_full")
    for token in (
        '"exit_code": 86 if registration_loss else 87',
        '"registration_loss": registration_loss',
        '"containment_proof_complete": registration_loss',
        '"evidence_status": "evidence_limited"',
        '"retry_allowed": False',
        '"cleanup_allowed": False',
    ):
        if token not in fatal:
            errors.add("fatal_full")
    reduced = _node_segment(source, "_v7_truncated_fatal_payload")
    omitted_tuple = reduced.split("for key in (", 1)[1].split("):", 1)[0]
    if (
        '"source_artifact"' in omitted_tuple
        or "reduced = dict(full)" not in reduced
        or 'reduced["full_frame_bytes"]' not in reduced
        or 'reduced["full_frame_sha256"]' not in reduced
        or 'reduced["omitted_fields"]' not in reduced
        or "del reduced[" in reduced
        or "reduced.pop(" in reduced
    ):
        errors.add("fatal_reduced")
    framing = _node_segment(source, "_v5_fatal_frame")
    if (
        'emergency["primary_error"] =' in framing
        or "fallback = dict(reduced_payload)" not in framing
        or "emergency = _v7_fatal_payload" not in framing
        or "emergency = _v7_truncated_fatal_payload" not in framing
        or framing.count("ensure_ascii=True") < 2
        or '.encode("ascii")' not in framing
        or '.encode("ascii", "backslashreplace")' not in framing
    ):
        errors.add("fatal_ascii")
    return errors


def test_packet_binds_v7_authority_and_static_only_boundary() -> None:
    packet = PACKET.read_text(encoding="utf-8")
    assert AMENDMENT_SHA256 in packet
    assert str(EXECUTOR) in packet
    assert str(Path(__file__)) in packet
    assert "V7" in packet


def test_containment_outcome_is_returned_and_consumed_by_fatal_payload() -> None:
    outcome = _function("_v7_containment_outcome")
    returns = [node for node in ast.walk(outcome) if isinstance(node, ast.Return)]
    assert returns
    assert isinstance(returns[-1].value, ast.Name)
    assert returns[-1].value.id == "payload"

    fatal = _function("_v7_fatal_payload")
    fatal_source = _segment(fatal)
    assert "containment = _v7_containment_outcome(exc)" in fatal_source
    mandatory = {
        "registration_loss",
        "containment_proof_complete",
        "containment_outcome",
        "job_identity",
        "pid",
        "process_creation_identity",
        "attempted_consumer_id",
        "promoted_receipt",
        "prior_global_head",
        "durable_head",
        "durable_final_exists",
        "registered_in_global_chain",
        "stage_c_failure_published",
        "success_report_published",
        "host_successor_publication_prohibited",
        "host_successor_promotion_allowed",
        "containment_repeated",
        "retry_allowed",
        "cleanup_allowed",
    }
    assert mandatory <= _string_constants(fatal)


def test_reopened_top_level_terminal_uses_containment_proof_loss() -> None:
    method = _method("_GlobalReceiptChain", "mark_top_level_publication")
    source = _segment(method)
    assert "terminal_reopened = False" in source
    assert "terminal_reopened = True" in source
    assert "if terminal_reopened:" in source
    proof_pos = source.index("raise _ContainmentProofLost(")
    registration_pos = source.index("lost = _ReceiptRegistrationLost(")
    assert proof_pos < registration_pos
    assert "top-level consumer does not complete the frozen lane" in source
    proof_method = _method("_GlobalReceiptChain", "require_contained_terminal_proof")
    assert "contained terminal proof" in _segment(proof_method)


def test_c01_has_one_authoritative_success_receipt_and_no_duplicate_promotion() -> None:
    emit = _segment(_function("_v5_c01_emit"))
    wrapper = _segment(_function("_c01_held_identity_with_receipts"))
    main_impl = _function("_main_impl")
    main_source = _segment(main_impl)

    assert '"trust_success": "result.json"' in emit
    assert "trust_success.json" not in _source()
    assert wrapper.count('"trust_success"') == 1
    assert '"held_identity": observation' in wrapper
    assert "C01 authoritative result receipt is absent" in main_source

    duplicate_promotions: list[str] = []
    for node in ast.walk(main_impl):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "_atomic_json":
            continue
        rendered = ast.unparse(node)
        if '"C01"' in rendered and '"result.json"' in rendered:
            duplicate_promotions.append(rendered)
    assert duplicate_promotions == []


def test_embedded_fallback_and_catalog_failures_are_structurally_fail_closed() -> None:
    authenticode = _segment(_function("_authenticode_identity"))
    assert "embedded[\"status\"] == _V5_TRUST_E_NOSIGNATURE" in authenticode
    assert "embedded[\"status\"] != _V5_TRUST_E_NOSIGNATURE" in authenticode
    assert 'setattr(exc, "c01_clean_typed_rejection", False)' in authenticode
    assert 'rejection.c01_clean_typed_rejection = False' in authenticode
    assert '"outcome": "failure"' in authenticode

    materialize = _segment(_function("_v5_materialize_catalog_candidates"))
    assert "rollback_errors" in materialize
    assert "catalog_candidate_materialization_rollback_close" in materialize
    assert "except BaseException:\n                pass" not in materialize

    catalog = _segment(_function("_v5_catalog_authenticode_identity"))
    intent = catalog.index('"catalog_candidate_intent"')
    identity_probe = catalog.index("identity_before = _identity_from_handle")
    assert intent < identity_probe
    assert "candidate_intent_ordinals" in catalog
    assert "catalog_materialization_cleanup" in catalog
    assert "CatalogCandidateNotEvaluated" in catalog

    hash_source = _segment(_function("_v5_catalog_hash"))
    assert hash_source.count('"catalog_hash_evidence"') >= 3
    assert "catalog_hash_restore_error" in hash_source
    assert "catalog_hash_position_error" in hash_source


def test_manifest_and_historical_pointer_contract_is_deterministic() -> None:
    source = _source()
    constants = _string_constants(_tree())
    collections = set(_literal_string_collections(source))
    manifest_schema = _constant_string_assignment("SCHEMA_V4_MANIFEST")
    ledger_schema = _constant_string_assignment("SCHEMA_IDENTITY_LEDGER")
    assert manifest_schema.endswith("/1") and not manifest_schema.endswith("/2")
    assert ledger_schema.endswith("/1") and not ledger_schema.endswith("/2")
    assert MANIFEST_FIELDS in collections
    assert MANIFEST_ENTRY_FIELDS in collections
    assert LEDGER_FIELDS in collections
    assert IDENTITY_ROW_FIELDS in collections
    assert "campaign_intent.json" in constants
    assert "stage_c_failure.json" in constants
    assert "v4_executor" in constants
    assert "v4_held_member" in constants
    assert "9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D" in source
    assert "E27CBFCBD61C44796E2CFDD031663245BDA8D6E4A43C1451B1FC505333908126" in source
    assert "143_022" in source
    assert "278_528" in source
    pointer_functions = [
        node
        for node in ast.walk(_tree())
        if isinstance(node, ast.FunctionDef)
        and {"campaign_intent.json", "stage_c_failure.json"}
        <= _string_constants(node)
    ]
    assert pointer_functions
    pointer_checker = "\n".join(_segment(node) for node in pointer_functions)
    assert 'expected_index = {"v4_executor": 1, "v4_held_member": 5}' in pointer_checker
    assert 'pointer = "/executor"' in pointer_checker
    assert 'pointer = "/campaign_held_wsl_identity"' in pointer_checker
    assert 'for relative in ("campaign_intent.json", "stage_c_failure.json"):' in pointer_checker
    assert "if selected_rows[0] != selected_rows[1]:" in pointer_checker


def test_raw_event_buffer_advances_only_after_reopened_global_node() -> None:
    emit = _segment(_function("_v5_c01_emit"))
    wrapper = _segment(_function("_c01_held_identity_with_receipts"))
    atomic_pos = emit.index("_atomic_json(final_path, envelope)")
    reopen_pos = emit.index("chain.nodes[-1]")
    clear_pos = emit.index('del context["pending_raw_events"]')
    assert atomic_pos < reopen_pos < clear_pos
    assert 'fatal.c01_pending_raw_events = raw_events' in emit
    assert 'setattr(exc, "c01_pending_raw_events", raw_events)' in emit
    assert "catalog_materialization_cleanup" in emit
    assert "catalog_context_release" in emit
    assert "pending_from_failure" in wrapper
    assert 'context["pending_raw_events"][:] = pending_from_failure' in wrapper


def test_candidate_attempts_are_ordered_and_publication_is_one_shot() -> None:
    helper = _segment(_function("_v7_close_and_publish_catalog_candidate"))
    immediate_close = _segment(_function("_v7_materialization_close_once"))
    catalog = _segment(_function("_v5_catalog_authenticode_identity"))
    materialize = _segment(_function("_v5_materialize_catalog_candidates"))

    assert helper.index(
        'candidate_event["handle_closed"] = close_proof["succeeded"] is True'
    ) < helper.index(
        'candidate_event["publication_attempted"] = True'
    )
    assert helper.count('_v5_record_c01_event(events, "catalog_candidate_result"') == 1
    assert "publication was already attempted" in helper
    assert '"retained_handle_after_failure"' in helper
    assert '"retained_handle_after_failure"' in immediate_close
    assert 'proof["succeeded"] = True' in immediate_close
    assert 'candidate_event.get("publication_attempted") is True' in catalog
    assert "candidate_operational_errors.append" in catalog
    assert 'candidate_event["outcome"] = "classified_non_success"' in catalog
    assert 'candidate_event["catalog_signer_policy_rejection"]' in catalog
    assert 'candidate_event["catalog_provider_error"]' in catalog
    assert "catalog_acquire_proof" in catalog
    assert "catalog_context_acquire" in catalog
    assert "catalog_enumeration_release_error" in catalog
    assert "enumerated_contexts" in catalog
    assert "registration_loss_cleanup" in catalog
    assert "c01-raw:catalog:registration-loss-cleanup" in catalog
    assert "continue" in catalog
    assert "one or more catalog candidates failed operational validation" in catalog
    assert "catalog_candidate_materialization_rollback_close" in materialize
    assert "catalog_materialization_close_proofs" in materialize
    assert "_v5_close_held_file(" not in materialize
    assert "CATALOG_IDENTITY_CONFLICT" in materialize
    assert "candidates.sort" in materialize

    candidate_loop = _candidate_loop(_source())
    assert not any(
        isinstance(node, (ast.Break, ast.Return))
        for node in ast.walk(candidate_loop)
    )
    assert sum(isinstance(node, ast.Continue) for node in ast.walk(candidate_loop)) >= 4
    assert candidate_loop.lineno < candidate_loop.end_lineno

    policy = _segment(_function("_v5_validate_microsoft_provider"))
    assert "_CatalogTrustDecisionRejected" in policy
    assert "WinTrust provider is absent" in policy
    assert "raise StageCError" in policy


def test_reopened_nodes_and_lanes_fail_closed_without_state_commit() -> None:
    register = _segment(_method("_GlobalReceiptChain", "register"))
    terminal = _segment(_method("_GlobalReceiptChain", "mark_top_level_publication"))
    finalizer = _segment(_function("_v5_finalize_run_consumers"))

    assert "_v5_receipt_from_final" in register
    assert register.index("_v5_receipt_from_final") < register.index("self.head =")
    assert terminal.index("_v5_receipt_from_final") < terminal.index("self._runs =")
    assert "raise _ContainmentProofLost(" in terminal
    assert "exact_failure_prefixes = [[], internal_failure[:1], internal_failure]" in finalizer
    assert "failure_final_count" not in finalizer
    for token in (
        'outer_ids != ["result.json", "post_snapshot.json"]',
        'outer_ids not in (',
        '["result.json"],',
        '["result.json", "post_snapshot.json"],',
        'f"run:{context[\'run_id\']}:outer-result"',
        'f"run:{context[\'run_id\']}:post-check-snapshot"',
        'f"run:{context[\'run_id\']}:campaign-final-snapshot"',
        'f"run:{context[\'run_id\']}:top-level-failure-published"',
        'f"run:{context[\'run_id\']}:top-level-success-published"',
        "observed not in allowed",
    ):
        assert token in finalizer


def test_full_reduced_and_ascii_fatal_forms_preserve_mandatory_truth() -> None:
    fatal_keys = _assigned_dict_keys(_source(), "_v7_fatal_payload", "payload")
    assert FATAL_COMMON_FIELDS <= fatal_keys

    fatal = _segment(_function("_v7_fatal_payload"))
    assert '"exit_code": 86 if registration_loss else 87' in fatal
    assert '"registration_loss": registration_loss' in fatal
    assert '"containment_proof_complete": registration_loss' in fatal
    assert '"evidence_status": "evidence_limited"' in fatal

    reduced = _segment(_function("_v7_truncated_fatal_payload"))
    assert '"source_artifact"' not in reduced.split("for key in (", 1)[1].split("):", 1)[0]
    assert 'reduced["full_frame_bytes"]' in reduced
    assert 'reduced["full_frame_sha256"]' in reduced
    assert 'reduced["omitted_fields"]' in reduced
    assert "reduced = dict(full)" in reduced
    assert "del reduced[" not in reduced
    assert "reduced.pop(" not in reduced

    framing = _segment(_function("_v5_fatal_frame"))
    assert "ensure_ascii=True" in framing
    assert '.encode("ascii")' in framing
    assert 'emergency["primary_error"] =' not in framing
    assert 'emergency["secondary_errors"] =' in framing
    assert "prior_secondary_errors" in framing
    assert "fallback = dict(reduced_payload)" in framing
    assert "emergency = _v7_fatal_payload" in framing
    assert "emergency = _v7_truncated_fatal_payload" in framing
    assert framing.count("ensure_ascii=True") >= 2


def test_registration_and_containment_loss_have_distinct_structural_paths() -> None:
    fatal = _segment(_function("_v7_fatal_payload"))
    mark = _segment(_method("_GlobalReceiptChain", "mark_top_level_publication"))
    campaign = _segment(
        _method("_GlobalReceiptChain", "mark_campaign_top_level_publication")
    )

    assert '"exit_code": 86 if registration_loss else 87' in fatal
    assert '"registration_loss": registration_loss' in fatal
    assert '"containment_proof_complete": registration_loss' in fatal
    assert "if prior is None and not registration_loss:" in fatal
    assert mark.index("terminal_reopened = True") < mark.index(
        "raise _ContainmentProofLost("
    )
    assert campaign.index("_v5_receipt_from_final") < campaign.index(
        "campaign terminal consumer ID is not exact"
    )

    registration = _segment(_method("_ReceiptRegistrationLost", "__init__"))
    for field in (
        "promoted_receipt",
        "prior_receipt",
        "durable_head",
        "run_id",
        "attempted_consumer_id",
        "attempt_id",
    ):
        assert f"self.{field}" in registration
    registration_calls = [
        node
        for node in ast.walk(_tree())
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "_ReceiptRegistrationLost"
    ]
    assert registration_calls
    for call in registration_calls:
        keywords = {keyword.arg for keyword in call.keywords}
        assert {"run_id", "attempted_consumer_id"} <= keywords


def test_deterministic_negative_mutations_are_rejected_structurally() -> None:
    source = _source()
    assert _structural_contract_errors(source) == set()

    manifest_schema = _constant_string_assignment("SCHEMA_V4_MANIFEST")
    manifest_mutation = _replace_once(
        source,
        f'"{manifest_schema}"',
        f'"{manifest_schema[:-1]}2"',
    )
    assert "manifest_schema" in _structural_contract_errors(manifest_mutation)

    historical_sha = "9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D"
    pointer_mutation = _replace_once(
        source, historical_sha, "0" + historical_sha[1:]
    )
    assert "historical_pointer" in _structural_contract_errors(pointer_mutation)

    for expected, member, error in (
        (MANIFEST_FIELDS, "identity_rows", "registered_manifest"),
        (MANIFEST_ENTRY_FIELDS, "is_link", "registered_manifest_entry"),
        (LEDGER_FIELDS, "acceptance_scope", "registered_ledger"),
        (IDENTITY_ROW_FIELDS, "row_id", "registered_identity_row"),
    ):
        member_node = _literal_collection_member(source, expected, member)
        collection_mutation = _replace_ast_node(
            source, member_node, repr("invalid_" + member)
        )
        assert error in _structural_contract_errors(collection_mutation)

    emit = _segment(_function("_v5_c01_emit"))
    invalid_buffer_order = _replace_once(
        emit,
        "_atomic_json(final_path, envelope)",
        'del context["pending_raw_events"][: len(raw_prefix)]',
    )
    buffer_mutation = _replace_once(source, emit, invalid_buffer_order)
    assert "raw_buffer_order" in _structural_contract_errors(buffer_mutation)

    candidate = _segment(_function("_v7_close_and_publish_catalog_candidate"))
    invalid_candidate = _replace_once(
        candidate,
        'candidate_event["handle_closed"] = close_proof["succeeded"] is True',
        'candidate_event["handle_closed"] = False',
    )
    candidate_mutation = _replace_once(source, candidate, invalid_candidate)
    assert "candidate_publication" in _structural_contract_errors(
        candidate_mutation
    )

    catalog_paths = _segment(_function("_v5_catalog_paths"))
    invalid_context_row = _replace_once(
        catalog_paths, "calls.append(call)", "discarded_call = call"
    )
    context_row_mutation = _replace_once(source, catalog_paths, invalid_context_row)
    assert "catalog_returned_context_row" in _structural_contract_errors(
        context_row_mutation
    )

    authenticode = _segment(_function("_authenticode_identity"))
    invalid_embedded = _replace_once(
        authenticode,
        'setattr(exc, "c01_clean_typed_rejection", False)',
        'setattr(exc, "c01_clean_typed_rejection", True)',
    )
    embedded_mutation = _replace_once(source, authenticode, invalid_embedded)
    assert "embedded_status_zero" in _structural_contract_errors(embedded_mutation)

    candidate_auth = _segment(_function("_v5_catalog_authenticode_identity"))
    candidate_loop = _candidate_loop(source)
    first_continue = next(
        node for node in ast.walk(candidate_loop) if isinstance(node, ast.Continue)
    )
    invalid_candidate_sequence = _replace_ast_node(
        candidate_auth, first_continue, "break"
    )
    candidate_sequence_mutation = _replace_once(
        source, candidate_auth, invalid_candidate_sequence
    )
    assert "candidate_sequence" in _structural_contract_errors(
        candidate_sequence_mutation
    )

    terminal = _segment(_method("_GlobalReceiptChain", "mark_top_level_publication"))
    invalid_terminal = _replace_once(
        terminal, "raise _ContainmentProofLost(", "raise _ReceiptRegistrationLost("
    )
    terminal_mutation = _replace_once(source, terminal, invalid_terminal)
    assert "terminal_proof_loss" in _structural_contract_errors(terminal_mutation)

    finalizer = _segment(_function("_v5_finalize_run_consumers"))
    invalid_lane = _replace_once(
        finalizer,
        "exact_failure_prefixes = [[], internal_failure[:1], internal_failure]",
        "exact_failure_prefixes = [[], completed_success, internal_failure]",
    )
    lane_mutation = _replace_once(source, finalizer, invalid_lane)
    assert "consumer_lane" in _structural_contract_errors(lane_mutation)

    invalid_lane_matrix = _replace_once(
        finalizer,
        '            ["result.json", "post_snapshot.json"],',
        '            ["result.json", "wrong_snapshot.json"],',
    )
    lane_matrix_mutation = _replace_once(source, finalizer, invalid_lane_matrix)
    assert "consumer_lane_matrix" in _structural_contract_errors(
        lane_matrix_mutation
    )

    registration = _segment(_method("_ReceiptRegistrationLost", "__init__"))
    invalid_registration = _replace_once(
        registration,
        "self.attempted_consumer_id = attempted_consumer_id",
        "ignored_attempted_consumer_id = attempted_consumer_id",
    )
    registration_mutation = _replace_once(source, registration, invalid_registration)
    assert "registration_loss_binding" in _structural_contract_errors(
        registration_mutation
    )

    fatal_payload = _segment(_function("_v7_fatal_payload"))
    invalid_full = _replace_once(
        fatal_payload, '        "prior_global_head": prior,\n', ""
    )
    full_mutation = _replace_once(source, fatal_payload, invalid_full)
    assert "fatal_full" in _structural_contract_errors(full_mutation)

    reduced = _segment(_function("_v7_truncated_fatal_payload"))
    invalid_reduced = _replace_once(
        reduced,
        '        "secondary_errors",\n',
        '        "secondary_errors",\n        "source_artifact",\n',
    )
    reduced_mutation = _replace_once(source, reduced, invalid_reduced)
    assert "fatal_reduced" in _structural_contract_errors(reduced_mutation)

    framing = _segment(_function("_v5_fatal_frame"))
    invalid_emergency = _replace_once(
        framing,
        'emergency["secondary_errors"] = [',
        'emergency["primary_error"] = [',
    )
    emergency_mutation = _replace_once(source, framing, invalid_emergency)
    assert "fatal_ascii" in _structural_contract_errors(emergency_mutation)


def test_failure_final_lane_is_derived_only_from_registered_consumers() -> None:
    finalizer = _function("_v5_finalize_run_consumers")
    argument_names = [argument.arg for argument in finalizer.args.args]
    argument_names += [argument.arg for argument in finalizer.args.kwonlyargs]
    assert "failure_final_count" not in argument_names
    source = _segment(finalizer)
    assert "exact_failure_prefixes = [[], internal_failure[:1], internal_failure]" in source
    assert "observed not in exact_failure_prefixes" in source
    assert "publisher_final_count" not in source
    assert "failure_final_count=" not in _source()


def test_real_structural_negative_lanes_replace_synthetic_fixtures() -> None:
    tree = _tree()
    source = _source()
    assert "key_union" not in source
    assert "fabricated" not in source

    fatal_raises = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Raise)
        and isinstance(node.exc, ast.Call)
        and isinstance(node.exc.func, ast.Name)
        and node.exc.func.id in {"_ReceiptRegistrationLost", "_ContainmentProofLost"}
    ]
    assert fatal_raises
    assert {node.exc.func.id for node in fatal_raises} == {
        "_ReceiptRegistrationLost",
        "_ContainmentProofLost",
    }

    terminal_mark = _method("_GlobalReceiptChain", "mark_top_level_publication")
    assert {"_v5_receipt_from_final", "require_contained_run"} <= set(
        _called_names(terminal_mark)
    )

    c01_emit = _function("_v5_c01_emit")
    constants = _string_constants(c01_emit)
    assert "classified_non_success" in constants
    assert "typed_rejection" in constants
    assert "non_success" not in constants


def test_executor_is_parseable_without_importing_or_executing_it() -> None:
    tree = _tree()
    assert isinstance(tree, ast.Module)
    compile(tree, str(EXECUTOR), "exec")
