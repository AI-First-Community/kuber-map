---
type: FIBO Class
title: "index return swap"
description: "return swap in which payments are based on a fee paid to the seller of the swap and on a floating reference price based on changes in the level of an index from an initial level to a level observed on some valuation date(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/IndexReturnSwap
tags: [DER, Release]
detail: "Payments to the parties may be made either on a periodic basis or on termination of the transaction. One party will receive a payment based upon the change in the level of the index between two valuation dates (multiplied by the notional amount of the swap), as modified by the fee paid to the seller of the swap. If the level of the index increases, the buyer of the swap will be entitled to a payment based on this performance, as such payment may be reduced (or negated) by the fee paid to the seller of the swap. If the level of the index decreases, the seller of the swap will be entitled to a payment based on this performance, as such payment may be increased by the fee paid to the seller of the swap."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/ReturnSwap.md", provenance: fibo}
---

return swap in which payments are based on a fee paid to the seller of the swap and on a floating reference price based on changes in the level of an index from an initial level to a level observed on some valuation date(s)

### Relationships
- is-a: [ReturnSwap](/DER/DerivativesContracts/Swaps/ReturnSwap.md)
