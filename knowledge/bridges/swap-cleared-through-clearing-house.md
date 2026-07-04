---
type: Cross-Domain Relation
title: "swap -> clearing house"
description: "Standardized OTC swaps are subject to mandatory central clearing through a clearing house acting as central counterparty."
tags: [bridge, DER, FBC]
relations:
  - {type: cleared-through, target: "/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md", provenance: curated}
source_class: "/DER/DerivativesContracts/Swaps/Swap.md"
kind: "cross-domain (DER->FBC)"
citation: "Dodd-Frank Act Title VII; EU EMIR (Regulation 648/2012) clearing obligation"
rationale: "Standardized OTC swaps are subject to mandatory central clearing through a clearing house acting as central counterparty. FIBO defines Swap (DER) and ClearingHouse (FBC) but leaves the cleared-through relationship implicit."
---

**swap** --[cleared-through]--> **clearing house**  _(curated bridge — cross-domain (DER->FBC))_

Standardized OTC swaps are subject to mandatory central clearing through a clearing house acting as central counterparty. FIBO defines Swap (DER) and ClearingHouse (FBC) but leaves the cleared-through relationship implicit.

*Citation:* Dodd-Frank Act Title VII; EU EMIR (Regulation 648/2012) clearing obligation
