---
type: FIBO Class
title: "structured finance instrument"
description: "pool-backed security wherein the risk associated with the pool has been uncoupled from the risk associated with the originating institution through a special purpose vehicle"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
tags: [SEC, Release]
detail: "Structured finance instruments represent a form of securitization technology which can be defined by three key characteristics: (1) pooling of financial assets, such as loans, bonds, or credit-default swaps; (2) de-linking of the credit risk of the asset pool from the credit risk of the originating firm, usually through use of a finite-lived, stand-alone special purpose vehicle (SPV); and (3) issuance by the SPV of 'tranched' liabilities backed by the asset pool. Structured finance instruments are typically presented to large financial institutions or companies with complicated financing needs that are unsatisfied with conventional financial products."
examples:
  - "Collateralized debt obligations (CDOs), synthetic financial instruments, collateralized bond obligations (CBOs), and syndicated loans are examples of structured finance instruments."
synonyms:
  - "structured finance"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md", provenance: fibo}
---

pool-backed security wherein the risk associated with the pool has been uncoupled from the risk associated with the originating institution through a special purpose vehicle

### Relationships
- is-a: [StructuredProduct](/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)
- is-a: [PoolBackedSecurity](/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)
