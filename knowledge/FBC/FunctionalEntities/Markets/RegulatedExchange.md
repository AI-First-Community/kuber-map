---
type: FIBO Class
title: "regulated exchange"
description: "regulated market that is operated by and/or managed by a market operator that brings together or facilitates the bringing together of multiple third-party buying and selling interests in financial instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
tags: [FBC, Release]
detail: "In the financial community in the EU, such an exchange operates in accordance with its non-discretionary rules in a way that results in a contract, in respect of the financial instruments admitted to trading under its rules and/or systems, and which is authorised and functions regularly and in accordance with the provisions of Title III of MiFID II."
synonyms:
  - "RM"
  - "regulated market"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-RMKT.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-regulated-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
---

regulated market that is operated by and/or managed by a market operator that brings together or facilitates the bringing together of multiple third-party buying and selling interests in financial instruments

### Relationships
- is-a: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-classified-by: [MarketCategoryClassifier-RMKT](/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-RMKT.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-regulated-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
