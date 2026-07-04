---
type: FIBO Class
title: "lifecycle event"
description: "kind of event that occurs during one or more stages of a lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent
tags: [FND, Release]
examples:
  - "a call notification or coupon payment as a part of a bond lifecycle"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
---

kind of event that occurs during one or more stages of a lifecycle

### Relationships
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- applies-to: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
