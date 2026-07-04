---
type: FIBO Class
title: "consumer credit requirement"
description: "Requirement set out on the lender about how they must treat the appliction to a loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "e..g being able to see and challenge information about them held by the credit agency or lender. e.g. can't publish opinions only facts, etc."
examples:
  - "A requirement that consumer-credit advertising state the representative APR."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalObligation.md", provenance: fibo}
  - {type: confers, target: "/LOAN/LoansGeneral/LoansRegulatory/ConsumerRight.md", provenance: fibo}
  - {type: overseen-by, target: "/LOAN/LoansGeneral/LoansRegulatory/ConsumerProtectionAgency.md", provenance: fibo}
---

Requirement set out on the lender about how they must treat the appliction to a loan

### Relationships
- is-a: [LegalObligation](/FND/Law/LegalCapacity/LegalObligation.md)
- confers: [ConsumerRight](/LOAN/LoansGeneral/LoansRegulatory/ConsumerRight.md)
- overseen-by: [ConsumerProtectionAgency](/LOAN/LoansGeneral/LoansRegulatory/ConsumerProtectionAgency.md)
