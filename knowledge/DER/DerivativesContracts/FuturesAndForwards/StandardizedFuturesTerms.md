---
type: FIBO Class
title: "standardized futures terms"
description: "contract terms established by a derivatives exchange that apply to any futures contract traded on that exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesTerms
tags: [DER, Release]
detail: "Standard symbology for the commodities are standardized by the exchanges as part of their standard contracts, for example trading in standard bushels, commonly defined kinds of oil and so on. These give the units in which lot sizes are described and defined."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Future.md", provenance: fibo}
  - {type: specifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
---

contract terms established by a derivatives exchange that apply to any futures contract traded on that exchange

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- is-a: [StandardizedTerms](/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)
- applies-to: [Future](/FBC/FinancialInstruments/FinancialInstruments/Future.md)
- specifies: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
