---
type: FIBO Class
title: "trading date rule"
description: "convention for determining trading dates defined with reference to some trading date calendar published by some trading facility or exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/TradingDateRule
tags: [SEC, Release]
detail: "Corresponds to several ISDA FpML enumeration entries for determining Calculation Date, but refers to other kinds of trading date defined in those calendars. These include Canadian, Australian and New Zealand dates. Note also that some of these have roll rules included within them for when the date determined by the specification returns a non working day, while others explicitly return a business day and require no date roll rule. At least one is silent on this matter."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md", provenance: fibo}
---

convention for determining trading dates defined with reference to some trading date calendar published by some trading facility or exchange

### Relationships
- is-a: [BusinessRecurrenceIntervalConvention](/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)
