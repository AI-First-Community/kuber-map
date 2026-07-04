---
type: FIBO Class
title: "security underwriter"
description: "party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution of any security, or participates or has a direct or indirect participation in any such undertaking, or participates or has a participation in the direct or indirect underwriting of any such undertaking"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter
tags: [SEC, Release]
core: true
examples:
  - "An investment bank that buys a new bond issue from the issuer to resell to investors."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
---

party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution of any security, or participates or has a direct or indirect participation in any such undertaking, or participates or has a participation in the direct or indirect underwriting of any such undertaking

### Relationships
- is-a: [Underwriter](/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)
- is-a: [ThirdPartyAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
