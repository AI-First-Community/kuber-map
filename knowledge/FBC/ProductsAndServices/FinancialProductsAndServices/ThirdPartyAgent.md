---
type: FIBO Class
title: "third-party agent"
description: "any service provider that is licensed to perform a legally binding function and has been legally empowered to act on behalf of another party"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
tags: [FBC, Release]
detail: "Note that third-party agent is defined as a service provider (organization) acting in an agency capacity, such as a law firm, accountancy, or investment bank. This is distinct from the concept of an individual (licensed agent), for example one who works for a broker-dealer, that is a registered agent licensed to sell securities."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md", provenance: fibo}
  - {type: is-a, target: "/FND/Law/LegalCapacity/Licensee.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
---

any service provider that is licensed to perform a legally binding function and has been legally empowered to act on behalf of another party

### Relationships
- is-a: [LegalAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- is-a: [Licensee](/FND/Law/LegalCapacity/Licensee.md)
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
