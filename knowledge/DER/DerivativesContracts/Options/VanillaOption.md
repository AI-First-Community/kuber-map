---
type: FIBO Class
title: "vanilla option"
description: "common option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
tags: [DER, Release]
detail: "Vanilla options include call or put options that have no special or unusual features, and are typically exchange traded."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
  - {type: has-contract-duration, target: "/CMNS/DatesAndTimes/ExplicitDuration.md", provenance: fibo}
  - {type: has-price-determination-method, target: "/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md", provenance: fibo}
---

common option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)

### Relationships
- is-a: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- has-contract-duration: [ExplicitDuration](/CMNS/DatesAndTimes/ExplicitDuration.md)
- has-price-determination-method: [PriceDeterminationMethod](/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
