---
type: FIBO Class
title: "correlation swap"
description: "over-the-counter statistical derivative that allows one to hedge risks associated with the observed average correlation of a collection of underlying products"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/CorrelationSwap
tags: [DER, Release]
detail: "Each product that can act as the underlier on which the correlation is based has periodically observable prices, such as a commodity, exchange rate, interest rate, or stock index. Correlation trading is a strategy in which the investor receives exposure to the average correlation of an index."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/StatisticalSwap.md", provenance: fibo}
---

over-the-counter statistical derivative that allows one to hedge risks associated with the observed average correlation of a collection of underlying products

### Relationships
- is-a: [StatisticalSwap](/DER/DerivativesContracts/Swaps/StatisticalSwap.md)
