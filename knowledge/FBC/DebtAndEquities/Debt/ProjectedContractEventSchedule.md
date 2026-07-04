---
type: FIBO Class
title: "projected contract event schedule"
description: "schedule of events, including but not limited to anticipated payment events, rate reset events and others that are expected to occur over the lifetime of the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
tags: [FBC, Release]
detail: "A projected schedule is a regular schedule that documents the anchor dates and frequency of occurrences, using rules, rather than providing an explicit list of dates. This method will project future event dates (transaction event dates), based on the frequencies specified and may be adjusted due to calendar restrictions and other rules to deal with holidays, weekends, and so forth in addition to contract-specific events."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/RegularSchedule.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
---

schedule of events, including but not limited to anticipated payment events, rate reset events and others that are expected to occur over the lifetime of the contract

### Relationships
- is-a: [RegularSchedule](/FND/DatesAndTimes/FinancialDates/RegularSchedule.md)
- applies-to: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
