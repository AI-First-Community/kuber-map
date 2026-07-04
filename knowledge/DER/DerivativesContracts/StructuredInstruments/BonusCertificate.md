---
type: FIBO Class
title: "bonus certificate"
description: "certificate whose minimum redemption is equal to the nominal value provided the barrier has not been breached, with a greater risk in relation to multiple underlying asset(s) (worst-of), allowing for a higher bonus level or lower barrier, and with a reduced risk compared to a direct investment into the underlying asset(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BonusCertificate
tags: [DER, Release]
detail: "Bonus certificates have a risk buffer for price losses in the underlying; the bonus guarantees a minimum return above the risk level. A bonus certificate represents an alternative to a direct investment in a share or an index. Investors primarily use them if they believe that despite rising prices setbacks are still likely to occur. 		 A bonus certificate is furnished with a bonus amount and an upper and lower price level. If the certificate expires with the price of the underlying ranging between these two levels, owners are paid out their bonuses. If the underlying was at or below the risk level during the certificate's lifetime, its price is that of the current value of the certificate at expiry. If the underlying is above the upper level at expiry, the investor fully participates in the price gains. Some bonus certificates have a profit cap. This is where the certificate stops participating in the price gains of the underlying.  A bonus certificate is issued at the current price of the underlying. The upper level is derived from adding the bonus to the issue price. The lower level is determined at issuance and usually expressed in percent."
examples:
  - "For example: You buy a bonus certificate based on a stock. The price of the stock at the time that you get the certificate is 100 Euros. The bonus level is 120 Euros, and the protection threshold is 80 Euros. Over the two-year term, the price of the stock fluctuates between 90 and 110 Euros. When the certificate matures at the end of the term, you receive the bonus price of 120 Euros."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
---

certificate whose minimum redemption is equal to the nominal value provided the barrier has not been breached, with a greater risk in relation to multiple underlying asset(s) (worst-of), allowing for a higher bonus level or lower barrier, and with a reduced risk compared to a direct investment into the underlying asset(s)

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
