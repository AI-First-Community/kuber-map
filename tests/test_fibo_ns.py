import fibo_ns as ns


def test_cluster_of_fibo_domain():
    assert ns.cluster_of("https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/MortgageLoan") == "LOAN"
    assert ns.cluster_of("https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty") == "FND"


def test_cluster_of_commons_and_lcc():
    assert ns.cluster_of("https://www.omg.org/spec/Commons/PartiesAndSituations/Party") == "CMNS"
    assert ns.cluster_of("https://www.omg.org/spec/LCC/Countries/CountryRepresentation/Country") == "LCC"


def test_cluster_of_external_is_none():
    assert ns.cluster_of("http://www.w3.org/2004/02/skos/core#Concept") is None
    assert ns.cluster_of("") is None


def test_iri_to_path_is_module_aware_and_collision_free():
    # FND has two distinct TransactionEvent classes; a flat scheme would collide.
    a = ns.iri_to_path("https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent")
    b = ns.iri_to_path("https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent")
    assert a == "/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md"
    assert b == "/FND/TransactionsExt/REATransactions/TransactionEvent.md"
    assert a != b


def test_iri_to_path_commons():
    assert ns.iri_to_path("https://www.omg.org/spec/Commons/PartiesAndSituations/Party") \
        == "/CMNS/PartiesAndSituations/Party.md"


def test_iri_to_path_unmappable_is_none():
    assert ns.iri_to_path("http://example.org/Foo") is None


def test_normalize_edge_type_camel_and_spaced_and_isa():
    assert ns.normalize_edge_type("isCollateralizedBy") == "is-collateralized-by"
    assert ns.normalize_edge_type("is performed by") == "is-performed-by"
    assert ns.normalize_edge_type("has contractual element") == "has-contractual-element"
    assert ns.normalize_edge_type("is-a") == "is-a"
