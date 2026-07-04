---
type: FIBO Class
title: "average earnings"
description: "measure of the average wage an hourly or salaried worker makes in a given period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageEarnings
tags: [IND, Release]
detail: "Average earnings are typically calculated on an hourly, daily, weekly, or monthly basis. They may be expressed as an amount of money or in terms of a percent change with respect to a prior period, depending on the jurisdiction and report."
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-reference-period, target: "/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md", provenance: fibo}
---

measure of the average wage an hourly or salaried worker makes in a given period of time

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-reference-period: [ExplicitRecurrenceInterval](/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)
