# ANYfem Dirty UI/Test Read-Only Assessment

Date: 2026-08-13 (Europe/Oslo)

Plan:
`C:\Github\ANYopenSoft\governance\plans\ANYFEM_DIRTY_UI_READ_ONLY_ASSESSMENT_PLAN.md`

Plan SHA-256:
`4448A242A5F2DE1A7252A2738F88D7B15F3F11E731171D44ECAB914146330273`

Pinned ANYfem HEAD:
`7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`

## Exact focused result

The registered cache-free external-temp command completed in 5.4 seconds.
Pytest result: `2 passed, 2 failed in 1.94s`; exit code 1.

Passed:

- `tests/test_scene.py::test_beams_are_drawn_differently_from_plain_lines`
- `tests/test_overlap_and_generator_ui.py::test_each_generator_type_exposes_only_applicable_inputs`

Failed:

- `tests/test_scene.py::test_coplanar_diagonal_beam_is_connected_and_drawn_continuously`
- `tests/test_overlap_and_generator_ui.py::test_overlap_fragment_command_is_feature_backed_atomic_and_undoable`

## Slice classification

### Beam overlay slice: defer unchanged

The `draw_overlay` field/default and beam/plain distinction are internally
coherent, and the first focused scene test passes. The diagonal test fails its
structural-topology assertion: diagonal edge nodes are not a subset of shell or
coupled beam nodes, and the generated mesh has no coupling entries. The slice
does not satisfy its registered completion rule. No production or test byte is
accepted or modified by this assessment.

### Overlap/generator contract-test slice: defer unchanged

The generator-form contract passes. The overlap-fragmentation case fails before
materialization: the returned feature is `blocked`, has zero outputs, and reports
`input 'faces' cannot be resolved`; the test expected three outputs. The
contract-only module is therefore incomplete against the pinned default source
and remains untracked and unchanged.

## Preservation evidence

- Branch remained `main`.
- HEAD remained `7a41baca4bd4d1a5cb538ec6148c6ca51c79d1f2`.
- Porcelain status remained exactly the same four entries.
- External base temp was fresh, removed safely, and absent after the run.
- `PYTHONDONTWRITEBYTECODE=1` and pytest cache disablement prevented repository
  cache/bytecode output.
- No source, test, index, ref, or remote was modified.

Preserved SHA-256 values:

| Path | SHA-256 |
|---|---|
| `src/anyfem/ui/scene.py` | `9E636A2ADC8BDE28A73632694C9D91AAA12AA229E0CABF5D4F045E30845C97DB` |
| `src/anyfem/ui/viewport.py` | `6BCDA7DA5FF7E81AEB860311B6EB94BA476381390D9CBFC8EAFBE9517AE90A10` |
| `tests/test_scene.py` | `E6AD70C9E1D410EE6536B64D2404934BD47F5E2741635691CDC3243FD78A1C81` |
| `tests/test_overlap_and_generator_ui.py` | `BED351383B22585AF4F65ECEBAC8ADA02797293584B618CEF4DC157D074200E0` |

## Verdict

Both slices are classified as deferred, not release evidence. Their bytes are
preserved for the owning task. No commit or completion action is authorized by
this assessment.
