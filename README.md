# Kuber Map · the treasury of financial knowledge

A curated, learner-first knowledge map of the **Financial Industry Business Ontology
([FIBO](https://github.com/edmcouncil/fibo))**, stored in Google's **Open Knowledge Format
(OKF)**. It's the knowledge base and taxonomy for building AI and agentic AI in finance:
grounded, provenance-tagged, and audit-ready.

Named for **Kubera**, the treasurer and god of wealth. Inspired by the
[Bodhi Map](https://github.com/AI-First-Community/Bodhi) approach: reveal how concepts
*connect*, not just what they mean.

> **Status:** the FIBO→OKF pipeline runs on FND + LOAN + FBC + BE plus the Commons (CMNS)
> upper ontology (1,440 concepts, 3,001 typed relations). The loan-origination use case is
> curated end to end (71 core concepts, 4 cross-domain bridges, a context pack, and an MCP
> retrieval endpoint), and the interactive map ships. The live grounded-vs-ungrounded eval is
> the next milestone. See [`PLAN.md`](PLAN.md) and [`BACKLOG.md`](BACKLOG.md).

## Why

FIBO is a formal, exhaustive ontology built for modelers. Kuber Map reshapes it into three
things it isn't today:

1. **A teachable map.** A hand-picked "core" view with learner-friendly framing, where every
   other FIBO explorer renders the whole thing exhaustively for experts.
2. **A cross-domain bridge layer.** Provenance-tagged links across FIBO's separately-governed
   domains, offered back to EDM Council.
3. **Agent grounding.** Per-use-case context packs (e.g. loan origination) that give financial
   AI agents accurate semantics with a FIBO provenance trail for audit.

## Two products in one repo

- **The map** (`index.html` landing + `app.html` graph): an interactive Cytoscape view of the
  curated ontology, forked from Bodhi and driven by `okf.config.js` + generated `js/data.js`.
- **The context pack** (`export/`): a use case's grounding closure exported as `pack.json`
  (for RAG), `context.md` (to inject into a prompt), a self-contained OKF slice, and an MCP
  retrieval server (`etl/mcp_server.py`) an agent can call. Every concept carries its FIBO IRI.

## Quick start

```bash
make setup      # create venv, install deps
make fibo       # fetch the pinned FIBO source        -> fibo-source/
make commons    # fetch the Commons upper ontology     -> commons-source/
make all        # extract -> build OKF bundle -> validate
make map        # OKF bundle -> js/data.js for the map
make check      # quality gate: lint + tests + validate + attribution guard
```

Then open `index.html` (serve the folder over http for the offline/PWA layer, e.g.
`python3 -m http.server`). Requires Python 3.11+, Node, and git. The generated `knowledge/`
bundle and `js/data.js` are committed, so the map is browsable without a rebuild.

Full walkthroughs are in **[`docs/`](docs/)**:
[Getting Started](docs/Getting-Started.md) · [Architecture](docs/Architecture.md).

## Repository layout

| Path | What |
|---|---|
| `etl/` | FIBO extraction → OKF pipeline + context-pack export + MCP server (Python) |
| `knowledge/` | Generated OKF bundle (do not hand-edit) |
| `curation/` | Hand-authored overlays: core set, bridges, definitions, examples, notes |
| `scripts/okf.js`, `okf.config.js`, `js/`, `app.html`, `index.html` | The map (JS + Cytoscape) |
| `export/` | Generated context packs (per use case) |
| `eval/` | Grounded-vs-ungrounded eval harness + benchmark |
| `tests/` | pytest quality gate |
| `PLAN.md`, `BACKLOG.md`, `CLAUDE.md` | Plan, execution tracker, contributor rules |

## License

MIT © 2026 Sanjeev Azad. Derives from FIBO (MIT, EDM Council) and the OMG Commons Ontology
Library; attribution retained via each concept's `resource:` IRI. See [`LICENSE`](LICENSE).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every change must pass `make check`, keep FIBO facts
grounded in source (no invented IRIs), and keep provenance (`fibo` vs `curated`) unblurred.
