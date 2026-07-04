---
type: FIBO Class
title: "reverse convertible certificate"
description: "participation certificate whose payout is conditional: should the underlying asset close below the strike on expiry, the underlying asset(s) and/ or a cash amount is redeemed; should the underlying asset close above the strike at expiry, the nominal amount plus the coupon is paid at redemption"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ReverseConvertibleCertificate
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md", provenance: fibo}
---

participation certificate whose payout is conditional: should the underlying asset close below the strike on expiry, the underlying asset(s) and/ or a cash amount is redeemed; should the underlying asset close above the strike at expiry, the nominal amount plus the coupon is paid at redemption

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- is-a: [StructuredFinanceWithoutPrincipalProtection](/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)
