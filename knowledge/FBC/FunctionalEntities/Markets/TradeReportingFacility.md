---
type: FIBO Class
title: "trade reporting facility"
description: "facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/TradeReportingFacility
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/SitesAndFacilities/Facility.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-TRFS.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FunctionalEntities/Markets/MarketIdentifier.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: operates-in-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: operates-in-municipality, target: "/CMNS/Locations/Municipality.md", provenance: fibo}
---

facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange

### Relationships
- is-a: [Facility](/CMNS/SitesAndFacilities/Facility.md)
- is-classified-by: [MarketCategoryClassifier-TRFS](/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-TRFS.md)
- is-identified-by: [MarketIdentifier](/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- is-managed-by: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- operates-in-country: [Country](/CMNS/Locations/Country.md)
- operates-in-municipality: [Municipality](/CMNS/Locations/Municipality.md)
