---
type: FIBO Class
title: "equity position"
description: "position in an equity instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityPosition
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md", provenance: fibo}
  - {type: has-owned-asset, target: "/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md", provenance: fibo}
  - {type: has-owning-party, target: "/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md", provenance: fibo}
---

position in an equity instrument

### Relationships
- is-a: [Position](/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md)
- has-owned-asset: [Shareholding](/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md)
- has-owning-party: [Shareholder](/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)
