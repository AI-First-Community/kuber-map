---
type: FIBO Class
title: "scoped measure"
description: "qualified measure that is constrained by filters on the statistical population to which it applies"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
tags: [FND, Release]
detail: "Note that (1) the anchor date reflects the start of the current series, such as 1982-1984 for the CPI, (2) the fixed comparative date might be something like March 2009, if one is comparing a current index against its value at the end of the great recession, (3) the relative comparative date might be something like a month or year ago, depending on the analysis requirements, and (4) the relative comparative period might be a 3 month average prior value, again depending on the analysis requirements."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/QualifiedMeasure.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Utilities/Analytics/FinitePopulation.md", provenance: fibo}
  - {type: has-coverage-area, target: "/FND/Utilities/Analytics/StatisticalArea.md", provenance: fibo}
  - {type: has-periodicity, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
---

qualified measure that is constrained by filters on the statistical population to which it applies

### Relationships
- is-a: [QualifiedMeasure](/FND/Utilities/Analytics/QualifiedMeasure.md)
- applies-to: [FinitePopulation](/FND/Utilities/Analytics/FinitePopulation.md)
- has-coverage-area: [StatisticalArea](/FND/Utilities/Analytics/StatisticalArea.md)
- has-periodicity: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
