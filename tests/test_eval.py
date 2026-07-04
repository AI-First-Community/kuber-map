import json
import os

import harness

ROOT = os.path.join(os.path.dirname(__file__), "..")
PACK = os.path.join(ROOT, "export", "loan-origination", "pack.json")
BENCH = os.path.join(ROOT, "eval", "benchmark.json")


def test_keyword_coverage_counts_multiword_keywords():
    ans = "a debt instrument where money or credit is repaid per the terms"
    cov = harness.keyword_coverage(ans, ["debt instrument", "money", "missing phrase"])
    assert cov == 2 / 3


def test_extract_citations_finds_fibo_iris_and_strips_trailing_dot():
    text = "see https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan."
    assert harness.extract_citations(text) == [
        "https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan"]


REAL_IRI = "https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan"


def test_score_answer_flags_invalid_citation_as_hallucination():
    q = {"id": "x", "expected_keywords": ["loan"], "grounds": [REAL_IRI]}
    # cites a FIBO-looking IRI that is NOT in the pack -> hallucination
    bad = harness.score_answer("a loan, see https://spec.edmcouncil.org/fibo/ontology/X/Fake",
                               q, {REAL_IRI})
    assert bad["hallucinated_citation"] is True
    assert bad["auditable"] is False


def test_score_answer_auditable_and_on_target():
    q = {"id": "x", "expected_keywords": ["loan"], "grounds": [REAL_IRI]}
    good = harness.score_answer(f"a loan; source: {REAL_IRI}", q, {REAL_IRI})
    assert good["auditable"] and good["cited_on_target"] and good["correct"]


def test_aggregate_ratios():
    rows = [{"correct": True, "coverage": 1.0, "auditable": True, "hallucinated_citation": False,
             "cited_on_target": True},
            {"correct": False, "coverage": 0.0, "auditable": False, "hallucinated_citation": True,
             "cited_on_target": False}]
    agg = harness.aggregate(rows)
    assert agg["accuracy"] == 0.5 and agg["auditable"] == 0.5 and agg["hallucination"] == 0.5


# ---- benchmark integrity (anti-hallucination guard on the gold set) ----

def test_benchmark_grounds_are_real_pack_iris():
    """Every question's `grounds` IRI must exist in the pack (concepts or bridge endpoints)."""
    pack = json.load(open(PACK))
    real = {c["iri"] for c in pack["concepts"]}
    for b in pack["bridges"]:
        real.add(b["source"])
        real.add(b["target"])
    bench = json.load(open(BENCH))["questions"]
    for q in bench:
        for iri in q["grounds"]:
            assert iri in real, f"{q['id']} grounds unknown IRI {iri}"


def test_benchmark_ids_unique_and_have_keywords():
    bench = json.load(open(BENCH))["questions"]
    ids = [q["id"] for q in bench]
    assert len(ids) == len(set(ids))
    assert all(q["expected_keywords"] and q["grounds"] for q in bench)
