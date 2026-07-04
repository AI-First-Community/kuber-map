---
type: FIBO Class
title: "interest payment schedule"
description: "regular, contract-specific schedule including the dates on which interest is due to be paid"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: has-occurrence, target: "/FBC/DebtAndEquities/Debt/InterestPayment.md", provenance: fibo}
---

regular, contract-specific schedule including the dates on which interest is due to be paid

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- has-occurrence: [InterestPayment](/FBC/DebtAndEquities/Debt/InterestPayment.md)
