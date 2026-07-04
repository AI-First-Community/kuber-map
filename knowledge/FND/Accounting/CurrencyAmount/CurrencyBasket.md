---
type: FIBO Class
title: "currency basket"
description: "selected group of currencies, in which the weighted average is used as a measure of the value or the amount of an obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyBasket
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

selected group of currencies, in which the weighted average is used as a measure of the value or the amount of an obligation

### Relationships
- is-a: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
- has-member: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
