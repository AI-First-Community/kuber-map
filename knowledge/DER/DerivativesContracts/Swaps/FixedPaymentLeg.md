---
type: FIBO Class
title: "fixed payment leg"
description: "swap leg that specifies contractual terms associated with a schedule of payments for any swap calculated by reference to a fixed annual rate"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedPaymentLeg
tags: [DER, Release]
detail: "Payments may be fixed or variable, which is independent from the function of the leg (payments, return etc.). The schedule may be expressed in one of two ways: as an explicit schedule of dates or as a formula for determining payment dates in advance (taking into account for example roll rules for non working days)."
synonyms:
  - "fixed payment stream terms"
  - "funding leg"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SwapLeg.md", provenance: fibo}
  - {type: has-payment-schedule, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
---

swap leg that specifies contractual terms associated with a schedule of payments for any swap calculated by reference to a fixed annual rate

### Relationships
- is-a: [SwapLeg](/DER/DerivativesContracts/Swaps/SwapLeg.md)
- has-payment-schedule: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
