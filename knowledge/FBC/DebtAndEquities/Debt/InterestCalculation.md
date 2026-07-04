---
type: FIBO Class
title: "interest calculation"
description: "event reflecting the calculation of interest"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestCalculation
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Calculation.md", provenance: fibo}
  - {type: has-interest-rate, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

event reflecting the calculation of interest

### Relationships
- is-a: [ContractLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- is-a: [Calculation](/FND/DatesAndTimes/Occurrences/Calculation.md)
- has-interest-rate: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
