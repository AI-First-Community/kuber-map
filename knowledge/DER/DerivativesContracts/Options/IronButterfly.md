---
type: FIBO Class
title: "iron butterfly"
description: "butterfly strategy that consists of two call options and two put options, three strike prices and the same expiration date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/IronButterfly
tags: [DER, Release]
detail: "The key to using this trade as part of a successful trading strategy is to forecast a time when option prices are likely to decline in value generally. This usually occurs during periods of sideways movement or a mild upward trend."
synonyms:
  - "iron fly"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/Butterfly.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

butterfly strategy that consists of two call options and two put options, three strike prices and the same expiration date

### Relationships
- is-a: [Butterfly](/DER/DerivativesContracts/Options/Butterfly.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
