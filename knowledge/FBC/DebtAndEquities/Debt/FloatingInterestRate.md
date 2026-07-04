---
type: FIBO Class
title: "floating interest rate"
description: "variable interest rate that is based on a specific index or benchmark rate"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FloatingInterestRate
tags: [FBC, Release]
detail: "The index used to determine the specific interest rate is generally included in the terms of the loan. In most cases, lenders will also charge a spread, or added percentage points on top of the established index rate. If a loan is billed as prime plus 2.5 percent, for a prime rate of 3.5 percent, the terms of the loan will require the borrower to pay off a 6 percent interest. Floating interest rates typically involve periodic reset dates for the loan, particularly when the index rate changes. Resets may also occur online at market predetermined intervals, with yearly adjustments being a common arrangement."
examples:
  - "Certain revolving credit, such as credit-card related debt, may adjust after a specified period of time to an absolute rate stated in the agreement (variable but not floating) rather than based on a benchmark rate (variable, floating)."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/VariableInterestRate.md", provenance: fibo}
---

variable interest rate that is based on a specific index or benchmark rate

### Relationships
- is-a: [VariableInterestRate](/FBC/DebtAndEquities/Debt/VariableInterestRate.md)
