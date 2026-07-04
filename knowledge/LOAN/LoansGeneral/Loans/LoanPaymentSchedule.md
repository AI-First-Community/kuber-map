---
type: FIBO Class
title: "loan payment schedule"
description: "regular or explicit (ad hoc) payment schedule associated with a given loan-specific account"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanPaymentSchedule
tags: [LOAN, Release]
core: true
detail: "Loan payment schedules may or may not be amortization schedules, i.e., they may or may not include principal."
examples:
  - "A monthly amortization schedule of principal and interest over 360 months."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: applies-to, target: "/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md", provenance: fibo}
---

regular or explicit (ad hoc) payment schedule associated with a given loan-specific account

### Relationships
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- applies-to: [LoanSpecificCustomerAccount](/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md)
