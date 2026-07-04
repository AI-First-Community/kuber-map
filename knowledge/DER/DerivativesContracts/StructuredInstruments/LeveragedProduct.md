---
type: FIBO Class
title: "leveraged product"
description: "structured product that provides a further enhanced yield (over and above that of a yield-enhancement product), often without any limit to the upside participation, and frequently with a stop-loss in order to limit potential capital losses"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/LeveragedProduct
tags: [DER, Release]
examples:
  - "Leveraged certificates are examples of leveraged products; they provide enhanced participation to an underlying with inbuilt leverage. Leveraged exposure is also provided on the downside performance of the underlying. Another example is a call warrant, which is simply a call option that is traded in a securitized format. This format is interesting in order to be able to trade a call option on underlyings for which no exchange traded option market exists."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md", provenance: fibo}
---

structured product that provides a further enhanced yield (over and above that of a yield-enhancement product), often without any limit to the upside participation, and frequently with a stop-loss in order to limit potential capital losses

### Relationships
- is-a: [StructuredProduct](/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)
