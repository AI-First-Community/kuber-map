---
type: FIBO Class
title: "fixed fixed interest rate swap"
description: "interest rate swap in which both parties pay a fixed interest rate that they could not otherwise obtain outside of a swap arrangement"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFixedInterestRateSwap
tags: [DER, Release]
examples:
  - "For example, each counterparty uses a different native currency, but wants to borrow money in the other counterparty's native currency."
synonyms:
  - "fixed-fixed interest rate swap"
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwap.md", provenance: fibo}
  - {type: exchanges, target: "/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg.md", provenance: fibo}
---

interest rate swap in which both parties pay a fixed interest rate that they could not otherwise obtain outside of a swap arrangement

### Relationships
- is-a: [InterestRateSwap](/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)
- exchanges: [FixedInterestRateLeg](/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg.md)
