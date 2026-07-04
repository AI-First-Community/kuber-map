---
type: FIBO Class
title: "bond with partial call"
description: "bond with a feature whereby the issue can be partially called for amounts that are at the discretion of the issuer"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondWithPartialCall
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/CallableBond.md", provenance: fibo}
  - {type: has-call-feature, target: "/SEC/Debt/Bonds/PartialCallFeature.md", provenance: fibo}
---

bond with a feature whereby the issue can be partially called for amounts that are at the discretion of the issuer

### Relationships
- is-a: [CallableBond](/SEC/Debt/Bonds/CallableBond.md)
- has-call-feature: [PartialCallFeature](/SEC/Debt/Bonds/PartialCallFeature.md)
