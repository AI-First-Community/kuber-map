---
type: FIBO Class
title: "ownership interest"
description: "classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used as collateral for the loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OwnershipInterest
tags: [LOAN, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Note that there are a number of variations for ownership interest that represent 'corner cases', including jurisdiction-specific variants, which can be added as needed for specific applications."
examples:
  - "Fee simple ownership"
  - "Leasehold"
  - "Joint tenancy"
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/FND/OwnershipAndControl/Ownership/Ownership.md", provenance: fibo}
---

classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used as collateral for the loan

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [Ownership](/FND/OwnershipAndControl/Ownership/Ownership.md)
