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
