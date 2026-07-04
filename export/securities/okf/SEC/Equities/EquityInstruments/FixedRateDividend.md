---
type: FIBO Class
title: "fixed rate dividend"
description: "dividend that provides a specified annual return on the nominal value (and any premium) paid on shares"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FixedRateDividend
tags: [SEC, Release]
detail: "In other words, the return is not variable depending on whether or not the company makes a profit. Annual dividends are calculated as a percentage of the par value, which is the price of the preferred stock at the time it was issued. Most preferred shares have fixed rate dividends."
examples:
  - "A preferred share's fixed 6% annual dividend."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredDividend.md", provenance: fibo}
  - {type: has-fixed-dividend-rate, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

dividend that provides a specified annual return on the nominal value (and any premium) paid on shares

### Relationships
- is-a: [PreferredDividend](/SEC/Equities/EquityInstruments/PreferredDividend.md)
- has-fixed-dividend-rate: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
