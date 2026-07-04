---
type: FIBO Class
title: "dividend schedule"
description: "payment schedule indicating the dates on which dividends are due to be paid"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendSchedule
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/RegularSchedule.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md", provenance: fibo}
---

payment schedule indicating the dates on which dividends are due to be paid

### Relationships
- is-a: [RegularSchedule](/FND/DatesAndTimes/FinancialDates/RegularSchedule.md)
- is-a: [PaymentSchedule](/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)
