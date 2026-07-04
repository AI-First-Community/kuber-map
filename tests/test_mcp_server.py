import json

import mcp_server
from retrieval import Pack

PACK = Pack({
    "use_case": "UC",
    "concepts": [{"iri": "https://ex/LTV", "title": "loan-to-value ratio", "facet": "Ratios",
                  "cluster": "LOAN", "definition": "ratio of loan to collateral value",
                  "definition_provenance": "fibo", "citation": "https://ex/LTV",
                  "relations": []}],
    "bridges": [{"id": "b1", "edge": "underlies", "provenance": "curated"}],
})


def _req(method, rid=1, **params):
    return {"jsonrpc": "2.0", "id": rid, "method": method, "params": params}


def test_initialize_reports_protocol_and_server():
    r = mcp_server.handle(_req("initialize"), PACK)
    assert r["result"]["protocolVersion"] == mcp_server.PROTOCOL_VERSION
    assert r["result"]["serverInfo"]["name"] == "bodhi-fibo-grounding"


def test_tools_list_exposes_three_tools():
    r = mcp_server.handle(_req("tools/list"), PACK)
    assert {t["name"] for t in r["result"]["tools"]} == {
        "search_concepts", "get_concept", "list_bridges"}


def test_tools_call_search_returns_citation():
    r = mcp_server.handle(
        _req("tools/call", name="search_concepts", arguments={"query": "loan value", "k": 3}), PACK)
    hits = json.loads(r["result"]["content"][0]["text"])
    assert hits[0]["citation"] == "https://ex/LTV"


def test_get_concept_missing_iri_is_error():
    r = mcp_server.handle(
        _req("tools/call", name="get_concept", arguments={"iri": "https://ex/none"}), PACK)
    assert r["result"]["isError"] is True


def test_notification_gets_no_response():
    assert mcp_server.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}, PACK) is None


def test_unknown_method_returns_error():
    r = mcp_server.handle(_req("does/not/exist"), PACK)
    assert r["error"]["code"] == -32601
