---
type: FIBO Class
title: "p a c-1 class"
description: "Planned Amortization Class tranche. PAC-1 is the most senior Planned Amortization Class tranche."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-1Class
tags: [SEC, Provisional]
detail: "Principal payment must follow a certain schedule. These tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md", provenance: fibo}
  - {type: takes-prepayment-after, target: "/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md", provenance: fibo}
---

Planned Amortization Class tranche. PAC-1 is the most senior Planned Amortization Class tranche.

### Relationships
- is-a: [PlannedAmortizationClassBond](/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md)
- takes-prepayment-after: [PAC-2Class](/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md)
