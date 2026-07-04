/* ============================================================================
   Bodhi Map for FIBO — Cytoscape renderer.
   Consumes js/data.js globals (CLUSTERS, LEVELS, RELATIONS, PROVENANCE, RELEASE, GRAPH)
   and renders the curated FIBO map: domain-coloured nodes, provenance-styled edges
   (curated cross-domain bridges shown distinctly), a core-default view with a
   "show full ontology" toggle, domain + maturity filters, search, and a detail panel
   that surfaces each concept's FIBO IRI citation + provenance.
   Adapted from Bodhi's js/graph.js (MIT, © Sanjeev Azad). Offline; no external calls.
   ============================================================================ */
(function () {
  'use strict';
  if (typeof GRAPH === 'undefined') return;
  var $ = function (s) { return document.querySelector(s); };
  var byId = Object.fromEntries(GRAPH.nodes.map(function (n) { return [n.id, n]; }));

  // ---- build elements ----------------------------------------------------------------
  var elements = [];
  GRAPH.nodes.forEach(function (n) {
    elements.push({ data: {
      id: n.id, label: n.label, cluster: n.cluster, level: n.level,
      maturity: n.maturity || 'n/a', core: !!n.core, summary: n.summary || '',
      color: (CLUSTERS[n.cluster] || {}).color || '#94a3b8',
    } });
  });
  GRAPH.edges.forEach(function (e, i) {
    elements.push({ data: {
      id: 'e' + i, source: e.s, target: e.t, r: e.r,
      provenance: e.provenance, bridge: !!e.bridge,
      color: e.bridge ? (PROVENANCE.curated.color)
        : ((RELATIONS[e.r] || {}).color || PROVENANCE.fibo.color),
      style: e.bridge ? 'dashed' : ((RELATIONS[e.r] || {}).style || 'solid'),
    } });
  });

  // ---- cytoscape ---------------------------------------------------------------------
  var cy = cytoscape({
    container: $('#cy'),
    elements: elements,
    minZoom: 0.05, maxZoom: 3, wheelSensitivity: 0.25,
    style: [
      { selector: 'node', style: {
        'background-color': 'data(color)', 'width': 18, 'height': 18,
        'border-width': 0, 'font-size': 9, 'color': '#cbd5e1',
        'text-wrap': 'wrap', 'text-max-width': 120, 'min-zoomed-font-size': 8,
        'label': '' } },
      { selector: 'node[?core]', style: {
        'width': 30, 'height': 30, 'border-width': 2, 'border-color': '#f8fafc',
        'label': 'data(label)', 'font-weight': 600 } },
      { selector: 'node:selected', style: {
        'border-width': 3, 'border-color': '#38bdf8', 'label': 'data(label)' } },
      { selector: 'edge', style: {
        'width': 1, 'line-color': 'data(color)', 'target-arrow-color': 'data(color)',
        'target-arrow-shape': 'triangle', 'arrow-scale': 0.6, 'curve-style': 'bezier',
        'line-style': 'data(style)', 'opacity': 0.5 } },
      { selector: 'edge[?bridge]', style: {
        'width': 2.4, 'opacity': 0.95, 'target-arrow-shape': 'triangle', 'z-index': 20 } },
      { selector: '.faded', style: { 'opacity': 0.07 } },
      { selector: '.faded-edge', style: { 'opacity': 0.04 } },
      { selector: '.hl', style: { 'opacity': 1 } },
      { selector: '.hidden', style: { 'display': 'none' } },
    ],
  });

  var HAS_FCOSE = typeof cy.layout === 'function' && !!(window.cytoscapeFcose || true);
  function layoutOpts() {
    try { return { name: 'fcose', quality: 'default', animate: false, randomize: true,
      nodeSeparation: 80, idealEdgeLength: 90, nodeRepulsion: 6000 }; }
    catch (e) { return { name: 'cose', animate: false }; }
  }
  function runLayout() {
    var visible = cy.elements(':visible');
    (visible.length ? visible : cy.elements()).layout(layoutOpts()).run();
    cy.fit(cy.elements(':visible'), 50);
  }

  // ---- filters (domain, maturity, core-only) -----------------------------------------
  var activeClusters = new Set(Object.keys(CLUSTERS));
  var activeLevels = new Set(Object.keys(LEVELS).map(Number));
  var coreOnly = true;

  function nodeVisible(n) {
    if (coreOnly && !n.data('core')) return false;
    if (!activeClusters.has(n.data('cluster'))) return false;
    if (!activeLevels.has(n.data('level'))) return false;
    return true;
  }
  function applyFilters() {
    cy.batch(function () {
      cy.nodes().forEach(function (n) { n.toggleClass('hidden', !nodeVisible(n)); });
      cy.edges().forEach(function (e) {
        e.toggleClass('hidden', e.source().hasClass('hidden') || e.target().hasClass('hidden'));
      });
    });
  }

  // ---- detail panel ------------------------------------------------------------------
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  function relationsHtml(id) {
    var out = [];
    GRAPH.edges.forEach(function (e) {
      var other, dir;
      if (e.s === id) { other = e.t; dir = '→'; } else if (e.t === id) { other = e.s; dir = '←'; } else return;
      var tn = byId[other]; if (!tn) return;
      var lbl = (RELATIONS[e.r] || {}).label || e.r;
      var tag = e.bridge ? ' <span class="prov prov-curated">curated bridge</span>' : '';
      out.push('<li>' + dir + ' <b>' + esc(lbl) + '</b> ' + esc(tn.label) + tag + '</li>');
    });
    return out.length ? '<ul class="rel-list">' + out.join('') + '</ul>' : '<p class="muted">No in-bundle relations.</p>';
  }
  function showNode(id) {
    var n = byId[id]; if (!n) return;
    var c = CLUSTERS[n.cluster] || {};
    var defProv = n.definitionProvenance === 'curated'
      ? ' <span class="prov prov-curated">curated definition</span>' : '';
    var panel = $('#panel');
    panel.innerHTML =
      '<button class="panel-close" aria-label="Close">✕</button>' +
      '<div class="panel-tag" style="--c:' + (c.color || '#888') + '">' + esc(c.label || n.cluster) +
        ' · ' + esc(n.maturity || 'n/a') + (n.core ? ' · core' : '') + '</div>' +
      '<h2>' + esc(n.label) + '</h2>' +
      '<p class="panel-def">' + esc(n.summary || n.detail || '(no definition)') + defProv + '</p>' +
      (n.resource ? '<p class="panel-cite"><span>cite:</span> <a href="' + esc(n.resource) +
        '" target="_blank" rel="noopener">' + esc(n.resource) + '</a></p>' : '') +
      '<h3>Relationships</h3>' + relationsHtml(id);
    panel.classList.add('open');
    panel.querySelector('.panel-close').addEventListener('click', closePanel);
    highlight(id);
  }
  function closePanel() { $('#panel').classList.remove('open'); clearHighlight(); }

  function highlight(id) {
    clearHighlight();
    var node = cy.getElementById(id);
    var hood = node.closedNeighborhood();
    cy.elements(':visible').not(hood).addClass('faded');
    cy.edges(':visible').not(hood.edges()).addClass('faded-edge');
    hood.addClass('hl');
  }
  function clearHighlight() { cy.elements().removeClass('faded faded-edge hl'); }

  cy.on('tap', 'node', function (evt) { showNode(evt.target.id()); });
  cy.on('tap', function (evt) { if (evt.target === cy) closePanel(); });

  // ---- search ------------------------------------------------------------------------
  var searchInput = $('#search'), searchResults = $('#searchResults');
  function renderSearch() {
    var q = (searchInput.value || '').trim().toLowerCase();
    if (!q) { searchResults.innerHTML = ''; searchResults.classList.remove('open'); return; }
    var hits = GRAPH.nodes.filter(function (n) { return n.label.toLowerCase().indexOf(q) !== -1; })
      .sort(function (a, b) { return (b.core ? 1 : 0) - (a.core ? 1 : 0) || a.label.length - b.label.length; })
      .slice(0, 12);
    searchResults.innerHTML = hits.map(function (n) {
      return '<div class="sr" data-id="' + n.id + '"><b>' + esc(n.label) + '</b><span>' +
        esc((CLUSTERS[n.cluster] || {}).label || n.cluster) + '</span></div>'; }).join('');
    searchResults.classList.toggle('open', hits.length > 0);
    Array.prototype.forEach.call(searchResults.querySelectorAll('.sr'), function (el) {
      el.addEventListener('click', function () { selectSearch(el.getAttribute('data-id')); });
    });
  }
  function selectSearch(id) {
    var n = byId[id]; if (!n) return;
    if (coreOnly && !n.core) { coreOnly = false; syncCoreBtn(); applyFilters(); }
    activeClusters.add(n.cluster); activeLevels.add(n.level);
    searchResults.classList.remove('open'); searchInput.value = '';
    var node = cy.getElementById(id);
    cy.animate({ center: { eles: node }, zoom: 1.2 }, { duration: 320 });
    showNode(id);
  }
  if (searchInput) searchInput.addEventListener('input', renderSearch);

  // ---- legends -----------------------------------------------------------------------
  function buildLegend() {
    var legend = $('#legend');
    if (legend) legend.innerHTML = Object.keys(CLUSTERS).map(function (k) {
      var c = CLUSTERS[k];
      return '<button class="leg-item active" data-cluster="' + k + '">' +
        '<span class="dot" style="background:' + c.color + '"></span>' + esc(c.label) + '</button>';
    }).join('');
    if (legend) Array.prototype.forEach.call(legend.querySelectorAll('.leg-item'), function (el) {
      el.addEventListener('click', function () {
        var k = el.getAttribute('data-cluster');
        if (activeClusters.has(k)) { activeClusters.delete(k); el.classList.remove('active'); }
        else { activeClusters.add(k); el.classList.add('active'); }
        applyFilters();
      });
    });
    var rel = $('#relLegend');
    if (rel) rel.innerHTML =
      '<div class="leg-row"><span class="line" style="background:' + PROVENANCE.fibo.color + '"></span>FIBO relation</div>' +
      '<div class="leg-row"><span class="line dashed" style="background:' + PROVENANCE.curated.color + '"></span>curated bridge</div>';
  }

  // ---- maturity chips + core toggle --------------------------------------------------
  function wireChips() {
    Array.prototype.forEach.call(document.querySelectorAll('.level-chip'), function (chip) {
      chip.addEventListener('click', function () {
        var lv = Number(chip.getAttribute('data-level'));
        if (activeLevels.has(lv)) { activeLevels.delete(lv); chip.classList.remove('active'); }
        else { activeLevels.add(lv); chip.classList.add('active'); }
        applyFilters();
      });
    });
  }
  var coreBtn = $('#coreToggle');
  function syncCoreBtn() { if (coreBtn) coreBtn.textContent = coreOnly ? 'Show full ontology' : 'Show core only'; }
  if (coreBtn) coreBtn.addEventListener('click', function () {
    coreOnly = !coreOnly; syncCoreBtn(); applyFilters(); runLayout();
  });

  // ---- toolbar -----------------------------------------------------------------------
  if ($('#fitBtn')) $('#fitBtn').addEventListener('click', function () { cy.fit(cy.elements(':visible'), 50); });
  if ($('#relayoutBtn')) $('#relayoutBtn').addEventListener('click', runLayout);
  var themeToggle = $('#themeToggle');
  if (themeToggle) themeToggle.addEventListener('click', function () {
    var cur = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', cur);
    try { localStorage.setItem('bodhi-theme', cur); } catch (e) {}
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'f' && document.activeElement !== searchInput) { e.preventDefault(); if (searchInput) searchInput.focus(); }
    if (e.key === 'Escape') closePanel();
  });

  // ---- init --------------------------------------------------------------------------
  buildLegend(); wireChips(); syncCoreBtn(); applyFilters(); runLayout();
  var stat = $('#stat');
  if (stat) stat.textContent = GRAPH.nodes.length + ' concepts · ' +
    GRAPH.nodes.filter(function (n) { return n.core; }).length + ' core · ' +
    GRAPH.edges.filter(function (e) { return e.bridge; }).length + ' curated bridges';
})();
