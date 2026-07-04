---
type: FIBO Class
title: "loan application"
description: "request by a potential borrower to a potential lender to borrow money containing information used to decide whether to grant the loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
tags: [LOAN, Provisional]
core: true
relations:
  - {type: is-a, target: "/CMNS/Documents/Document.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/Loans/LoanToValueRatio.md", provenance: fibo}
  - {type: has-application-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-date-received, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-submitted-by, target: "/FND/Arrangements/Reporting/Requester.md", provenance: fibo}
---

request by a potential borrower to a potential lender to borrow money containing information used to decide whether to grant the loan

### Relationships
- is-a: [Document](/CMNS/Documents/Document.md)
- comprises: [AllBorrowersMonthlyIncome](/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md)
- comprises: [BorrowerMonthlyIncome](/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)
- comprises: [TotalDebtExpenseRatio](/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md)
- comprises: [CombinedLoanToValueRatio](/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md)
- comprises: [LoanToValueRatio](/LOAN/LoansGeneral/Loans/LoanToValueRatio.md)
- has-application-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-date-received: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-submitted-by: [Requester](/FND/Arrangements/Reporting/Requester.md)
