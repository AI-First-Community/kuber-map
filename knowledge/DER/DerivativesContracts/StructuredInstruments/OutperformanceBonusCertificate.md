---
type: FIBO Class
title: "outperformance bonus certificate"
description: "certificate that allows disproportionate participation (outperformance) in positive performance above the strike, in which the minimum redemption is equal to the nominal value provided the barrier has not been breached, with greater risk multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier, and reduced risk compared to a direct investment into the underlying asset(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceBonusCertificate
tags: [DER, Release]
detail: "The outperformance bonus certificate combines the strengths of both outperformance and normal bonus certificates. This means that you’re protected on the downside by a bonus level (i.e., a feature of bonus certificates) but nevertheless have the opportunity to participate disproportionately in upside gains in the underlying instrument (the 'outperformance certificate' dimension). If you compare all three structured product types with each other, you’ll see that outperformance bonus certificates come up a bit short in terms of the characteristics of the other two forms. In other words, the disproportionate participation rate (outperformance) is usually somewhat lower than with a 'plain vanilla' outperformance certificate. This is because additional bonus protection has to be bought in order to structure the product properly. The same applies to the bonus dimension: because such a certificate still affords disproportionate participation, its downside protection level is more modest."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/BonusCertificate.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate.md", provenance: fibo}
---

certificate that allows disproportionate participation (outperformance) in positive performance above the strike, in which the minimum redemption is equal to the nominal value provided the barrier has not been breached, with greater risk multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier, and reduced risk compared to a direct investment into the underlying asset(s)

### Relationships
- is-a: [BonusCertificate](/DER/DerivativesContracts/StructuredInstruments/BonusCertificate.md)
- is-a: [OutperformanceCertificate](/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate.md)
