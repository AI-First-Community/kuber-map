---
type: FIBO Class
title: "observed best value"
description: "observed value of the underlying asset as of some date during the lookback period that is considered the best value from the perspective of the option holder during the lookback period (depending on whether the option is a call or put)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ObservedBestValue
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

observed value of the underlying asset as of some date during the lookback period that is considered the best value from the perspective of the option holder during the lookback period (depending on whether the option is a call or put)

### Relationships
- is-a: [MarketPrice](/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)
- has-as-of-date: [Date](/CMNS/DatesAndTimes/Date.md)
