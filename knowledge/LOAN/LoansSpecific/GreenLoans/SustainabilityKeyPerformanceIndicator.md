---
type: FIBO Class
title: "sustainability key performance indicator"
description: "measurable performance indicator that is sustainability specific"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicator
tags: [LOAN, Release]
detail: "A sustainability KPI must be: (a) relevant, core and material to the borrower's overall business, and of high strategic significance to the borrower's current and/or future operations; (b) measurable or quantifiable on a consistent methodological basis; and (c) able to be benchmarked (i.e. as much as possible using an external reference or definitions to facilitate the assessment of the SPT's level of ambition). A clear definition of the KPI(s) should be provided by the borrower and should include the applicable scope or parameters, as well as the calculation methodology, a definition of a baseline and be benchmarked against an industry standard and/or industry peers where feasible."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/KeyPerformanceIndicator.md", provenance: fibo}
  - {type: has-observed-value, target: "/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure.md", provenance: fibo}
  - {type: has-target-value, target: "/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md", provenance: fibo}
  - {type: is-identified-by, target: "/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicatorIdentifier.md", provenance: fibo}
---

measurable performance indicator that is sustainability specific

### Relationships
- is-a: [KeyPerformanceIndicator](/FND/Utilities/Analytics/KeyPerformanceIndicator.md)
- has-observed-value: [ObservedIndicatorValueStructure](/LOAN/LoansSpecific/GreenLoans/ObservedIndicatorValueStructure.md)
- has-target-value: [SustainabilityPerformanceTarget](/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md)
- is-identified-by: [SustainabilityKeyPerformanceIndicatorIdentifier](/LOAN/LoansSpecific/GreenLoans/SustainabilityKeyPerformanceIndicatorIdentifier.md)
