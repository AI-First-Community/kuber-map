---
type: FIBO Class
title: "security trading status"
description: "status of the security in terms of whether it is trading or not, and any special considerations relating to trading"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStatus.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

status of the security in terms of whether it is trading or not, and any special considerations relating to trading

### Relationships
- is-a: [LifecycleStatus](/FND/Arrangements/Lifecycles/LifecycleStatus.md)
- classifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
