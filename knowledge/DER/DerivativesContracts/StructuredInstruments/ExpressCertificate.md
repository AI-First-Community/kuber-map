---
type: FIBO Class
title: "express certificate"
description: "participation certificate whose payout is conditional: should the underlying trade above the strike on the observation date, an early redemption consisting of nominal price plus an additional coupon amount is paid"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ExpressCertificate
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md", provenance: fibo}
---

participation certificate whose payout is conditional: should the underlying trade above the strike on the observation date, an early redemption consisting of nominal price plus an additional coupon amount is paid

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- is-a: [StructuredFinanceWithoutPrincipalProtection](/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)
