---
type: Cross-Domain Relation
title: "customer -> legal person"
description: "A customer is a party role played by a legal person (or a natural person)."
tags: [bridge, FND, CMNS]
relations:
  - {type: played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: curated}
source_class: "/FND/ProductsAndServices/ProductsAndServices/Customer.md"
kind: "role->entity gap (FND->CMNS)"
citation: "FIBO FND party-role vs entity modeling; KYC customer onboarding"
rationale: "A customer is a party role played by a legal person (or a natural person). Resolving 'the customer' to the underlying legal entity is core to KYC onboarding, but FIBO leaves the role-to-entity link implicit."
---

**customer** --[played-by]--> **legal person**  _(curated bridge — role->entity gap (FND->CMNS))_

A customer is a party role played by a legal person (or a natural person). Resolving 'the customer' to the underlying legal entity is core to KYC onboarding, but FIBO leaves the role-to-entity link implicit.

*Citation:* FIBO FND party-role vs entity modeling; KYC customer onboarding
