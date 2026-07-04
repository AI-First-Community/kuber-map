---
type: FIBO Class
title: "borrower disclosure requirement"
description: "regulatory requirement that a lender disclose specified information to a borrower or prospective borrower — such as the terms and costs of a loan product — conferring a corresponding right to that information and governing how the borrower is assessed"
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement
tags: [LOAN, Provisional]
core: true
examples:
  - "The TILA-RESPA (TRID) Loan Estimate a lender must give within 3 business days."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md", provenance: fibo}
  - {type: confers, target: "/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight.md", provenance: fibo}
  - {type: governs, target: "/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md", provenance: fibo}
---

regulatory requirement that a lender disclose specified information to a borrower or prospective borrower — such as the terms and costs of a loan product — conferring a corresponding right to that information and governing how the borrower is assessed

### Relationships
- is-a: [DisclosureRequirement](/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md)
- confers: [ProductDisclosureRight](/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight.md)
- governs: [BorrowerAssessment](/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md)
