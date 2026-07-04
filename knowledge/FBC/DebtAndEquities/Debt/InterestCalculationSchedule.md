---
type: FIBO Class
title: "interest calculation schedule"
description: "regular, contract-specific schedule including the dates on which interest is calculated"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculationSchedule
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: has-occurrence, target: "/FBC/DebtAndEquities/Debt/InterestCalculation.md", provenance: fibo}
---

regular, contract-specific schedule including the dates on which interest is calculated

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- has-occurrence: [InterestCalculation](/FBC/DebtAndEquities/Debt/InterestCalculation.md)
