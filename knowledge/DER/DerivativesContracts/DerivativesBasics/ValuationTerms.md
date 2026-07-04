---
type: FIBO Class
title: "valuation terms"
description: "contract terms specific to valuation of the underlying asset(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ValuationTerms
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: has-date-of-assessment, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: involves, target: "/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation.md", provenance: fibo}
---

contract terms specific to valuation of the underlying asset(s)

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- has-date-of-assessment: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- involves: [UnderlyingAssetValuation](/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation.md)
