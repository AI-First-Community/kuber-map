---
type: FIBO Class
title: "fund position"
description: "position in some fund, which may be defined in terms of fund units"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundPosition
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md", provenance: fibo}
  - {type: has-owned-asset, target: "/SEC/Funds/Funds/FundHolding.md", provenance: fibo}
  - {type: has-owning-party, target: "/SEC/Funds/Funds/FundHolder.md", provenance: fibo}
---

position in some fund, which may be defined in terms of fund units

### Relationships
- is-a: [Position](/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md)
- has-owned-asset: [FundHolding](/SEC/Funds/Funds/FundHolding.md)
- has-owning-party: [FundHolder](/SEC/Funds/Funds/FundHolder.md)
