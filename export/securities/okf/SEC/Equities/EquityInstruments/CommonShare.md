---
type: FIBO Class
title: "common share"
description: "share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets and earnings"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
tags: [SEC, Release]
detail: "In the event that the corporation is liquidated, claims of secured and unsecured creditors and owners of bonds and preferred shares take precedence over claims of common share holders."
examples:
  - "One ordinary share of Amazon.com, Inc. carrying one vote."
examples_provenance: curated
synonyms:
  - "ordinary share"
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
  - {type: has-dividend, target: "/SEC/Equities/EquityInstruments/OrdinaryDividend.md", provenance: fibo}
---

share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets and earnings

### Relationships
- is-a: [Share](/SEC/Equities/EquityInstruments/Share.md)
- has-dividend: [OrdinaryDividend](/SEC/Equities/EquityInstruments/OrdinaryDividend.md)
