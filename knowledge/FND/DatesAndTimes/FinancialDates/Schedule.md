---
type: FIBO Class
title: "schedule"
description: "collection of events, observations, or other occurrences and the associated dates and/or times when they will be done"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
tags: [FND, Release]
detail: "The overall period covers the entire DatePeriod of the Schedule, from the earliest Date to the final Date of the Schedule. Schedules may be ad hoc, essentially a list of dates and events without any consistency in the durations between events, regular, in which case there is a consistently recurring interval between events, or a combination of the two. There may be a single overall period, or more than one if the schedule is extended for some reason."
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: has-overall-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

collection of events, observations, or other occurrences and the associated dates and/or times when they will be done

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- has-overall-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
