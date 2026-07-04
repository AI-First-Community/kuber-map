---
type: FIBO Class
title: "interest payment terms"
description: "contract terms for payment of interest on a debt"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
tags: [FBC, Release]
detail: "Interest is usually payable on any outstanding principal amount, therefore interest relates to the amount of debt outstanding at any given point of time, not to the principal amount advanced at the time that the loan was advanced or the debt security issued (aside from the initial payment). Note that in most cases, the dates and payment frequencies for interest will coincide with the dates and payment frequencies related to the principal."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/DebtTerms.md", provenance: fibo}
  - {type: governs-payment-of, target: "/FBC/DebtAndEquities/Debt/Interest.md", provenance: fibo}
  - {type: has-accrual-basis, target: "/FBC/DebtAndEquities/Debt/DayCountConvention.md", provenance: fibo}
  - {type: has-compounding-frequency, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-first-rate-change-term, target: "/CMNS/DatesAndTimes/ExplicitDuration.md", provenance: fibo}
  - {type: has-initial-interest-accrual-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-initial-interest-payment-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-interest-payment-day, target: "/FND/DatesAndTimes/BusinessDates/DayOfMonth.md", provenance: fibo}
  - {type: has-interest-payment-frequency, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-interest-rate, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
  - {type: has-interest-rate-cap, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
---

contract terms for payment of interest on a debt

### Relationships
- is-a: [DebtTerms](/FBC/DebtAndEquities/Debt/DebtTerms.md)
- governs-payment-of: [Interest](/FBC/DebtAndEquities/Debt/Interest.md)
- has-accrual-basis: [DayCountConvention](/FBC/DebtAndEquities/Debt/DayCountConvention.md)
- has-compounding-frequency: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-first-rate-change-term: [ExplicitDuration](/CMNS/DatesAndTimes/ExplicitDuration.md)
- has-initial-interest-accrual-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-initial-interest-payment-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-interest-payment-day: [DayOfMonth](/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)
- has-interest-payment-frequency: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-interest-rate: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
- has-interest-rate-cap: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
