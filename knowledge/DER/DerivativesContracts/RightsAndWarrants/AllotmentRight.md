---
type: FIBO Class
title: "allotment right"
description: "privileges allotted to existing security holders, entitling them to receive new securities free of charge"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRight
tags: [DER, Release]
detail: "Allotment generally means the distribution of equity, particularly shares granted to a participating underwriting firm during an initial public offering (IPO)."
synonyms:
  - "bonus right"
relations:
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md", provenance: fibo}
  - {type: has-expression, target: "/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula.md", provenance: fibo}
---

privileges allotted to existing security holders, entitling them to receive new securities free of charge

### Relationships
- is-a: [EquityDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)
- is-a: [Entitlement](/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
- has-expression: [AllotmentRightFormula](/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula.md)
