# Third-party notices

Kuber Map for FIBO is licensed under the MIT License (see [`LICENSE`](LICENSE),
© 2026 Sanjeev Azad). It incorporates, derives from, and redistributes the third-party
works below. Each is used under its own license, reproduced here. Where this project
redistributes substantial portions of a work (for example, FIBO class definitions in the
generated `knowledge/` bundle and the `export/` context packs), the required copyright and
permission notices are preserved below.

---

## FIBO — Financial Industry Business Ontology

The generated `knowledge/` OKF bundle, the `export/` context packs, the `eval/` benchmarks,
and any curated definition/example grounded in FIBO incorporate content extracted from FIBO
(class labels, `skos:definition` text, IRIs, and relationships).

- **Source:** https://github.com/edmcouncil/fibo (pinned commit — see `fibo-source.pin`)
- **License:** MIT License
- **Copyright:** © 2016–2025 EDM Council, Inc. and © 2016–2025 Object Management Group, Inc.

```
Copyright (c) EDM Council, Inc.
Copyright (c) Object Management Group, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## Commons (CMNS) — OMG Commons Ontology Library

The `CMNS` concepts in the bundle and packs incorporate content from the OMG Commons
Ontology Library (FIBO's upper ontology), fetched via content negotiation from
`https://www.omg.org/spec/Commons/`.

- **License:** MIT License (per each module's embedded `dct:license`)
- **Copyright:** © 2011–2025 Thematix Partners LLC, © 2013–2025 EDM Council, Inc., and
  © 2013–2025 Object Management Group, Inc.

The MIT permission notice above applies equally to the Commons content.

## Bodhi Map (user-interface fork)

The interactive map's front end (`css/style.css`, `js/graph.js`, `app.html` structure) is
forked from the Bodhi Map project and adapted to FIBO.

- **License:** MIT License
- **Copyright:** © 2026 Sanjeev Azad

## Cytoscape.js

Graph rendering library (`js/cytoscape.min.js`).

- **License:** MIT License
- **Copyright:** © 2016–2024 The Cytoscape Consortium

## cytoscape-fcose, cose-base, layout-base

fcose layout extension and its dependencies (`js/cytoscape-fcose.js`, `js/cose-base.js`,
`js/layout-base.js`).

- **License:** MIT License

## Manrope (font)

Web fonts under `fonts/manrope-*.woff2`.

- **License:** SIL Open Font License, Version 1.1 (OFL-1.1)

---

## Trademarks

**FIBO** and **EDM Council** are trademarks of EDM Council, Inc. **OMG** and **Object
Management Group** are trademarks of Object Management Group, Inc. This is an independent,
community project; it is **not affiliated with, sponsored by, or endorsed by** the EDM
Council or the Object Management Group. References to FIBO are nominative — they describe
the ontology this project maps and grounds against.
