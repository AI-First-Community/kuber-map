---
type: FIBO Class
title: "transition loan"
description: "credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) designed to help a business or organization shift from carbon-intensive or environmentally harmful practices to more sustainable and environmentally friendly operations"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionLoan
tags: [LOAN, Release]
relations:
  - {type: has-schedule, target: "/FND/Agreements/Contracts/MilestoneSchedule.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/DisclosureProvision.md", provenance: fibo}
  - {type: has-contractual-element, target: "/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision.md", provenance: fibo}
  - {type: has-strategy, target: "/LOAN/LoansSpecific/GreenLoans/TransitionStrategy.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md", provenance: fibo}
  - {type: has-milestone-provision, target: "/FND/Agreements/Contracts/ContractMilestone.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md", provenance: fibo}
---

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) designed to help a business or organization shift from carbon-intensive or environmentally harmful practices to more sustainable and environmentally friendly operations

### Relationships
- has-schedule: [MilestoneSchedule](/FND/Agreements/Contracts/MilestoneSchedule.md)
- has-contractual-element: [DisclosureProvision](/FND/Agreements/Contracts/DisclosureProvision.md)
- has-contractual-element: [TransitionUseOfProceedsProvision](/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision.md)
- has-strategy: [TransitionStrategy](/LOAN/LoansSpecific/GreenLoans/TransitionStrategy.md)
- is-a: [CommercialLoan](/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)
- has-milestone-provision: [ContractMilestone](/FND/Agreements/Contracts/ContractMilestone.md)
- is-a: [CreditAgreementRepaidPeriodically](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
