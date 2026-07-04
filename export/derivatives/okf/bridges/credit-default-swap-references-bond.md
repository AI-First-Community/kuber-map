---
type: Cross-Domain Relation
title: "credit default swap -> bond"
description: "A credit default swap transfers the credit risk of a reference obligation, typically a bond of the reference entity."
tags: [bridge, DER, SEC]
relations:
  - {type: references, target: "/SEC/Debt/Bonds/Bond.md", provenance: curated}
source_class: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md"
kind: "cross-domain (DER->SEC)"
citation: "ISDA Credit Derivatives Definitions (reference obligation)"
rationale: "A credit default swap transfers the credit risk of a reference obligation, typically a bond of the reference entity. FIBO models the CDS (DER) and the bond (SEC) in separate domains but does not draw the edge from the swap to the debt security it references."
---

**credit default swap** --[references]--> **bond**  _(curated bridge — cross-domain (DER->SEC))_

A credit default swap transfers the credit risk of a reference obligation, typically a bond of the reference entity. FIBO models the CDS (DER) and the bond (SEC) in separate domains but does not draw the edge from the swap to the debt security it references.

*Citation:* ISDA Credit Derivatives Definitions (reference obligation)
