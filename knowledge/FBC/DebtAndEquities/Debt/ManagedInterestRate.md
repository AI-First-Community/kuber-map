---
type: FIBO Class
title: "managed interest rate"
description: "variable interest rate charged by a financial institution for borrowing that is not prescribed as a margin over base rate but is set from time to time by the institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ManagedInterestRate
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/VariableInterestRate.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
---

variable interest rate charged by a financial institution for borrowing that is not prescribed as a margin over base rate but is set from time to time by the institution

### Relationships
- is-a: [VariableInterestRate](/FBC/DebtAndEquities/Debt/VariableInterestRate.md)
- is-managed-by: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
