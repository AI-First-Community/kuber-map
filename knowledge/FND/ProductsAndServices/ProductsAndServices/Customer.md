---
type: FIBO Class
title: "customer"
description: "party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Buyer.md", provenance: fibo}
  - {type: buys-from, target: "/FND/ProductsAndServices/ProductsAndServices/Supplier.md", provenance: fibo}
---

party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers

### Relationships
- is-a: [Buyer](/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- buys-from: [Supplier](/FND/ProductsAndServices/ProductsAndServices/Supplier.md)
