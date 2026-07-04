---
type: FIBO Class
title: "strike price"
description: "price at which a lot of the underlying asset may be bought or sold when the contract is exercised"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "For call options, the strike price is the price at which the security may be purchased by the option holder; for put options, the strike price is the price at which the security may be sold."
examples:
  - "The $200 strike at which an Apple call may be exercised."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

price at which a lot of the underlying asset may be bought or sold when the contract is exercised

### Relationships
- is-a: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
