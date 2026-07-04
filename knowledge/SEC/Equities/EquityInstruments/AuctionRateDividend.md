---
type: FIBO Class
title: "auction rate dividend"
description: "preferred share dividend whose rate is periodically reset through an auction, typically every 7, 14, 28, or 35 days"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AuctionRateDividend
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredDividend.md", provenance: fibo}
  - {type: has-adjustable-dividend-rate, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

preferred share dividend whose rate is periodically reset through an auction, typically every 7, 14, 28, or 35 days

### Relationships
- is-a: [PreferredDividend](/SEC/Equities/EquityInstruments/PreferredDividend.md)
- has-adjustable-dividend-rate: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
