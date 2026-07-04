---
type: FIBO Class
title: "lifecycle stage occurrence"
description: "realization of a phase in a given lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: comprises, target: "/FND/Arrangements/Lifecycles/LifecycleEventOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
  - {type: is-stage-of, target: "/FND/Arrangements/Lifecycles/LifecycleOccurrence.md", provenance: fibo}
---

realization of a phase in a given lifecycle

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- comprises: [LifecycleEventOccurrence](/FND/Arrangements/Lifecycles/LifecycleEventOccurrence.md)
- exemplifies: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
- is-stage-of: [LifecycleOccurrence](/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)
