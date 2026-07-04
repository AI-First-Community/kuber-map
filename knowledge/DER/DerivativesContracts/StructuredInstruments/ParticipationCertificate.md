---
type: FIBO Class
title: "participation certificate"
description: "participation product that provides the possibility to participate in the gains or losses in the price of an asset, subject to counterparty risk"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
tags: [DER, Release]
detail: "In many cases, certificates do not give the investor the right to receive dividend distributions from the underlying stocks or other assets. For example: You buy a bonus certificate issued by your bank which is based on a stock that pays annual dividends. During the certificate's term, the bank holds the underlying stock and receives the dividends. At the end of the term, the bank pays the predefined bonus, even though the actual price of the stock is lower (but not below the protection threshold).Depending on the type of certificate, the exact terms and conditions, and the contract's expiry date, it is possible that the investor may receive the underlying asset instead of money at the end of the investment term. That is often the case with discount certificates based on stocks, for example, when their price sits below the predetermined cap. If the certificate's issuer becomes insolvent, the assets which underly the certificate are considered part of the issuer's liquid assets. This is in contrast to owning actual securities or shares in investment funds, as these are segregated assets which remain the property of the investor if the broker or custodian bank fails."
synonyms:
  - "bearer debt note"
  - "certificate"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md", provenance: fibo}
---

participation product that provides the possibility to participate in the gains or losses in the price of an asset, subject to counterparty risk

### Relationships
- is-a: [ParticipationInstrument](/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument.md)
- is-a: [StructuredFinanceInstrument](/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)
