---
type: FIBO Class
title: "sustainability performance target"
description: "collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
tags: [LOAN, Release]
relations:
  - {type: is-identified-by, target: "/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue.md", provenance: fibo}
  - {type: has-date-period, target: "/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
---

collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan

### Relationships
- is-identified-by: [SustainabilityPerformanceTargetIdentifier](/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier.md)
- has-member: [TargetIndicatorValue](/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue.md)
- has-date-period: [CalculationPeriod](/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
