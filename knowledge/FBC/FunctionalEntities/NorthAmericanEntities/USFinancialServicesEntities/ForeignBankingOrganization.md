---
type: FIBO Class
title: "foreign banking organization"
description: "financial service provider that is headquartered outside the United States and that can acquire or establish freestanding banks or bank holding companies in the United States"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBankingOrganization
tags: [FBC, Release]
detail: "Foreign banking organization means:  (1) A foreign bank, as defined in section 1(b)(7) of the International Banking Act of 1978 (12 U.S.C. 3101(7)), that:  	(i) Operates a branch, agency, or commercial lending company subsidiary in the United States;  	(ii) Controls a bank in the United States; or  	(iii) Controls an Edge corporation acquired after March 5, 1987; and  (2) Any company of which the foreign bank is a subsidiary. These entities are regulated and supervised as domestic institutions."
synonyms:
  - "FBO"
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
