---
type: FIBO Class
title: "protective put"
description: "put option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at with a strike price equal or close to the current price of the underlying asset, on or before a specified date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectivePut
tags: [DER, Release]
detail: "A protective put is a risk management and options strategy that involves holding a long position in the underlying asset (e.g., stock). A protective put strategy is analogous to the nature of insurance. The main goal of a protective put is to limit potential losses that may result from an unexpected price drop of the underlying asset"
synonyms:
  - "synthetic call"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
  - {type: has-calculated-market-value, target: "/DER/DerivativesContracts/Options/OptionPremium.md", provenance: fibo}
---

put option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at with a strike price equal or close to the current price of the underlying asset, on or before a specified date

### Relationships
- is-a: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
- has-calculated-market-value: [OptionPremium](/DER/DerivativesContracts/Options/OptionPremium.md)
