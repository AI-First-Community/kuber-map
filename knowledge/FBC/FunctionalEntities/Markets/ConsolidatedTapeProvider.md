---
type: FIBO Class
title: "consolidated tape provider"
description: "data reporting services provider that is authorized to provide the service of collecting trade reports for financial instruments from regulated markets, MTFs, OTFs and APAs and consolidating them into a continuous electronic live data stream providing price and volume data per financial instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ConsolidatedTapeProvider
tags: [FBC, Release]
detail: "Consolidated tape is an electronic system that collates real-time exchange-listed data, such as price and volume, and disseminates it to investors. Through the consolidated tape, various major exchanges, including the New York Stock Exchange, the NASDAQ, and the Chicago Board Options Exchange, report trades and quotes."
synonyms:
  - "CTP"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CTPS.md", provenance: fibo}
---

data reporting services provider that is authorized to provide the service of collecting trade reports for financial instruments from regulated markets, MTFs, OTFs and APAs and consolidating them into a continuous electronic live data stream providing price and volume data per financial instrument

### Relationships
- is-a: [DataReportingServicesProvider](/FBC/FunctionalEntities/Markets/DataReportingServicesProvider.md)
- is-classified-by: [MarketCategoryClassifier-CTPS](/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CTPS.md)
