---
type: FIBO Class
title: "payment schedule"
description: "schedule for delivery of money in fulfillment of an obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
tags: [FND, Release]
examples:
  - "Examples include coupon payment, loan payment, and interest payment schedules, among others."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: has-member, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md", provenance: fibo}
---

schedule for delivery of money in fulfillment of an obligation

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- has-member: [Payment](/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)
