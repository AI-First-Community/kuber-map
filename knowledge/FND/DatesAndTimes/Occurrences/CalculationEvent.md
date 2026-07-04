---
type: FIBO Class
title: "calculation event"
description: "kind of event that is either scheduled or triggered by something, such as a related financial event, that causes a calculation to be performed"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/CalculationEvent
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: classifies, target: "/FND/DatesAndTimes/Occurrences/Calculation.md", provenance: fibo}
---

kind of event that is either scheduled or triggered by something, such as a related financial event, that causes a calculation to be performed

### Relationships
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- classifies: [Calculation](/FND/DatesAndTimes/Occurrences/Calculation.md)
