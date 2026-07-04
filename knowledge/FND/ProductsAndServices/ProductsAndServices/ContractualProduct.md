---
type: FIBO Class
title: "contractual product"
description: "product that takes the form of an agreement"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ContractualProduct
tags: [FND, Release]
detail: "This represents the case where the product itself is a contract, such as a life insurance policy or financial instrument, rather than a product or service whose terms of use, license to use, or terms of service are specified in a product."
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
  - {type: is-exemplified-by, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
---

product that takes the form of an agreement

### Relationships
- is-a: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
- is-exemplified-by: [Contract](/FND/Agreements/Contracts/Contract.md)
