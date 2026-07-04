---
type: FIBO Class
title: "listing service"
description: "service provided by an exchange to facilitate securities trading"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListingService
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-provisioned-by, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: provides, target: "/SEC/Securities/SecuritiesListings/Listing.md", provenance: fibo}
---

service provided by an exchange to facilitate securities trading

### Relationships
- is-a: [FinancialService](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
- is-provided-by: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-provisioned-by: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- provides: [Listing](/SEC/Securities/SecuritiesListings/Listing.md)
