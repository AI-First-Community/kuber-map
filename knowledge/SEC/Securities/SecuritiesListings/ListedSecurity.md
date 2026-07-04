---
type: FIBO Class
title: "listed security"
description: "registered security listed on at least one exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
tags: [SEC, Release]
core: true
detail: "One can, as appropriate, multiply classify a share as being a common share and listed share, and, in the case whereby multiple securities are issued in different currencies (i.e., there are multiple listed shares corresponding to a given common share that have different identifiers, including more than one ISIN, CUSIP, share class FIGI), multiply classify the listed share individuals as individuals of the same common share."
examples:
  - "Apple Inc. (AAPL) common stock, listed on Nasdaq."
examples_provenance: curated
synonyms:
  - "exchange-traded security"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesListings/RegisteredSecurity.md", provenance: fibo}
  - {type: has-home-exchange, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: has-original-place-of-listing, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-listed-via, target: "/SEC/Securities/SecuritiesListings/Listing.md", provenance: fibo}
---

registered security listed on at least one exchange

### Relationships
- is-a: [RegisteredSecurity](/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)
- has-home-exchange: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- has-original-place-of-listing: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-listed-via: [Listing](/SEC/Securities/SecuritiesListings/Listing.md)
