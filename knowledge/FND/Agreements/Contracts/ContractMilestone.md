---
type: FIBO Class
title: "contract milestone"
description: "classifier for an event (milestone), or set of events related to the status or level of completion of a designated activity, task, or segment of work required for contract fulfillment"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: classifies, target: "/FND/Agreements/Contracts/MilestoneEvent.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ConditionPrecedent.md", provenance: fibo}
---

classifier for an event (milestone), or set of events related to the status or level of completion of a designated activity, task, or segment of work required for contract fulfillment

### Relationships
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- classifies: [MilestoneEvent](/FND/Agreements/Contracts/MilestoneEvent.md)
- applies-to: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-a: [ConditionPrecedent](/FND/Agreements/Contracts/ConditionPrecedent.md)
