---
type: FIBO Class
title: "default event"
description: "credit event representing a failure to meet a contractual obligation, such as failure to repay a debt including interest or principal on a loan or security"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
tags: [FBC, Release]
detail: "A default can occur when a borrower is unable to make timely payments, misses payments, or avoids or stops making payments, typically with respect to a single transaction. A default has adverse effects on the borrower's credit and ability to borrow in the future, and allows the creditor to demand immediate repayment of the obligation in full."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/Agreements/Contracts/BreachOfCovenant.md", provenance: fibo}
---

credit event representing a failure to meet a contractual obligation, such as failure to repay a debt including interest or principal on a loan or security

### Relationships
- is-a: [ObligationSpecificCreditEvent](/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)
- exemplifies: [BreachOfCovenant](/FND/Agreements/Contracts/BreachOfCovenant.md)
