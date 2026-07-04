---
type: FIBO Class
title: "currency identifier"
description: "sequence of characters representing some currency"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyIdentifier
tags: [FND, Release]
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
