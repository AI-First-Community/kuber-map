---
type: FIBO Class
title: "credit report"
description: "report describing the creditworthiness and related credit attributes of a borrower"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport
tags: [FBC, Provisional]
detail: "This is typically provided by a credit rating agency but could be produced by an internal proprietary model as well."
relations:
  - {type: is-a, target: "/FND/Arrangements/Ratings/RatingReport.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/CreditRatings/CreditInquiry.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/CreditRatings/CreditMessage.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/CreditRatings/CreditRating.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/CreditRatings/CreditTradeline.md", provenance: fibo}
  - {type: concerns-party, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/DebtAndEquities/CreditRatings/CreditReportProduct.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-coverage-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/DebtAndEquities/CreditRatings/CreditReportCategory.md", provenance: fibo}
  - {type: is-identified-by, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: is-produced-by, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md", provenance: fibo}
---

report describing the creditworthiness and related credit attributes of a borrower

### Relationships
- is-a: [RatingReport](/FND/Arrangements/Ratings/RatingReport.md)
- comprises: [CreditInquiry](/FBC/DebtAndEquities/CreditRatings/CreditInquiry.md)
- comprises: [CreditMessage](/FBC/DebtAndEquities/CreditRatings/CreditMessage.md)
- comprises: [CreditRating](/FBC/DebtAndEquities/CreditRatings/CreditRating.md)
- comprises: [CreditTradeline](/FBC/DebtAndEquities/CreditRatings/CreditTradeline.md)
- concerns-party: [Party](/CMNS/PartiesAndSituations/Party.md)
- exemplifies: [CreditReportProduct](/FBC/DebtAndEquities/CreditRatings/CreditReportProduct.md)
- has-as-of-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-coverage-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- is-classified-by: [CreditReportCategory](/FBC/DebtAndEquities/CreditRatings/CreditReportCategory.md)
- is-identified-by: [Identifier](/CMNS/Identifiers/Identifier.md)
- is-produced-by: [CreditRatingAgency](/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
