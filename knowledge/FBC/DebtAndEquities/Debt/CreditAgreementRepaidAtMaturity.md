---
type: FIBO Class
title: "credit agreement repaid at maturity"
description: "credit agreement in which accrued interest may be periodically repaid or paid at maturity, but principal is paid at maturity"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity
tags: [FBC, Release]
examples:
  - "The most common example of a credit agreement repaid at maturity is a bond."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
---

credit agreement in which accrued interest may be periodically repaid or paid at maturity, but principal is paid at maturity

### Relationships
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
