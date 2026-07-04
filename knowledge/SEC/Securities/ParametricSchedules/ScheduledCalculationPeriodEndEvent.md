---
type: FIBO Class
title: "scheduled calculation period end event"
description: "the end date of a specific calculation period"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/ScheduledCalculationPeriodEndEvent
tags: [SEC, Release]
detail: "Note that this is not necessarily the same as the day before the next period's start date. Calculation schedules specify periods of time, with a start and an end as well as a duration, with the end date being determined by some convention or published list of dates. FpML for CalculationPeriod 'A type defining the parameters used in the calculation of a fixed or floating rate calculation period amount. This type forms part of cashflows representation of a swap stream.'"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
---

the end date of a specific calculation period

### Relationships
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
