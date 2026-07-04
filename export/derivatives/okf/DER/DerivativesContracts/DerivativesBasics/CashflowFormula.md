---
type: FIBO Class
title: "cashflow formula"
description: "formula for determining cashflows for a derivative instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowFormula
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "The formula 'notional x (SOFR + 0.5%)' for a swap's floating leg."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Formula.md", provenance: fibo}
  - {type: has-expression, target: "/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md", provenance: fibo}
---

formula for determining cashflows for a derivative instrument

### Relationships
- is-a: [Formula](/FND/Utilities/Analytics/Formula.md)
- has-expression: [CashflowExpression](/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md)
