---
type: FIBO Class
title: "perpetual preferred share"
description: "preferred share that has no fixed maturity date"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PerpetualPreferredShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

preferred share that has no fixed maturity date

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
