---
type: FIBO Class
title: "key performance indicator"
description: "measurable target that indicates how an individual or business is performing in terms of meeting its goals"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/KeyPerformanceIndicator
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/QualifiedMeasure.md", provenance: fibo}
  - {type: has-observed-value, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-target-value, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
---

measurable target that indicates how an individual or business is performing in terms of meeting its goals

### Relationships
- is-a: [QualifiedMeasure](/FND/Utilities/Analytics/QualifiedMeasure.md)
- has-observed-value: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-target-value: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
