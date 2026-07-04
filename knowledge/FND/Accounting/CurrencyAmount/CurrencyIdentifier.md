---
type: FIBO Class
title: "currency identifier"
description: "sequence of characters representing some currency"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier
tags: [FND, Release]
detail: "The first (left-most) two characters of the ISO 4217 3-letter currency identifier relate to the currency authority that issues the currency, and is, in most cases the ISO 3166-1 alpha 2 code for the geopolitical entity whose central bank is the issuer. The third (right-most) character of the identifier (alphabetic code) is an indicator derived from the name of the major currency unit or fund. If the currency is not associated with a single geographical entity as described in ISO 3166-1, typically a specially allocated identifier (alpha-2 code) is used to describe the currency authority. This code has been allocated by the Maintenance Agency from within the user-assigned range of codes XA to XZ specified in 8.1.3 of ISO 3166-1:2013. The character following X will be a mnemonic, where possible, derived from the name of the geographical area concerned."
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

sequence of characters representing some currency

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
