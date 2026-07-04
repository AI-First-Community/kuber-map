---
type: FIBO Class
title: "organized trading facility"
description: "multi-lateral system which is not an RM or an MTF and in which multiple third-party buying and selling interests in bonds, structured finance products, emission allowances or derivatives are able to interact in the system in a way that results in a contract in accordance with the provisions of Title II of MiFID II"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility
tags: [FBC, Release]
detail: "OTFs were introduced by the European Commission as part of MiFID II and are focused on non-equities such as derivatives and cash bond markets.  OTFs are intended to be similar in scope to a swap execution facility (SEF), a type of entity created by the Dodd-Frank Act in the U.S. The goal of SEFs and OTFs is to bring transparency and structure to OTC derivatives trading. Unlike RMs and MTFs, operators of OTFs will have discretion as to how to execute orders, subject to pre-transparency and best execution obligations."
synonyms:
  - "OTF"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-OTFS.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
---

multi-lateral system which is not an RM or an MTF and in which multiple third-party buying and selling interests in bonds, structured finance products, emission allowances or derivatives are able to interact in the system in a way that results in a contract in accordance with the provisions of Title II of MiFID II

### Relationships
- is-a: [AlternativeTradingSystem](/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md)
- is-classified-by: [MarketCategoryClassifier-OTFS](/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-OTFS.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-managed-by: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
