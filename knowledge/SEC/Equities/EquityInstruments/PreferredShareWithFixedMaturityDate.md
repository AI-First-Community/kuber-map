---
type: FIBO Class
title: "preferred share with fixed maturity date"
description: "preferred share whose maturity date is set, typically according to the terms of the prospectus"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

preferred share whose maturity date is set, typically according to the terms of the prospectus

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
