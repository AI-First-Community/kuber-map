---
type: FIBO Class
title: "reg z"
description: "US Fed regulation 'Truth in Lending Act' uniform standards for electronic delivery of disclosures"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/RegZ
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "Creditors may delivery disclosures electronic if they obtain consumer's consent. Also relate to international, and foreign languages. This is disclosures about the Product."
examples:
  - "Regulation Z, implementing the US Truth in Lending Act."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement.md", provenance: fibo}
---

US Fed regulation "Truth in Lending Act" uniform standards for electronic delivery of disclosures

### Relationships
- is-a: [ProductDisclosureRequirement](/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement.md)
