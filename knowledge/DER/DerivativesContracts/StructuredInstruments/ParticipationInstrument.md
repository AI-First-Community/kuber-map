---
type: FIBO Class
title: "participation instrument"
description: "structured product that provides the possibility to participate in the performance of an asset or basket of assets"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument
tags: [DER, Release]
detail: "The construction is generally based on a low exercise price option (LEPO) (base value less discounted future dividends) which in some cases might be comparable to a direct investment in the underlying asset(s) or a LEPO combined with other options, which together provide the desired disbursement profile. These assets could be anything, from equities, funds, bonds, ETFs indices to a mix of those. The most common participation products are tracker certificates, providing 1-to-1 participation to the performance of a basket of securities."
synonyms:
  - "participation product"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md", provenance: fibo}
---

structured product that provides the possibility to participate in the performance of an asset or basket of assets

### Relationships
- is-a: [StructuredProduct](/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)
- is-a: [SecurityBasedDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)
