---
type: FIBO Class
title: "equity correlation swap"
description: "correlation swap that allows one to hedge risks associated with the observed average correlation of a collection of underlying equity products"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityCorrelationSwap
tags: [DER, Release]
detail: "The underlier for the leg can be any of (1) dividend stream for a single stock, (2) change in value for a single share, (3) change in value for a basket of shares, (4) change in value for an index, (5) value of a dividend stream for a basket of shares, or (6) comparison of the change in value of a given share or basket or index against something else - for example, a single share against an index, which is the thing you are cross-correlating with the volatility of the share."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/CorrelationSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md", provenance: fibo}
---

correlation swap that allows one to hedge risks associated with the observed average correlation of a collection of underlying equity products

### Relationships
- is-a: [CorrelationSwap](/DER/DerivativesContracts/Swaps/CorrelationSwap.md)
- is-a: [EquitySwap](/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)
