---
type: FIBO Class
title: "preferred share with auction rate dividend"
description: "preferred share whose dividend rate is periodically reset through an auction, such as a Dutch auction"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-dividend, target: "/SEC/Equities/EquityInstruments/AuctionRateDividend.md", provenance: fibo}
---

preferred share whose dividend rate is periodically reset through an auction, such as a Dutch auction

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-dividend: [AuctionRateDividend](/SEC/Equities/EquityInstruments/AuctionRateDividend.md)
