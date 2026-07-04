---
type: FIBO Class
title: "credit risk assessment"
description: "risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment
tags: [LOAN, Provisional]
core: true
detail: "If the risk assessment is based on one of the automated underwriting sytems, then the underwriting automation category is 'automated'. This dependency could be automated (as it were)."
examples:
  - "Scoring an applicant's probability of default from credit and income data."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentActivity.md", provenance: fibo}
  - {type: applies-to, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
  - {type: has-input, target: "/FBC/DebtAndEquities/CreditRatings/CreditReport.md", provenance: fibo}
  - {type: has-input, target: "/LOAN/LoansGeneral/LoanApplications/PreApprovalContract.md", provenance: fibo}
  - {type: has-input, target: "/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest.md", provenance: fibo}
  - {type: has-input, target: "/LOAN/LoansGeneral/LoanApplications/PublicRecord.md", provenance: fibo}
  - {type: has-output, target: "/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision.md", provenance: fibo}
  - {type: uses-factor, target: "/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md", provenance: fibo}
  - {type: uses-factor, target: "/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md", provenance: fibo}
  - {type: uses-factor, target: "/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md", provenance: fibo}
  - {type: uses-factor, target: "/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md", provenance: fibo}
---

risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan

### Relationships
- is-a: [AssessmentActivity](/FND/Arrangements/Assessments/AssessmentActivity.md)
- applies-to: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
- has-input: [CreditReport](/FBC/DebtAndEquities/CreditRatings/CreditReport.md)
- has-input: [PreApprovalContract](/LOAN/LoansGeneral/LoanApplications/PreApprovalContract.md)
- has-input: [PreApprovalRequest](/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest.md)
- has-input: [PublicRecord](/LOAN/LoansGeneral/LoanApplications/PublicRecord.md)
- has-output: [UnderwritingDecision](/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision.md)
- uses-factor: [AllBorrowersMonthlyIncome](/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md)
- uses-factor: [BorrowerMonthlyIncome](/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)
- uses-factor: [TotalDebtExpenseRatio](/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md)
- uses-factor: [CombinedLoanToValueRatio](/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md)
