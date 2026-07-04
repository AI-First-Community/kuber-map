---
type: FIBO Class
title: "soft credit event"
description: "default event that is repairable"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/SoftCreditEvent
tags: [FBC, Release]
detail: "If the default is not repaired within a grace period, then a failure to repair (failure to pay) credit event is triggered, potentially as a hard default."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md", provenance: fibo}
---

default event that is repairable

### Relationships
- is-a: [DefaultEvent](/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)
