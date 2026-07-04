---
type: FIBO Class
title: "funds identifier"
description: "sequence of characters that can be used to uniquely identify funds"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/FundsIdentifier
tags: [FND, Release]
relations:
  - {type: identifies, target: "/FND/Accounting/CurrencyAmount/Funds.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
---

sequence of characters that can be used to uniquely identify funds

### Relationships
- identifies: [Funds](/FND/Accounting/CurrencyAmount/Funds.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
