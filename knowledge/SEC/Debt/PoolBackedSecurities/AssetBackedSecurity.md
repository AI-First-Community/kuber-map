---
type: FIBO Class
title: "asset-backed security"
description: "debt instrument backed by receivables other than those arising out of real estate loans or mortgages"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
tags: [SEC, Release]
detail: "An asset-backed security (ABS) is a type of financial investment that is collateralized by an underlying pool of assets—usually ones that generate a cash flow from debt, such as loans, leases, credit card balances, or receivables. It takes the form of a bond or note, paying income at a fixed rate for a set amount of time, until maturity. ABS are financial securities backed by income-generating assets such as credit card receivables, home equity loans, student loans, and auto loans. Pooling assets into an ABS is a process called securitization. One difference between an ABS and a collateralized debt obligation (CDO) is that the CDO issuer is generally a special purpose vehicle (SPV) or trust. Asset-backed securities, for example home equity loans (HEL), credit cards, and so forth are backed by receivables [payments] that are either secured (such as HEL) or unsecured (for example, credit cards). They are typically tranched based on default risk."
synonyms:
  - "ABS"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md", provenance: fibo}
  - {type: has-tranche-type, target: "/SEC/Debt/CollateralizedDebtObligations/TrancheType.md", provenance: fibo}
---

debt instrument backed by receivables other than those arising out of real estate loans or mortgages

### Relationships
- is-a: [PoolBackedSecurity](/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)
- has-tranche-type: [TrancheType](/SEC/Debt/CollateralizedDebtObligations/TrancheType.md)
