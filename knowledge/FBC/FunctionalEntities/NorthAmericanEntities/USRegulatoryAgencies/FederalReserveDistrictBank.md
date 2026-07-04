---
type: FIBO Class
title: "Federal Reserve district bank"
description: "Federal Reserve district and member bank, with jurisdiction over a specific region of the US, named for the city in which the reserve bank is located"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrictBank
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md", provenance: fibo}
  - {type: has-jurisdiction, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrict.md", provenance: fibo}
  - {type: is-part-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md", provenance: fibo}
---

Federal Reserve district and member bank, with jurisdiction over a specific region of the US, named for the city in which the reserve bank is located

### Relationships
- is-a: [CentralBank](/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank.md)
- is-a: [FederalReserveSystemMember](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveSystemMember.md)
- has-jurisdiction: [FederalReserveDistrict](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrict.md)
- is-part-of: [FederalReserveRegulatoryAgencyAndCentralBank](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank.md)
