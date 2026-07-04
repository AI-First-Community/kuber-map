# Kuber Map · the treasury of financial knowledge

A curated, learner-first knowledge map of the **Financial Industry Business Ontology
([FIBO](https://github.com/edmcouncil/fibo))**, stored in Google's **Open Knowledge Format
(OKF)**. It's the knowledge base and taxonomy for building AI and agentic AI in finance:
grounded, provenance-tagged, and audit-ready.

Named for **Kubera**, the treasurer and god of wealth. Inspired by the
[Bodhi Map](https://github.com/AI-First-Community/Bodhi) approach: reveal how concepts
*connect*, not just what they mean.

> **Status:** the FIBO→OKF pipeline runs on all ten FIBO domains (FND, LOAN, FBC, BE, SEC,
> DER, IND, MD, BP, CAE) plus the Commons (CMNS) upper ontology — 3,104 concepts, 6,676 typed
> relations, 68 sub-domain clusters. **Five use cases** are curated end to end — loan origination,
> KYC / beneficial ownership, securities, regulatory reporting, and derivatives (284 core concepts
> in total, each with worked examples on the card) — wired by **19 validated cross-domain bridges**,
> with per-use-case context packs and an MCP retrieval endpoint. The interactive map ships (with a
> use-case lens) and covers every domain. The grounded-vs-ungrounded eval is proven across **four
> domains and two models** (gpt-4o-mini and gpt-4o): **+44.5pt aggregate accuracy lift over 209
> questions, 96.2% auditable, 0% grounded hallucination**. The 19 bridges are packaged as an EDM
> Council contribution proposal (`contrib/`). See [`PLAN.md`](PLAN.md), [`BACKLOG.md`](BACKLOG.md),
> and [`SPIKE_RESULTS.md`](SPIKE_RESULTS.md).

## Why

FIBO is a formal, exhaustive ontology built for modelers. Kuber Map reshapes it into three
things it isn't today:

1. **A teachable map.** A hand-picked "core" view with learner-friendly framing, where every
   other FIBO explorer renders the whole thing exhaustively for experts.
2. **A cross-domain bridge layer.** Provenance-tagged links across FIBO's separately-governed
   domains, offered back to EDM Council.
3. **Agent grounding.** Per-use-case context packs (loan origination, KYC, securities, regulatory
   reporting, derivatives) that give financial AI agents accurate semantics with a FIBO provenance
   trail for audit — the eval shows this lifts accuracy and takes auditability toward 100%.

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

MIT © 2026 Sanjeev Azad — see [`LICENSE`](LICENSE).

This project incorporates and redistributes content from **FIBO** (MIT, © EDM Council & OMG) and
the **OMG Commons Ontology Library** (MIT, © EDM Council, OMG & Thematix Partners) — both permissive
and MIT-compatible — plus vendored MIT/OFL front-end libraries. Their copyright and permission
notices, and a trademark disclaimer, are in **[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)**.
FIBO/EDM Council/OMG are trademarks of their owners; this is an independent project, not affiliated
with or endorsed by them.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every change must pass `make check`, keep FIBO facts
grounded in source (no invented IRIs), and keep provenance (`fibo` vs `curated`) unblurred.
