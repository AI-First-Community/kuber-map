---
type: FIBO Class
title: "contract for difference"
description: "cash-settled derivative where the parties agree to exchange on the maturity of the contract the difference between the current value of the underlying asset and the initial value of that asset when the contract is initiated"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ContractForDifference
tags: [DER, Release]
detail: "These contracts can also be on the difference of two assets' prices. They can also be on the difference of a single asset of different maturities (like a bond or futures contracts)."
examples:
  - "For example, suppose the initial price of share XYZ is $100 and a CFD for 1000 shares is exchanged. Both the buyer and seller must post some margin. If the price goes to $105, then the buyer gets $5,000 from the seller. If the price goes to $95, the buyer pays the seller $5,000. This contract avoids ownership of the stock and all the associated transactions issues (like stamp taxes). The contract also allows for leverage (typically 10:1) because the margin that must be posted is only a fraction of the value of the underlying asset."
synonyms:
  - "CFD"
  - "spread trading"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
---

cash-settled derivative where the parties agree to exchange on the maturity of the contract the difference between the current value of the underlying asset and the initial value of that asset when the contract is initiated

### Relationships
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
