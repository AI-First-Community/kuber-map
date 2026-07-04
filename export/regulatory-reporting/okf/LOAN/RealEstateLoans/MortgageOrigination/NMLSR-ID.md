---
type: FIBO Class
title: "Nationwide Mortgage Licensing System and Registry Identifier"
description: "the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS."
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "The NMLS identifier uniquely identifies licensed mortgage companies and loan originators; it appears on loan documents to support accountability."
detail_provenance: curated
examples:
  - "The unique identifier a mortgage loan originator holds in the NMLS registry."
examples_provenance: curated
synonyms:
  - "NMLSR ID"
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LicenseIdentifier.md", provenance: fibo}
---

the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.

### Relationships
- is-a: [LicenseIdentifier](/FND/Law/LegalCapacity/LicenseIdentifier.md)
