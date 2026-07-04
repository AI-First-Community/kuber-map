---
type: FIBO Class
title: "bank identifier"
description: "identifier that uniquely identifies the financial institution and, when appropriate, the branch of that financial institution servicing an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

identifier that uniquely identifies the financial institution and, when appropriate, the branch of that financial institution servicing an account

### Relationships
- is-a: [FinancialServiceProviderIdentifier](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- identifies: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
