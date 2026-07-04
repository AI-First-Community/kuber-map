/* Bodhi Map for FIBO — service worker (offline + installable PWA).
   Precaches the app shell so the map works offline after install; runtime-caches
   everything else same-origin (cache-first). Bump CACHE to invalidate. */
const CACHE = 'bodhi-fibo-v0.6.0';
const PRECACHE = [
  './', './index.html', './app.html',
  './css/style.css',
  './js/cytoscape.min.js', './js/layout-base.js', './js/cose-base.js', './js/cytoscape-fcose.js',
  './js/data.js', './js/graph.js', './js/sw-register.js',
  './manifest.json',
  './images/bodhi-fibo.png',
  './icons/icon-192.png', './icons/icon-512.png', './icons/icon-maskable-512.png',
  './fonts/manrope-400.woff2', './fonts/manrope-500.woff2', './fonts/manrope-600.woff2',
  './fonts/manrope-700.woff2', './fonts/manrope-800.woff2'
];

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
  // Network-first: always serve the freshest build when online (this map is under active
  // development, so a stale cache must never win); fall back to the cache when offline.
  event.respondWith((async () => {
    try {
      const res = await fetch(req);
      if (res && res.status === 200 && res.type === 'basic') {
        const cache = await caches.open(CACHE);
        cache.put(req, res.clone());
      }
      return res;
    } catch (err) {
      const cached = await caches.match(req);
      if (cached) return cached;
      if (req.mode === 'navigate') return (await caches.match('./index.html')) || (await caches.match('./app.html'));
      throw err;
    }
  })());
});
