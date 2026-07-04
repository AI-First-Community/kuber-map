---
type: Cross-Domain Relation
title: "account holder -> legal entity identifier"
description: "An institutional account holder is identified for KYC by its Legal Entity Identifier."
tags: [bridge, FBC, BE]
relations:
  - {type: identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: curated}
source_class: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md"
kind: "cross-domain (FBC->BE)"
citation: "ISO 17442 (LEI); KYC / CDD account onboarding"
rationale: "An institutional account holder is identified for KYC by its Legal Entity Identifier. FIBO models accounts and their holders but does not connect an account holder to its LEI."
---

**account holder** --[identified-by]--> **legal entity identifier**  _(curated bridge — cross-domain (FBC->BE))_

An institutional account holder is identified for KYC by its Legal Entity Identifier. FIBO models accounts and their holders but does not connect an account holder to its LEI.

*Citation:* ISO 17442 (LEI); KYC / CDD account onboarding
