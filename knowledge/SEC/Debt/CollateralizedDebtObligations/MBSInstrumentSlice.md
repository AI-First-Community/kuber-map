---
type: FIBO Class
title: "m b s instrument slice"
description: "A holding of an individual slice or slices of a tranche."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice
tags: [SEC, Provisional]
detail: "These may be held in different notes, with different denominations. Tranche slice in this sense is only relevant in the context of something like a CDO or analogous things such as CBO."
relations:
  - {type: is-a, target: "/SEC/Securities/SecurityAssets/Portfolio.md", provenance: fibo}
---

A holding of an individual slice or slices of a tranche.

### Relationships
- is-a: [Portfolio](/SEC/Securities/SecurityAssets/Portfolio.md)
