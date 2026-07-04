# Bodhi Map for FIBO — Project Plan (v2)

> A curated, **learner-first** knowledge map for the **Financial Industry Business Ontology (FIBO)** that doubles as **audit-ready grounding for financial AI agents** — with a provenance-tagged **cross-domain bridge layer** contributed back to EDM Council.

Status: **Building — Loan-Origination MLV (Phase 1)** · Owner: Sanjeev Azad · Last updated: 2026-07-04

> **Execution status lives in [`BACKLOG.md`](BACKLOG.md)** (what's done / what's next). Snapshot: pipeline + quality gates + FND/LOAN/FBC/BE extraction done; 71 core concepts + 4 cross-domain bridges curated; published private to `AI-First-Community/Bodhi-Map-For-FinTech`. Next: wire `core:` into the bundle → context-pack export → grounded-vs-ungrounded eval. Fresh checkout: `make setup && make fibo && make all`.

> **v2 changelog.** This revision followed a three-lens adversarial audit (readiness, ROI, uniqueness). Major changes: (1) **re-sequenced roadmap** — agent-grounding is now Phase 1, not Phase 3; (2) **corrected two overstated claims** — FIBO cross-domain linking and OKF typed-frontmatter (§3, §6); (3) added an **OWL-restriction extraction spike** and **level-of-detail rendering** as hard Phase-1 requirements; (4) reframed the value prop and novelty around **pedagogical curation + intra-FIBO bridges**, treating OKF and agent-grounding as enablers, not the thesis. See §12 for the audit trail.

---

## 1. The sharpest framing (what we're actually building)

> **We turn FIBO into audit-ready grounding for financial AI agents — so they stop hallucinating on financial semantics, and you can prove to a regulator exactly which concepts justified every decision.**

The interactive map is the **demo and the curation surface**, not the product. The product is a **curated FIBO subgraph + cross-domain bridges, exportable as per-use-case grounding context** for financial AI agents, with provenance/citation for audit.

**Value ranking (drives the roadmap):**
1. **Agent-grounding (~70%)** — the only pillar touching a pain with a budget: financial AI agents hallucinate on domain semantics and can't show a regulator *why* they answered. → **Phase 1.**
2. **Cross-domain bridges (~25%)** — near-zero standalone value, but the **moat**: they make multi-domain use cases coherent and are hard to copy (curation, not code). → the connective tissue that makes pillar 1 work.
3. **The map (~5%)** — a fork of Bodhi's Cytoscape UI; its jobs are (a) sales/demo and (b) the human review surface for curating bridges. Not a business on its own.

The old v1 ordering (map → bridges → agents) was inverted relative to value and has been corrected.

---

## 2. Background (the three ingredients)

### 2.1 Bodhi Map — the UI we reuse
Hand-curated Cytoscape graph (128 concepts, 12 clusters, 6 typed edges). MIT-licensed, **owned by us** (© 2026 Sanjeev Azad). Fork it wholesale for the rendering/curation surface.
- **Corrected structure** (verified against the repo): build tool is **`scripts/okf.js` (JavaScript)**, app entry is **`app.html`**. There is **no `js/graph.js`** and **no Python `build_data.py`** in Bodhi. → We extend `scripts/okf.js` for the OKF→`data.js` build and keep the Python work confined to FIBO extraction (§5). Runtime is buildless; regenerating `data.js` is a build step.

### 2.2 Google OKF v0.1 — an export format, not the thesis
Markdown+YAML bundle spec (Google Cloud, June 2026). Required frontmatter `type`; recommended `title/description/resource/tags/timestamp`; reserved `index.md`/`log.md`.
- **Correction (load-bearing):** OKF types relationships by **prose around body markdown links**, *not* by frontmatter. A `relations:` frontmatter block is spec-legal (unknown keys tolerated) but **inert to any generic OKF consumer** — only our own build script reads it. So the "agents consume *typed* OKF slices" claim is false for generic agents; they see untyped links like plain markdown.
- **Consequence:** treat OKF as one **export format** among several (also emit JSON / Cypher / an MCP endpoint). If OKF stalls, the curated FIBO+bridges graph still stands. Don't bet the value prop on OKF.

### 2.3 FIBO — the subject matter
OWL ontology, RDF/XML (also TTL/JSON-LD via the ontology-publisher). **~2,446 classes** in the current Production release. 10 domains: FND, BE, FBC, SEC, DER, IND, LOAN, BP, CAE, MD. MIT-licensed — redistribution/derivatives OK with attribution.
- **Maturity** is annotated via `fibo-fnd-utl-av:hasMaturityLevel` (Release / Provisional / Informative) **at the ontology-file level, not per class** — must be *propagated* down to classes. Several domains (BP, CAE, MD, parts of DER/IND/SEC) are **Provisional** and churn quarterly.
- **Relationships are not flat triples:** object-property relations (`secured-by`, `hasUnderlier`, `party-to`) live in **`owl:Restriction` blank-node axioms** on `rdfs:subClassOf`. The extractor must walk restrictions, not just triples (§5, spike).

---

## 3. Corrected theses (what survives scrutiny)

### 3.1 Cross-domain linking — corrected claim
**v1 said** FIBO is "deliberately thin on links across domains." **That's overstated.** FIBO ships `FND/Relations/Relations.rdf`, and FND is `owl:imported` by BE/FBC/SEC/IND — **FND-mediated cross-domain linking is FIBO's backbone.**

**The real, defensible gap** (this is the contribution):
- **Lateral, peer-to-peer bridges** between business domains that don't route through FND (e.g. LOAN↔SEC for securitization, LOAN↔BE for reporting entities).
- **Learner-facing surfacing** of cross-domain relations that *exist in the axioms but are buried* in restriction blank nodes and invisible in the official Viewer.

We must **measure** actual cross-domain imports first, then scope bridges to genuine lateral gaps — or the contribution won't survive EDM Council review.

### 3.2 Agent grounding — corrected claim
Grounding is real and valuable, but **not novel** (OG-RAG, Wipro, FinKario, Springer alignment work already do FIBO-grounded RAG). Our defensible delta is narrow and practical: **per-use-case curated context packs with cross-domain bridges + provenance citations for audit** — better than naive "dump FIBO in a vector DB" because vector similarity misses multi-hop cross-domain paths, which is exactly what curated bridges provide.

---

## 4. Uniqueness — where the moat actually is

No single pillar is novel: interactive FIBO viz is commoditized (official Viewer, GraphDB/Graphwise, WebVOWL); FIBO-grounds-agents is a crowded field; "OKF bundle → Cytoscape graph" is already an off-the-shelf tool (`okf-skills`). **The defensible angle is the intersection, led by the two least-fashionable parts:**

> **Pedagogical curation of FIBO** (a *teachable* map with a hand-picked "core" default — nobody does this; every competitor renders FIBO exhaustively for experts) **+ a provenance-tagged intra-FIBO cross-domain bridge layer** offered back to EDM Council.

OKF and agent-grounding are **on-trend enablers**, not the novelty claim. Lead with curation + bridges.

⚠️ **Strategic:** the **EDM Council OKG (Open Knowledge Graph) Innovation Lab** is both the best distribution/legitimacy path *and* the party most likely to build the cross-domain layer first. **Engage them early** (FIBO Community of Practice / EDMConnect) rather than building in a vacuum.

---

## 5. Architecture

```
bodhi-fibo/
├── fibo-source/            # git submodule → edmcouncil/fibo, PINNED to a Production tag
├── etl/                    # Python (rdflib / owlready2) — FIBO extraction ONLY
│   ├── extract.py          #   OWL → intermediate JSON. MUST walk owl:Restriction blank nodes,
│   │                       #   not just triples. Propagate per-ontology hasMaturityLevel → classes.
│   ├── freq.py             #   object-property frequency analysis → which edges to promote
│   └── validate.py         #   link integrity, orphans, provenance, IRI→path round-trip
├── knowledge/              # GENERATED OKF bundle (interchange + one export format)
│   ├── index.md
│   ├── FND/ LOAN/ FBC/ BE/ … (added one domain at a time, §7)
│   ├── bridges/            # CURATED intra-FIBO cross-domain layer (§8) — the moat
│   └── use-cases/          # AGENT grounding packs (§6) — the product
├── scripts/okf.js          # EXTENDED from Bodhi: OKF bundle → js/data.js (typed edges via our convention)
├── export/                 # per-use-case context packs: OKF slice + JSON + MCP endpoint (§6)
├── okf.config.js           # controlled vocab: edge types, cluster colors, use-case lenses
├── js/data.js              # GENERATED
├── app.html + js/          # forked Bodhi UI (Cytoscape + fcose) + LOD/lazy-load (§9)
└── fonts/ vendor/          # vendored locally (offline)
```

**Pipeline:** `fibo-source (OWL)` → `extract.py` (restriction-aware) → intermediate JSON → OKF bundle (+ hand-authored `bridges/`, `use-cases/`) → `scripts/okf.js` → `js/data.js` → Cytoscape; and → `export/` context packs for agents.

**Two toolchains, cleanly split:** Python does FIBO OWL extraction (where the hard axiom-walking lives); JS (`scripts/okf.js`, extended from Bodhi) does bundle→`data.js`. Don't reinvent the JS build in Python.

### OKF file model (per FIBO class)
```markdown
---
type: FIBO Class
title: Mortgage Loan                          # rdfs:label
description: A loan secured by real property.  # skos:definition, trimmed (many classes lack one — see coverage risk)
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/.../MortgageLoan
tags: [LOAN, Release]                           # domain + PROPAGATED maturity
core: true                                      # in curated default view?
relations:                                      # OUR convention (inert to generic OKF consumers — see §2.2)
  - {type: is-a,        target: /LOAN/Loan.md,             provenance: fibo}
  - {type: secured-by,  target: /FND/.../RealProperty.md,  provenance: fibo}
  - {type: reported-in, target: /BE/.../RegulatoryReport.md, provenance: curated}   # a cross-domain bridge
---
Definition + learner notes. Related concepts ALSO linked inline as body markdown so
generic OKF consumers still get the (untyped) graph: see [Loan](/LOAN/Loan.md).
```
`provenance: fibo|curated` is essential: it lets us style bridge edges distinctly, and **export only curated edges** as the EDM Council contribution.

---

## 6. Agent-grounding layer — the product (Phase 1)

Each use case pins to the FIBO subgraph that grounds it and exports a portable context pack.

```markdown
---
type: Agentic Use Case
title: Loan Origination & Underwriting Agent
description: Assesses a mortgage application against borrower, collateral, and regulatory concepts.
tags: [use-case, lending, LOAN, FND, FBC, BE]
grounds_in:                                     # the curated subgraph (closure exported as a context pack)
  - /LOAN/.../MortgageLoan.md
  - /FND/.../RealProperty.md
  - /FBC/.../Borrower.md
  - /BE/.../RegulatoryReport.md
agent:
  workflow: [ingest-application, resolve-entities, value-collateral, check-eligibility, decision]
  guardrails: [FIBO-provenance-citation, human-in-loop-on-decline, audit-trail]
---
```

**Exports** (`export/`): the `grounds_in` closure as (a) an OKF slice, (b) plain JSON for RAG, (c) an **MCP tool / retrieval endpoint** an agent calls. Each answer carries the FIBO concept IRIs that grounded it → the audit trail.

**Candidate use cases:** Loan Origination (Phase 1), KYC/beneficial-ownership (BE+FND), regulatory reporting (BE+FBC+MD), derivatives risk (DER+SEC+IND+MD), corporate actions (CAE+SEC), settlement (BP+SEC+FBC).

---

## 7. Domain selector & incremental onboarding

UI control to pick one domain / a set / "All". Repeatable onboarding recipe per domain: scope `extract.py` → write `knowledge/<DOMAIN>/` → author `index.md` + tag `core:` → add cluster color → author lateral bridges to loaded domains → rebuild.

**Order (value + dependency):** FND → **LOAN** → FBC → BE → SEC → DER → IND → MD → BP → CAE. FND first (everyone imports it); LOAN first "real" domain (concrete, high FinTech value, the Phase-1 use case).

---

## 8. Cross-domain bridge layer — the moat / the contribution

Curated `bridges/` files asserting **lateral** cross-domain relations FIBO doesn't draw natively, each with a `rationale:` + citation.

```markdown
---
type: Cross-Domain Relation
title: Mortgage Loan → Mortgage-Backed Security
description: Pooled mortgage loans serve as the underlier of an MBS.
tags: [bridge, LOAN, SEC]
relations:
  - {type: underlies, target: /SEC/.../MortgageBackedSecurity.md, provenance: curated}
source_class: /LOAN/.../MortgageLoan.md
rationale: Documented justification + citation, for EDM Council review.
---
```

**Contribution caveat:** EDM Council models relations as formal `owl:Restriction` axioms under a **DCO-signed PR + working-group** governance process. Informal `rationale:` strings won't merge as-is; budget to **re-model accepted bridges in their axiom style**. Engage the OKG Lab first (§4).

---

## 9. Rendering & scale (hard Phase-1 requirement, not deferred)

~2,446 classes + subClassOf + promoted property edges ≈ **5,000–10,000 elements** — fcose chokes at that size. **Level-of-detail + lazy per-domain loading is required in Phase 1**, not a "may need later." Curated **core view is the default** landing (readable); "Show full ontology" loads per-domain on demand. Maturity/level filter reuses Bodhi's level control.

---

## 10. Roadmap (re-sequenced: value first)

**Phase 0 — Scaffold** (can start today 🟢)
Fork Bodhi (own it), pin FIBO submodule to a Production tag, stub `okf.config.js`, ETL skeleton.

**Phase 0.5 — De-risking spikes** (blockers before real ETL)
1. **OWL restriction/blank-node extraction spike** on FND+LOAN — prove we can pull typed object-property relations, not just triples.
2. Decide serialization (RDF/XML from GitHub vs pre-serialized TTL/JSON-LD) + pin release. **Done (spike):** RDF/XML via rdflib; pinned to commit `ae12db3` — note FIBO has **no Production git tags** (only `2018Q3`); releases roll on `master`, so we pin a SHA. See `fibo-source.pin`.
3. Define **IRI→path mapping** + version-churn/diff strategy + per-class maturity propagation.
4. Object-property **frequency analysis** → which edges to promote.
5. **Definition/label coverage stat** → sizes the curation budget.

**Phase 1 — Minimum Lovable Version: prove the value** (the answer to "is this just fancy tech?")
- **One use case end-to-end: Loan Origination** (LOAN+FND+FBC+BE). Hand-curate ~40–60 concepts + the 5–10 lateral bridges it needs (skip full extraction).
- Ship the **context pack + retrieval endpoint** (the product), and the curated map (the demo/curation UI) with LOD.
- **Value-proof eval:** loan-underwriting agent on a 50–100 Q financial-semantics benchmark, **grounded vs ungrounded** — score accuracy, hallucination rate, and % of answers carrying a valid FIBO provenance citation. **Target: ≥15–20pt accuracy lift + 100% auditable answers.** If it doesn't move, we learned cheaply.

**Phase 2 — Harden the moat**
Full restriction-aware ETL for FND+LOAN; more lateral bridges with rationales; second use case (KYC).

**Phase 3 — Scale domains** (§7 recipe) with bridges + use cases per domain.

**Phase 4 — Contribute + publish**
Export curated bridges (`provenance: curated`), re-model in axiom style, DCO-signed PR to `edmcouncil/fibo` via OKG Lab; publish the map as top-of-funnel.

---

## 11. ROI — honest estimates

| Claim | Estimate | Certainty |
|---|---|---|
| Engineer-time saved grounding one agent use case (vs hand-curating FIBO context + cross-domain links) | ~80–150 senior-engineer hours / use case | Low–medium (plausible, unbenchmarked) — **the one number worth putting in a deck** |
| Accuracy lift / hallucination drop from ontology grounding | External: ~54% avg KG-RAG accuracy lift; hallucination ~48–63%→~1.7% (clinical) | Medium, **cross-domain analogy** — must measure our own *financial* number; do not present clinical stats as ours |
| Regulatory concept→report lineage effort | 6-figure consulting line; even 10–20% cut is real | Speculative — requires building lineage (not yet scoped) |
| EDM Council contribution | Credibility/marketing; **~$0 direct revenue** | High certainty it doesn't pay bills |

**Buyers with a checkbook:** the **AI/agent builder** (primary) and the **compliance/model-risk team** (traceable lineage). Ontologists, modelers, and FinTech engineers are users/contributors/spectators, not customers.

---

## 12. Readiness verdict & risks

**🟡 YELLOW.** Phase 0 starts today (licenses MIT, FIBO parseable, Bodhi structure confirmed). Phase 1 ETL is gated on the Phase-0.5 spikes.

**Must-resolve blockers:** (1) OWL restriction/blank-node extraction; (2) reframe + measure the cross-domain thesis; (3) pin release + serialization + maturity propagation; (4) IRI→path + churn strategy; (5) LOD rendering.

**Underweighted risks:** curation is **person-months** and financial/legal definition rewrites carry accuracy/liability risk (real SME review, not rubber-stamp); Provisional domains churn quarterly and break `core:`/bridge references keyed to moved IRIs; EDM OKG Lab may build the bridge layer first; OKF ecosystem is 4 weeks old (hence: export format, not thesis).

**Audit trail (v1→v2):** three-lens review — Readiness (verified FIBO/OKF/Bodhi facts, found the restriction-extraction gap), ROI (found the inverted value ranking, defined the MLV eval), Uniqueness (found the true differentiator is curation + intra-FIBO bridges). All three independently flagged the same reframe.

---

## 13. Sources
- Bodhi Map — https://github.com/AI-First-Community/Bodhi
- OKF spec — https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- FIBO — https://github.com/edmcouncil/fibo · Viewer https://spec.edmcouncil.org · Ontology guide (repo `ONTOLOGY_GUIDE.md`)
- EDM Council OKG Innovation Lab — https://spec.edmcouncil.org/ · FIBO CoP (EDMConnect)
- Prior art: Ontotext/Graphwise GraphDB+FIBO; OG-RAG (Wipro); FinKario (arXiv 2508.00961); FinRegOnt; FIB-DM; okf-skills
- Grounding evidence: KG-RAG hallucination-reduction survey (arXiv 2311.07914)
