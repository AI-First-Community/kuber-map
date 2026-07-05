# A proposal to the EDM Council

### Curated cross-domain bridges and a learner-first grounding layer for FIBO

**To:** EDM Council — FIBO Community of Practice / OKG (Open Knowledge Graph) Innovation Lab

**From:** Sanjeev Azad · <sanjeev.azad@gmail.com> · maintainer, **Kuber Map for FIBO**

**Project:** <https://github.com/AI-First-Community/kuber-map> · **License:** MIT

**Re:** Contributing 19 grounded cross-domain relations back to FIBO, and a demonstrated, measurable case for FIBO as grounding for financial AI

---

## 1. Executive summary

FIBO is the reason this work is possible: an open, rigorous, industry-owned model of financial
concepts. Building on the pinned Production release, I created **Kuber Map** — an open,
MIT-licensed, *learner-first* map of FIBO that also packages FIBO as **audit-ready grounding
context for financial AI agents**.

Two things came out of that work that I would like to offer back to the Council:

1. **A contribution:** **19 curated cross-domain relations** that FIBO does not currently draw —
   each grounded in real FIBO/Commons classes, non-duplicative, and backed by a rationale and an
   external regulation/standard citation. They are packaged for review as a methodology document,
   an RDF/Turtle serialization, and a one-page visual brief.
2. **Evidence:** a **measured demonstration** that grounding a language model in curated FIBO
   context lifts accuracy by **+45.3 points**, takes auditability from **0% to 97%**, and drives
   hallucinated citations to **0%** — a concrete, citable proof of FIBO's value for the AI use
   cases the industry is racing toward.

I am not asking the Council to adopt anything as-is. I am asking you to **review** the relations,
tell me which (if any) are worth drawing in FIBO and how you would prefer each modeled, and — if
they meet your bar — **recognize and accept** the accepted subset through your normal governance.
Everything is open and free to use.

## 2. About the project (context for the contribution)

- **Kuber Map** extracts all ten FIBO domains plus the OMG Commons library — **3,104 concepts,
  deterministically generated** and byte-for-byte reproducible from a pinned commit.
- On top of that it curates **five learner-first use cases** (loan origination, KYC/beneficial
  ownership, securities, regulatory reporting, derivatives) and exports each as a portable
  **context pack** an AI agent can retrieve and **cite** — every concept carries its FIBO IRI, and
  provenance (`fibo` vs `curated`) is never blurred.
- It is an **independent, community project** built on FIBO (© EDM Council / OMG). It is not
  affiliated with, or endorsed by, the EDM Council or OMG — and this proposal seeks to open exactly
  that conversation.

## 3. The contribution — 19 cross-domain relations

**Honest framing first.** FND-mediated linking is FIBO's backbone, so this is *not* a claim that
FIBO lacks cross-domain structure. What these 19 relations are:

- **Lateral, peer-to-peer bridges** that do not route through FND — e.g. a mortgage-backed
  security *backed-by* the mortgages that back it (SEC↔LOAN); a credit default swap *references* a
  bond (DER↔SEC).
- **Entity-resolution links** to the Legal Entity Identifier (ISO 17442) that KYC and reporting
  need — e.g. a reporting party, an issuer, or an account holder *identified-by* its LEI.
- A few **role→entity** and **intra-domain** gaps FIBO leaves implicit — e.g. a lender *played-by*
  a financial institution; a regulatory report *submitted-to* the agency that requires it.

**Why they are safe to review.** Every relation passed an automated grounding gate before
inclusion:

1. **Both endpoints are real FIBO/Commons classes**, resolved against the pinned source — no
   invented IRIs.
2. **FIBO does not already assert the edge** (source→target) — nothing here duplicates FIBO.
3. **Each carries a rationale and an external citation** — a regulation or standard (e.g. SEC
   Regulation AB, ISO 17442, FATF Recommendations 24 & 25, Dodd-Frank Title VII / EU EMIR, ISDA
   Credit Derivatives Definitions) — so the real-world basis is traceable.

**What this deliberately does not do.** It does not assert any FIBO object property. The relations
are expressed in a neutral `kmb:` namespace; identifying the right FIBO/Commons property for each
(or minting one) is the reviewer's call. The intent is to surface the *gap* precisely and let the
working group decide the modeling.

Full detail is in the accompanying files (§7).

## 4. Why this is worth the Council's attention — the measured value

The strategic case for FIBO right now is AI: every financial institution wants language models in
production, and few can trust them there, because a model is fluent but not *grounded* — it
describes a mortgage or a beneficial owner convincingly but approximately, and cannot show a
regulator why it answered.

I measured what grounding in curated FIBO context does about that. The same model answered the same
benchmark **with** the FIBO context pack and **without** it, scored deterministically (no model
grading itself):

| | Ungrounded | Grounded |
|---|---|---|
| **Accuracy** | 47.5% | **92.8%**  (+45.3 pt) |
| **Answers citing a real FIBO IRI** | 0% | **97.0%** |
| **Hallucinated citations** | 55% | **0%** |

Across **263 questions in five financial domains** on `gpt-4o-mini`, corroborated on the stronger
`gpt-4o` — where the lift **held**, which is the point: the value is in the grounding, not the
model. Crucially, the gains depend on **multi-hop, cross-domain paths** — exactly what a curated
bridge layer provides and what naive vector retrieval misses. In other words, **the bridges are not
decoration; they are load-bearing for the value FIBO can demonstrably deliver to AI.**

(Full methodology and per-domain results: `SPIKE_RESULTS.md` in the repository.)

## 5. What I am asking of the Council

1. **Review** the 19 relations for validity and non-duplication.
2. **Guide the modeling** — for any worth drawing, tell me the FIBO/Commons object property you'd
   map each to (or whether to propose a new one).
3. **Recognize and accept** the accepted subset through your normal governance. I will **re-model
   accepted relations as formal `owl:Restriction` axioms in FIBO style** and submit them as a
   DCO-signed pull request, adapting to whatever your CONTRIBUTING process and contributor terms
   require.

## 6. What I am offering the Council

Beyond the relations themselves, I would be glad for this work to be useful to the Council and its
members:

- **An open, citable reference** that FIBO grounding *measurably* improves financial-AI accuracy
  and auditability — a concrete story the Council or its members may choose to point to when
  advising institutions on trustworthy AI. I would welcome co-developing a short, jointly-reviewed
  case study if that is of interest.
- **A learner-first on-ramp to FIBO** — a curated, teachable view that lowers the barrier for
  newcomers, which complements the exhaustive official Viewer rather than competing with it.
- **Ongoing curation** — more use cases and bridges are in progress, all under the same grounding
  discipline, and all offered back.

To be clear, whether and how the Council showcases or references this is entirely your call; I offer
it in the spirit of contribution, and I would be honored if it proved useful in that way.

## 7. Attachments and references

- **`bridge-brief.pdf`** — one-page visual brief: the six strongest relations, diagrammed.
- **`edmc-bridge-contribution.md`** — full proposal: methodology, grounding gate, all 19 with
  source/target IRIs, rationale, and citation.
- **`fibo-bridges.ttl`** — RDF/Turtle serialization (each relation a `kmb:` triple plus an
  `owl:Axiom` carrying rationale, citation, and provenance; parses in rdflib).
- **Repository:** <https://github.com/AI-First-Community/kuber-map> · **Value proof:**
  `SPIKE_RESULTS.md` and the project wiki.

## 8. Governance, licensing, and good faith

The project is **MIT-licensed**; the contribution is offered under terms compatible with FIBO's own
MIT licensing, and I will sign your DCO/CLA as required. I will keep the neutral `kmb:` namespace
until the working group agrees on modeling, assert no unverified FIBO properties, and respect the
Council's review process throughout. FIBO, EDM Council, and OMG are trademarks of their owners; this
is an independent contribution offered for consideration.

Thank you for FIBO, and for considering this. I would welcome a conversation at whatever venue you
think best — the FIBO Community of Practice, the OKG Innovation Lab, or otherwise.

With appreciation,

**Sanjeev Azad**
Maintainer, Kuber Map for FIBO
<sanjeev.azad@gmail.com> · <https://github.com/AI-First-Community/kuber-map>
