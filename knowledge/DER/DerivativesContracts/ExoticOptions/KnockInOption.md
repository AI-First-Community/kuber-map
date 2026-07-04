---
type: FIBO Class
title: "knock-in option"
description: "barrier option that is not triggered until a certain price threshold is met"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockInOption
tags: [DER, Release]
detail: "If the price is never reached, it is as if the contract never existed. However, if the underlying asset reaches a specified barrier, the knock-in option comes into existence. The difference between a knock-in and knock-out option is that a knock-in option comes into existence only when the underlying security reaches a barrier, while a knock-out option ceases to exist when the underlying security reaches a barrier."
examples:
  - "Assume an investor purchases a knock-in put option with a down Direction, with a barrier price of $90 and a strike price of $100. The underlying security is trading at $110, and the option expires in three months. If the price of the underlying security reaches $90, the option comes into existence and becomes a vanilla option with a strike price of $100. Thereafter, the holder of the option has the right to sell the underlying asset at the strike price of $100, even though it is trading below $90. It is this right that gives the option value. The put option remains active until the expiration date, even if the underlying security rebounds back above $90. However, if the underlying asset does not fall below the barrier price during the life of the contract, the down-and-in option expires worthless. Just because the barrier is reached does not assure a profit on the trade since the underlying would need to stay below $100 (after triggering the barrier) in order for the option to have value."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/ExoticOptions/BarrierOption.md", provenance: fibo}
  - {type: has-first-barrier-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-first-rebate-amount, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

barrier option that is not triggered until a certain price threshold is met

### Relationships
- is-a: [BarrierOption](/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- has-first-barrier-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-first-rebate-amount: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
