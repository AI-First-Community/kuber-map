---
type: FIBO Class
title: "knock-out option"
description: "barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset is reached"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockOutOption
tags: [DER, Release]
detail: "A knock-out option sets a cap on the level an option can reach in the holder's favor. As knock-out options limit the profit potential for the option buyer, they can be purchased for a smaller premium than an equivalent option without a knock-out stipulation."
examples:
  - "Assume an investor purchases a Knock-Out call option with a down Direction, also called a 'Down and Out Option', on a stock that is trading at $60 with a strike price of $55 and a barrier of $50. Assume the stock trades below $50, at any time, before the call option expires. Therefore, the down-and-out call option promptly ceases to exist."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/ExoticOptions/BarrierOption.md", provenance: fibo}
  - {type: has-first-barrier-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-first-rebate-amount, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset is reached

### Relationships
- is-a: [BarrierOption](/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- has-first-barrier-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-first-rebate-amount: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
