---
type: FIBO Class
title: "principal repayment terms"
description: "contract terms that specify requirements for repayment of the principal"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/DebtTerms.md", provenance: fibo}
  - {type: governs-payment-of, target: "/FBC/DebtAndEquities/Debt/Principal.md", provenance: fibo}
  - {type: has-extension-provision, target: "/FND/Agreements/Contracts/ExtensionProvision.md", provenance: fibo}
  - {type: has-initial-principal-payment-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-principal-payment-day, target: "/FND/DatesAndTimes/BusinessDates/DayOfMonth.md", provenance: fibo}
  - {type: has-principal-payment-frequency, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-principal-repayment-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

contract terms that specify requirements for repayment of the principal

### Relationships
- is-a: [DebtTerms](/FBC/DebtAndEquities/Debt/DebtTerms.md)
- governs-payment-of: [Principal](/FBC/DebtAndEquities/Debt/Principal.md)
- has-extension-provision: [ExtensionProvision](/FND/Agreements/Contracts/ExtensionProvision.md)
- has-initial-principal-payment-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-principal-payment-day: [DayOfMonth](/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)
- has-principal-payment-frequency: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-principal-repayment-date: [Date](/CMNS/DatesAndTimes/Date.md)
