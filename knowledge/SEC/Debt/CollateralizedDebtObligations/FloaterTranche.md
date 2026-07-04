---
type: FIBO Class
title: "floater tranche"
description: "A floater tranche is a tranche that is keyed to an index and a spread."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/FloaterTranche
tags: [SEC, Provisional]
detail: "For example, 3 month LIBOR +50 -- meaning that the coupon would be whatever the 3 month LIBOR is plus 50 basis points. This is not a continuously updated number, rather it resets at specified intervals."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md", provenance: fibo}
  - {type: has-recurrence-interval, target: "/FND/DatesAndTimes/BusinessDates/DayOfMonth.md", provenance: fibo}
---

A floater tranche is a tranche that is keyed to an index and a spread.

### Relationships
- is-a: [TranchedMBSInstrument](/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- has-recurrence-interval: [DayOfMonth](/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)
