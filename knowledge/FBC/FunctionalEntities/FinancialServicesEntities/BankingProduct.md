---
type: FIBO Class
title: "banking product"
description: "product provided to consumers and businesses by a depository institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct
tags: [FBC, Release]
examples:
  - "Examples include checking account, savings account, certificate of deposit, debit or pre-paid card, or credit card."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md", provenance: fibo}
---

product provided to consumers and businesses by a depository institution

### Relationships
- is-a: [FinancialProduct](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- is-provided-by: [DepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)
