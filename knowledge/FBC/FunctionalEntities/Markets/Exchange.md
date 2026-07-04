---
type: FIBO Class
title: "exchange"
description: "any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
tags: [FBC, Release]
detail: "An exchange is typically a corporation or mutual organization that provides securities trading services, where securities may be bought and sold by third parties. As a facility, an exchange is also a place of trade associated with a particular site, i.e., stock exchange, regulated market such as an Electronic Trading Platform (ECN), or unregulated market, such as an Automated Trading System (ATS), or market data provider. Stock exchanges also provide facilities for the issue and redemption of securities as well as other financial instruments and capital events including the payment of income and dividends.  The securities traded on a stock exchange include: shares issued by companies, unit trusts, derivatives, pooled investment products and bonds. To be able to trade a security on a certain stock exchange, it has to be listed there. Usually there is a central location at least for recordkeeping, but trade is less and less linked to such a physical place, as modern markets are electronic networks, which gives them advantages of speed and cost of transactions. Trade on an exchange is by members only."
synonyms:
  - "market"
relations:
  - {type: is-a, target: "/CMNS/SitesAndFacilities/Facility.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FunctionalEntities/Markets/MarketIdentifier.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: operates-in-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: operates-in-municipality, target: "/CMNS/Locations/Municipality.md", provenance: fibo}
  - {type: provides, target: "/SEC/Securities/SecuritiesListings/ListingService.md", provenance: fibo}
---

any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange

### Relationships
- is-a: [Facility](/CMNS/SitesAndFacilities/Facility.md)
- is-identified-by: [MarketIdentifier](/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- is-managed-by: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- operates-in-country: [Country](/CMNS/Locations/Country.md)
- operates-in-municipality: [Municipality](/CMNS/Locations/Municipality.md)
- provides: [ListingService](/SEC/Securities/SecuritiesListings/ListingService.md)
