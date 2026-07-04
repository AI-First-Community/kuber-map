---
type: Cross-Domain Relation
title: "asset-backed security -> loan"
description: "An asset-backed security is collateralized by a pool of receivables such as auto or consumer loans."
tags: [bridge, SEC, LOAN]
relations:
  - {type: backed-by, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: curated}
source_class: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md"
kind: "cross-domain (SEC->LOAN)"
citation: "SEC Regulation AB, 17 CFR 229.1100; securitization structuring"
rationale: "An asset-backed security is collateralized by a pool of receivables such as auto or consumer loans. FIBO defines the ABS in SEC and the loan in LOAN but leaves the backing relationship between the security and its underlying loans implicit."
---

**asset-backed security** --[backed-by]--> **loan**  _(curated bridge — cross-domain (SEC->LOAN))_

An asset-backed security is collateralized by a pool of receivables such as auto or consumer loans. FIBO defines the ABS in SEC and the loan in LOAN but leaves the backing relationship between the security and its underlying loans implicit.

*Citation:* SEC Regulation AB, 17 CFR 229.1100; securitization structuring
