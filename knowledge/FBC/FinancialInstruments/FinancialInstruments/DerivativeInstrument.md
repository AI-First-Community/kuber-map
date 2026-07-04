---
type: FIBO Class
title: "derivative instrument"
description: "financial instrument that confers on its holders certain rights or obligations, whose value is derived from one or more underlying assets"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
tags: [FBC, Release]
detail: "Derivative contracts owe their availability to the existence of markets for an underlying asset or a portfolio of assets on which such agreements are written. The derivative itself is merely a contract between two or more parties. Its value is determined by fluctuations in the underlying asset. Most derivatives are characterized by high leverage. Note that the quantity value associated with the derivative represents the quantity of the underlier. The price of the underlier is included in settlement terms."
examples:
  - "The three major categories of derivatives are (1) forward and future contracts, (2) options contracts, and (3) swaps. The most common underlying assets include stocks, bonds, commodities, currencies, interest rates and market indexes."
synonyms:
  - "derivative contract"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: has-expiration-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-initial-exchange-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: has-settlement-terms, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: has-underlier, target: "/FBC/FinancialInstruments/FinancialInstruments/Underlier.md", provenance: fibo}
  - {type: has-valuation-terms, target: "/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md", provenance: fibo}
---

financial instrument that confers on its holders certain rights or obligations, whose value is derived from one or more underlying assets

### Relationships
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- has-expiration-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-initial-exchange-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- has-settlement-terms: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- has-underlier: [Underlier](/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)
- has-valuation-terms: [ValuationTerms](/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md)
