---
type: FIBO Class
title: "green loan"
description: "credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) made available exclusively to finance, re-finance or guarantee, in whole or in part, new and/or existing eligible green projects that are aligned to the four core components of the Green Loan Principles (GLP)"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenLoan
tags: [LOAN, Release]
examples:
  - "Example categories of eligibility contained in the LMA's Green Loan Principles (GLP) include loans designed to facilitate renewable energy, energy efficiency, climate change adaptation and green buildings that meet regional, national or internationally recognised standards or certifications."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/DisclosureProvision.md", provenance: fibo}
  - {type: has-contractual-element, target: "/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision.md", provenance: fibo}
  - {type: has-milestone-provision, target: "/FND/Agreements/Contracts/ContractMilestone.md", provenance: fibo}
  - {type: has-schedule, target: "/FND/Agreements/Contracts/MilestoneSchedule.md", provenance: fibo}
---

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) made available exclusively to finance, re-finance or guarantee, in whole or in part, new and/or existing eligible green projects that are aligned to the four core components of the Green Loan Principles (GLP)

### Relationships
- is-a: [CreditAgreementRepaidPeriodically](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- has-contractual-element: [DisclosureProvision](/FND/Agreements/Contracts/DisclosureProvision.md)
- has-contractual-element: [GreenProjectUseOfProceedsProvision](/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision.md)
- has-milestone-provision: [ContractMilestone](/FND/Agreements/Contracts/ContractMilestone.md)
- has-schedule: [MilestoneSchedule](/FND/Agreements/Contracts/MilestoneSchedule.md)
