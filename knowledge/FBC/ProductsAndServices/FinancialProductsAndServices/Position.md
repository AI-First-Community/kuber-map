---
type: FIBO Class
title: "position"
description: "investor's stake, i.e., a holding, in a particular asset (such as an individual security)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Position
tags: [FBC, Release]
detail: "A position can be long or short, and it can be in any asset class, such as stocks, bonds, futures, or options. A position can be open (current) or closed (past), but in general use, unless a position is specifically referred to as closed, the assumption is that it references an open position."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Holding.md", provenance: fibo}
---

investor's stake, i.e., a holding, in a particular asset (such as an individual security)

### Relationships
- is-a: [Holding](/FBC/ProductsAndServices/FinancialProductsAndServices/Holding.md)
