---
type: FIBO Class
title: "capped option"
description: "option with an established profit cap or cap price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CappedOption
tags: [DER, Release]
detail: "The cap price is equal to the option's strike price plus a cap interval for a call option or the strike price minus a cap interval for a put option. A capped option is automatically exercised when the underlying security closes at or above (for a call) or at or below (for a put) the option's cap price."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: has-cap-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

option with an established profit cap or cap price

### Relationships
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- has-cap-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
