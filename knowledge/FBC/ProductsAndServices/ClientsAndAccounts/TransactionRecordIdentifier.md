---
type: FIBO Class
title: "transaction record identifier"
description: "unique identifier for record of transactions"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md", provenance: fibo}
---

unique identifier for record of transactions

### Relationships
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- identifies: [TransactionRecord](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)
