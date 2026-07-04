---
type: FIBO Class
title: "occurrence-based date"
description: "calculated date that is defined with respect to the occurrence of some occurrence kind"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate
tags: [FND, Release]
detail: "The 'hasDateValue' property of an OccurrenceBasedDate is not set until the Occurrence happens. The 'triggeredBy' property relates an OccurrenceBasedDate to the OccurrenceKind that gives the meaning of the OccurrenceBasedDate."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/CalculatedDate.md", provenance: fibo}
  - {type: is-triggered-by, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
---

calculated date that is defined with respect to the occurrence of some occurrence kind

### Relationships
- is-a: [CalculatedDate](/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)
- is-triggered-by: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
