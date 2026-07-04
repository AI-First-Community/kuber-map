---
type: FIBO Class
title: "market rate"
description: "value of a rate established in the marketplace for a set of instruments or that describes the economic climate for an industry and/or political region (e.g., SOFR, Prime)"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
tags: [IND, Release]
examples:
  - "Financial market rates include, but are not limited to reference rates, foreign exchange rates, lending rates, bankers' acceptance rates, and so forth."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Ratio.md", provenance: fibo}
  - {type: is-value-of, target: "/FND/Utilities/Analytics/ScopedMeasure.md", provenance: fibo}
---

value of a rate established in the marketplace for a set of instruments or that describes the economic climate for an industry and/or political region (e.g., SOFR, Prime)

### Relationships
- is-a: [Ratio](/CMNS/QuantitiesAndUnits/Ratio.md)
- is-value-of: [ScopedMeasure](/FND/Utilities/Analytics/ScopedMeasure.md)
