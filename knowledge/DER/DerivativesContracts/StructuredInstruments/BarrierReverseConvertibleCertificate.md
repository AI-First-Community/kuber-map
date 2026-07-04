---
type: FIBO Class
title: "barrier reverse convertible certificate"
description: "participation certificate whose payout is conditional: should the barrier never be breached, the nominal price plus coupon is paid at redemption; if the barrier is breached the product changes into a reverse convertible"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierReverseConvertibleCertificate
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md", provenance: fibo}
---

participation certificate whose payout is conditional: should the barrier never be breached, the nominal price plus coupon is paid at redemption; if the barrier is breached the product changes into a reverse convertible

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- is-a: [StructuredFinanceWithoutPrincipalProtection](/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)
