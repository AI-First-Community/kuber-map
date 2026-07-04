---
type: FIBO Class
title: "Asian option classifier"
description: "financial instrument classifier that classifies Asian options based on whether they are rate-based or price based"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOptionClassifier
tags: [DER, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
  - {type: classifies, target: "/DER/DerivativesContracts/ExoticOptions/AsianOption.md", provenance: fibo}
---

financial instrument classifier that classifies Asian options based on whether they are rate-based or price based

### Relationships
- is-a: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- classifies: [AsianOption](/DER/DerivativesContracts/ExoticOptions/AsianOption.md)
