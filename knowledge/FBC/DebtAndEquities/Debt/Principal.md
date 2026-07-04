---
type: FIBO Class
title: "principal"
description: "with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or capital gains"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
tags: [FBC, Release]
core: true
detail: "The amount borrowed that must be repaid, separate from interest; the outstanding principal drives interest accrual and the payoff amount."
detail_provenance: curated
examples:
  - "The $300,000 original balance of a mortgage, excluding interest."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Aspect.md", provenance: fibo}
  - {type: is-principal-of, target: "/FBC/DebtAndEquities/Debt/Debt.md", provenance: fibo}
---

with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or capital gains

### Relationships
- is-a: [Aspect](/CMNS/Classifiers/Aspect.md)
- is-principal-of: [Debt](/FBC/DebtAndEquities/Debt/Debt.md)
