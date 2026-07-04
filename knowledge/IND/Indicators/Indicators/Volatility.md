---
type: FIBO Class
title: "volatility"
description: "statistical measure of the dispersion around the average of some random variable over some period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility
tags: [IND, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Dispersion.md", provenance: fibo}
  - {type: has-argument, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-date-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

statistical measure of the dispersion around the average of some random variable over some period of time

### Relationships
- is-a: [Dispersion](/FND/Utilities/Analytics/Dispersion.md)
- has-argument: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-date-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
