---
type: FIBO Class
title: "derivative settlement terms"
description: "settlement terms specifying additional details with respect to what is to be delivered when, to whom, under what conditions at the time of settlement"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeSettlementTerms
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: has-additional-costs, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-underlying-asset-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

settlement terms specifying additional details with respect to what is to be delivered when, to whom, under what conditions at the time of settlement

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- is-a: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- has-additional-costs: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-underlying-asset-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
