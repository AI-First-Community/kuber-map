---
type: FIBO Class
title: "fixed income option"
description: "option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying fixed income assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/FixedIncomeOption
tags: [DER, Release]
detail: "Fixed income options, or debt options, are derivatives contracts that use bonds or other fixed-income securities as their underlying asset."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md", provenance: fibo}
---

option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying fixed income assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)

### Relationships
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- is-a: [DebtInstrumentDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md)
