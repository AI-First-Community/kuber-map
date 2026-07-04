---
type: FIBO Class
title: "bond registrar"
description: "party responsible for maintaining records on behalf of the issuer that identify the owners of a registered bond issue"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondRegistrar
tags: [SEC, Release]
detail: "The trustee under a bond contract often also acts as registrar."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registrar.md", provenance: fibo}
  - {type: registers, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
---

party responsible for maintaining records on behalf of the issuer that identify the owners of a registered bond issue

### Relationships
- is-a: [LegalAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- is-a: [Registrar](/CMNS/RegistrationAuthorities/Registrar.md)
- registers: [Bond](/SEC/Debt/Bonds/Bond.md)
