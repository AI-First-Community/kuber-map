---
type: FIBO Class
title: "schedule stub"
description: "date period before the start of the recurring part of a schedule or after the end of the recurring part, which may be associated with a specific occurrence kind"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub
tags: [FND, Release]
examples:
  - "A 30 year mortgage calls for monthly payments on the first day of each month, according to a RegularSchedule. If the mortgage does not start on the first day of a calendar month, then an initial ScheduleStub specifies the payment due for the DatePeriod up to the first day of the next calendar month. Similarly, a final ScheduleStub specifies the last payment due for the DatePeriod after the end of the last full calendar month."
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: comprises, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: has-date-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-occurrence, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

date period before the start of the recurring part of a schedule or after the end of the recurring part, which may be associated with a specific occurrence kind

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- comprises: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- has-date-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-occurrence: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
