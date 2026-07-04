---
type: FIBO Class
title: "exchange"
description: "any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/SitesAndFacilities/Facility.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FunctionalEntities/Markets/MarketIdentifier.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: operates-in-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: operates-in-municipality, target: "/CMNS/Locations/Municipality.md", provenance: fibo}
---

any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange

### Relationships
- is-a: [Facility](/CMNS/SitesAndFacilities/Facility.md)
- is-identified-by: [MarketIdentifier](/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- is-managed-by: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- operates-in-country: [Country](/CMNS/Locations/Country.md)
- operates-in-municipality: [Municipality](/CMNS/Locations/Municipality.md)
