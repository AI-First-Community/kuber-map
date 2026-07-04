---
type: FIBO Class
title: "interest rate option"
description: "option that giving the buyer (holder) the right, but not the obligation, to receive a cash payment if market interest rate of a reference rate is higher or lower, depending on the option, than the strike rate of the option"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/InterestRateOption
tags: [DER, Release]
detail: "The amount of the payment will be based on the difference between the market rate on the exercise date and the strike rate, multiplied by the notional principal specified in the option contract, to calculate the total payment."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: has-strike-rate, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
---

option that giving the buyer (holder) the right, but not the obligation, to receive a cash payment if market interest rate of a reference rate is higher or lower, depending on the option, than the strike rate of the option

### Relationships
- is-a: [InterestRateDerivative](/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- has-strike-rate: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
