---
type: FIBO Class
title: "schedule stub"
description: "date period before the start of the recurring part of a schedule or after the end of the recurring part, which may be associated with a specific occurrence kind"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub
tags: [FND, Release]
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
