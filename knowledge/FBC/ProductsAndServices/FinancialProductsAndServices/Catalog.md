---
type: FIBO Class
title: "catalog"
description: "publication including a list of products available for sale with their descriptions and possibly prices"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/Publishers/Publication.md", provenance: fibo}
  - {type: describes, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
  - {type: is-identified-by, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
---

publication including a list of products available for sale with their descriptions and possibly prices

### Relationships
- is-a: [Publication](/BE/FunctionalEntities/Publishers/Publication.md)
- describes: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
- is-identified-by: [Identifier](/CMNS/Identifiers/Identifier.md)
