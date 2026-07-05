// record-demos.mjs — regenerate the README demo GIFs from the *running* app.
//
// The GIFs in images/demo-*.gif are captured, never hand-made: this script drives
// the real app in a headless browser, screenshots a scripted interaction frame by
// frame, downscales, and encodes an animated GIF. Re-run it after a UI change so the
// demos never drift from reality.
//
// This is a dev-only tool and deliberately NOT a repo dependency (the project keeps
// its JS deps minimal). Install the three packages ad hoc, serve the repo, then run:
//
//   npm install playwright gifenc pngjs      # one-time; downloads a headless Chromium
//   npx playwright install chromium
//   python3 -m http.server 8099              # serve the repo root (separate terminal)
//   node scripts/record-demos.mjs            # writes images/demo-*.gif
//
// Options: BASE=http://localhost:8099 (server URL), OUT=images (output dir).

import { chromium } from 'playwright';
import { mkdirSync, rmSync, readdirSync, writeFileSync, readFileSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { PNG } from 'pngjs';
import { GIFEncoder, quantize, applyPalette } from 'gifenc';

const BASE = process.env.BASE || 'http://localhost:8099';
const OUT = process.env.OUT || 'images';
const FRAME_MS = 110; // capture cadence ≈ 9 fps; also the GIF frame delay
const TMP = join(tmpdir(), 'kuber-demo-frames');

// Bilinear downscale of an RGBA buffer — keeps text crisp at GIF widths.
function resize(src, sw, sh, dw, dh) {
  const d = new Uint8Array(dw * dh * 4);
  for (let y = 0; y < dh; y++) {
    const sy = (y + 0.5) * sh / dh - 0.5, y0 = Math.max(0, Math.floor(sy)), y1 = Math.min(sh - 1, y0 + 1), fy = sy - y0;
    for (let x = 0; x < dw; x++) {
      const sx = (x + 0.5) * sw / dw - 0.5, x0 = Math.max(0, Math.floor(sx)), x1 = Math.min(sw - 1, x0 + 1), fx = sx - x0;
      const a = (y0 * sw + x0) * 4, b = (y0 * sw + x1) * 4, c = (y1 * sw + x0) * 4, e = (y1 * sw + x1) * 4, di = (y * dw + x) * 4;
      for (let k = 0; k < 4; k++) {
        const t = src[a + k] * (1 - fx) + src[b + k] * fx, u = src[c + k] * (1 - fx) + src[e + k] * fx;
        d[di + k] = (t * (1 - fy) + u * fy) | 0;
      }
    }
  }
  return d;
}

// Encode a directory of PNG frames into one looping GIF with a single global palette
// (smaller file, no inter-frame flicker). The last frame is held before the loop.
function encodeGif(dir, out, dw, colors) {
  const files = readdirSync(dir).filter((f) => f.endsWith('.png')).sort();
  const frames = [];
  let dh = 0;
  for (const f of files) {
    const png = PNG.sync.read(readFileSync(join(dir, f)));
    dh = Math.round(png.height * dw / png.width);
    frames.push(resize(png.data, png.width, png.height, dw, dh));
  }
  // Global palette sampled from every 4th frame.
  const sample = [];
  frames.forEach((fr, i) => { if (i % 4 === 0) sample.push(fr); });
  const merged = new Uint8Array(sample.reduce((s, fr) => s + fr.length, 0));
  let o = 0; sample.forEach((fr) => { merged.set(fr, o); o += fr.length; });
  const pal = quantize(merged, colors, { format: 'rgb444' });
  const gif = GIFEncoder();
  frames.forEach((fr, i) => {
    gif.writeFrame(applyPalette(fr, pal, 'rgb444'), dw, dh, {
      palette: i === 0 ? pal : undefined,
      delay: i === frames.length - 1 ? 1500 : FRAME_MS,
    });
  });
  gif.finish();
  writeFileSync(out, gif.bytes());
  return (statSync(out).size / 1024).toFixed(0);
}

const browser = await chromium.launch({ headless: true });

async function scene(name, { w, h, url, init, outW, colors = 128, steps }) {
  const dir = join(TMP, name);
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  if (init) await ctx.addInitScript(init);
  const page = await ctx.newPage();
  let n = 0;
  const shoot = async () => { n++; await page.screenshot({ path: join(dir, `f-${String(n).padStart(4, '0')}.png`) }); };
  const hold = async (ms) => { const k = Math.max(1, Math.round(ms / FRAME_MS)); for (let i = 0; i < k; i++) { await shoot(); await page.waitForTimeout(FRAME_MS); } };
  const tryClick = async (sel) => { const el = page.locator(sel).first(); if (await el.count()) { try { await el.click({ timeout: 2500 }); return true; } catch { /* optional */ } } return false; };
  try {
    await page.goto(BASE + url, { waitUntil: 'networkidle', timeout: 30000 });
    await steps({ page, shoot, hold, tryClick });
    const kb = encodeGif(dir, join(OUT, `${name}.gif`), outW, colors);
    console.log(`OK   ${name.padEnd(14)} ${n} frames -> ${kb} KB`);
  } catch (e) {
    console.log(`FAIL ${name}: ${String(e.message).split('\n')[0]}`);
  }
  await ctx.close();
}

// Desktop scenes preseed localStorage so the welcome modal / theme are deterministic.
const DESK = { w: 1280, h: 800, init: () => { localStorage.setItem('kuber-welcomed', '1'); localStorage.setItem('kuber-theme', 'dark'); } };
const graphReady = async (page) => { await page.waitForSelector('#cy canvas', { timeout: 20000 }); await page.waitForTimeout(2600); };

await scene('demo-explore', { ...DESK, url: '/app.html', outW: 880, colors: 144, steps: async ({ page, hold, tryClick }) => {
  await graphReady(page); await hold(900);
  await page.click('#search'); await page.type('#search', 'loan', { delay: 120 }); await hold(800);
  await tryClick('.sr-item[data-goto]'); await hold(2400);
  try { await page.selectOption('#lens', { index: 1 }); } catch { /* lens optional */ } await hold(2200);
} });

await scene('demo-wizard', { ...DESK, url: '/app.html', outW: 800, steps: async ({ page, hold, tryClick }) => {
  await graphReady(page); await hold(700);
  await tryClick('#startDecision'); await hold(1400);
  await tryClick('.fb-answer'); await hold(1500);
  await tryClick('.fb-answer'); await hold(2000);
} });

await scene('demo-guided', { ...DESK, url: '/app.html', outW: 860, steps: async ({ page, hold, tryClick }) => {
  await graphReady(page); await hold(700);
  await tryClick('#startPath'); await hold(2000);
  await tryClick('#guidedBox a[data-goto], #guidedBox button'); await hold(2200);
} });

await scene('demo-compare', { ...DESK, url: '/app.html', outW: 860, steps: async ({ page, hold, tryClick }) => {
  await graphReady(page); await hold(700);
  await tryClick('#compareBtn'); await hold(1800);
  await tryClick('.cmp-tab[data-i="1"]'); await hold(1800);
} });

const MOB = { w: 390, h: 844 };
await scene('demo-mobile', { ...MOB, url: '/m.html', outW: 300, init: () => { localStorage.setItem('kuber-theme', 'dark'); }, steps: async ({ page, hold, tryClick }) => {
  await hold(1700);
  await tryClick('#introGo'); await hold(800);
  await tryClick('#chips .chip >> nth=2'); await hold(1300);
  await tryClick('.card[data-id]'); await hold(2400);
  await page.keyboard.press('Escape'); await hold(800);
  await tryClick('#themeToggle'); await hold(1500);
} });

await scene('demo-agents', { ...MOB, url: '/m.html', outW: 300, init: () => { localStorage.setItem('kuber-welcomed', '1'); localStorage.setItem('kuber-theme', 'dark'); }, steps: async ({ page, hold, tryClick }) => {
  await hold(900);
  await tryClick('#mAgents'); await hold(2800);
} });

await browser.close();
console.log('done — GIFs written to', OUT);
