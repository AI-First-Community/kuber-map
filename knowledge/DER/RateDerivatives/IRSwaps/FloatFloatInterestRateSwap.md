---
type: FIBO Class
title: "float float interest rate swap"
description: "interest rate swap that exchanges cashflows based on two different floating interest rates"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatFloatInterestRateSwap
tags: [DER, Release]
detail: "This is a swap in which two parties swap variable interest rates based on different money markets, and this is usually done to limit interest-rate risk that a company faces as a result of having differing lending and borrowing rates."
synonyms:
  - "basis rate swap"
  - "float-float interest rate swap"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/BasisSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwap.md", provenance: fibo}
  - {type: exchanges, target: "/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md", provenance: fibo}
---

interest rate swap that exchanges cashflows based on two different floating interest rates

### Relationships
- is-a: [BasisSwap](/DER/DerivativesContracts/Swaps/BasisSwap.md)
- is-a: [InterestRateSwap](/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)
- exchanges: [FloatingInterestRateLeg](/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md)
