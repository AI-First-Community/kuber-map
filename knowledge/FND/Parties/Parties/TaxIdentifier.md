---
type: FIBO Class
title: "tax identifier"
description: "identifier assigned to a taxpayer that enables compulsory financial charges and other levies to be imposed on the taxpayer by a governmental organization in order to fund government spending and various public expenditures"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier
tags: [FND, Release]
detail: "Tax identifiers are used for various tax-related purposes in the United States and in other countries under the Common Reporting Standard (CRS)."
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FND/Parties/Parties/TaxIdentificationScheme.md", provenance: fibo}
---

identifier assigned to a taxpayer that enables compulsory financial charges and other levies to be imposed on the taxpayer by a governmental organization in order to fund government spending and various public expenditures

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [Party](/CMNS/PartiesAndSituations/Party.md)
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-member-of: [TaxIdentificationScheme](/FND/Parties/Parties/TaxIdentificationScheme.md)
