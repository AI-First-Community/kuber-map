---
type: FIBO Class
title: "unique product identifier registry entry"
description: "entry in a unique product identifier registry"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierRegistryEntry
tags: [DER, Release]
detail: "The Reference Data Library (RDL) is a set of reference data elements, together with their values, which is properly organized and maintained by the UPI service provider. The library associates UPI codes with the values of the reference data elements characterizing the product. Each entry in the library (the registry entry) contains a minimum number of elements as defined in the ISO standard, and may be extended by the service provider."
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: applies-to, target: "/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md", provenance: fibo}
  - {type: is-included-in, target: "/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierReferenceDataLibrary.md", provenance: fibo}
---

entry in a unique product identifier registry

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- applies-to: [OverTheCounterDerivativeInstrument](/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- comprises: [UniqueProductIdentifier](/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md)
- is-included-in: [UniqueProductIdentifierReferenceDataLibrary](/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierReferenceDataLibrary.md)
