---
type: FIBO Class
title: "preferred dividend"
description: "commitment to distribute a portion of earnings to shareholders, similar to a dividend but often with a fixed payment amount and schedule"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Dividend.md", provenance: fibo}
  - {type: has-dividend-grace-period, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
  - {type: has-fixed-dividend-rate, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

commitment to distribute a portion of earnings to shareholders, similar to a dividend but often with a fixed payment amount and schedule

### Relationships
- is-a: [Dividend](/SEC/Equities/EquityInstruments/Dividend.md)
- has-dividend-grace-period: [Duration](/CMNS/DatesAndTimes/Duration.md)
- has-fixed-dividend-rate: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
