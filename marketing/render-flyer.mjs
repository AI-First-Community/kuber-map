// render-flyer.mjs — render marketing/flyer.html to a print-ready PDF + a preview PNG.
//
// Dev-only, not a repo dependency. One-time setup, then run from the repo root:
//
//   npm install playwright
//   npx playwright install chromium
//   node marketing/render-flyer.mjs
//
// Outputs a dark and a light set: kuber-map-flyer{,-light}.pdf (A4) + .png.

import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.goto('file://' + join(here, 'flyer.html'), { waitUntil: 'load' });
try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch { /* fonts optional */ }
await page.waitForTimeout(700);

async function emit(name) {
  await page.pdf({
    path: join(here, `${name}.pdf`),
    format: 'A4', printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
  });
  const sheet = await page.$('.sheet');
  await sheet.screenshot({ path: join(here, `${name}.png`) });
}

await emit('kuber-map-flyer');                                             // dark (default)
await page.evaluate(() => document.querySelector('.sheet').classList.add('light'));
await page.waitForTimeout(300);
await emit('kuber-map-flyer-light');                                       // light
await browser.close();
console.log('wrote kuber-map-flyer{,-light}.pdf + .png');
