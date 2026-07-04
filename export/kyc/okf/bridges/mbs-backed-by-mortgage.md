---
type: Cross-Domain Relation
title: "mortgage-backed security -> mortgage"
description: "A mortgage-backed security represents claims on the cash flows from an underlying pool of mortgage loans."
tags: [bridge, SEC, LOAN]
relations:
  - {type: backed-by, target: "/LOAN/RealEstateLoans/Mortgages/Mortgage.md", provenance: curated}
source_class: "/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md"
kind: "cross-domain (SEC->LOAN)"
citation: "SEC Regulation AB, 17 CFR 229.1100 (asset-backed securities, loan-level data)"
rationale: "A mortgage-backed security represents claims on the cash flows from an underlying pool of mortgage loans. FIBO models the security (SEC) and the mortgage instrument (LOAN) in separate domains but does not draw the edge from the MBS to the mortgage loans that back it, which securitization and loan-level disclosure analysis need."
---

**mortgage-backed security** --[backed-by]--> **mortgage**  _(curated bridge — cross-domain (SEC->LOAN))_

A mortgage-backed security represents claims on the cash flows from an underlying pool of mortgage loans. FIBO models the security (SEC) and the mortgage instrument (LOAN) in separate domains but does not draw the edge from the MBS to the mortgage loans that back it, which securitization and loan-level disclosure analysis need.

*Citation:* SEC Regulation AB, 17 CFR 229.1100 (asset-backed securities, loan-level data)
