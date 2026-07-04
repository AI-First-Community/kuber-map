---
type: FIBO Class
title: "borrower disclosure requirement"
description: "Disclosure requirement obliging a lender to give a borrower specified information about a loan product, conferring the borrower's product disclosure right."
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "In the US these are implemented through the TILA-RESPA Integrated Disclosure (TRID) rule, giving borrowers standardized Loan Estimate and Closing Disclosure documents."
detail_provenance: curated
examples:
  - "The requirement to give a borrower a Loan Estimate within three business days of application."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md", provenance: fibo}
  - {type: confers, target: "/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight.md", provenance: fibo}
  - {type: governs, target: "/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md", provenance: fibo}
---

Disclosure requirement obliging a lender to give a borrower specified information about a loan product, conferring the borrower's product disclosure right.

### Relationships
- is-a: [DisclosureRequirement](/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md)
- confers: [ProductDisclosureRight](/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight.md)
- governs: [BorrowerAssessment](/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md)
