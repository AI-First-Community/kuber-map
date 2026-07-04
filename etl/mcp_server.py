#!/usr/bin/env python3
"""
MCP retrieval endpoint for a FIBO context pack (PLAN.md §6) — the tool an AI agent calls
to ground its answers.

A minimal Model Context Protocol server over stdio (newline-delimited JSON-RPC 2.0),
implemented in the standard library only (no SDK dependency), exposing three tools:

  search_concepts(query, k)  keyword-search the pack; each hit carries its FIBO citation IRI
  get_concept(iri)           full grounding record for a concept (with provenance-tagged edges)
  list_bridges()             the curated cross-domain bridges in the pack

Every result carries `citation` (a FIBO IRI) and `provenance` (fibo | curated) so the agent
can cite exactly which concept justified each claim and a regulator can trace it.

Usage:
    python etl/mcp_server.py --pack export/loan-origination/pack.json
"""
import argparse
import json
import sys

from retrieval import Pack

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "bodhi-fibo-grounding", "version": "0.1.0"}

TOOLS = [
    {
        "name": "search_concepts",
        "description": "Search the curated FIBO grounding pack for concepts relevant to a query. "
                       "Returns concepts each with a `citation` (FIBO IRI) to cite in answers.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "natural-language query"},
                "k": {"type": "integer", "description": "max results (default 5)"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_concept",
        "description": "Fetch the full grounding record for one FIBO concept by its IRI, "
                       "including its provenance-tagged relations.",
        "inputSchema": {
            "type": "object",
            "properties": {"iri": {"type": "string", "description": "the concept's FIBO IRI"}},
            "required": ["iri"],
        },
    },
    {
        "name": "list_bridges",
        "description": "List the curated cross-domain bridges in the pack (provenance: curated).",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _result(payload):
    """Wrap a tool payload as MCP tool content (text block of JSON)."""
    return {"content": [{"type": "text", "text": json.dumps(payload, indent=2)}]}


def call_tool(pack, name, args):
    if name == "search_concepts":
        return _result(pack.search(args.get("query", ""), int(args.get("k", 5))))
    if name == "get_concept":
        rec = pack.get(args.get("iri", ""))
        return _result(rec) if rec else _err_result(f"no concept with iri {args.get('iri')!r}")
    if name == "list_bridges":
        return _result(pack.bridges)
    return _err_result(f"unknown tool {name!r}")


def _err_result(msg):
    return {"content": [{"type": "text", "text": msg}], "isError": True}


def handle(req, pack):
    """Dispatch one JSON-RPC request; return a response dict, or None for notifications."""
    method, rid = req.get("method"), req.get("id")

    def ok(result):
        return {"jsonrpc": "2.0", "id": rid, "result": result}

    if method == "initialize":
        return ok({"protocolVersion": PROTOCOL_VERSION,
                   "capabilities": {"tools": {}}, "serverInfo": SERVER_INFO})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": TOOLS})
    if method == "tools/call":
        params = req.get("params", {})
        return ok(call_tool(pack, params.get("name"), params.get("arguments", {})))
    if method is not None and method.startswith("notifications/"):
        return None                       # notifications get no response
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": f"method not found: {method}"}}


def serve(pack, stdin=sys.stdin, stdout=sys.stdout):
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(req, pack)
        if resp is not None:
            stdout.write(json.dumps(resp) + "\n")
            stdout.flush()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", default="export/loan-origination/pack.json")
    args = ap.parse_args()
    serve(Pack.load(args.pack))


if __name__ == "__main__":
    main()
