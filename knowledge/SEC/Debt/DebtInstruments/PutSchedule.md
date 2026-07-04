---
type: FIBO Class
title: "put schedule"
description: "a schedule that defines the events associated with the put feature of a debt instrument, i.e, the dates on which the debt instrument may be sold at what price by the holder"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutSchedule
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/PutEvent.md", provenance: fibo}
---

a schedule that defines the events associated with the put feature of a debt instrument, i.e, the dates on which the debt instrument may be sold at what price by the holder

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- comprises: [PutEvent](/SEC/Debt/DebtInstruments/PutEvent.md)
