---
type: FIBO Class
title: "index credit default swap"
description: "credit default swap that references a family of standardized credit derivative indices, where the underlying reference entities are a defined basket of credit from a particular geographic region (e.g. Asia, North America, Europe), and/or credit rating level (e.g. emerging markets, high yield, investment grade)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/IndexCreditDefaultSwap
tags: [DER, Release]
detail: "Credit default indices trade in standard maturities, and the reference entities are typically the most liquid; the reference portfolio is reassessed periodically to maintain this."
relations:
  - {type: is-a, target: "/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md", provenance: fibo}
---

credit default swap that references a family of standardized credit derivative indices, where the underlying reference entities are a defined basket of credit from a particular geographic region (e.g. Asia, North America, Europe), and/or credit rating level (e.g. emerging markets, high yield, investment grade)

### Relationships
- is-a: [MultiNameCreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md)
