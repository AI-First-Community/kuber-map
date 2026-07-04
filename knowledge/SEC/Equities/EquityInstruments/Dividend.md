---
type: FIBO Class
title: "dividend"
description: "announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class of security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
tags: [SEC, Release]
core: true
detail: "The amount and timing of payment is set by the board of directors, typically quarterly. Dividends may be paid in the form of money, shares, scrip, or on rare occasion, property."
examples:
  - "A quarterly cash dividend of US$0.24 per share declared by a company's board."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: has-distribution-method, target: "/SEC/Equities/EquityInstruments/DividendDistributionMethod.md", provenance: fibo}
  - {type: has-payment-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-schedule, target: "/SEC/Equities/EquityInstruments/DividendSchedule.md", provenance: fibo}
---

announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class of security

### Relationships
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- has-distribution-method: [DividendDistributionMethod](/SEC/Equities/EquityInstruments/DividendDistributionMethod.md)
- has-payment-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-schedule: [DividendSchedule](/SEC/Equities/EquityInstruments/DividendSchedule.md)
