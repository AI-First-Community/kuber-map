---
type: FIBO Class
title: "loan-specific customer account"
description: "account held by the borrower associated with a specific loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md", provenance: fibo}
  - {type: has-loan-balance, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md", provenance: fibo}
  - {type: has-payment-history, target: "/LOAN/LoansGeneral/Loans/PaymentHistory.md", provenance: fibo}
  - {type: has-payment-schedule, target: "/LOAN/LoansGeneral/Loans/LoanPaymentSchedule.md", provenance: fibo}
  - {type: is-held-by, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: relates-to, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
---

account held by the borrower associated with a specific loan

### Relationships
- is-a: [CustomerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- is-a: [LoanOrCreditAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- has-loan-balance: [Balance](/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- has-payment-history: [PaymentHistory](/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- has-payment-schedule: [LoanPaymentSchedule](/LOAN/LoansGeneral/Loans/LoanPaymentSchedule.md)
- is-held-by: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- relates-to: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
