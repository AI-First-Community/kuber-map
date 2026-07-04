---
type: FIBO Class
title: "preferred share with adjustable rate dividend"
description: "preferred share whose dividend rate varies according to some benchmark"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAdjustableRateDividend
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-dividend, target: "/SEC/Equities/EquityInstruments/AdjustableRateDividend.md", provenance: fibo}
---

preferred share whose dividend rate varies according to some benchmark

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-dividend: [AdjustableRateDividend](/SEC/Equities/EquityInstruments/AdjustableRateDividend.md)
