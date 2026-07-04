---
type: FIBO Class
title: "amortization schedule"
description: "schedule of periodic payments (repayment installments) that specify changes in the balance of the debt over time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AmortizationSchedule
tags: [FBC, Release]
detail: "Payments are divided into equal amounts for the duration of the loan or debt instrument, making it the simplest repayment model. A greater amount of the payment is applied to interest at the beginning of the amortization schedule, while more money is applied to principal at the end."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/Debt/PrincipalPaymentSchedule.md", provenance: fibo}
  - {type: embodies, target: "/FBC/DebtAndEquities/Debt/Amortization.md", provenance: fibo}
---

schedule of periodic payments (repayment installments) that specify changes in the balance of the debt over time

### Relationships
- is-a: [ProjectedContractEventSchedule](/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
- comprises: [InterestPaymentSchedule](/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)
- comprises: [PrincipalPaymentSchedule](/FBC/DebtAndEquities/Debt/PrincipalPaymentSchedule.md)
- embodies: [Amortization](/FBC/DebtAndEquities/Debt/Amortization.md)
