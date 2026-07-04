---
type: FIBO Class
title: "collar"
description: "option trading strategy that involves buying a downside put and selling an upside call that is implemented to protect against large losses, but which also limits large upside gains"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Collar
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

option trading strategy that involves buying a downside put and selling an upside call that is implemented to protect against large losses, but which also limits large upside gains

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
