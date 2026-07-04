---
type: FIBO Class
title: "regular floater tranche"
description: "A floater tranche is a tranche that is keyed to an index and a spread. The spread is added to the index."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/RegularFloaterTranche
tags: [SEC, Provisional]
detail: "For example, 3 month LIBOR +50 -- meaning that the coupon would be whatever the 3 month LIBOR is plus 50 basis points. This is not a continuously updated number, rather it resets at specified intervals."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md", provenance: fibo}
---

A floater tranche is a tranche that is keyed to an index and a spread. The spread is added to the index.

### Relationships
- is-a: [FloaterTranche](/SEC/Debt/CollateralizedDebtObligations/FloaterTranche.md)
