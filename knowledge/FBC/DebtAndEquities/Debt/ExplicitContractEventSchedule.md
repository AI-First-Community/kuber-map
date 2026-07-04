---
type: FIBO Class
title: "explicit contract event schedule"
description: "schedule of events, including but not limited to payment events, rate reset events and others that will occur over the lifetime of the credit agreement"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ExplicitContractEventSchedule
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/AdHocSchedule.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
---

schedule of events, including but not limited to payment events, rate reset events and others that will occur over the lifetime of the credit agreement

### Relationships
- is-a: [AdHocSchedule](/FND/DatesAndTimes/FinancialDates/AdHocSchedule.md)
- applies-to: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
