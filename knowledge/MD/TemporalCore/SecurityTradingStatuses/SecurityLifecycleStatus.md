---
type: FIBO Class
title: "security lifecycle status"
description: "status of a security within its lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityLifecycleStatus
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStatus.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

status of a security within its lifecycle

### Relationships
- is-a: [LifecycleStatus](/FND/Arrangements/Lifecycles/LifecycleStatus.md)
- classifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
