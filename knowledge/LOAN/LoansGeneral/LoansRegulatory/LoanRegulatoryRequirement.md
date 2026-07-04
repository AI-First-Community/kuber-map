---
type: FIBO Class
title: "loan regulatory requirement"
description: "A regulatory requirement defined in regulations by a comsumer credit act or other legislation."
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanRegulatoryRequirement
tags: [LOAN, Provisional]
core: true
detail: "Presence of a loan regulatory requirement associated with a loan indicates that the loan is regulated by the UK Consumer credit act or the equivalent in continental Europe."
examples:
  - "Ability-to-Repay / Qualified Mortgage rules"
  - "HMDA data collection"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalObligation.md", provenance: fibo}
  - {type: administered-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: is-mandated-by, target: "/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw.md", provenance: fibo}
  - {type: regulates, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
---

A regulatory requirement defined in regulations by a comsumer credit act or other legislation.

### Relationships
- is-a: [LegalObligation](/FND/Law/LegalCapacity/LegalObligation.md)
- administered-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- is-mandated-by: [ConsumerCreditProtectionLaw](/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw.md)
- regulates: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
