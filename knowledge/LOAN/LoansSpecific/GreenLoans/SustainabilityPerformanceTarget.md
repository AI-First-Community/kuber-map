---
type: FIBO Class
title: "sustainability performance target"
description: "collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
tags: [LOAN, Release]
detail: "An SLL borrower should clearly communicate to its lenders its rationale for the selection of its KPI(s) (i.e. relevance, materiality, whether it is core to the borrower’s overall business) and the motivation for the SPT(s) (i.e. ambition level, benchmarking approach and how the borrower intends to reach such SPTs). Borrowers are encouraged to position this information within the context of their overarching objectives, sustainability strategy, policy, sustainability commitments and/or processes relating to sustainability. The process for calibration of the SPT(s) per KPI is key to the structuring of SLLs, since it will be the expression of the level of ambition the borrower is ready to commit to. The SPTs must be set in good faith and remain relevant (so long as they apply) and ambitious throughout the life of the loan."
synonyms:
  - "SPT"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-date-period, target: "/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue.md", provenance: fibo}
  - {type: is-identified-by, target: "/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier.md", provenance: fibo}
---

collection of quantitative target values used to calibrate the level of achievement a borrower makes with respect to a key performance indicator, by date, including, but not limited to, the methodology used to calculate its value at any point over the lifetime of a loan

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-date-period: [CalculationPeriod](/FND/DatesAndTimes/FinancialDates/CalculationPeriod.md)
- has-member: [TargetIndicatorValue](/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue.md)
- is-identified-by: [SustainabilityPerformanceTargetIdentifier](/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier.md)
