---
type: FIBO Class
title: "rate of return"
description: "net gain or loss on an investment over a specified time period, expressed as a percentage of the investment's initial cost or value as of a specific point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/RateOfReturn
tags: [FBC, Release]
synonyms:
  - "RoR"
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Percentage.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

net gain or loss on an investment over a specified time period, expressed as a percentage of the investment's initial cost or value as of a specific point in time

### Relationships
- is-a: [Percentage](/CMNS/QuantitiesAndUnits/Percentage.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- refers-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
