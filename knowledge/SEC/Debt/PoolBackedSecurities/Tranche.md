---
type: FIBO Class
title: "tranche"
description: "segment of a pool of securities, typically debt instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche
tags: [SEC, Release]
core: true
detail: "A tranche is one of a number of related securities in the same offering that represents a partition of a debt pool whose cash flow is derived from the combined cash flows of the instruments in that partition."
examples:
  - "The senior AAA-rated tranche of a securitization, paid before the junior tranches."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md", provenance: fibo}
  - {type: has-attachment-point, target: "/SEC/Debt/PoolBackedSecurities/AttachmentPoint.md", provenance: fibo}
  - {type: has-detachment-point, target: "/SEC/Debt/PoolBackedSecurities/DetachmentPoint.md", provenance: fibo}
  - {type: is-estimated-value-of, target: "/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md", provenance: fibo}
---

segment of a pool of securities, typically debt instruments

### Relationships
- is-a: [StructuredFinanceInstrument](/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)
- has-attachment-point: [AttachmentPoint](/SEC/Debt/PoolBackedSecurities/AttachmentPoint.md)
- has-detachment-point: [DetachmentPoint](/SEC/Debt/PoolBackedSecurities/DetachmentPoint.md)
- is-estimated-value-of: [CollateralValueAsOfDate](/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
