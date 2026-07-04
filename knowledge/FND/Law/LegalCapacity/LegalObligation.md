---
type: FIBO Class
title: "legal obligation"
description: "an obligation or duty that is enforceable by a court"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
tags: [FND, Release]
core: true
detail: "The borrower's court-enforceable duty to repay under the credit agreement; failure gives the lender legal remedies, including foreclosure of the collateral."
detail_provenance: curated
examples:
  - "The borrower's court-enforceable duty to repay the mortgage."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/Duty.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

an obligation or duty that is enforceable by a court

### Relationships
- is-a: [Duty](/FND/Law/LegalCapacity/Duty.md)
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
