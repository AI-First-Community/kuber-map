---
type: FIBO Class
title: "guaranty"
description: "commitment whereby something is formally assured if a party with primary liability fails to perform"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
tags: [FBC, Release]
detail: "The commitment may cover a debt, cash flows on a debt instrument (such as interest payments), or performance of some obligation."
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-guaranteed-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-priority-level, target: "/FBC/DebtAndEquities/Guaranty/PriorityLevel.md", provenance: fibo}
  - {type: holds-during, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: is-guaranteed-by, target: "/FBC/DebtAndEquities/Guaranty/Guarantor.md", provenance: fibo}
---

commitment whereby something is formally assured if a party with primary liability fails to perform

### Relationships
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-guaranteed-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-priority-level: [PriorityLevel](/FBC/DebtAndEquities/Guaranty/PriorityLevel.md)
- holds-during: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- is-guaranteed-by: [Guarantor](/FBC/DebtAndEquities/Guaranty/Guarantor.md)
