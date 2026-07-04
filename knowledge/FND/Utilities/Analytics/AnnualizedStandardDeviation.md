---
type: FIBO Class
title: "annualized standard deviation"
description: "standard deviation for some measure over a specific reference period"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AnnualizedStandardDeviation
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StandardDeviation.md", provenance: fibo}
  - {type: has-reference-period, target: "/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md", provenance: fibo}
---

standard deviation for some measure over a specific reference period

### Relationships
- is-a: [StandardDeviation](/FND/Utilities/Analytics/StandardDeviation.md)
- has-reference-period: [ExplicitRecurrenceInterval](/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)
