---
type: Cross-Domain Relation
title: "total return swap -> security"
description: "A total return swap pays the total economic return of a reference security in exchange for a financing rate."
tags: [bridge, DER, FBC]
relations:
  - {type: references, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: curated}
source_class: "/DER/DerivativesContracts/Swaps/TotalReturnSwap.md"
kind: "cross-domain (DER->FBC)"
citation: "ISDA total return swap documentation; synthetic financing structures"
rationale: "A total return swap pays the total economic return of a reference security in exchange for a financing rate. FIBO models the total return swap (DER) and Security (FBC) but does not link the swap to the security whose return it pays."
---

**total return swap** --[references]--> **security**  _(curated bridge — cross-domain (DER->FBC))_

A total return swap pays the total economic return of a reference security in exchange for a financing rate. FIBO models the total return swap (DER) and Security (FBC) but does not link the swap to the security whose return it pays.

*Citation:* ISDA total return swap documentation; synthetic financing structures
