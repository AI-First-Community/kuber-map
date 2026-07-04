---
type: FIBO Class
title: "international bank account identifier"
description: "identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for use internationally"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InternationalBankAccountIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/StructuredIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/CMNS/Locations/GeographicRegionIdentifier.md", provenance: fibo}
---

identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for use internationally

### Relationships
- is-a: [BankAccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/BankAccountIdentifier.md)
- is-a: [StructuredIdentifier](/CMNS/ContextualIdentifiers/StructuredIdentifier.md)
- comprises: [BasicBankAccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/BasicBankAccountIdentifier.md)
- comprises: [GeographicRegionIdentifier](/CMNS/Locations/GeographicRegionIdentifier.md)
