---
type: FIBO Class
title: "strangle"
description: "option trading strategy in which the investor holds a position in both a call and a put option with different strike prices, but with the same expiration date and underlying asset"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Strangle
tags: [DER, Release]
detail: "A strangle is a good strategy if you think the underlying security will experience a large price movement in the near future but are unsure of the direction. However, it is profitable mainly if the asset swings sharply in price."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

option trading strategy in which the investor holds a position in both a call and a put option with different strike prices, but with the same expiration date and underlying asset

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
