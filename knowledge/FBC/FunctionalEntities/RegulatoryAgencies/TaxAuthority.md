---
type: FIBO Class
title: "tax authority"
description: "regulatory agency that has jurisdiction over the assessment, determination, collection, imposition and other aspects of any tax"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/TaxAuthority
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: has-jurisdiction, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: issues, target: "/FND/Parties/Parties/TaxIdentifier.md", provenance: fibo}
  - {type: manages, target: "/FND/Parties/Parties/TaxIdentificationScheme.md", provenance: fibo}
---

regulatory agency that has jurisdiction over the assessment, determination, collection, imposition and other aspects of any tax

### Relationships
- is-a: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- has-jurisdiction: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- issues: [TaxIdentifier](/FND/Parties/Parties/TaxIdentifier.md)
- manages: [TaxIdentificationScheme](/FND/Parties/Parties/TaxIdentificationScheme.md)
