---
type: FIBO Class
title: "p a c-2 class"
description: "Planned Amortization Class tranche. PAC-2 refers to a support tranche that is given a scheduled payment structure like a PAC bond."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PAC-2Class
tags: [SEC, Provisional]
detail: "Principal payment must follow a certain schedule. These tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches. For example, let's say you have a deal with a PAC tranche and a support tranche (i.e., a tranche that is a support tranche and is therefore subordinate to the PAC tranche) that has a scheduled payment structure like you did with the PAC bond. That support bond then is called the PAC-2 bond. If you continue, and create another support tranche that also has scheduled payments, that would become the PAC-3 bond."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md", provenance: fibo}
  - {type: takes-prepayment-after, target: "/SEC/Debt/CollateralizedDebtObligations/PAC-3Class.md", provenance: fibo}
---

Planned Amortization Class tranche. PAC-2 refers to a support tranche that is given a scheduled payment structure like a PAC bond.

### Relationships
- is-a: [PlannedAmortizationClassBond](/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond.md)
- takes-prepayment-after: [PAC-3Class](/SEC/Debt/CollateralizedDebtObligations/PAC-3Class.md)
