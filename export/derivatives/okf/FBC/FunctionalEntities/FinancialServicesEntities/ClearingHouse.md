---
type: FIBO Class
title: "clearing house"
description: "financial service provider that is exchange affiliated and provides clearing services, including the validation, delivery, and settlement of financial transactions, for financial intermediaries"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
tags: [FBC, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A central counterparty such as LCH that clears interest-rate swaps."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: provides, target: "/FBC/FunctionalEntities/FinancialServicesEntities/ClearingService.md", provenance: fibo}
---

financial service provider that is exchange affiliated and provides clearing services, including the validation, delivery, and settlement of financial transactions, for financial intermediaries

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- provides: [ClearingService](/FBC/FunctionalEntities/FinancialServicesEntities/ClearingService.md)
