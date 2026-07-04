# Backlog — Bodhi Map for FIBO

Living execution tracker. `PLAN.md` = design/source-of-truth; this file = what's done and what's next.
Pick the top unchecked item under **Immediate next** to continue. Every change must pass `make check`.

Last updated: 2026-07-04

---

## Status snapshot

**Done**
- ✅ Repo scaffold, MIT/FOSS files, quality gates (`ruff` + `pytest` + `validate` + attribution/employer guard), `CLAUDE.md`.
- ✅ FIBO→OKF pipeline: `etl/extract.py` (walks `owl:Restriction` blank nodes), `etl/to_okf.py`, `etl/validate.py`, `etl/fibo_ns.py`.
- ✅ De-risking spike passed + ETL hardened (kebab edges, module-aware collision-free paths, namespace classification, maturity propagation). See `SPIKE_RESULTS.md`.
- ✅ **Deterministic extraction** — `best_literal()` prefers en-US labels/definitions; stable relation order (is-a first, then typed). `make all` now reproduces the bundle byte-for-byte. Fixed `make setup` on fresh checkouts (setuptools flat-layout).
- ✅ Domains **emitted** in the bundle: **FND, LOAN, FBC, BE** (~1,288 concepts). Default `DOMAINS = FND LOAN FBC BE` so the loan-origination core + bridge endpoints all resolve to real nodes.
- ✅ Loan-Origination curation: **71 core concepts** (`curation/loan-origination.json`) + **4 validated cross-domain bridges** (`curation/bridges.json`, `knowledge/bridges/`). Tools: `etl/nominate_core.py`, `etl/bridges.py`.
- ✅ **`core:` wired into the bundle** — `to_okf.py` stamps `core: true` on all 71 curated concepts (frontmatter + index markers); `make curate` = nominate + bridges + rebuild.
- ✅ **Definition-rewrite overlay** — `curation/definitions.json` supplies learner-friendly definitions for the 7 core concepts FIBO ships with no `skos:definition` (each grounded in its FIBO superclass/axioms); `to_okf.py` applies them as `definition_provenance: curated`, keeps FIBO's `resource:` IRI, and refuses to overwrite any real FIBO definition.
- ✅ Published to GitHub (private): `AI-First-Community/Bodhi-Map-For-FinTech`, reproducible via `make fibo`.

**Not started:** context-pack export, the agent eval, the map UI, additional domains/use-cases, EDM contribution.

**Fresh-checkout setup:** `make setup && make fibo && make all` then `make check`.

---

## Immediate next (in order)

1. ✅ **Wire `core:` into the bundle** — done. `to_okf.py` reads `curation/loan-origination.json`, stamps `core: true` on all 71 concepts + marks them in each `index.md`; `make curate` runs nominate + bridges + rebuild.
2. ✅ **Learner-friendly definition rewrites** — done. `curation/definitions.json` covers the 7 empty-definition core concepts (*mortgage product*, *loan phase*, *consumer credit protection law*, the lifecycle phases/status, *borrower disclosure requirement*); applied as `definition_provenance: curated`, grounded in each class's FIBO superclass. The other 6 thin-but-present defs were left as FIBO's (Rule 1 — don't replace real FIBO text).
3. **Context-pack export** (the product) — `etl/export_pack.py`: take a use-case's `grounds_in` closure (71 core + 4 bridges) and emit (a) an OKF slice, (b) flat JSON for RAG, (c) an MCP tool / retrieval endpoint. One pack = one agent's grounding context, each concept carrying its FIBO IRI for citation. ◀ **next**
4. **Grounded-vs-ungrounded eval** (the value proof) — `eval/`: a 50–100 Q financial-semantics benchmark for loan underwriting; run an agent **with** vs **without** the context pack; score accuracy, hallucination rate, and % answers carrying a valid FIBO provenance citation. **Target: ≥15–20pt accuracy lift + 100% auditable.**

---

## Epics

### E1 — Complete the Loan-Origination MLV (value proof)  ◀ current focus
- [x] Wire `core:` flag from curation into generated bundle (`to_okf.py`)
- [x] `make curate` target (nominate_core + bridges + rebuild)
- [x] Definition-rewrite overlay for thin-def core concepts (curation input + `to_okf` apply)
- [ ] `etl/export_pack.py` — grounds_in closure → OKF slice + JSON + MCP endpoint
- [ ] `eval/` harness: benchmark, grounded vs ungrounded runner, scorecard
- [ ] Write up MLV result in `SPIKE_RESULTS.md` (the accuracy/hallucination/auditability numbers)

### E2 — The map UI (fork of Bodhi)
- [ ] Vendor Bodhi frontend (`app.html`, Cytoscape.js + fcose) into repo
- [ ] Extend `scripts/okf.js` → generate `js/data.js` (nodes + typed+provenance edges) from `knowledge/`
- [ ] Cluster colors per FIBO domain; edge styling by type; bridges styled distinctly (curated)
- [ ] Domain selector; maturity (Release/Provisional/Informative) filter; **core-view default + "show full ontology" toggle**
- [ ] Level-of-detail / lazy per-domain loading (required — 5–10k elements at full scale)
- [ ] Use-case lens (highlight a use-case subgraph) + reverse lookup (concept → use cases)
- [ ] Offline/PWA parity with Bodhi; no CDN

### E3 — Bridges & second use case
- [ ] Decide fate of intra-domain bridges (e.g. `lender played-by financial-institution`) vs cross-domain-only for EDM
- [ ] Map working bridge edge-names → formal FIBO object properties
- [ ] Second use case: **KYC / beneficial-ownership** (BE + FND) — nominate core + bridges + pack
- [ ] Regulatory-reporting use case (BE + FBC + MD) — needs MD domain

### E4 — Scale domains
- [ ] Onboard SEC, DER, IND, MD, BP, CAE (per-domain recipe in PLAN §7)
- [ ] Load Commons (CMNS) source so CMNS targets resolve to real nodes (currently pending links)
- [ ] Per-domain `core:` sets + lateral bridges + `index.md`

### E5 — EDM Council contribution
- [ ] Export curated bridges (`provenance: curated`) with rationale + citation as a proposal artifact
- [ ] Re-model accepted bridges as formal `owl:Restriction` axioms in FIBO style
- [ ] Engage EDM Council OKG Innovation Lab / FIBO CoP (DCO-signed PR) — *timing is user's call*

### E6 — Tech-debt / cleanups
- [ ] Edge-label normalization edge cases (camelCase from properties defined in unloaded domains)
- [ ] Review 219 orphan nodes (roots vs genuinely disconnected)
- [ ] Bump/refresh FIBO pin deliberately (churns generated files, may move IRIs) — document process
- [ ] Optional: shellcheck for `scripts/*.sh` in the gate

---

## Open decisions (need a call)
- **Repo visibility:** currently private; flip to public when ready for FOSS launch.
- **Commit generated `knowledge/`?** currently yes (browsable without rebuild). Revisit if it gets noisy at scale.
- **Intra-domain bridges** in the EDM contribution set — include or agent-only? (see E3)
- **Eval agent/model + benchmark authoring** — who writes the 50–100 gold questions; which model runs the agent.

## Key facts to not re-derive
- FIBO relations are `owl:Restriction` blank-node axioms, not flat triples (extractor handles this).
- `hasMaturityLevel` is per-ontology → propagated to classes.
- OKF types links by body prose, not frontmatter → our `relations:` typing is a private convention (fine for our build; generic OKF consumers see untyped links).
- FIBO has no Production git tags (only `2018Q3`); we pin a commit SHA (`fibo-source.pin`).
- No AI attribution / no employer references anywhere (guard-enforced); author = Sanjeev Azad <sanjeev.azad@gmail.com>.
