/* ============================================================================
   Bodhi Map for FIBO — controlled vocabulary + presentation config (Node + browser).
   The OKF bundle under knowledge/ holds the concepts (nodes) and their typed,
   provenance-tagged relations (edges); this file holds the clusters (FIBO domains),
   relation styling, maturity levels, and release. scripts/okf.js inlines it into the
   generated js/data.js. Adapted from Bodhi's okf.config.js (MIT, © Sanjeev Azad).
   ============================================================================ */
(function (root, factory) {
  const o = factory();
  if (typeof module === 'object' && module.exports) module.exports = o;      // Node (scripts/okf.js)
  else {                                                                       // browser
    root.CLUSTERS = o.CLUSTERS; root.RELATIONS = o.RELATIONS; root.LEVELS = o.LEVELS;
    root.RELEASE = o.RELEASE; root.PROVENANCE = o.PROVENANCE;
  }
})(typeof self !== 'undefined' ? self : this, function () {

  const RELEASE = { version: '0.1.0', label: 'v0.1.0' };

  // Clusters = FIBO domains emitted in the bundle. Keys MUST match the `cluster` value
  // stamped on each node (the domain code). Colors are distinct per domain.
  const CLUSTERS = {
    FND:  { label: 'Foundations (FND)',        color: '#3b82f6' },
    LOAN: { label: 'Loans (LOAN)',             color: '#10b981' },
    FBC:  { label: 'Business & Commerce (FBC)', color: '#f59e0b' },
    BE:   { label: 'Business Entities (BE)',   color: '#8b5cf6' },
  };

  // Maturity, propagated per class, reused as Bodhi's "level" filter dimension.
  const LEVELS = { 1: 'Release', 2: 'Provisional', 3: 'Informative' };
  const MATURITY_LEVEL = { Release: 1, Provisional: 2, Informative: 3 };

  // Provenance drives edge styling: FIBO-extracted vs our curated cross-domain bridges
  // (the moat — rendered distinctly).
  const PROVENANCE = {
    fibo:    { label: 'FIBO',    color: '#64748b', style: 'solid' },
    curated: { label: 'curated bridge', color: '#e11d48', style: 'dashed' },
  };

  // Relation styling for the most frequent FIBO object properties; unknown types fall
  // back to their kebab name and a neutral style in the UI. is-a is the taxonomic spine.
  const RELATIONS = {
    'is-a':            { label: 'is a type of',    color: '#64748b', style: 'solid' },
    'is-classified-by':{ label: 'is classified by', color: '#0ea5e9', style: 'solid' },
    'comprises':       { label: 'comprises',       color: '#14b8a6', style: 'solid' },
    'identifies':      { label: 'identifies',      color: '#06b6d4', style: 'solid' },
    'is-identified-by':{ label: 'is identified by', color: '#06b6d4', style: 'solid' },
    'applies-to':      { label: 'applies to',      color: '#a78bfa', style: 'dotted' },
    'is-played-by':    { label: 'is played by',    color: '#f97316', style: 'solid' },
    'has-party-role':  { label: 'has party role',  color: '#f97316', style: 'solid' },
    'governs':         { label: 'governs',         color: '#ef4444', style: 'solid' },
    'is-governed-by':  { label: 'is governed by',  color: '#ef4444', style: 'solid' },
    // curated bridge edge-names (provenance: curated) — surfaced distinctly
    'reported-in':     { label: 'reported in',     color: '#e11d48', style: 'dashed' },
    'filed-by':        { label: 'filed by',        color: '#e11d48', style: 'dashed' },
    'played-by':       { label: 'played by',       color: '#e11d48', style: 'dashed' },
  };

  return { RELEASE, CLUSTERS, LEVELS, MATURITY_LEVEL, PROVENANCE, RELATIONS };
});
