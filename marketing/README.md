# Marketing kit

Launch collateral for Kuber Map. Audience: **FinTech leaders** and the teams building their AI —
so the copy leads with *auditable, grounded, standards-based*, and every number is the measured
result from [`../SPIKE_RESULTS.md`](../SPIKE_RESULTS.md), not a claim.

## What's here

| File | Use |
|---|---|
| `flyer.html` | Source of the one-page flyer — theme-aware (dark default; add `.light` on `.sheet`). |
| `kuber-map-flyer.pdf` / `.png` | **Dark** A4 flyer — print/share-ready + image for posts and slides. |
| `kuber-map-flyer-light.pdf` / `.png` | **Light** A4 flyer — for light decks, print, and light-mode feeds. |
| `render-flyer.mjs` | Regenerate both themes (PDF + PNG) from `flyer.html` (see its header). |
| `launch-linkedin.md` | LinkedIn launch post (business tone). |
| `launch-x-thread.md` | X / Twitter thread (8 tweets). |
| `launch-show-hn.md` | Show HN post + r/fintech and r/MachineLearning variants (candid, technical). |
| `launch-announcement.md` | Long-form announcement / blog / Discussions post. |

## The message (keep it consistent)

- **The problem:** LLMs are fluent but not grounded; in finance, approximately-right is wrong — the
  kind of wrong that passes a demo and fails an audit.
- **The answer:** grounding in FIBO (the industry's open standard), not a bigger model.
- **The proof:** +45.3pt accuracy · 97% auditable · 0% hallucinated citations — 263 questions across
  5 use cases on gpt-4o-mini, corroborated on gpt-4o, scored deterministically.
- **The ask:** try the live app; contribute a use case or a bridge.

Always pair claims with the "measured, not claimed" framing, and keep the EDM Council / OMG
trademark disclaimer when space allows (it's on the flyer and in the announcement).

## Brand quick-reference

- **Wordmark:** Kuber Map · tagline "the treasury of financial knowledge" (named for Kubera, the
  treasurer / god of wealth).
- **Palette:** deep green `#0a1410` (bg) · accent green `#4fe08a` · gold `#f3c969` · ink `#eaf3ee`.
- **Type:** Manrope (vendored in `../fonts/`).
- **Emblem:** `../images/kuber-map.png`. **QR to the app:** `../images/install-qr.png`.
- **Maker byline:** "Innovate With **Sanjeev**" with a green→gold spark mark, in the flyer footer.
  Both a dark and a light flyer set are provided — use whichever suits the channel/background.

## Assets to attach

- Flyer: `kuber-map-flyer.png`.
- Demos: `../images/demo-explore.gif` (hero), `../images/demo-agents.gif` (the grounding value),
  `../images/demo-mobile.gif` (the app). See the README for the rest.

## Links (use everywhere)

- Live app: <https://ai-first-community.github.io/kuber-map/>
- Repo: <https://github.com/AI-First-Community/kuber-map>
- Contribute: <https://github.com/AI-First-Community/kuber-map/contribute>
