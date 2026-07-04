---
type: FIBO Class
title: "ordinary dividend"
description: "dividend that is paid to shareholders periodically"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/OrdinaryDividend
tags: [SEC, Release]
detail: "Most dividends are considered ordinary, unless they are specifically designated as qualified dividends. Note that the terms related to ordinary dividend payment are typically specified in the context of a board resolution rather than contractually."
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Dividend.md", provenance: fibo}
  - {type: has-payment-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

dividend that is paid to shareholders periodically

### Relationships
- is-a: [Dividend](/SEC/Equities/EquityInstruments/Dividend.md)
- has-payment-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
