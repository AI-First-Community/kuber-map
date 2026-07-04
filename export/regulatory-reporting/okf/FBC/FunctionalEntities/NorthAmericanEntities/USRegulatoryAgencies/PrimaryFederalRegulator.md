---
type: FIBO Class
title: "primary federal regulator"
description: "federal regulatory agency that is designated as the main agency responsible for oversight of a given institution for an institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/PrimaryFederalRegulator
tags: [FBC, Release]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "The Office of the Comptroller of the Currency (OCC) as the primary federal regulator of a national bank."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md", provenance: fibo}
---

federal regulatory agency that is designated as the main agency responsible for oversight of a given institution for an institution

### Relationships
- is-a: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- is-played-by: [GovernmentBody](/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
