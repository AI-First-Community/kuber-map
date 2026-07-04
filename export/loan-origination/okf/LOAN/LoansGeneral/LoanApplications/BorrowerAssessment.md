---
type: FIBO Class
title: "borrower assessment"
description: "assessment report detailing information about the borrower and their credit history that may be relevant to the loan application"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
tags: [LOAN, Provisional]
core: true
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating.md", provenance: fibo}
  - {type: comprises, target: "/LOAN/LoansGeneral/Loans/PaymentHistory.md", provenance: fibo}
  - {type: has-date-of-assessment, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-about, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: is-about, target: "/LOAN/LoansGeneral/LoanApplications/LoanApplication.md", provenance: fibo}
---

assessment report detailing information about the borrower and their credit history that may be relevant to the loan application

### Relationships
- is-a: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
- comprises: [IncomeVerificationReport](/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport.md)
- comprises: [IndividualPersonCreditRating](/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating.md)
- comprises: [PaymentHistory](/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- has-date-of-assessment: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-about: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- is-about: [LoanApplication](/LOAN/LoansGeneral/LoanApplications/LoanApplication.md)
