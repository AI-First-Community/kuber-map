---
type: FIBO Class
title: "discount certificate"
description: "participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the underlying asset(s) and/or a cash amount is redeemed should the underlying asset close below the strike on expiry, for which, in return, the potential profit is capped"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/DiscountCertificate
tags: [DER, Release]
detail: "At the end of the certificate's maturity, a cash disbursement occurs. If the price of the underlying when the maturity is up is higher than the maximal payout or identical to it, the issuer pays the maximum amount. If the price of the underlying is less than the cap, the issuer pays either the current price of the certificate in cash or he gives the investor the underlying, for example a share, at its current price. The issuer can choose. The cash payout is obligatory in the case of discount certificates on indices, currencies or interest. Discount certificates are ideal for conservative investors that want to guard against market fluctuations and who expect in the medium term sideways-moving prices. Because the buyer of a discount certificate does not profit from price gains that are higher than the cap, this form of investment is best suited for a medium-term oriented engagement. If the certificate reaches its cap before the maturity, the investor should take the profits. The maximum profit that an investor can reach with a discount certificate is calculated by taking the difference between the purchase price and the cap on the underlying. Losses, in contrast, are lessened by the discount. The investor suffers a loss only when the price of the underlying at the end of the maturity has fallen so far that the discount is depleted. The discount thus works as a buffer against risk."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md", provenance: fibo}
---

participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the underlying asset(s) and/or a cash amount is redeemed should the underlying asset close below the strike on expiry, for which, in return, the potential profit is capped

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- is-a: [StructuredFinanceWithoutPrincipalProtection](/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)
