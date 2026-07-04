---
type: FIBO Class
title: "regulation identifier"
description: "an identifier associated with a regulation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/Law/LegalCapacity/Regulation.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme.md", provenance: fibo}
---

an identifier associated with a regulation

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Regulation](/FND/Law/LegalCapacity/Regulation.md)
- is-member-of: [RegulationIdentificationScheme](/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme.md)
