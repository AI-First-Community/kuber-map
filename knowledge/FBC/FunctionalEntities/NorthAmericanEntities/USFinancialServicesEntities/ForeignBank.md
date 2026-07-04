---
type: FIBO Class
title: "foreign bank"
description: "financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate, organized under such laws, of any such institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank
tags: [FBC, Release]
detail: "For the purposes of the International Banking Act of 1978, the term 'foreign bank' includes, without limitation, foreign commercial banks, foreign merchant banks and other foreign institutions that engage in banking activities usual in connection with the business of banking in the countries where such foreign institutions are organized or operating. Foreign bank means an organization that is organized under the laws of a foreign country and that engages directly in the business of banking outside the United States. The term foreign bank does not include a central bank of a foreign country that does not engage or seek to engage in a commercial banking business in the United States through an office."
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
