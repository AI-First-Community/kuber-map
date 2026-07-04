---
type: Cross-Domain Relation
title: "legal entity -> legal entity identifier"
description: "For KYC and entity resolution a legal entity is identified by its Legal Entity Identifier (ISO 17442)."
tags: [bridge, CMNS, BE]
relations:
  - {type: identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: curated}
source_class: "/CMNS/Organizations/LegalEntity.md"
kind: "cross-domain (CMNS->BE)"
citation: "ISO 17442 (LEI); FATF Recommendation 24"
rationale: "For KYC and entity resolution a legal entity is identified by its Legal Entity Identifier (ISO 17442). FIBO defines LegalEntityIdentifier and applies it to LEI-registered entities, but does not link the base LegalEntity class to it, leaving generic entity-to-LEI resolution implicit."
---

**legal entity** --[identified-by]--> **legal entity identifier**  _(curated bridge — cross-domain (CMNS->BE))_

For KYC and entity resolution a legal entity is identified by its Legal Entity Identifier (ISO 17442). FIBO defines LegalEntityIdentifier and applies it to LEI-registered entities, but does not link the base LegalEntity class to it, leaving generic entity-to-LEI resolution implicit.

*Citation:* ISO 17442 (LEI); FATF Recommendation 24
