---
type: FIBO Class
title: "capitalization-based weighting function"
description: "weighting function derived from the relative market capitalization (share price times the number of shares outstanding) of the companies tracked by an index"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CapitalizationBasedWeightingFunction
tags: [IND, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/WeightingFunction.md", provenance: fibo}
  - {type: has-market-capitalization, target: "/IND/MarketIndices/BasketIndices/MarketCapitalization.md", provenance: fibo}
---

weighting function derived from the relative market capitalization (share price times the number of shares outstanding) of the companies tracked by an index

### Relationships
- is-a: [WeightingFunction](/FND/Utilities/Analytics/WeightingFunction.md)
- has-market-capitalization: [MarketCapitalization](/IND/MarketIndices/BasketIndices/MarketCapitalization.md)
