---
type: FIBO Class
title: "student loan asset-backed security"
description: "asset-backed security based on student loan receivables"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanAssetBackedSecurity
tags: [SEC, Release]
detail: "If the credit risk of the pool has been decoupled from the institution via an SPV, then student loan asset-backed securities are also structured finance instruments. The main purpose behind Student Loan ABS is to diversify the risk for lenders across many investors. By pooling and then packaging the loans into securities and selling them to investors, agencies can spread around the default risk, which allows them to give out more loans and larger loans. This way, more students have access to loans, investors have a diversifying investment instrument, and lenders can generate consistent cash flow from their securitization and debt collection services."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Debt/AssetBackedSecurities/StudentLoanPool.md", provenance: fibo}
---

asset-backed security based on student loan receivables

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- is-based-on: [StudentLoanPool](/SEC/Debt/AssetBackedSecurities/StudentLoanPool.md)
