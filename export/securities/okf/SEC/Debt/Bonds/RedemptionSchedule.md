---
type: FIBO Class
title: "redemption schedule"
description: "repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionSchedule
tags: [SEC, Release]
examples:
  - "A sinking-fund schedule that redeems 10% of a bond issue each year."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/RedemptionEvent.md", provenance: fibo}
---

repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates

### Relationships
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- comprises: [RedemptionEvent](/SEC/Debt/DebtInstruments/RedemptionEvent.md)
