---
type: FIBO Class
title: "variable debt principal"
description: "principal that is defined in relation to some variable and so varies over time, as principal"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableDebtPrincipal
tags: [SEC, Release]
detail: "Not the same as principal paydown. This is when the principal itself varies over time, usually as a result of being defined in relation to some index such as an inflation index. Forms the debt principal in instruments such as inflation bonds."
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/PubliclyIssuedDebt.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

principal that is defined in relation to some variable and so varies over time, as principal

### Relationships
- is-a: [PubliclyIssuedDebt](/SEC/Debt/DebtInstruments/PubliclyIssuedDebt.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
