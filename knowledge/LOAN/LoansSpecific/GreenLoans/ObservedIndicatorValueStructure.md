---
type: FIBO Class
title: "observed indicator value structure"
description: "collection of observations for some key performance indicator measured over a specified window of time"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-date-period, target: "/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValue.md", provenance: fibo}
---

collection of observations for some key performance indicator measured over a specified window of time

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-date-period: [CalculationPeriod](/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md)
- has-member: [ObservedIndicatorValue](/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValue.md)
