---
type: FIBO Class
title: "exotic option"
description: "option that has a non-standard payout structure or other feature"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
tags: [DER, Release]
detail: "Exotic options include Asian options and lookback options, and are mostly traded in the over-the-counter market."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

option that has a non-standard payout structure or other feature

### Relationships
- is-a: [OverTheCounterDerivativeInstrument](/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- is-a: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
