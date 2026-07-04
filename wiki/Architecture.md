# Architecture

Two toolchains, one bundle in the middle.

```
FIBO OWL/RDF ──(Python ETL)──▶ knowledge/ OKF bundle ──(JS build)──▶ js/data.js ──▶ the map
                                     │
                                     └──(Python)──▶ export/ context packs ──▶ AI agents
```

## 1. Extract (`etl/extract.py`)

FIBO ships as OWL/RDF where the interesting relationships hide inside `owl:Restriction` blank-node
axioms on `rdfs:subClassOf`, not as flat triples. `extract.py` walks those into a flat
`out/intermediate.json`. Extraction is **deterministic** (stable label/relation ordering) so the
bundle reproduces byte-for-byte. `fibo_ns.py` classifies every IRI into a cluster (FIBO domain /
`CMNS` / `LCC`).

## 2. Build the OKF bundle (`etl/to_okf.py`)

One markdown file per concept, with YAML frontmatter (`type`, `title`, `description`, `resource:`
the FIBO IRI, `tags`, `core:`, `use_cases:`, `relations:`). Curation overlays are applied here —
per-use-case core sets, definitions, examples, notes — each grounded in a real FIBO IRI. Only
`knowledge/bridges/` and the `curation/` overlays are hand-authored; everything else is generated.

**Provenance is never blurred:** every edge and overlaid field is tagged `fibo` or `curated`.
Overlays only fill gaps; they never overwrite real FIBO text.

## 3. Curation (`curation/`)

A use case is spec-driven (see **[Use Cases](Use-Cases)**): a facet spec resolved by
`nominate_core.py`, cross-domain bridges gated by `bridges.py`, and example/definition overlays.
`validate.py` checks the bundle for broken links, orphans, and self-loops.

## 4. The map (`scripts/okf.js` + `okf.config.js` + `js/`)

`okf.config.js` holds everything that isn't a concept — the domains (split into module
sub-clusters), maturity levels, relation styling (curated bridges drawn distinctly), and the
interactive flows. `scripts/okf.js build` emits `js/data.js`. `js/graph.js` (forked from Bodhi,
small edits) renders it with Cytoscape + fcose; the CSS is byte-identical to Bodhi. The default
view lays out only the visible core, so load stays fast even with the full 3,104-node ontology.

## 5. Context packs + eval (`etl/export_pack.py`, `eval/`)

`export_pack.py` emits a use case's grounding closure as `pack.json` (RAG), `context.md` (prompt
injection), and an OKF slice. `etl/retrieval.py` + `etl/mcp_server.py` expose it as an MCP retrieval
endpoint. `eval/harness.py` measures the grounded-vs-ungrounded lift deterministically — see
**[Value Proof](Value-Proof)**.

Fuller version in
[docs/Architecture.md](https://github.com/AI-First-Community/Bodhi-Map-For-FinTech/blob/main/docs/Architecture.md).
