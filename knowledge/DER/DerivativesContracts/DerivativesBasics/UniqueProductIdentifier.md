---
type: FIBO Class
title: "unique product identifier"
description: "sequence of characters uniquely identifying an OTC derivative product that is reportable to a trade repository"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier
tags: [DER, Release]
detail: "The UPI code consists of 12 alphanumeric characters decomposed as follows: 		- the two-character prefix 'QZ' 		- nine alphanumeric characters (upper case A-Z and 0-9 only, excluding the vowel characters (A, E, I, O, U) and the character Y) without separators or special characters 		- one alphanumeric check character (A-Z and 0-9 only, excluding the vowel characters (A, E, I, O, U) and the character Y), calculated using the method specified in Annex C of the specification document."
synonyms:
  - "UPI"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/ContextualIdentifiers/StructuredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md", provenance: fibo}
  - {type: is-registered-by, target: "/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider.md", provenance: fibo}
---

sequence of characters uniquely identifying an OTC derivative product that is reportable to a trade repository

### Relationships
- is-a: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- is-a: [StructuredIdentifier](/CMNS/ContextualIdentifiers/StructuredIdentifier.md)
- identifies: [OverTheCounterDerivativeInstrument](/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- is-registered-by: [UniqueProductIdentifierServiceProvider](/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider.md)
