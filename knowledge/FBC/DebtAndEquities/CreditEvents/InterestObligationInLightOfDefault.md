---
type: FIBO Class
title: "interest obligation in light of default"
description: "obligation in respect of default(s) in the performance of any payment obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault
tags: [FBC, Release]
examples:
  - "Prior to the occurrence or effective designation of an early termination date in respect of the relevant transaction, a party that defaults in the performance of any payment obligation will, to the extent permitted by law (and in the case of an ISDA Master Agreement is subject to Section 6(c)), be required to pay interest (before as well as after judgment) on the overdue amount to the other party on demand in the same currency as such overdue amount, for the period from (and including) the original due date for payment to (but excluding) the date of actual payment, at the default rate. Such interest will be calculated on the basis of daily compounding and the actual number of days elapsed."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/ContingentObligation.md", provenance: fibo}
  - {type: is-a, target: "/FND/Law/LegalCapacity/ContractualObligation.md", provenance: fibo}
  - {type: has-default-interest-compounding-basis, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: is-mandated-by, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md", provenance: fibo}
---

obligation in respect of default(s) in the performance of any payment obligation

### Relationships
- is-a: [ContingentObligation](/FND/Law/LegalCapacity/ContingentObligation.md)
- is-a: [ContractualObligation](/FND/Law/LegalCapacity/ContractualObligation.md)
- has-default-interest-compounding-basis: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- is-mandated-by: [PaymentObligation](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation.md)
