---
type: FIBO Class
title: "borrower assessment"
description: "assessment report detailing information about the borrower and their credit history that may be relevant to the loan application"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
tags: [LOAN, Provisional]
core: true
detail: "Includes credit rating information. Ongoing assessment reports both good and bad credit rating information. In the US, by regulation, lender is required to respot person's payment history on a monthly basis. This is the basis on which peope's score is changed. So the lender's reporting to the credit bureau may affect that person's credit rating. this may give rise to credit disputes. Also there is a scenario where the borrower may contact the lender and ask for some change. For student loans, they can apply for a deferment payment based on change in circumstances e.g. if losing job, or becoming disabled, then there are specific programs which they can apply for. can defer paymen for a time, and if proven eligible (e.g. also if in military, being deployed), then if they subbut the relevant document, they approve and change their repayment term, perhaps temporarily and then revert to the previously agreed terms. This results from the borrower contacting the lender."
examples:
  - "A summary of the applicant's income, employment, and credit history."
examples_provenance: curated
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
