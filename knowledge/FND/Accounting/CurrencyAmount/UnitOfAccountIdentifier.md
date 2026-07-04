---
type: FIBO Class
title: "unit of account identifier"
description: "sequence of characters that can be used to uniquely identify a nominal monetary unit"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/UnitOfAccountIdentifier
tags: [FND, Release]
relations:
  - {type: identifies, target: "/FND/Accounting/CurrencyAmount/UnitOfAccount.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
---

sequence of characters that can be used to uniquely identify a nominal monetary unit

### Relationships
- identifies: [UnitOfAccount](/FND/Accounting/CurrencyAmount/UnitOfAccount.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
