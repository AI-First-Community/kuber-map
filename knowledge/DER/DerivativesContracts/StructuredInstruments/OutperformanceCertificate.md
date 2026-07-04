---
type: FIBO Class
title: "outperformance certificate"
description: "certificate that allows disproportionate participation (outperformance) in positive performance above the strike, reflecting underlying price moves 1:1 (adjusted by the conversion ratio and any related fees), and whose risk is comparable to direct investment in the underlying asset(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate
tags: [DER, Release]
examples:
  - "For example: You buy an outperformance certificate based on a stock. The certificate’s strike price is 100 Euros and its participation factor is 150 percent. If the price of the underlying stock surpasses the strike price of 100 Euros, you are rewarded with a 150 percent return, instead of just 100 percent. If the price of the stock climbs to 110 Euros, for example, the value of the certificate would be 115 Euros."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
---

certificate that allows disproportionate participation (outperformance) in positive performance above the strike, reflecting underlying price moves 1:1 (adjusted by the conversion ratio and any related fees), and whose risk is comparable to direct investment in the underlying asset(s)

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
