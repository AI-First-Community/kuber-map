# Context pack — KYC & Beneficial Ownership (entity resolution)

Audit-ready FIBO grounding for a financial AI agent.

## Files
- `pack.json` — structured concept + bridge records (RAG / programmatic retrieval).
- `context.md` — the same content rendered for direct injection into an LLM prompt.
- `okf/` — a self-contained OKF slice (concept + bridge markdown).

## Retrieval endpoint (MCP)
An agent can query this pack over the Model Context Protocol:

```
python etl/mcp_server.py --pack export/KYC & Beneficial Ownership (entity resolution)/pack.json
```

Tools: `search_concepts(query, k)`, `get_concept(iri)`, `list_bridges()` — each result
carries the FIBO `citation` IRI and `provenance`.

## Citation model
58 concepts, 4 curated bridges. Each concept's `citation` is its
FIBO `resource` IRI — an agent cites it to justify a claim. `provenance` on every edge
and definition is `fibo` (from FIBO) or `curated` (authored here, grounded in FIBO).

Regenerate with `make pack` (after `make all`).
