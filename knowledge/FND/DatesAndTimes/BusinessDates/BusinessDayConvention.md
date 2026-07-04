---
type: FIBO Class
title: "business day convention"
description: "convention that enumerates the possible ways to handle a date that falls on a weekend or holiday"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
tags: [FND, Release]
relations:
  - {type: has-business-center, target: "/CMNS/Locations/BusinessCenter.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md", provenance: fibo}
---

convention that enumerates the possible ways to handle a date that falls on a weekend or holiday

### Relationships
- has-business-center: [BusinessCenter](/CMNS/Locations/BusinessCenter.md)
- is-a: [BusinessRecurrenceIntervalConvention](/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)
