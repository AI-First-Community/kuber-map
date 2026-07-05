# Roadmap

Where Kuber Map is and where it's going. This is direction, not a contract — priorities shift with
community input. The design source of truth is [`PLAN.md`](PLAN.md); the detailed tracker is
[`BACKLOG.md`](BACKLOG.md). Want to help? See the
[good first issues](https://github.com/AI-First-Community/kuber-map/contribute).

## ✅ Shipped

- **The full ontology, extracted** — all ten FIBO domains + OMG Commons: **3,104 concepts, 6,676
  typed relations**, deterministically generated (byte-for-byte reproducible) from pinned source.
- **Five curated use cases** — loan origination, KYC / beneficial ownership, securities, regulatory
  reporting, derivatives: **284 curated core concepts + 19 validated cross-domain bridges**, each
  with worked examples and a grounding context pack.
- **The product: grounding for agents** — per-use-case context packs (`pack.json` for RAG,
  `context.md` for prompt injection, a self-contained OKF slice) + a stdlib **MCP retrieval
  server**. Every concept carries its FIBO IRI as an audit citation.
- **Value, measured** — grounded vs ungrounded eval across 5 domains and 2 models: **+45.3 pt
  accuracy, 97% auditable, 0% hallucinated citations**. The lift is model-robust.
- **The map** — an interactive Cytoscape graph (desktop) and a purpose-built mobile PWA, both over
  one generated data layer: use-case lens, provenance-styled bridges, IRI-citation panel, offline.
- **Open & community-ready** — MIT, public, GitHub Pages, a 9-page wiki, CI gate, issue/PR
  templates, CODEOWNERS, security & support policies.

## 🔜 Next

- **More use cases** — payments & settlement, insurance underwriting, ESG / sustainability
  reporting. Each is spec-driven (`curation/usecases/*.json`), no code — the highest-leverage
  contribution. ([Authoring guide](https://github.com/AI-First-Community/kuber-map/wiki/Use-Case-Authoring))
- **More cross-domain bridges** — the moat and our contribution back to the EDM Council. Every
  bridge is provenance-tagged and citation-backed.
- **Engage the EDM Council** — offer the packaged bridge contribution (`contrib/`) upstream.
- **Mobile PWA polish** — continue the audit-driven improvements (provenance surfacing, per-use-case
  onboarding, small UX wins).

## 🌅 Later

- **Formalize the bridge vocabulary** — map our working edge names to formal FIBO/RDF object
  properties so the contribution is drop-in for modelers.
- **Scale the full-graph view** — per-domain lazy loading for the whole 3k+ ontology (fine today;
  revisit at 5–10k on screen).
- **Broaden the eval** — more models and more domains, to keep the "grounding beats a bigger model"
  claim honest as models improve.
- **Deeper agent integrations** — worked examples wiring the context packs / MCP server into common
  agent frameworks.

## How to help

The fastest paths in: **author a use case**, **propose a cross-domain bridge** (with a citation), or
**improve the map / mobile app**. Read [`CONTRIBUTING.md`](CONTRIBUTING.md), pick a
[good first issue](https://github.com/AI-First-Community/kuber-map/contribute), and open a PR — every
change runs the same quality gate (`ruff` + `pytest` + `validate` + attribution guard) in CI.
