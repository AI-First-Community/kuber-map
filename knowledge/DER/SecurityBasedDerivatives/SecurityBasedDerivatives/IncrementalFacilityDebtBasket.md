---
type: FIBO Class
title: "incremental facility debt basket"
description: "basket of credit facilities whose constituents are extensible, allowing companies to borrow an additional term loan or revolving credit facility (or increase the commitments applicable thereto) under the same credit agreement subject to certain parameters"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/IncrementalFacilityDebtBasket
tags: [DER, Release]
detail: "The incremental debt basket is available to borrowers and guarantors only; it cannot be used by non-guarantor entities to raise indebtedness. The size of the incremental debt basket varies depending on the size and creditworthiness of the credit group. The principle of a basket consists of allowing the borrower, up to a maximum determined amount, to make restricted payments, disposals or investments, or take on incremental debt. Commonly, a basket is expressed as subject to restrictions based on a fixed ('hard cap') amount (e.g., may not exceed EUR 5,000,000)."
synonyms:
  - "builder basket"
relations:
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket.md", provenance: fibo}
---

basket of credit facilities whose constituents are extensible, allowing companies to borrow an additional term loan or revolving credit facility (or increase the commitments applicable thereto) under the same credit agreement subject to certain parameters

### Relationships
- is-a: [CreditFacilityDebtBasket](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket.md)
