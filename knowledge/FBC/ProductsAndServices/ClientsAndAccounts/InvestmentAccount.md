---
type: FIBO Class
title: "investment account"
description: "account that provides a record of deposits of funds and/or securities held at a financial institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount
tags: [FBC, Release]
detail: "The typical objectives of an investment account are to achieve long term growth, income or capital preservation from the deposited asset portfolio. Investment accounts are typically not insured."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

account that provides a record of deposits of funds and/or securities held at a financial institution

### Relationships
- is-a: [InvestmentOrDepositAccount](/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md)
- is-provided-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
