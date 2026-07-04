---
type: FIBO Class
title: "amortizing bond"
description: "bond that regularly pays down the principal (face value) on the debt along with its interest expense over the life of the bond"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/AmortizingBond
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: has-repayment-terms, target: "/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md", provenance: fibo}
---

bond that regularly pays down the principal (face value) on the debt along with its interest expense over the life of the bond

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- has-repayment-terms: [BondAmortizationPaymentTerms](/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
