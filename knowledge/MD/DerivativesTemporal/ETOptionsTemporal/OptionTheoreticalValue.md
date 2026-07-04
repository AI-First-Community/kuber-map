---
type: FIBO Class
title: "option theoretical value"
description: "fair value of the option as determined by an option pricing model"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionTheoreticalValue
tags: [MD, Provisional]
detail: "The pricing model (such as the Black-Scholes model) takes into account current values such as implied volatility, the price of the underlying, the strike price, and time to expiration to determine what an option should be worth. Each of the input values fluctuate, which means theoretical price will also be a fluctuating value."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md", provenance: fibo}
---

fair value of the option as determined by an option pricing model

### Relationships
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- refers-to: [PricingModel](/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md)
