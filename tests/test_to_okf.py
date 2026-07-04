import json

import to_okf


def test_load_core_iris_collects_flagged_entries(tmp_path):
    """core: true entries with a real iri are collected; files without a `core` list
    (e.g. bridges.json) are ignored, not errored on."""
    good = tmp_path / "loan.json"
    good.write_text(json.dumps({"core": [
        {"iri": "https://ex/A", "core": True},
        {"iri": "https://ex/B", "core": True},
        {"iri": "https://ex/C", "core": False},   # flag off -> excluded
        {"core": True},                            # no iri -> excluded
    ]}))
    bridges = tmp_path / "bridges.json"
    bridges.write_text(json.dumps({"bridges": [{"id": "x"}]}))

    core = to_okf.load_core_iris([str(good), str(bridges)])
    assert core == {"https://ex/A", "https://ex/B"}


def test_load_core_iris_tolerates_missing_file():
    assert to_okf.load_core_iris(["/does/not/exist.json"]) == set()


def test_emit_stamps_core_flag():
    rec = {"iri": "https://ex/A", "title": "a", "description": None,
           "cluster": "LOAN", "maturity": "Release", "relations": []}
    assert "core: true" in to_okf.emit(rec, is_core=True)
    assert "core: true" not in to_okf.emit(rec, is_core=False)


def test_load_definitions_collects_overrides(tmp_path):
    f = tmp_path / "defs.json"
    f.write_text(json.dumps({"definitions": [
        {"iri": "https://ex/A", "definition": "our text"},
        {"iri": "https://ex/B"},                 # no definition -> excluded
        {"definition": "orphan"},                # no iri -> excluded
    ]}))
    assert to_okf.load_definitions([str(f)]) == {"https://ex/A": "our text"}


def test_emit_marks_curated_definition_provenance():
    rec = {"iri": "https://ex/A", "title": "a", "description": "our learner def",
           "cluster": "LOAN", "maturity": "Release", "relations": []}
    curated = to_okf.emit(rec, curated_def=True)
    assert "definition_provenance: curated" in curated
    # FIBO's resource IRI is always preserved, never rewritten as ours.
    assert "resource: https://ex/A" in curated
    assert "definition_provenance" not in to_okf.emit(rec, curated_def=False)
