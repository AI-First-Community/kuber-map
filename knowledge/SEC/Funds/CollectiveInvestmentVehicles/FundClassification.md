---
type: FIBO Class
title: "fund classification"
description: "The category of the fund according to the asset class. This is a published code by which the Fund is classified. Further notes: Could be EFCF codes. This is the way in which 'Type of fund' is articulated."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundClassification
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/SEC/Securities/Pools/CollectiveInvestmentVehicle.md", provenance: fibo}
---

The category of the fund according to the asset class. This is a published code by which the Fund is classified. Further notes: Could be EFCF codes. This is the way in which "Type of fund" is articulated.

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [CollectiveInvestmentVehicle](/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
