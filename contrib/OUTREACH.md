# EDM Council outreach — engaging on the bridge contribution

> **Hand-authored** (not generated). Companion to `edmc-bridge-contribution.md` (the proposal) and
> `fibo-bridges.ttl` (RDF/Turtle). Nothing here is sent automatically — use it when *you* decide to
> engage. Two ready-to-send drafts are below: **(A)** a Community-of-Practice intro note and **(B)** a
> pull-request description for `edmcouncil/fibo`.

## What we're offering, in one paragraph

While building **Kuber Map** — an open, learner-first map of FIBO that doubles as grounding context
for financial AI agents — we surfaced **19 cross-domain relations FIBO does not currently draw**,
each needed to make a real financial use case (loan origination, KYC, securities, regulatory
reporting, derivatives) coherent. Every relation is grounded (both endpoints are real FIBO/Commons
classes), non-duplicative (FIBO doesn't already assert it), and carries a **rationale + an external
regulation/standard citation**. They're expressed in a neutral `kmb:` namespace — we identify the
*gap*; we deliberately do **not** assert unverified FIBO object properties.

## Be honest about what these are (framing)

FND-mediated linking is FIBO's backbone, so "FIBO doesn't link across domains" would be wrong to
claim. What these 19 actually are:

- **Lateral, peer-to-peer bridges** that don't route through FND (e.g. `MortgageBackedSecurity
  —backed-by→ Mortgage` across SEC↔LOAN; `CreditDefaultSwap —references→ Bond` across DER↔SEC).
- **Relations that exist in intent but aren't drawn** — role→entity links FIBO leaves implicit
  (e.g. `Lender —played-by→ FinancialInstitution`), and a few **intra-domain gaps** (e.g.
  `RegulatoryReport —submitted-to→ RegulatoryAgency`).
- **Entity resolution links** to `LegalEntityIdentifier` (ISO 17442) that KYC/reporting need.

Lead with the strongest, least-contestable subset (the securitization and ISO-17442/LEI links are
well-cited) rather than all 19 at once.

## Checklist before you send

- [ ] `make contrib` so `edmc-bridge-contribution.md` + `fibo-bridges.ttl` match the current bundle.
- [ ] Read the **current** `CONTRIBUTING` guide and contributor terms (CLA/DCO) at
      <https://github.com/edmcouncil/fibo> — the governance process is theirs to define; confirm it
      before assuming a mechanism.
- [ ] **Engage the Community of Practice first** (draft A) — these need working-group review and
      re-modeling as formal `owl:Restriction` axioms, not a silent merge.
- [ ] Sign commits with DCO (`git commit -s`) so each carries
      `Signed-off-by: Sanjeev Azad <sanjeev.azad@gmail.com>`.
- [ ] Keep the neutral `kmb:` namespace until reviewers map each edge to a FIBO/Commons property (or
      agree to mint one).

---

## Cover email — to accompany the attachments (shortest; paste-and-send)

> Attach **`edm-council-proposal.pdf`** and **`bridge-brief.pdf`**. Use this when emailing directly;
> use draft A instead when posting to a forum/CoP.

**Subject:** Contribution proposal for FIBO — 19 grounded cross-domain relations + a measured grounding case

Hello,

I maintain **Kuber Map** (<https://github.com/AI-First-Community/kuber-map>), an open, MIT-licensed,
learner-first map of FIBO. While curating five financial use cases on the pinned Production release,
I collected **19 cross-domain relations FIBO doesn't currently draw** — each grounded in real
FIBO/Commons classes, non-duplicative, and backed by a rationale and a regulation/standard citation
— and I'd like to offer them back to the Council for review. Along the way I also measured what
grounding in curated FIBO context does for financial AI (accuracy **+45.3 points**, auditability
**0%→97%**, hallucinated citations **→0%**), which I hope makes a useful, citable case for FIBO.

The **attached proposal** and **one-page brief** have the detail; I'd welcome the working group's
view on which relations are worth drawing and how you'd prefer each modeled, and I'm happy to adapt
to your contribution process. Thank you for FIBO — it's been a pleasure to build on.

Best regards,
Sanjeev Azad · <sanjeev.azad@gmail.com>

---

## A) Intro note — FIBO Community of Practice / EDMConnect / OKG Innovation Lab

> Post to the FIBO CoP (EDMConnect) or email the OKG Innovation Lab. Keep it short; attach the
> one-page **`bridge-brief.pdf`** (the six strongest bridges, diagrammed — dark or `-light` variant)
> and link `edmc-bridge-contribution.md` for the full 19.

**Subject:** Proposed cross-domain relations for FIBO — 19 grounded, cited bridges for review

Hello,

I maintain **Kuber Map** (<https://github.com/AI-First-Community/kuber-map>), an open, MIT-licensed,
learner-first map of FIBO that also packages per-use-case grounding context for financial AI agents.

While curating five use cases on top of the pinned Production source, I repeatedly hit the same kind
of gap: two FIBO (or Commons) classes that a real workflow clearly relates, where FIBO models both
endpoints but doesn't draw the edge — e.g. a mortgage-backed security to the mortgages that back it,
a reporting party to its LEI, a regulatory report to the agency it's submitted to.

I've collected **19 such relations**, each with (1) real FIBO/Commons endpoints, (2) a check that
FIBO doesn't already assert it, and (3) a rationale plus an external regulation/standard citation
(e.g. Reg AB, ISO 17442, FATF R.24/25, Dodd-Frank Title VII / EMIR). They're written in a neutral
`kmb:` namespace — I'm identifying gaps, not asserting FIBO properties.

I'd value the working group's view on two things: **(1)** whether any of these are worth drawing in
FIBO (or already exist somewhere I've missed), and **(2)** for the ones that are, how you'd prefer
each mapped to a FIBO/Commons object property so they can be modeled as proper `owl:Restriction`
axioms. Full proposal (methodology + per-use-case tables) and an RDF/Turtle serialization are in the
repo under `contrib/`.

Is the CoP the right venue for this, or would you point me to another? Happy to adapt the format to
whatever the review process expects.

Thank you for FIBO — it's been a pleasure to build on.

Best regards,
Sanjeev Azad · <sanjeev.azad@gmail.com>

---

## B) Pull-request description — `edmcouncil/fibo`

> Open as a **proposal/discussion** PR (or issue) *after* the CoP conversation, not before. Title
> and body below.

**Title:** Proposal: 19 grounded cross-domain relations for review (`kmb:` namespace, not asserted in FIBO)

**Body:**

### What this proposes
19 cross-domain relations that FIBO does not currently draw, surfaced while building learner-first,
agent-grounding maps of FIBO for five financial use cases (loan origination, KYC & beneficial
ownership, securities, regulatory reporting, derivatives). This is a **proposal for discussion**, not
a request to merge as-is — the relations are expressed in a neutral `kmb:` namespace and would need
the working group to map each to a FIBO/Commons object property before being modeled as
`owl:Restriction` axioms.

### Why it's safe to review
Each relation passed an automated grounding gate before inclusion:
1. **Both endpoints are real FIBO/Commons classes**, resolved against the pinned Production source —
   no invented IRIs.
2. **FIBO does not already assert the edge** (source→target), so nothing here duplicates FIBO.
3. **Each carries a rationale + an external citation** (regulation or standard) so the real-world
   basis is traceable.

### What this deliberately does *not* do
It does not assert any FIBO object property. `kmb:` is a holding namespace; identifying the right
property (or minting one) is the reviewer's call.

### Scope / framing
These are **lateral** relations that don't route through FND, plus a few role→entity and
intra-domain gaps — not a claim that FIBO lacks cross-domain linking (FND-mediated linking is its
backbone). Examples: `MortgageBackedSecurity —backed-by→ Mortgage` (SEC↔LOAN, Reg AB);
`ReportingParty —identified-by→ LegalEntityIdentifier` (FND↔BE, ISO 17442);
`CreditDefaultSwap —references→ Bond` (DER↔SEC, ISDA).

### Files
- `contrib/edmc-bridge-contribution.md` — methodology + all 19 with rationale and citation.
- `contrib/fibo-bridges.ttl` — RDF/Turtle; each bridge a proposed `kmb:` triple + an `owl:Axiom`
  annotation carrying rationale, citation, and provenance (parses in rdflib).

### The ask
Review for (a) validity/duplication and (b) preferred FIBO/Commons property mapping for any worth
drawing. I'll re-model accepted relations as formal `owl:Restriction` axioms in FIBO style.

Signed-off-by: Sanjeev Azad <sanjeev.azad@gmail.com>
