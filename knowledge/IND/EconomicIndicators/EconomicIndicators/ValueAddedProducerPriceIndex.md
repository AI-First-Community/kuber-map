---
type: FIBO Class
title: "value-added producer price index"
description: "economic indicator representing a weighted average of the input and output producer price indices"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ValueAddedProducerPriceIndex
tags: [IND, Release]
synonyms:
  - "value-added PPI"
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md", provenance: fibo}
  - {type: has-input, target: "/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex.md", provenance: fibo}
  - {type: has-input, target: "/IND/EconomicIndicators/EconomicIndicators/OutputProducerPriceIndex.md", provenance: fibo}
---

economic indicator representing a weighted average of the input and output producer price indices

### Relationships
- is-a: [ProducerPriceIndex](/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md)
- has-input: [InputProducerPriceIndex](/IND/EconomicIndicators/EconomicIndicators/InputProducerPriceIndex.md)
- has-input: [OutputProducerPriceIndex](/IND/EconomicIndicators/EconomicIndicators/OutputProducerPriceIndex.md)
