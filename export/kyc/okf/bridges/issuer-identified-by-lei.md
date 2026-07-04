---
type: Cross-Domain Relation
title: "issuer -> legal entity identifier"
description: "For securities issuance and regulatory reporting a securities issuer is identified by its Legal Entity Identifier."
tags: [bridge, FBC, BE]
relations:
  - {type: identified-by, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: curated}
source_class: "/FBC/FinancialInstruments/FinancialInstruments/Issuer.md"
kind: "cross-domain (FBC->BE)"
citation: "ISO 17442 (LEI); MiFID II / ESMA and SEC issuer identification"
rationale: "For securities issuance and regulatory reporting a securities issuer is identified by its Legal Entity Identifier. FIBO defines the Issuer role (FBC) and the LegalEntityIdentifier (BE) but does not connect an issuer to its LEI."
---

**issuer** --[identified-by]--> **legal entity identifier**  _(curated bridge — cross-domain (FBC->BE))_

For securities issuance and regulatory reporting a securities issuer is identified by its Legal Entity Identifier. FIBO defines the Issuer role (FBC) and the LegalEntityIdentifier (BE) but does not connect an issuer to its LEI.

*Citation:* ISO 17442 (LEI); MiFID II / ESMA and SEC issuer identification
