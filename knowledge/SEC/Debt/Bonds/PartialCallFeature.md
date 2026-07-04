---
type: FIBO Class
title: "partial call feature"
description: "call feature whereby the issuer can recall part of the issue on scheduled dates, where bonds are selected to be called according to some rule, or by selecting various bonds at random"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCallFeature
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/CallFeature.md", provenance: fibo}
  - {type: has-partial-redemption-allocation-convention, target: "/SEC/Debt/Bonds/PartialRedemptionAllocationConvention.md", provenance: fibo}
---

call feature whereby the issuer can recall part of the issue on scheduled dates, where bonds are selected to be called according to some rule, or by selecting various bonds at random

### Relationships
- is-a: [CallFeature](/SEC/Debt/DebtInstruments/CallFeature.md)
- has-partial-redemption-allocation-convention: [PartialRedemptionAllocationConvention](/SEC/Debt/Bonds/PartialRedemptionAllocationConvention.md)
