---
type: FIBO Class
title: "financial holding company"
description: "financial entity engaged in a broad range of banking-related activities as permitted under the Gramm-Leach-Bliley Act of 1999"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FinancialHoldingCompany
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md", provenance: fibo}
  - {type: has-primary-federal-regulator, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FHD.md", provenance: fibo}
---

financial entity engaged in a broad range of banking-related activities as permitted under the Gramm-Leach-Bliley Act of 1999

### Relationships
- is-a: [BankHoldingCompany](/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md)
- has-primary-federal-regulator: [BoardOfGovernorsOfTheFederalReserveSystem](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem.md)
- is-classified-by: [NICEntityTypeClassifier-FHD](/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FHD.md)
