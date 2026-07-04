---
type: FIBO Class
title: "market segment-level market"
description: "section of an exchange/market/trade reporting facility that specialises in one or more specific instruments or that is regulated differently"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
tags: [FBC, Release]
examples:
  - "Dark pool"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketLevelClassifier-SGMT.md", provenance: fibo}
  - {type: is-part-of, target: "/FBC/FunctionalEntities/Markets/OperatingLevelMarket.md", provenance: fibo}
---

section of an exchange/market/trade reporting facility that specialises in one or more specific instruments or that is regulated differently

### Relationships
- is-a: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-classified-by: [MarketLevelClassifier-SGMT](/FBC/FunctionalEntities/Markets/MarketLevelClassifier-SGMT.md)
- is-part-of: [OperatingLevelMarket](/FBC/FunctionalEntities/Markets/OperatingLevelMarket.md)
