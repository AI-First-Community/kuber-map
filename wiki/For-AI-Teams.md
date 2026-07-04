# For AI teams: grounding your agent

If you are building a financial AI agent, this is the part that matters to you: a **context pack**
is a portable, provenance-tagged grounding closure for one use case that you inject into your agent.
It is model-agnostic and dependency-free. This page shows what's in it and three ways to use it.

## What a context pack is

Run `make pack` (or take one from `export/`). Each use case produces `export/<use-case>/`:

| File | What it is |
|---|---|
| `pack.json` | structured records for retrieval / RAG (see shape below) |
| `context.md` | the same knowledge as one Markdown doc, ready to inject into a prompt |
| `okf/` | a self-contained OKF slice (the concept files + bridges) |
| `README.md` | what the pack contains and how it was built |

`pack.json` shape:

```jsonc
{
  "use_case": "KYC & Beneficial Ownership",
  "counts": { "concepts": 58, "bridges": 4 },
  "concepts": [
    {
      "iri": "https://spec.edmcouncil.org/fibo/ontology/BE/.../BeneficialOwner",
      "title": "beneficial owner",
      "definition": "party that enjoys the benefits of ownership...",
      "definition_provenance": "fibo",          // fibo | curated — never blurred
      "citation": "https://spec.edmcouncil.org/fibo/ontology/BE/.../BeneficialOwner",
      "facet": "Ownership & control", "cluster": "BE", "maturity": "Release",
      "relations": [ { "type": "is-a", "target": "...", "provenance": "fibo" } ]
    }
  ],
  "bridges": [
    { "edge": "identified-by", "source_title": "legal entity", "target_title": "legal entity identifier",
      "provenance": "curated", "rationale": "...", "citation": "ISO 17442; FATF Rec. 24" }
  ]
}
```

The key property: **every concept carries its FIBO `citation` IRI and a `provenance` tag**, so any
answer your agent produces can be traced back to the standard, and your additions are never confused
with FIBO's.

## Option 1 — Inject the context (simplest)

For a small use case, drop `context.md` straight into your system prompt or a retrieval-augmented
turn, and instruct the model to cite. That is exactly what the eval's grounded run does:

```
<contents of export/<uc>/context.md>

Answer the question using the FIBO grounding context above. On a final line, write
"Sources:" followed by the resource IRI(s) from the context that support your answer.
```

That single instruction is what takes auditability from 0% to ~100% (see **[Value Proof](Value-Proof)**).

## Option 2 — Retrieve from the pack (RAG)

For a larger use case, retrieve the top concepts per question instead of injecting everything.
`etl/retrieval.py` provides weighted keyword search over a pack with no dependencies:

```python
from retrieval import Pack
pack = Pack.load("export/kyc/pack.json")
hits = pack.search("who is the ultimate beneficial owner of a company?", k=4)
for h in hits:
    print(h["title"], "->", h["citation"])   # inject h["definition"] + cite h["citation"]
```

Or bring your own vector store: `pack.json` is plain records with stable IRIs as ids.

## Option 3 — Call the MCP retrieval endpoint

`etl/mcp_server.py` is a stdlib-only MCP stdio server your agent framework can call directly. Tools:

| Tool | Purpose |
|---|---|
| `search_concepts` | keyword search → concepts with definition, citation IRI, provenance |
| `get_concept` | fetch one concept by IRI |
| `list_bridges` | the curated cross-domain bridges for the use case |

Every result carries the citation IRI + provenance, so the agent can cite exactly which concept
justified an answer and a regulator can trace it.

## The grounding pattern (why it works)

1. **Retrieve** the relevant grounded concepts for the question from the pack.
2. **Inject** their definitions + IRIs into the prompt.
3. **Require a citation** — instruct the model to end with `Sources: <IRI>`, and only cite IRIs
   present in the context.
4. **Verify** if you need to: the IRIs are real and checkable against FIBO.

This is model-agnostic. The [eval harness](Value-Proof) measured a **+44.5pt accuracy lift, 96.2%
auditability, 0% grounded hallucination** across four domains and two models with exactly this
pattern. Point `eval/harness.py` at your own benchmark and pack to measure it on your stack:

```bash
EVAL_LLM_CMD='your-model-cli' python eval/harness.py --adapter llm \
  --benchmark eval/<uc>-benchmark.json --pack export/<uc>/pack.json
```

No vendor SDK is required — the harness pipes a prompt to any command on stdin.
