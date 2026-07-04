---
type: FIBO Class
title: "option holder"
description: "party that owns an option"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionHolder
tags: [DER, Release]
detail: "In a call, the option holder has the right, but not the obligation, to buy the underlying asset, while, in a put, the option holder has the right to sell the underlying asset. An option holder may sell the option contract itself, at which point the buyer becomes the option holder. Once the instrument is exercised there are typically additional, relevant obligations with regard to settlement."
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
  - {type: holds, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

party that owns an option

### Relationships
- is-a: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
- holds: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
