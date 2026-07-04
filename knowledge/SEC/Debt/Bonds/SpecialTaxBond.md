---
type: FIBO Class
title: "special tax bond"
description: "bond secured by revenues derived from designated taxes other than ad valorem taxes"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SpecialTaxBond
tags: [SEC, Release]
examples:
  - "For example, bonds for a particular purpose might be supported by sales, cigarette, fuel or business license taxes."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/MunicipalBond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/SecuredBond.md", provenance: fibo}
---

bond secured by revenues derived from designated taxes other than ad valorem taxes

### Relationships
- is-a: [MunicipalBond](/SEC/Debt/Bonds/MunicipalBond.md)
- is-a: [SecuredBond](/SEC/Debt/Bonds/SecuredBond.md)
