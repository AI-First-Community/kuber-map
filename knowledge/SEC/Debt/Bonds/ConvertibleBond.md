---
type: FIBO Class
title: "convertible bond"
description: "bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the equity price rises above a specified level (strike price)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond
tags: [SEC, Release]
core: true
detail: "If the equity price remains below the strike price throughout the term of the bond it matures and is redeemed like a regular bond. The conversion ratio and strike price are usually set when the convertible bond is issued."
examples:
  - "A Tesla convertible note the holder can convert into a set number of Tesla shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/BondConversionTerms.md", provenance: fibo}
---

bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the equity price rises above a specified level (strike price)

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- is-a: [ConvertibleSecurity](/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md)
- has-contractual-element: [BondConversionTerms](/SEC/Debt/Bonds/BondConversionTerms.md)
