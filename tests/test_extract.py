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


def test_maturity_taken_from_label_bearing_home_not_referencing_file():
    """Thing is defined (with a label) in the Release mini.rdf and merely referenced by the
    Provisional aref_provisional.rdf. Its maturity must be Release — the home file wins even
    though the Provisional file is processed first."""
    recs = _records()
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


def test_multilingual_label_prefers_en_us():
    """A class with en-US and en-GB labels must resolve to the en-US spelling, so the
    generated bundle is stable regardless of rdflib's iteration order."""
    recs = _records()
    assert recs["RegionalThing"]["title"] == "colorful thing"


def test_extraction_is_deterministic():
    """Running extraction twice must yield identical records (relation order and
    label/definition choice are all deterministic)."""
    g1, cs1, _ = extract.load_domains(FIXTURES, ["FND"])
    g2, cs2, _ = extract.load_domains(FIXTURES, ["FND"])
    assert extract.extract(g1, cs1) == extract.extract(g2, cs2)


def test_relations_sorted_is_a_first():
    """is-a edges precede typed edges; within a group, order is stable by (type, target)."""
    recs = _records()
    types = [e["type"] for e in recs["SpecialThing"]["relations"]]
    assert types == sorted(types, key=lambda t: (t != "is-a", t))


def test_multi_filler_restriction_keeps_named_target():
    """A restriction with both a named someValuesFrom and an anonymous union must still
    yield the NAMED target — never dropped because the store yielded the BNode first."""
    recs = _records()
    edges = {(e["type"], e["target_cluster"]) for e in recs["MultiFillerThing"]["relations"]}
    assert ("relates-to", "CMNS") in edges     # named Party filler, deterministically chosen
