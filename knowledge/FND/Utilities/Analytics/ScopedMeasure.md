---
type: FIBO Class
title: "scoped measure"
description: "qualified measure that is constrained by filters on the statistical population to which it applies"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/QualifiedMeasure.md", provenance: fibo}
  - {type: has-periodicity, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Utilities/Analytics/FinitePopulation.md", provenance: fibo}
  - {type: has-coverage-area, target: "/FND/Utilities/Analytics/StatisticalArea.md", provenance: fibo}
---

qualified measure that is constrained by filters on the statistical population to which it applies

### Relationships
- is-a: [QualifiedMeasure](/FND/Utilities/Analytics/QualifiedMeasure.md)
- has-periodicity: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- applies-to: [FinitePopulation](/FND/Utilities/Analytics/FinitePopulation.md)
- has-coverage-area: [StatisticalArea](/FND/Utilities/Analytics/StatisticalArea.md)
