---
type: FIBO Class
title: "participating preferred share"
description: "preferred share that, in addition to paying a stipulated dividend, gives the holder the right to participate with common share holders in additional distributions of earnings under specified conditions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ParticipatingPreferredShare
tags: [SEC, Release]
detail: "Participating preferred shares are rare, typically only issued when needed to attract investors."
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-dividend, target: "/SEC/Equities/EquityInstruments/OrdinaryDividend.md", provenance: fibo}
---

preferred share that, in addition to paying a stipulated dividend, gives the holder the right to participate with common share holders in additional distributions of earnings under specified conditions

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-dividend: [OrdinaryDividend](/SEC/Equities/EquityInstruments/OrdinaryDividend.md)
