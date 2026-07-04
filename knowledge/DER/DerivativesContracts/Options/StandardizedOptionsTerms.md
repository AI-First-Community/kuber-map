---
type: FIBO Class
title: "standardized options terms"
description: "standardized contract terms established by a securities or options exchange or by an options clearing entity"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StandardizedOptionsTerms
tags: [DER, Release]
detail: "Such terms may relate to the underlying instruments, exercise price, expiration date, and contract size, for example."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md", provenance: fibo}
  - {type: applies-to, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: has-price-determination-method, target: "/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md", provenance: fibo}
---

standardized contract terms established by a securities or options exchange or by an options clearing entity

### Relationships
- is-a: [StandardizedTerms](/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)
- applies-to: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- has-price-determination-method: [PriceDeterminationMethod](/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
