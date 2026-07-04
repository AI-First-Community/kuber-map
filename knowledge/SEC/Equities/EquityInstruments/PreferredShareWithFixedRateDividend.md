---
type: FIBO Class
title: "preferred share with fixed rate dividend"
description: "preferred share whose dividends are set, typically according to the terms of the prospectus"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-dividend, target: "/SEC/Equities/EquityInstruments/FixedRateDividend.md", provenance: fibo}
---

preferred share whose dividends are set, typically according to the terms of the prospectus

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-dividend: [FixedRateDividend](/SEC/Equities/EquityInstruments/FixedRateDividend.md)
