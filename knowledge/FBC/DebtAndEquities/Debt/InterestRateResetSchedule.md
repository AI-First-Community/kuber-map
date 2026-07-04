---
type: FIBO Class
title: "interest rate reset schedule"
description: "regular, contract-specific schedule including the dates on which a rate reset, and corresponding actual rate, is recalculated"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestRateResetSchedule
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: has-occurrence, target: "/FBC/DebtAndEquities/Debt/InterestRateReset.md", provenance: fibo}
---

regular, contract-specific schedule including the dates on which a rate reset, and corresponding actual rate, is recalculated

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- has-occurrence: [InterestRateReset](/FBC/DebtAndEquities/Debt/InterestRateReset.md)
