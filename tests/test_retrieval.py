import retrieval
from retrieval import Pack

PACK = {
    "use_case": "UC",
    "concepts": [
        {"iri": "https://ex/LTV", "title": "loan-to-value ratio", "facet": "Ratios",
         "cluster": "LOAN", "definition": "ratio of loan principal to appraised collateral value",
         "definition_provenance": "fibo", "citation": "https://ex/LTV"},
        {"iri": "https://ex/Borrower", "title": "borrower", "facet": "Parties",
         "cluster": "FBC", "definition": "a party that receives a loan",
         "definition_provenance": "fibo", "citation": "https://ex/Borrower"},
    ],
    "bridges": [{"id": "b1", "provenance": "curated"}],
}


def test_tokens_drops_stopwords_and_punctuation():
    assert retrieval.tokens("A loan-to-value ratio of the asset") == ["loan", "value", "ratio", "asset"]


def test_search_ranks_title_match_first_with_citation():
    hits = Pack(PACK).search("loan to value ratio", k=5)
    assert hits[0]["iri"] == "https://ex/LTV"
    assert hits[0]["citation"] == "https://ex/LTV"     # every hit is citable
    assert hits[0]["score"] > 0


def test_search_returns_empty_when_nothing_matches():
    assert Pack(PACK).search("cryptocurrency derivatives", k=5) == []


def test_search_is_deterministic():
    p = Pack(PACK)
    assert p.search("loan", k=5) == p.search("loan", k=5)


def test_get_returns_full_record_or_none():
    p = Pack(PACK)
    assert p.get("https://ex/Borrower")["title"] == "borrower"
    assert p.get("https://ex/missing") is None
