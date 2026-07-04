---
type: FIBO Class
title: "interest obligation in light of default"
description: "obligation in respect of default(s) in the performance of any payment obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault
tags: [FBC, Release]
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
