---
type: FIBO Class
title: "t a c tranche"
description: "Targeted Amortization Class. This is related to a PAC tranche and has a payment schedule geared towards a specified prepayment speed (called the pricing speed). Agency CMO"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TACTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md", provenance: fibo}
  - {type: specifies, target: "/SEC/Debt/CollateralizedDebtObligations/TACTrancheAmortizationSchedule.md", provenance: fibo}
---

Targeted Amortization Class. This is related to a PAC tranche and has a payment schedule geared towards a specified prepayment speed (called the pricing speed). Agency CMO

### Relationships
- is-a: [AgencyCMO](/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- is-a: [TranchedMBSInstrument](/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- specifies: [TACTrancheAmortizationSchedule](/SEC/Debt/CollateralizedDebtObligations/TACTrancheAmortizationSchedule.md)
