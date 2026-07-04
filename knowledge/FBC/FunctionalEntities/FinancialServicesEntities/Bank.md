---
type: FIBO Class
title: "bank"
description: "depository institution, usually a corporation, that accepts deposits, makes loans, pays checks, and performs related services, for individual members of the public, businesses or other organizations"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md", provenance: fibo}
  - {type: provides, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CommercialLendingService.md", provenance: fibo}
  - {type: provides, target: "/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount.md", provenance: fibo}
---

depository institution, usually a corporation, that accepts deposits, makes loans, pays checks, and performs related services, for individual members of the public, businesses or other organizations

### Relationships
- is-a: [DepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)
- provides: [CommercialLendingService](/FBC/ProductsAndServices/ClientsAndAccounts/CommercialLendingService.md)
- provides: [DemandDepositAccount](/FBC/ProductsAndServices/ClientsAndAccounts/DemandDepositAccount.md)
