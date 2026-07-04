---
type: FIBO Class
title: "international bank account identifier"
description: "identifier for a bank account that is an expanded version of the basic bank account number (BBAN), intended for use internationally"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InternationalBankAccountIdentifier
tags: [FBC, Release]
detail: "Note that international bank account numbers are formatted uniquely by country. A description of the country-specific formats is available from SWIFT (https://www.swift.com/), which is the ISO registrar for ISO 13616. The IBAN structure is defined in ISO 13616-1 and consists of a two-letter ISO 3166-1 country code, followed by two check digits and up to thirty alphanumeric characters for a BBAN (Basic Bank Account Number) which has a fixed length per country and, included within it, a bank identifier with a fixed position and a fixed length per country. The check digits are calculated based on the scheme defined in ISO/IEC 7064 (MOD97-10)."
examples:
  - "For an account in Switzerland, suppose that an example domestic account number is 762 1162-3852.957. Suppose further that the bank identifier portion of that domestic account number is 762, or normalized for the BBAN is '00762'. For that example, the corresponding BBAN is '00762011623852957' and IBAN is 'CH9300762011623852957'."
synonyms:
  - "IBAN"
  - "international bank account number"
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
