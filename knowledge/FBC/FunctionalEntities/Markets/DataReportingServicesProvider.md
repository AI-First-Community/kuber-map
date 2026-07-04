---
type: FIBO Class
title: "data reporting services provider"
description: "market data provider and reporting party that reports and/or publishes data on securities transactions, including required regulatory reporting for such transactions, and as such is subject to regulatory supervision"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider
tags: [FBC, Release]
synonyms:
  - "DRSP"
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/Publishers/MarketDataProvider.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Reporting/ReportingParty.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FunctionalEntities/Markets/MarketIdentifier.md", provenance: fibo}
  - {type: operates-in-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: operates-in-municipality, target: "/CMNS/Locations/Municipality.md", provenance: fibo}
---

market data provider and reporting party that reports and/or publishes data on securities transactions, including required regulatory reporting for such transactions, and as such is subject to regulatory supervision

### Relationships
- is-a: [MarketDataProvider](/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
- is-a: [ReportingParty](/FND/Arrangements/Reporting/ReportingParty.md)
- is-identified-by: [MarketIdentifier](/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- operates-in-country: [Country](/CMNS/Locations/Country.md)
- operates-in-municipality: [Municipality](/CMNS/Locations/Municipality.md)
