---
type: FIBO Class
title: "bond with warrant"
description: "bond that is issued together with one or more warrant(s) attached as part of the offer, the warrant(s) granting the holder the right to purchase a designated security, often the common stock of the issuer of the debt, at a specified price"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondWithWarrant
tags: [SEC, Release]
detail: "This concept is needed primarily to support cases where the bond issuer is the issuer of the warrant."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: involves, target: "/DER/DerivativesContracts/RightsAndWarrants/Warrant.md", provenance: fibo}
---

bond that is issued together with one or more warrant(s) attached as part of the offer, the warrant(s) granting the holder the right to purchase a designated security, often the common stock of the issuer of the debt, at a specified price

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- involves: [Warrant](/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)
