---
type: FIBO Class
title: "synthetic debt instrument pool"
description: "A cash flow structure which synthesizes the behavior of a portfolio of debt securities. For example a synthesized portfolio of CDO / Bonds / ABS using Total Returns Swaps and CDS. This does exist, it is just manufactured from different instruments."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPool
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: funded-by, target: "/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md", provenance: fibo}
  - {type: has-underlying-contract, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md", provenance: fibo}
  - {type: makes-reference-to, target: "/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio.md", provenance: fibo}
---

A cash flow structure which synthesizes the behavior of a portfolio of debt securities. For example a synthesized portfolio of CDO / Bonds / ABS using Total Returns Swaps and CDS. This does exist, it is just manufactured from different instruments.

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- funded-by: [SyntheticDebtInstrumentPoolFundingAsset](/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md)
- has-underlying-contract: [CreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)
- makes-reference-to: [SyntheticCDOPortfolio](/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio.md)
