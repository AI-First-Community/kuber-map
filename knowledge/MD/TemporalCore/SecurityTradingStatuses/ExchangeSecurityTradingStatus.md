---
type: FIBO Class
title: "exchange security trading status"
description: "trading status of a listed security on a given trading exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/ExchangeSecurityTradingStatus
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStatus.md", provenance: fibo}
  - {type: classifies, target: "/SEC/Securities/SecuritiesListings/Listing.md", provenance: fibo}
---

trading status of a listed security on a given trading exchange

### Relationships
- is-a: [LifecycleStatus](/FND/Arrangements/Lifecycles/LifecycleStatus.md)
- classifies: [Listing](/SEC/Securities/SecuritiesListings/Listing.md)
