---
type: FIBO Class
title: "ad hoc schedule"
description: "schedule consisting of some number of individual events that are not necessarily recurring"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocSchedule
tags: [FND, Release]
detail: "Other ontologies can extend AdHocSchedule and/or AdHocScheduleEntry as needed to relate the date to something. In particular, the Occurrences ontology extends AdHocScheduleEntry to associate an OccurrenceKind with each entry. The intended meaning is that an Occurrence of the OccurrenceKind happens on the corresponding Date."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: has-member, target: "/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry.md", provenance: fibo}
---

schedule consisting of some number of individual events that are not necessarily recurring

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- has-member: [AdHocScheduleEntry](/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry.md)
