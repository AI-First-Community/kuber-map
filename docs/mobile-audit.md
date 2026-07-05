# Mobile PWA audit (`m.html`)

Consolidated from a four-lens review (UX, visual/responsive/a11y, performance/PWA, content/FIBO-value)
of the mobile UI. The **desktop UI (`app.html`, `graph.js`, `css/style.css`) is out of scope and must
not change.** Every fix below uses data already in `js/data.js`.

## Verdict

The mobile **shell is good** (bottom sheets, offline PWA, 16px search input, safe-areas, tool parity,
FIBO IRI citation surfaced). This is **not a rewrite.** The failures sit in three layers on top of it —
**information architecture, performance/payload, accessibility** — plus the mobile view does not yet
convey the **product's value**.

## P0 — blockers

1. **Wrong default & no curated navigation.** Opens on **all 3,104** concepts grouped by **68 raw FIBO
   clusters**; `n.core` (188 curated) and the **5 use cases** are never read. The value is invisible; the
   overwhelming thing is the default.
2. **Performance: 4.6 MB parsed + 3,104 cards rendered synchronously.** `data.js` = 466 KB gzip / 4.6 MB
   parsed on every load; `render()` builds ~15k DOM nodes in one pass and **re-renders on every
   keystroke** (no debounce; a per-node fallback scans all 6,687 edges).
3. **Accessibility: core content unreachable.** Concept cards and connection rows are **click-only
   `<div>`s** (no keyboard / screen-reader / Switch Control). The three sheets declare `aria-modal` but
   **never move, trap, or restore focus.**
4. **Product value hidden.** The 19 curated **bridges** render like any FIBO edge; **provenance
   (fibo/curated)** is barely shown; the **agent-grounding** story (the #1 value, +45pt eval) is absent.

## P1 — major

5. **Mobile-native gaps:** hardware **Back exits the app** instead of closing a sheet; no back-stack when
   drilling connection→connection; **no per-concept deep-link / share.**
6. **PWA payload:** SW precaches **~2.1 MB a phone never uses** (Cytoscape libs 757 KB + 1.34 MB hero
   image); network-first **re-downloads 466 KB `data.js` every visit**; `start_url: app.html` launches the
   installed app into desktop, then redirects.
7. **Factual error:** FIBO **maturity** (Release/Provisional/Informative) is mislabeled as learning
   **difficulty** ("foundations → advanced").
8. **Reachability:** primary controls in the **top zone**; filter rows **scroll away** (not sticky); 68
   chips in a **hidden-scroll rail** with no affordance.
9. **Responsive/visual:** no **horizontal** safe-area (landscape notch clip); **tap targets < 44px**; **no
   light theme** / no `prefers-color-scheme`.

## P2 — polish

Search ignores synonyms/examples/use-cases; emoji icons clash with the brand; toasts not announced; no
`<h1>`; no font preload; `manrope-500` precached but unused; `theme-color` mismatch; unreliable iOS
body-scroll lock.

## Keep (do not lose)

Bottom-sheet detail with sticky in-sheet header; the **16px search input** (prevents iOS zoom); top/bottom
safe-areas; offline SW + tasteful update banner; the **FIBO IRI citation** in every sheet; **wizard /
Guided Path / Compare** parity; **My Map** personalization; event delegation; strong dark-theme contrast;
and correctly **omitting the graph** on mobile.

## Rebuild plan (phased, desktop-safe)

- **Phase 1 — Reframe the IA** *(highest value, small code, no build change)*: default to the curated
  **core**; make the **5 use cases** the primary chip row; add a **Core ⇄ Full (3,104)** toggle; fix the
  header count; add a **"curated bridge" pill** on connections; **relabel maturity** (R/P/I).
- **Phase 2 — Performance & PWA**: window/paginate the list + debounce search + precompute the superclass
  map; split the SW precache (mobile core vs desktop-on-demand) + cache-first/SWR for static assets; give
  `m.html` its own manifest (`start_url: m.html`); optionally a lite index + lazy detail.
- **Phase 3 — Accessibility & mobile-native**: real focusable controls + focus trap/restore on sheets;
  **hardware-back closes the sheet**; per-concept **deep-link + share**; sticky filters; thumb-zone
  controls; 44px targets; horizontal safe-area; list semantics.
- **Phase 4 — Value & polish**: provenance pills + a **"For agents"** surface with one eval stat; light
  theme; SVG icons; a first-run "what is this" card.
