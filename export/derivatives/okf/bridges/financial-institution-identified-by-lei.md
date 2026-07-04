---
type: Cross-Domain Relation
title: "financial institution -> legal entity identifier"
description: "For KYC / entity resolution a financial institution is identified by its Legal Entity Identifier."
tags: [bridge, FBC, BE]
relations:
  - {type: identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: curated}
source_class: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md"
kind: "cross-domain (FBC->BE)"
citation: "ISO 17442 (LEI); FIBO BE LegalEntityIdentifier"
rationale: "For KYC / entity resolution a financial institution is identified by its Legal Entity Identifier. FIBO defines LegalEntityIdentifier in BE but does not connect FinancialInstitution to it."
---

**financial institution** --[identified-by]--> **legal entity identifier**  _(curated bridge — cross-domain (FBC->BE))_

For KYC / entity resolution a financial institution is identified by its Legal Entity Identifier. FIBO defines LegalEntityIdentifier in BE but does not connect FinancialInstitution to it.

*Citation:* ISO 17442 (LEI); FIBO BE LegalEntityIdentifier
