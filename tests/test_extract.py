import extract
from conftest import FIXTURES


def _records():
    g, class_source, files = extract.load_domains(FIXTURES, ["FND"])
    recs = extract.extract(g, class_source)
    return {r["id"]: r for r in recs}


def test_restriction_yields_typed_cross_cluster_edge():
    """The crux: a relation buried in an owl:Restriction blank node must be extracted as a
    typed edge, normalized, with its filler classified into the right (cross) cluster."""
    recs = _records()
    st = recs["SpecialThing"]
    edges = {(e["type"], e["target_cluster"]) for e in st["relations"]}
    assert ("is-a", "FND") in edges                 # named superclass
    assert ("relates-to", "CMNS") in edges          # restriction filler, cross-cluster, normalized


def test_maturity_propagated_from_ontology_header():
    recs = _records()
    assert recs["SpecialThing"]["maturity"] == "Release"
    assert recs["Thing"]["maturity"] == "Release"


def test_labels_and_definitions_extracted():
    recs = _records()
    assert recs["Thing"]["title"] == "thing"
    assert recs["Thing"]["description"] == "a thing"


def test_no_self_loops_and_provenance_is_fibo():
    recs = _records()
    for r in recs.values():
        for e in r["relations"]:
            assert e["target"] != r["iri"], "self-loop leaked"
            assert e["provenance"] == "fibo"
