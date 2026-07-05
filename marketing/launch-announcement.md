# Launch announcement / blog post

> Long-form. Usable as a blog, a Medium/Substack piece, a company post, or a GitHub Discussions
> announcement. Audience: FinTech leaders and the teams building their AI. ~800 words.

---

## Kuber Map: grounding financial AI in the industry's own language

Every FinTech leader I talk to has run the same experiment. They put a large language model in front
of a financial task — summarize this loan file, flag KYC risk, draft a regulatory report — and the
demo is dazzling. Then someone asks the only question that matters in a regulated business: *how do
we know it's right, and can we prove it?* The room goes quiet, and the pilot never ships.

This is the gap between "we tried GenAI" and "we run on it." And it is not a gap you close with a
bigger model.

### Fluent is not the same as grounded

A language model is fluent but not grounded. It will describe a mortgage, a beneficial owner, or a
credit risk assessment convincingly — but *approximately*. It has read a great deal about finance;
it has been taught the precise, shared definitions the industry actually operates on by no one. In
most domains, approximately-right is good enough. In finance, approximately-right is wrong, and it is
the specific kind of wrong that survives a demo and collapses under an audit.

The industry already solved the definitions problem. **FIBO** — the Financial Industry Business
Ontology, maintained by the EDM Council — is a formal, open standard for exactly these concepts and
how they relate. The catch is that FIBO is built for modelers: it's an exhaustive OWL ontology, not
something you hand to an AI agent or a new analyst. The knowledge is there; the usability isn't.

### What Kuber Map does

**Kuber Map** reshapes FIBO into three things it isn't out of the box:

1. **A teachable map.** A hand-curated, learner-first "core" view — the concepts that matter for a
   real task, framed to be understood — instead of the full ontology rendered for experts.
2. **A cross-domain bridge layer.** FIBO's domains are governed separately, so some real-world links
   aren't drawn. We add them, tag them as our curation with a rationale and citation, and offer them
   back to the EDM Council.
3. **Grounding for agents.** Each use case is exported as a portable **context pack** — structured
   records for retrieval, a prompt-injection document, and a self-contained data slice — plus an MCP
   endpoint an agent can call. Every concept carries its FIBO IRI, so every answer can cite its
   source.

Crucially, provenance is never blurred: everything is labeled either `fibo` (extracted from the
standard) or `curated` (added by a human). That single discipline is what makes an answer auditable
— you can always show a reviewer, or a regulator, exactly where a claim came from and whether it's
the standard talking or us.

### The proof, measured

Grounding is easy to *assert*. We measured it. We asked the same model the same benchmark questions
twice — once with the curated FIBO context pack, once without — and scored the answers
deterministically, with string and IRI checks rather than another model grading the first.

- **Accuracy rose 45 points**, from 47.5% to 92.8%.
- **Auditable answers** — ones that cite a real FIBO IRI — went from **0% to 97%**.
- **Hallucinated citations** fell from **55% to 0%**.

That's across 263 questions and five use cases (loan origination, KYC and beneficial ownership,
securities, regulatory reporting, and derivatives) on gpt-4o-mini, corroborated on a stronger model
(gpt-4o, 157 questions across three of them). The most important result is the
one that's easy to miss: the lift **held on the stronger model**. The bigger model did not close the
gap. Grounding does something scale doesn't.

### Open, free, and built to contribute to

Kuber Map is MIT-licensed and runs entirely in your browser — there's no backend, no signup, and
nothing to buy. You can try the live app, install it as a desktop or mobile app, and use it offline.
The context packs and the retrieval server are in the repository, ready to drop into a RAG pipeline
or an agent.

It's also built to be improved by the community. The highest-leverage contribution — adding a new
use case — is spec-driven: a single JSON file, no code, with the tooling verifying every concept
against real FIBO. Payments, insurance, and ESG reporting are the obvious next ones, and they're
open.

- **Try it:** https://ai-first-community.github.io/kuber-map/
- **Source, docs, and good first issues:** https://github.com/AI-First-Community/kuber-map

If your team is trying to move AI from a promising demo to something you can put in front of a
regulator, I'd genuinely like your feedback — and your pull requests.

*Kuber Map is an independent, community project built on FIBO (© EDM Council / OMG). It is not
affiliated with or endorsed by the EDM Council or OMG.*
