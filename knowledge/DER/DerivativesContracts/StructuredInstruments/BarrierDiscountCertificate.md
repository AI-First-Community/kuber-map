---
type: FIBO Class
title: "barrier discount certificate"
description: "participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the maximum redemption amount (Cap) is paid out if the barrier is never breached"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierDiscountCertificate
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md", provenance: fibo}
---

participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the maximum redemption amount (Cap) is paid out if the barrier is never breached

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- is-a: [StructuredFinanceWithoutPrincipalProtection](/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)
