---
type: FIBO Class
title: "key performance indicator"
description: "measurable target that indicates how an individual or business is performing in terms of meeting its goals"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/KeyPerformanceIndicator
tags: [FND, Release]
detail: "Although they are both designed to measure performance, KPIs and metrics have different characteristics and are used by businesses in different ways. Metrics are measures used to track progress and evaluate success, while KPIs are metrics tied to specific goals during a certain period of time. KPIs are designed to align with business goals and targets, while metrics evaluate the performance of particular processes. Key Performance Indicators (KPIs) are the critical (key) quantifiable indicators of progress toward an intended result. KPIs provide a focus for strategic and operational improvement, create an analytical basis for decision making and help focus attention on what matters most. Managing with the use of KPIs includes setting targets (the desired level of performance) and tracking progress against those targets."
examples:
  - "Examples include profits, sales numbers, employee turnover and average annual expenses."
synonyms:
  - "KPI"
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
