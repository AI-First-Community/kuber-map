// render-proposal.mjs — render contrib/edm-council-proposal.md to a professional PDF.
//
// Single-sourced from the markdown (edit the .md; the PDF is generated). Dev-only.
// Requires pandoc (markdown -> html) and playwright (html -> pdf). One-time setup:
//
//   brew install pandoc            # or your OS package manager
//   npm install playwright && npx playwright install chromium
//   node contrib/render-proposal.mjs
//
// Output: contrib/edm-council-proposal.pdf

import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { writeFileSync, unlinkSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { tmpdir } from 'node:os';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const asset = (p) => 'file://' + join(root, p);

// 1) markdown -> html fragment (pandoc)
const body = execFileSync('pandoc', [join(here, 'edm-council-proposal.md'), '-f', 'markdown', '-t', 'html5'], { encoding: 'utf8' });

// 2) wrap in a restrained, document-grade print template
const html = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>EDM Council proposal</title>
<style>
@font-face{font-family:'Manrope';font-weight:400;src:url('${asset('fonts/manrope-400.woff2')}') format('woff2');}
@font-face{font-family:'Manrope';font-weight:600;src:url('${asset('fonts/manrope-600.woff2')}') format('woff2');}
@font-face{font-family:'Manrope';font-weight:700;src:url('${asset('fonts/manrope-700.woff2')}') format('woff2');}
@font-face{font-family:'Manrope';font-weight:800;src:url('${asset('fonts/manrope-800.woff2')}') format('woff2');}
:root{--green:#1f7a44;--ink:#1a2620;--muted:#4c6b5b;--line:#dbe6df;}
*{box-sizing:border-box;}
body{font-family:'Manrope',-apple-system,sans-serif;color:var(--ink);font-size:10.6pt;line-height:1.5;margin:0;}
.lh{display:flex;align-items:center;gap:11px;padding-bottom:9px;border-bottom:2px solid var(--green);margin-bottom:16px;}
.lh img{width:34px;height:34px;}
.lh .wm{font-weight:800;font-size:15pt;letter-spacing:-.01em;}
.lh .wm span{color:var(--green);}
.lh .tag{margin-left:auto;font-size:8.6pt;color:var(--muted);text-align:right;line-height:1.4;}
h1{font-size:18pt;color:var(--ink);margin:6px 0 2px;letter-spacing:-.01em;}
h3{font-size:12pt;color:var(--green);font-weight:700;margin:0 0 12px;}
h2{font-size:12.5pt;color:var(--green);margin:20px 0 7px;padding-bottom:3px;border-bottom:1px solid var(--line);}
p{margin:0 0 9px;} ul,ol{margin:0 0 9px;padding-left:20px;} li{margin:3px 0;}
strong{color:#0f1c15;}
code{font-family:ui-monospace,Menlo,monospace;font-size:9.4pt;background:#eef4f0;padding:1px 4px;border-radius:3px;}
a{color:var(--green);text-decoration:none;}
hr{border:0;border-top:1px solid var(--line);margin:16px 0;}
table{border-collapse:collapse;width:100%;margin:10px 0;font-size:10pt;}
th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;}
th{background:#eef4f0;color:#0f1c15;font-weight:700;}
h2,h3{break-after:avoid;} table,ul,ol{break-inside:avoid;}
</style></head><body>
<div class="lh"><img src="${asset('images/kuber-map.png')}" alt=""><div class="wm">Kuber <span>Map</span> for FIBO</div>
<div class="tag">Proposal to the EDM Council<br>Sanjeev Azad · MIT · independent contribution</div></div>
${body}
</body></html>`;

const tmp = join(tmpdir(), 'kuber-proposal.html');
writeFileSync(tmp, html);

// 3) html -> pdf (playwright), with page numbers in the footer
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + tmp, { waitUntil: 'load' });
try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch { /* fonts optional */ }
await page.waitForTimeout(500);
await page.pdf({
  path: join(here, 'edm-council-proposal.pdf'),
  format: 'A4', printBackground: true,
  margin: { top: '16mm', bottom: '16mm', left: '18mm', right: '18mm' },
  displayHeaderFooter: true, headerTemplate: '<span></span>',
  footerTemplate: '<div style="width:100%;font-size:8px;color:#888;padding:0 18mm;text-align:right;font-family:sans-serif;">Kuber Map for FIBO — proposal to the EDM Council · page <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
});
await browser.close();
unlinkSync(tmp);
console.log('wrote contrib/edm-council-proposal.pdf');
