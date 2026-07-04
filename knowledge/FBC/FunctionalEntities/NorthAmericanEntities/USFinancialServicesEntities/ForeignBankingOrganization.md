---
type: FIBO Class
title: "foreign banking organization"
description: "financial service provider that is headquartered outside the United States and that can acquire or establish freestanding banks or bank holding companies in the United States"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBankingOrganization
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: has-home-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: has-home-country-supervisor, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBO.md", provenance: fibo}
---

financial service provider that is headquartered outside the United States and that can acquire or establish freestanding banks or bank holding companies in the United States

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- has-home-country: [Country](/CMNS/Locations/Country.md)
- has-home-country-supervisor: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- is-classified-by: [NICEntityTypeClassifier-FBO](/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBO.md)
