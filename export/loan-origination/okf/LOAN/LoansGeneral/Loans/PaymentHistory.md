---
type: FIBO Class
title: "payment history"
description: "record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer in order to fulfill their re-payment obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
tags: [LOAN, Release]
core: true
detail: "The borrower's record of on-time and late payments; central to credit scoring and to servicing and default decisions."
detail_provenance: curated
examples:
  - "24 months of on-time mortgage payments with one 30-day late."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md", provenance: fibo}
  - {type: applies-to-account, target: "/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md", provenance: fibo}
  - {type: has-individual-payment, target: "/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction.md", provenance: fibo}
---

record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer in order to fulfill their re-payment obligation

### Relationships
- is-a: [TransactionRecord](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)
- applies-to-account: [LoanSpecificCustomerAccount](/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md)
- has-individual-payment: [IndividualPaymentTransaction](/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction.md)
