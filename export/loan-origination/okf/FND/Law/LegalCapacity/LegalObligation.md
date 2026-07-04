---
type: FIBO Class
title: "legal obligation"
description: "an obligation or duty that is enforceable by a court"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
tags: [FND, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "The borrower's court-enforceable duty to repay under the credit agreement; failure gives the lender legal remedies, including foreclosure of the collateral."
detail_provenance: curated
examples:
  - "A covered lender's legal obligation to file a HMDA report each year."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/Duty.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

an obligation or duty that is enforceable by a court

### Relationships
- is-a: [Duty](/FND/Law/LegalCapacity/Duty.md)
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
