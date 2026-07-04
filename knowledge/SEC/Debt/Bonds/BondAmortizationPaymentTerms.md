---
type: FIBO Class
title: "bond amortization payment terms"
description: "terms that include a schedule for repayment of the principal over the lifetime of the bond, typically in equal payments at regular intervals"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md", provenance: fibo}
  - {type: has-schedule, target: "/FBC/DebtAndEquities/Debt/AmortizationSchedule.md", provenance: fibo}
---

terms that include a schedule for repayment of the principal over the lifetime of the bond, typically in equal payments at regular intervals

### Relationships
- is-a: [BondPrincipalRepaymentTerms](/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md)
- has-schedule: [AmortizationSchedule](/FBC/DebtAndEquities/Debt/AmortizationSchedule.md)
