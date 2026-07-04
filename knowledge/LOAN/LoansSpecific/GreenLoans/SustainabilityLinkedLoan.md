---
type: FIBO Class
title: "sustainability-linked loan"
description: "credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) for which the economic characteristics can vary depending on whether the borrower achieves ambitious, material and quantifiable predetermined sustainability performance objectives aligned with Sustainability-Linked Loan Principles (SSLP)"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityLinkedLoan
tags: [LOAN, Release]
detail: "A borrower's sustainability performance is measured using sustainability performance targets (SPTs), which include key performance indicators, external ratings and/or equivalent metrics that measure improvements in the borrower's sustainability profile."
examples:
  - "The use of proceeds in relation to a SLL is not a determinant in its categorisation and, in most instances, SLLs will be used for general corporate purposes. Instead, SLLs look to support a borrower in improving its sustainability performance."
synonyms:
  - "SLL"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/DisclosureProvision.md", provenance: fibo}
  - {type: has-milestone-provision, target: "/FND/Agreements/Contracts/ContractMilestone.md", provenance: fibo}
  - {type: has-schedule, target: "/FND/Agreements/Contracts/MilestoneSchedule.md", provenance: fibo}
  - {type: has-strategy, target: "/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy.md", provenance: fibo}
---

credit agreement and/or contingent facility (such as a bonding line, guarantee line or letter of credit) for which the economic characteristics can vary depending on whether the borrower achieves ambitious, material and quantifiable predetermined sustainability performance objectives aligned with Sustainability-Linked Loan Principles (SSLP)

### Relationships
- is-a: [CreditAgreementRepaidPeriodically](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- is-a: [CommercialLoan](/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)
- has-contractual-element: [DisclosureProvision](/FND/Agreements/Contracts/DisclosureProvision.md)
- has-milestone-provision: [ContractMilestone](/FND/Agreements/Contracts/ContractMilestone.md)
- has-schedule: [MilestoneSchedule](/FND/Agreements/Contracts/MilestoneSchedule.md)
- has-strategy: [SustainabilityBusinessStrategy](/LOAN/LoansSpecific/GreenLoans/SustainabilityBusinessStrategy.md)
