---
type: FIBO Class
title: "change of security trading status event"
description: "An event in which the trading status of a tradable security changes."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ChangeOfSecurityTradingStatusEvent
tags: [CAE, Provisional]
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateChangeOfStatusEvent.md", provenance: fibo}
  - {type: applies-to, target: "/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus.md", provenance: fibo}
---

An event in which the trading status of a tradable security changes.

### Relationships
- is-a: [CorporateChangeOfStatusEvent](/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateChangeOfStatusEvent.md)
- applies-to: [SecurityTradingStatus](/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus.md)
