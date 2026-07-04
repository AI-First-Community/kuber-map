# Context pack — Loan Origination & Underwriting (residential mortgage)

Audit-ready FIBO grounding for a financial AI agent.

## Files
- `pack.json` — structured concept + bridge records (RAG / programmatic retrieval).
- `context.md` — the same content rendered for direct injection into an LLM prompt.
- `okf/` — a self-contained OKF slice (concept + bridge markdown).

## Citation model
71 concepts, 4 curated bridges. Each concept's `citation` is its
FIBO `resource` IRI — an agent cites it to justify a claim. `provenance` on every edge
and definition is `fibo` (from FIBO) or `curated` (authored here, grounded in FIBO).

Regenerate with `make pack` (after `make all`).
