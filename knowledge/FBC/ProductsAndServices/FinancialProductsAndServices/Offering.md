---
type: FIBO Class
title: "offering"
description: "expression of interest in providing something to someone that is contingent upon acceptance, forbearance, or some other consideration, as might be desired by an offeree(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering
tags: [FBC, Release]
detail: "An offering may or may not be considered a 'state of affairs' or situation, depending on the circumstances. In some cases such as a prospectus or other offering in the context of financial services, an offering may also be classified as a situation. Users may choose to model an individual offering as both an offering and situation, depending on the circumstances, in other words. The making of an offer is the first of three steps in the traditional process of forming a valid contract: an offer, an acceptance of the offer, and an exchange of consideration. (Consideration is the act of doing something or promising to do something that a person is not legally required to do, or the forbearance or the promise to forbear from doing something that he or she has the legal right to do.)"
relations:
  - {type: has-party-role, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Offeree.md", provenance: fibo}
  - {type: has-party-role, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md", provenance: fibo}
---

expression of interest in providing something to someone that is contingent upon acceptance, forbearance, or some other consideration, as might be desired by an offeree(s)

### Relationships
- has-party-role: [Offeree](/FBC/ProductsAndServices/FinancialProductsAndServices/Offeree.md)
- has-party-role: [Offeror](/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md)
- is-issued-by: [Offeror](/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md)
