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
- ✅ **All ten FIBO domains emitted**: FND, LOAN, FBC, BE, SEC, DER, IND, MD, BP, CAE + Commons (CMNS) — **3,104 concepts, 6,676 typed relations, 68 sub-domain clusters**. `scripts/fetch_fibo.sh` sparse-checks out all ten; `DOMAINS`/`CLUSTERS` and `okf.config.js` cover every domain. The map now spans all of FIBO; the curated use-case cores stay the default lens.
- ✅ Loan-Origination curation: **71 core concepts** (`curation/loan-origination.json`) + **4 validated cross-domain bridges** (`curation/bridges.json`, `knowledge/bridges/`). Tools: `etl/nominate_core.py`, `etl/bridges.py`.
- ✅ **`core:` wired into the bundle** — `to_okf.py` stamps `core: true` on all 71 curated concepts (frontmatter + index markers); `make curate` = nominate + bridges + rebuild.
- ✅ **Definition-rewrite overlay** — `curation/definitions.json` supplies learner-friendly definitions for the 7 core concepts FIBO ships with no `skos:definition` (each grounded in its FIBO superclass/axioms); `to_okf.py` applies them as `definition_provenance: curated`, keeps FIBO's `resource:` IRI, and refuses to overwrite any real FIBO definition.
- ✅ **Context-pack export** (the product, `etl/export_pack.py` + `make pack`) — `export/loan-origination/` with `pack.json` (structured RAG records), `context.md` (LLM-injectable grounding doc), and a self-contained `okf/` slice. 71 concepts + 4 bridges, each carrying its FIBO IRI as citation + `provenance` on every edge/definition.
- ✅ **MCP retrieval endpoint** — `etl/mcp_server.py` (stdlib-only MCP stdio server) + `etl/retrieval.py` (weighted keyword search). Tools: `search_concepts`, `get_concept`, `list_bridges`; every hit carries citation IRI + provenance. Reusable by the eval runner.
- ✅ **Eval harness + benchmark** — `eval/` with 53 gold questions (all `grounds` IRIs resolved from the pack), deterministic scoring (accuracy / hallucination / auditability), and a pluggable model adapter (`make eval` = offline mechanism check; `--adapter llm` = live via a user `EVAL_LLM_CMD`, no vendor SDK). **Live value-proof numbers still pending** (needs model choice + question review).
- ✅ **Second use case (KYC / beneficial-ownership)** — 58 core + 4 bridges + pack, via spec-driven `nominate_core`/`bridges` (`curation/usecases/`).
- ✅ **Third use case (Securities instruments & issuance)** — 59 curated core concepts (`curation/securities.json`) + **curated illustrative examples on the cards** (`curation/securities-examples.json`, 59 concepts) + 3 validated cross-domain bridges (`curation/securities-bridges.json`: MBS→mortgage, ABS→loan, issuer→LEI) + pack (`export/securities/`). Map now shows **11 curated bridges**.
- ✅ Published to GitHub (private): `AI-First-Community/Bodhi-Map-For-FinTech`, reproducible via `make fibo`.

**Map UI (E2):** data layer + vendored frontend + FIBO `app.html`/`graph.js` shipped (core-default view, domain/maturity filters, provenance-styled bridges, IRI-citation panel, offline PWA). Needs browser visual verification.

**Not started:** eval corroboration on a 2nd/3rd use case, per-domain lazy loading, further domains/use-cases, EDM contribution.

**Fresh-checkout setup:** `make setup && make fibo && make commons && make all` then `make check`.

---

## Immediate next (in order)

1. ✅ **Wire `core:` into the bundle** — done. `to_okf.py` reads `curation/loan-origination.json`, stamps `core: true` on all 71 concepts + marks them in each `index.md`; `make curate` runs nominate + bridges + rebuild.
2. ✅ **Learner-friendly definition rewrites** — done. `curation/definitions.json` covers the 7 empty-definition core concepts (*mortgage product*, *loan phase*, *consumer credit protection law*, the lifecycle phases/status, *borrower disclosure requirement*); applied as `definition_provenance: curated`, grounded in each class's FIBO superclass. The other 6 thin-but-present defs were left as FIBO's (Rule 1 — don't replace real FIBO text).
3. ✅ **Context-pack export** (the product) — done. `export_pack.py`/`make pack` emit OKF slice + flat JSON + `context.md`; `etl/mcp_server.py` + `etl/retrieval.py` provide the MCP retrieval endpoint.
4. ✅ **Grounded-vs-ungrounded eval** (the value proof) — DONE. gpt-4o-mini: **+39.6pt accuracy lift**, auditability 0%→**98.1%**, hallucination 0% (SPIKE_RESULTS.md). Corroborate with gpt-4o + a 2nd use case (KYC) — pick the model, review the gold questions, run `--adapter llm` (EVAL_LLM_CMD), and write the accuracy/hallucination/auditability numbers into `SPIKE_RESULTS.md`. **Target: ≥15–20pt accuracy lift + 100% auditable.** ◀ **next (needs a user call: model + question review)**

---

## Epics

### E1 — Complete the Loan-Origination MLV (value proof)  ◀ current focus
- [x] Wire `core:` flag from curation into generated bundle (`to_okf.py`)
- [x] `make curate` target (nominate_core + bridges + rebuild)
- [x] Definition-rewrite overlay for thin-def core concepts (curation input + `to_okf` apply)
- [x] `etl/export_pack.py` — grounds_in closure → OKF slice + JSON + `context.md`
- [x] MCP retrieval endpoint (`etl/mcp_server.py` + `etl/retrieval.py`)
- [x] `eval/` harness: benchmark (53 Q), grounded vs ungrounded runner, scorecard (offline; live adapter ready)
- [x] **Ran the live eval** (gpt-4o-mini via OpenAI): **+39.6pt accuracy lift** (45.3% → 84.9%), auditability 0% → **98.1%**, grounded hallucination **0%**. See `SPIKE_RESULTS.md`.
- [x] Wrote up the MLV result in `SPIKE_RESULTS.md` (accuracy +39.6pt, auditability 98.1%, grounded hallucination 0%)

### E2 — The map UI (fork of Bodhi)
- [x] **Data layer** — `scripts/okf.js build` (+ `make map`) + `okf.config.js` generate `js/data.js` from `knowledge/`: 1284 nodes (71 core), 2108 edges (4 curated bridges), every edge provenance-tagged; deterministic. Handles our module-nested paths + inline-object relations (Bodhi's parser could not).
- [x] Vendored Bodhi frontend (Cytoscape.js + fcose libs, `css/style.css`, Manrope fonts, PWA icons/SW/manifest).
- [x] **Faithful Bodhi UI** — `app.html`/`js/graph.js`/`css/style.css` taken from the Bodhi source; FIBO is driven the way Bodhi is designed for, through `okf.config.js` (taxonomy/vocab/flows) + generated `data.js`. **CSS byte-identical**; `graph.js` differs by only ~6 tiny contained edits (core flag, maturity levels, core-default filter, "new"→Core toggle, generated cluster groups). All Bodhi chrome retained: cluster-hull compound nodes, fcose layout, minimap, legend dock, fuzzy search, welcome, theme, deep-linking.
- [x] FIBO adaptations via config: 4 domain clusters; **curated bridges dashed/red by provenance**; **core-default view + Core/full toggle**; maturity filter; detail panel shows FIBO IRI citation + provenance; real flows — a loan-origination decision guide, the underwriting **guided tour**, and mortgage-type / party-role **comparison tables** (all referenced by FIBO IRI, resolved to node ids at build); "for agents" OKF export.
- [x] **Sub-domain clustering** — each domain split one level into its FIBO **modules** as sub-clusters (30 total: FBC→4, FND→15, BE→8, LOAN→3), shaded within the domain hue; canvas shows a hull per sub-domain, legend groups them under the domain (collapsible, counts). Generated in `data.js` (`CLUSTERS` + `CLUSTER_GROUPS`).
- [x] Offline/PWA: **network-first** service worker (fresh when online, cache offline fallback — avoids stale-cache during dev), no CDN (all libs/fonts vendored).
- [ ] Optional: 2-level nesting (domain super-hull around module hulls) if desired
- [ ] Per-domain lazy loading for the full-ontology view (currently one `data.js`; fine at 1.3k, revisit at 5–10k scale)
- [x] **Use-case lens** — toolbar selector focuses one use case's curated subgraph (Loan origination / KYC / Securities); each detail card shows use-case badges (reverse lookup: concept → use cases), clickable to activate the lens. Membership flows from `curation/usecases/*.json` via `use_cases:` frontmatter.

### E3 — Bridges & second use case
- [ ] Decide fate of intra-domain bridges (e.g. `lender played-by financial-institution`) vs cross-domain-only for EDM
- [ ] Map working bridge edge-names → formal FIBO object properties
- [x] **Second use case: KYC / beneficial-ownership** — 58 curated core concepts (`curation/kyc.json`) + 4 cross-domain bridges (`curation/kyc-bridges.json`) + context pack (`export/kyc/`). Backbone party/entity classes come from Commons (CMNS). Tooling is now **spec-driven** (`curation/usecases/*.json`), so a use case is a repeatable recipe.
- [x] **Third use case: Securities instruments & issuance** — 59 core (`curation/securities.json`), curated examples overlay for the cards (`curation/securities-examples.json`), 3 cross-domain bridges (`curation/securities-bridges.json`), pack (`export/securities/`). New `backed-by` relation added for the MBS→mortgage / ABS→loan bridges.
- [ ] Regulatory-reporting use case (BE + FBC + MD) — needs MD domain

### E4 — Scale domains
- [x] **Onboard SEC, DER, IND, MD, BP, CAE** — all six loaded alongside FND/LOAN/FBC/BE + CMNS. Full FIBO now emitted: 3,104 concepts / 6,676 edges / 68 sub-clusters, gate green. Pending (not-yet-loaded) edges fell ~580 → 217 (remaining targets are LCC).
- [x] **Loaded Commons (CMNS)** — `scripts/fetch_commons.sh` fetches the 19 OMG Commons modules FIBO imports (content-negotiated RDF); `extract.py` loads them as CMNS. Resolved ~580 edges: pending links 693 → 114; graph now 1,440 nodes / 3,001 edges. (Commons isn't SHA-pinnable via OMG deref — a reproducibility caveat vs. the fibo pin.)
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
- **Eval agent/model** — benchmark now drafted in-repo (53 Q, `eval/benchmark.json`, grounded in the pack); still open: which model runs the live agent, and SME review of the gold answers before numbers are treated as authoritative.

## Key facts to not re-derive
- FIBO relations are `owl:Restriction` blank-node axioms, not flat triples (extractor handles this).
- `hasMaturityLevel` is per-ontology → propagated to classes.
- OKF types links by body prose, not frontmatter → our `relations:` typing is a private convention (fine for our build; generic OKF consumers see untyped links).
- FIBO has no Production git tags (only `2018Q3`); we pin a commit SHA (`fibo-source.pin`).
- No AI attribution / no employer references anywhere (guard-enforced); author = Sanjeev Azad <sanjeev.azad@gmail.com>.
