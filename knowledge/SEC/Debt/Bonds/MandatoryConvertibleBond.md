---
type: FIBO Class
title: "mandatory convertible bond"
description: "convertible bond that converts into shares at maturity regardless of the equity price"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MandatoryConvertibleBond
tags: [SEC, Release]
detail: "The conversion ratio at maturity reflects the equity price and par value of the bond when issued. There is also typically a second higher conversion ratio if the equity price rises above the strike during the term of the bond."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/ConvertibleBond.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/BondConversionTerms.md", provenance: fibo}
---

convertible bond that converts into shares at maturity regardless of the equity price

### Relationships
- is-a: [ConvertibleBond](/SEC/Debt/Bonds/ConvertibleBond.md)
- has-contractual-element: [BondConversionTerms](/SEC/Debt/Bonds/BondConversionTerms.md)
