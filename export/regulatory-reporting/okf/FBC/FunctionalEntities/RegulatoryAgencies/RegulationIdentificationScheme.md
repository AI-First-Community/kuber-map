---
type: FIBO Class
title: "regulation identification scheme"
description: "a scheme for organizing information and allocating identifiers to regulations"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme
tags: [FBC, Release]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "The 'Regulation A/B/C…' labelling scheme used to identify US Federal Reserve regulations."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Identifiers/IdentificationScheme.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier.md", provenance: fibo}
---

a scheme for organizing information and allocating identifiers to regulations

### Relationships
- is-a: [IdentificationScheme](/CMNS/Identifiers/IdentificationScheme.md)
- has-member: [RegulationIdentifier](/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier.md)
