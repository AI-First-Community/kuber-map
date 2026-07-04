---
type: FIBO Class
title: "economic indicator"
description: "statistical measure of economic activity that is regular and comparable in the context of a statistical area (region), used for analysis of economic performance and predictions of future performance"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
tags: [IND, Release]
detail: "The two main features of any indicator are the regularity with which they are measured and published, and the fact that they are comparable from one release to the next."
examples:
  - "Example indicators include the average work week, weekly claims for unemployment insurance, new orders, vendor performance, stock prices, and changes in the money supply."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ScopedMeasure.md", provenance: fibo}
  - {type: has-coverage-area, target: "/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md", provenance: fibo}
  - {type: has-release-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-reporting-period, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
  - {type: has-series-origin, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

statistical measure of economic activity that is regular and comparable in the context of a statistical area (region), used for analysis of economic performance and predictions of future performance

### Relationships
- is-a: [ScopedMeasure](/FND/Utilities/Analytics/ScopedMeasure.md)
- has-coverage-area: [GovernmentSpecifiedStatisticalArea](/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)
- has-release-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-reporting-period: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
- has-series-origin: [Date](/CMNS/DatesAndTimes/Date.md)
