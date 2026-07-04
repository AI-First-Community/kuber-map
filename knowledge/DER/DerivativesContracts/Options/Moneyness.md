---
type: FIBO Class
title: "moneyness"
description: "classifier for a derivative relating its strike price to the price of its underlying asset"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness
tags: [DER, Release]
detail: "Moneyness describes the intrinsic value of an option in its current state. The term moneyness is most commonly used with put and call options and is an indicator as to the comparative value of the option with respect to its exercise/strike price. Moneyness can be measured with respect to the underlying stock or other asset's current/spot price or its future price."
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

classifier for a derivative relating its strike price to the price of its underlying asset

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
