---
type: FIBO Class
title: "precious metal identifier"
description: "sequence of characters uniquely identifying the precious metal in some context"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetalIdentifier
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/Accounting/CurrencyAmount/PreciousMetal.md", provenance: fibo}
---

sequence of characters uniquely identifying the precious metal in some context

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [PreciousMetal](/FND/Accounting/CurrencyAmount/PreciousMetal.md)
