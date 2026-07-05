// render-ebook.mjs — render marketing/ebook.html to a LinkedIn-ready PDF (+ a cover PNG).
//
// Dev-only, not a repo dependency. One-time setup, then run from the repo root:
//
//   npm install playwright
//   npx playwright install chromium
//   node marketing/render-ebook.mjs
//
// Output: marketing/kuber-map-ebook.pdf        (dark, 20 × 1080×1350 pages — a 4:5 LinkedIn document)
//         marketing/kuber-map-ebook-light.pdf  (light variant)
//         marketing/kuber-map-ebook-cover.png  (the dark cover, for the post's lead image)

import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.goto('file://' + join(here, 'ebook.html'), { waitUntil: 'load' });
try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch { /* fonts optional */ }
await page.waitForTimeout(700);
const n = await page.locator('.page').count();

async function emitPdf(name) {
  await page.pdf({ path: join(here, name), width: '1080px', height: '1350px', printBackground: true, pageRanges: `1-${n}` });
}

await emitPdf('kuber-map-ebook.pdf');                                            // dark (default)
await page.locator('.page').first().screenshot({ path: join(here, 'kuber-map-ebook-cover.png') });
await page.evaluate(() => document.querySelector('.book').classList.add('light'));
await page.waitForTimeout(300);
await emitPdf('kuber-map-ebook-light.pdf');                                      // light
await browser.close();
console.log(`wrote kuber-map-ebook{,-light}.pdf (${n} pages) + kuber-map-ebook-cover.png`);
