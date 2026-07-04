---
type: FIBO Class
title: "borrowing capacity"
description: "upper bound on the total amount of money that a lender believes a party has the ability to repay an obligation when due, as of some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowingCapacity
tags: [FBC, Release]
detail: "The notion of borrowing capacity is related to management decisions pertaining to credit, i.e., the creditworthiness of the borrower, loan amount, risk tolerance, and so forth, and may be reassessed from time to time depending on the type of credit agreement and regulatory requirements. Determining borrowing capacity is typically done as a part of loan origination, especially for residential mortgages."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: applies-to, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: has-date-of-assessment, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
---

upper bound on the total amount of money that a lender believes a party has the ability to repay an obligation when due, as of some point in time

### Relationships
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- applies-to: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- has-date-of-assessment: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-evidenced-by: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
