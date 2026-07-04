---
type: FIBO Class
title: "double barrier option"
description: "barrier option applied to currencies or over the counter stocks that works as a binary, or digital option in that it pays out only under defined circumstances, or it is worthless, at expiration"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DoubleBarrierOption
tags: [DER, Release]
detail: "Considered an exotic option, a double barrier option is a combination of two single barrier options, with one barrier above and one barrier below the current price of the underlying. It is a bet by the holder that the underlying asset will move significantly, in the case of a knock-in barrier option, or will move by a very small amount, in the case of a knock-out barrier option, over the life of the contract. Traders use these options when they have an opinion on volatility but not on the direction of the underlying asset's next price move. A barrier option is a type of option where the payoff, and the very existence of the option, depends on whether or not the underlying asset reaches a predetermined price."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/ExoticOptions/BarrierOption.md", provenance: fibo}
  - {type: has-first-barrier-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-first-rebate-amount, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: has-second-barrier-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-second-rebate-amount, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

barrier option applied to currencies or over the counter stocks that works as a binary, or digital option in that it pays out only under defined circumstances, or it is worthless, at expiration

### Relationships
- is-a: [BarrierOption](/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- has-first-barrier-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-first-rebate-amount: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- has-second-barrier-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-second-rebate-amount: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
