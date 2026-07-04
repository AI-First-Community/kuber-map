---
type: FIBO Class
title: "rate reset time of day"
description: "time of day that an interest rate is reset, as indicated by some interest rate authority or market data provider"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RateResetTimeOfDay
tags: [FBC, Release]
examples:
  - "Examples include certain rates published by the Federal Reserve Board in their H.15 schedule, which are published at 4:15 pm on business days that are not holidays in the US."
relations:
  - {type: is-a, target: "/CMNS/DatesAndTimes/TimeOfDay.md", provenance: fibo}
  - {type: has-business-center, target: "/CMNS/Locations/BusinessCenter.md", provenance: fibo}
---

time of day that an interest rate is reset, as indicated by some interest rate authority or market data provider

### Relationships
- is-a: [TimeOfDay](/CMNS/DatesAndTimes/TimeOfDay.md)
- has-business-center: [BusinessCenter](/CMNS/Locations/BusinessCenter.md)
