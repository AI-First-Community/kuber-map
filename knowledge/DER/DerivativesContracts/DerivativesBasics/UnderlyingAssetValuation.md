---
type: FIBO Class
title: "underlying asset valuation"
description: "assessment activity to estimate the value of an underlying asset of a derivative"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/ValueAssessment.md", provenance: fibo}
  - {type: evaluates, target: "/FBC/FinancialInstruments/FinancialInstruments/Underlier.md", provenance: fibo}
  - {type: has-calculation-agent, target: "/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent.md", provenance: fibo}
---

assessment activity to estimate the value of an underlying asset of a derivative

### Relationships
- is-a: [ValueAssessment](/FND/Arrangements/Assessments/ValueAssessment.md)
- evaluates: [Underlier](/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)
- has-calculation-agent: [CalculationAgent](/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent.md)
