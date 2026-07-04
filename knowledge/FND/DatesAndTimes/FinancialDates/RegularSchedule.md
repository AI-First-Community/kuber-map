---
type: FIBO Class
title: "regular schedule"
description: "schedule whose time intervals recur regularly"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule
tags: [FND, Release]
relations:
  - {type: has-business-day-convention, target: "/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md", provenance: fibo}
  - {type: has-final-stub, target: "/FND/DatesAndTimes/FinancialDates/ScheduleStub.md", provenance: fibo}
  - {type: has-anchor-date, target: "/FND/DatesAndTimes/FinancialDates/AnchorDate.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
  - {type: has-recurrence-interval, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-initial-stub, target: "/FND/DatesAndTimes/FinancialDates/ScheduleStub.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: comprises, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: has-occurrence, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

schedule whose time intervals recur regularly

### Relationships
- has-business-day-convention: [BusinessDayConvention](/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)
- has-final-stub: [ScheduleStub](/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- has-anchor-date: [AnchorDate](/FND/DatesAndTimes/FinancialDates/AnchorDate.md)
- is-a: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
- has-recurrence-interval: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-initial-stub: [ScheduleStub](/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- comprises: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- has-occurrence: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
