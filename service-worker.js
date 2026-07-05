/* Kuber Map for FIBO — service worker (offline + installable PWA).
   Precaches a LEAN, mobile-first shell (the desktop-only Cytoscape engine, graph.js and the
   1.3 MB hero image are NOT precached — they runtime-cache on first use if the desktop graph
   is ever opened). Static assets are served stale-while-revalidate (instant from cache, refreshed
   in the background); HTML navigations are network-first. Bump CACHE to invalidate. */
const CACHE = 'kuber-map-v1.11.0';

// Mobile-first shell: the pages, the shared data, the fonts actually used, icons, manifests.
const PRECACHE = [
  './', './index.html', './app.html', './m.html',
  './css/style.css',
  './js/data.js', './js/sw-register.js',
  './manifest.json', './manifest-m.json',
  './images/install-qr.png',
  './icons/icon-192.png', './icons/icon-512.png', './icons/icon-maskable-512.png',
  './fonts/manrope-400.woff2', './fonts/manrope-600.woff2',
  './fonts/manrope-700.woff2', './fonts/manrope-800.woff2'
];
// Desktop-only / heavy assets are deliberately NOT precached (runtime-cached on demand):
//   js/cytoscape.min.js, js/layout-base.js, js/cose-base.js, js/cytoscape-fcose.js,
//   js/graph.js, images/kuber-map.png, fonts/manrope-500.woff2

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(PRECACHE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return; // let cross-origin pass through

  // HTML navigations: network-first so a new build is picked up immediately; fall back to cache
  // (and to the mobile/landing shell) when offline.
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const res = await fetch(req);
        if (res && res.status === 200) { const c = await caches.open(CACHE); c.put(req, res.clone()); }
        return res;
      } catch (err) {
        return (await caches.match(req)) || (await caches.match('./m.html')) || (await caches.match('./index.html'));
      }
    })());
    return;
  }

  // Static assets (data.js, fonts, icons, css, libs, images): stale-while-revalidate.
  // Serve from cache instantly (no re-downloading the 466 KB data.js every visit), and refresh
  // in the background. Freshness across deploys is handled by the versioned CACHE + the
  // "new version available" banner in js/sw-register.js.
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const cached = await cache.match(req);
    const network = fetch(req).then((res) => {
      if (res && res.status === 200 && res.type === 'basic') cache.put(req, res.clone());
      return res;
    }).catch(() => null);
    return cached || (await network) || Response.error();
  })());
});
