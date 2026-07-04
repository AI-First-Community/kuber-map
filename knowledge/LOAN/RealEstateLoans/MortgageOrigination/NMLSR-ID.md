---
type: FIBO Class
title: "Nationwide Mortgage Licensing System and Registry Identifier"
description: "the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS."
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID
tags: [LOAN, Provisional]
core: true
examples:
  - "NMLS #1234567 assigned to a licensed mortgage loan originator."
examples_provenance: curated
synonyms:
  - "NMLSR ID"
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LicenseIdentifier.md", provenance: fibo}
---

the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.

### Relationships
- is-a: [LicenseIdentifier](/FND/Law/LegalCapacity/LicenseIdentifier.md)
