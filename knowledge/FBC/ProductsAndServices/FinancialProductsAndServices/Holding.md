---
type: FIBO Class
title: "holding"
description: "real or personal property (assets), including but not limited to financial assets, to which one holds title and of which one has possession"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Holding
tags: [FBC, Release]
detail: "Note that a holding may refer to a single asset, such as a piece of real estate, a portfolio of assets, multiple portfolios, and so forth, and is frequently aggregated over multiple assets."
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Ownership.md", provenance: fibo}
  - {type: has-owned-asset, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
---

real or personal property (assets), including but not limited to financial assets, to which one holds title and of which one has possession

### Relationships
- is-a: [Ownership](/FND/OwnershipAndControl/Ownership/Ownership.md)
- has-owned-asset: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
