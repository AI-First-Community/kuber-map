---
type: FIBO Class
title: "foreign bank"
description: "financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate, organized under such laws, of any such institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md", provenance: fibo}
  - {type: has-home-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: has-home-country-supervisor, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBK.md", provenance: fibo}
---

financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate, organized under such laws, of any such institution

### Relationships
- is-a: [Bank](/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)
- has-home-country: [Country](/CMNS/Locations/Country.md)
- has-home-country-supervisor: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- is-classified-by: [NICEntityTypeClassifier-FBK](/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBK.md)
