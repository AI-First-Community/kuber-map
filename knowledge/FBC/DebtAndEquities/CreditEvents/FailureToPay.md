---
type: FIBO Class
title: "failure to pay"
description: "default event that is triggered following any applicable grace period in which a payment obligation is missed"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPay
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md", provenance: fibo}
  - {type: has-grace-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

default event that is triggered following any applicable grace period in which a payment obligation is missed

### Relationships
- is-a: [DefaultEvent](/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)
- has-grace-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
