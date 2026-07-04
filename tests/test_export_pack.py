import export_pack


def _recs():
    return {
        "https://ex/Loan": {"iri": "https://ex/Loan", "title": "loan", "cluster": "LOAN",
                            "maturity": "Release", "description": "a loan",
                            "relations": [{"type": "is-a", "target": "https://ex/Debt",
                                           "provenance": "fibo"}]},
        "https://ex/Debt": {"iri": "https://ex/Debt", "title": "debt", "cluster": "FBC",
                            "maturity": "Release", "description": "a debt", "relations": []},
        "https://ex/Empty": {"iri": "https://ex/Empty", "title": "empty thing", "cluster": "LOAN",
                             "maturity": "Provisional", "description": None, "relations": []},
    }


def test_concept_carries_iri_citation_and_resolves_relation_titles():
    core = [{"iri": "https://ex/Loan", "facet": "Instrument"}]
    concepts = export_pack.build_concepts(core, _recs(), {})
    c = concepts[0]
    assert c["citation"] == "https://ex/Loan"        # the IRI is the audit citation
    assert c["definition_provenance"] == "fibo"
    assert c["relations"][0]["target_title"] == "debt"   # target IRI resolved to a title


def test_curated_definition_only_fills_empty_fibo_def():
    core = [{"iri": "https://ex/Empty", "facet": "X"}, {"iri": "https://ex/Loan", "facet": "X"}]
    defs = {"https://ex/Empty": "our learner def", "https://ex/Loan": "SHOULD NOT WIN"}
    concepts = {c["iri"]: c for c in export_pack.build_concepts(core, _recs(), defs)}
    # empty FIBO def -> curated override applied
    assert concepts["https://ex/Empty"]["definition"] == "our learner def"
    assert concepts["https://ex/Empty"]["definition_provenance"] == "curated"
    # real FIBO def -> override refused, FIBO text kept
    assert concepts["https://ex/Loan"]["definition"] == "a loan"
    assert concepts["https://ex/Loan"]["definition_provenance"] == "fibo"


def test_bridges_are_curated_with_resolved_titles():
    bridges = [{"id": "b1", "edge": "reported-in", "kind": "gap",
                "source": "https://ex/Loan", "target": "https://ex/Debt",
                "rationale": "why", "citation": "cite"}]
    out = export_pack.build_bridges(bridges, _recs())
    assert out[0]["provenance"] == "curated"
    assert out[0]["source_title"] == "loan"
    assert out[0]["target_title"] == "debt"


def test_context_md_renders_citations_and_provenance():
    core = [{"iri": "https://ex/Loan", "facet": "Instrument"}]
    concepts = export_pack.build_concepts(core, _recs(), {})
    md = export_pack.render_context_md("UC", concepts, [])
    assert "https://ex/Loan" in md          # citation IRI present
    assert "provenance" in md
