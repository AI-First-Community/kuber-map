---
type: FIBO Class
title: "variable interest expression"
description: "an expression used to determine a variable interest payment amount"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableInterestExpression
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-argument, target: "/SEC/Debt/DebtInstruments/FullyIndexedInterestRate.md", provenance: fibo}
---

an expression used to determine a variable interest payment amount

### Relationships
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-argument: [FullyIndexedInterestRate](/SEC/Debt/DebtInstruments/FullyIndexedInterestRate.md)
