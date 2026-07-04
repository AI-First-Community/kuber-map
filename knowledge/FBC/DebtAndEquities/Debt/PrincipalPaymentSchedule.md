---
type: FIBO Class
title: "principal payment schedule"
description: "regular, contract-specific schedule including the dates on which some percentage or all of the principal is due to be (re)paid"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalPaymentSchedule
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: has-occurrence, target: "/FBC/DebtAndEquities/Debt/PrincipalPayment.md", provenance: fibo}
---

regular, contract-specific schedule including the dates on which some percentage or all of the principal is due to be (re)paid

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- has-occurrence: [PrincipalPayment](/FBC/DebtAndEquities/Debt/PrincipalPayment.md)
