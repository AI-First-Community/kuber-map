---
type: FIBO Class
title: "listed bond"
description: "bond that may be traded on an exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ListedBond
tags: [SEC, Release]
detail: "Most exchange traded bonds are corporate bonds (but most corporate bonds are not exchange traded bonds)."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesListings/ListedSecurity.md", provenance: fibo}
---

bond that may be traded on an exchange

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- is-a: [ListedSecurity](/SEC/Securities/SecuritiesListings/ListedSecurity.md)
