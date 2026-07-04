---
type: FIBO Class
title: "corporate change of status event"
description: "Some change to the status of some security."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateChangeOfStatusEvent
tags: [CAE, Provisional]
detail: "This is generally described by a corporate event message. For example, change in trading status, listing status."
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/CorporateAction.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleEvent.md", provenance: fibo}
---

Some change to the status of some security.

### Relationships
- is-a: [CorporateAction](/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- is-a: [LifecycleEvent](/FND/Arrangements/Lifecycles/LifecycleEvent.md)
