---
type: FIBO Class
title: "banking service"
description: "financial service offered by a depository institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankingService
tags: [FBC, Release]
examples:
  - "Examples include cash management service, foreign exchange service, lending or credit service, investment service, insurance service, merchant service, payroll service, and the like."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md", provenance: fibo}
---

financial service offered by a depository institution

### Relationships
- is-a: [FinancialService](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
- is-provided-by: [DepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)
