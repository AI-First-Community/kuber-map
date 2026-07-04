---
type: FIBO Class
title: "mini-future certificate"
description: "entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, and whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate
tags: [DER, Release]
detail: "The price of a mini-future always corresponds to its intrinsic value, i.e. the capital outlay, plus the bid-ask spread. The financing costs associated with building up the leverage effect are offset against the capital outlay on a daily basis, thereby eliminating the need for a premium. Investors have to pay only financing costs they actually utilize. In contrast to options, factors like volatility have no influence at all on the price of mini-futures."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/ExoticOptions/BarrierOption.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md", provenance: fibo}
---

entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, and whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price

### Relationships
- is-a: [BarrierOption](/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- is-a: [SecurityBasedDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)
- is-a: [Entitlement](/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
