---
type: FIBO Class
title: "national bank"
description: "commercial bank whose charter is approved by the Office of the Comptroller of the Currency (OCC) rather than by a state banking agency"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NationalBank
tags: [FBC, Release]
detail: "National Banks are required to be members of the Federal Reserve System and belong to the Federal Deposit Insurance Corporation."
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md", provenance: fibo}
  - {type: has-primary-federal-regulator, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalBankingRegulator.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NAT.md", provenance: fibo}
---

commercial bank whose charter is approved by the Office of the Comptroller of the Currency (OCC) rather than by a state banking agency

### Relationships
- is-a: [CommercialBank](/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md)
- is-a: [USBank](/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md)
- is-a: [FederalReserveSystemMember](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md)
- has-primary-federal-regulator: [NationalBankingRegulator](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalBankingRegulator.md)
- is-classified-by: [NICEntityTypeClassifier-NAT](/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-NAT.md)
