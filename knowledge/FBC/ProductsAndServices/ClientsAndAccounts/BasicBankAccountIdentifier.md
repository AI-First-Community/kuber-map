---
type: FIBO Class
title: "basic bank account identifier"
description: "identifier that uniquely identifies an individual account at a specific financial institution in a particular country and which includes a bank identifier of the financial institution servicing that account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/StructuredIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier.md", provenance: fibo}
---

identifier that uniquely identifies an individual account at a specific financial institution in a particular country and which includes a bank identifier of the financial institution servicing that account

### Relationships
- is-a: [BankAccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- is-a: [StructuredIdentifier](/CMNS/ContextualIdentifiers/StructuredIdentifier.md)
- comprises: [BankAccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- comprises: [BankIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/BankIdentifier.md)
