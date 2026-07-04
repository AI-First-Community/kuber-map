---
type: FIBO Class
title: "forward rate agreement"
description: "agreement to exchange an interest rate commitment on a notional amount at a future date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ForwardRateAgreement
tags: [DER, Release]
detail: "The FRA determines the rates to be used along with the termination date and notional value. FRAs are cash-settled with the payment based on the net difference between the interest rate of the contract and the floating rate in the market called the reference rate. The notional amount is not exchanged, but rather a cash amount based on the rate differentials and the notional value of the contract."
synonyms:
  - "FRA"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md", provenance: fibo}
---

agreement to exchange an interest rate commitment on a notional amount at a future date

### Relationships
- is-a: [InterestRateDerivative](/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)
