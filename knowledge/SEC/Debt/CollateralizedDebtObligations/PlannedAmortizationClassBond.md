---
type: FIBO Class
title: "planned amortization class bond"
description: "Planned Amortization Class tranche.This is a tranche where the principal payment must follow a certain schedule."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/PlannedAmortizationClassBond
tags: [SEC, Provisional]
detail: "These tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches. There are usually several PAC tranches created. PAC-1, PAC-2, PAC-3 -- this requires some more explanation. PAC-2 refers to a support tranche that is given a scheduled payment structure like a PAC bond. For example, let's say you have a deal with a PAC tranche and a support tranche (i.e., a tranche that is a support tranche and is therefore subordinate to the PAC tranche) that has a scheduled payment structure like you did with the PAC bond. That support bond then is called the PAC-2 bond. If you continue, and create another support tranche that also has scheduled payments, that would become the PAC-3 bond. Prospectus will cover each class. Prospectus is at the level of an issue."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md", provenance: fibo}
  - {type: specifies, target: "/SEC/Debt/CollateralizedDebtObligations/PACTrancheAmortizationSchedule.md", provenance: fibo}
---

Planned Amortization Class tranche.This is a tranche where the principal payment must follow a certain schedule.

### Relationships
- is-a: [AgencyCMO](/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- specifies: [PACTrancheAmortizationSchedule](/SEC/Debt/CollateralizedDebtObligations/PACTrancheAmortizationSchedule.md)
