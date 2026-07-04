---
type: FIBO Class
title: "deposit account"
description: "account that provides a record of money placed with a depository institution for safekeeping and management"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md", provenance: fibo}
---

account that provides a record of money placed with a depository institution for safekeeping and management

### Relationships
- is-a: [BankingProduct](/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct.md)
- is-a: [InvestmentOrDepositAccount](/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md)
- is-provided-by: [DepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)
