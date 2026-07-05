# EDM Council contribution — documentation hub

**One place for everything you need to engage the EDM Council** about Kuber Map's cross-domain
bridge contribution: the proposal, the machine-readable serialization, the outreach copy, a
review-ready visual brief, and pointers to the supporting evidence elsewhere in the repo.

This whole `contrib/` folder is self-contained — you can hand it (or a zip of it) to a reviewer.

## Start here (recommended order)

1. **[bridge-brief.pdf](bridge-brief.pdf)** — the 30-second version: the six strongest bridges,
   diagrammed, each with a rationale + citation. (`-light` variant for print/formal use.)
2. **[edmc-bridge-contribution.md](edmc-bridge-contribution.md)** — the full proposal: methodology,
   the grounding gate, and all **19** relations with source/target IRIs, rationale, and citation.
3. **[OUTREACH.md](OUTREACH.md)** — how to actually engage: a pre-send checklist, a **Community-of-
   Practice intro note** (draft A), and a **DCO-signed pull-request description** (draft B).

## In this folder

| File | What | Origin |
|---|---|---|
| `edmc-bridge-contribution.md` | Full proposal — 19 bridges, methodology, per-use-case tables | **generated** (`make contrib`) |
| `fibo-bridges.ttl` | RDF/Turtle — each bridge a `kmb:` triple + an `owl:Axiom` carrying rationale/citation/provenance (parses in rdflib) | **generated** (`make contrib`) |
| `OUTREACH.md` | Checklist + CoP intro note + DCO-signed PR description | hand-authored |
| `bridge-brief.html` | Source of the one-page brief (theme-aware) | hand-authored |
| `bridge-brief{,-light}.pdf` / `.png` | The one-page brief, dark + light, print-ready | rendered |
| `render-brief.mjs` | Regenerate the brief PDFs/PNGs from the HTML | hand-authored |

## Supporting evidence & context (lives elsewhere — linked so you don't hunt for it)

- **Why grounding matters (the value proof):** [`../SPIKE_RESULTS.md`](../SPIKE_RESULTS.md) and the
  wiki [Value Proof](https://github.com/AI-First-Community/kuber-map/wiki/Value-Proof) — grounded vs
  ungrounded: +45.3pt accuracy, 97.0% auditable, 0% hallucination. Context for *why* a curated,
  cited bridge layer is worth drawing.
- **The bridges, explained for humans:** wiki
  [Cross-Domain Bridges](https://github.com/AI-First-Community/kuber-map/wiki/Cross-Domain-Bridges).
- **The gate that keeps them honest:** [`../etl/bridges.py`](../etl/bridges.py) (resolves both
  endpoints against the pinned FIBO source; rejects any edge FIBO already asserts) and
  [`../etl/export_bridges.py`](../etl/export_bridges.py) (packages this folder).
- **The bridge sources (curation input):** [`../curation/`](../curation/) — the `*-bridges.json`
  files (one per use case), each edge with a `rationale` + citation.
- **Strategy & honest framing:** [`../PLAN.md`](../PLAN.md) §3.1 (the *corrected* cross-domain
  claim — FND-mediated linking is FIBO's backbone; these are lateral gaps), §4 (why the EDM Council
  OKG Innovation Lab is the right venue), §8 (the bridge layer + contribution governance).

## Regenerate

```bash
make contrib                 # -> edmc-bridge-contribution.md + fibo-bridges.ttl (from the bundle)
node contrib/render-brief.mjs  # -> bridge-brief{,-light}.pdf + .png (needs: npm i playwright)
```

## When you're ready to engage

Follow **[OUTREACH.md](OUTREACH.md)**: post the CoP note (attach `bridge-brief.pdf`, link the full
proposal) **first**, incorporate the working group's steer on property mapping, then open the PR.
Sending is a deliberate, outward-facing step — nothing here goes anywhere automatically.
