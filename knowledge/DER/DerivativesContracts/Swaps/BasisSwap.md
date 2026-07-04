---
type: FIBO Class
title: "basis swap"
description: "swap in which payment streams are referenced to different bases"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/BasisSwap
tags: [DER, Release]
detail: "A basis swap can have two legs of the same tenor but different indices, e.g., 3 month LIBOR vs. 3 month TIBOR. The difference in this case is not driven by different interest rate periods but from different markets, i.e., the difference in efficiency between the two markets. The objective is to hedge against basis risk which is the difference in price between two markets. See also forward swap, as a means for controlling interest rate."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/RatesSwap.md", provenance: fibo}
---

swap in which payment streams are referenced to different bases

### Relationships
- is-a: [RatesSwap](/DER/DerivativesContracts/Swaps/RatesSwap.md)
