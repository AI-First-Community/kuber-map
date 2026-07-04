---
type: FIBO Class
title: "annualized standard deviation"
description: "standard deviation for some measure over a specific reference period"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AnnualizedStandardDeviation
tags: [FND, Release]
detail: "Standard deviation applied to the annual rate of return of an investment provides insights on the historical volatility of that investment. The greater the standard deviation of the price of a security, the greater the volatility. Multiplying monthly standard deviation by the square root of twelve (12) is an industry standard method of approximating annualized standard deviations of monthly returns."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/StandardDeviation.md", provenance: fibo}
  - {type: has-reference-period, target: "/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md", provenance: fibo}
---

standard deviation for some measure over a specific reference period

### Relationships
- is-a: [StandardDeviation](/FND/Utilities/Analytics/StandardDeviation.md)
- has-reference-period: [ExplicitRecurrenceInterval](/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)
