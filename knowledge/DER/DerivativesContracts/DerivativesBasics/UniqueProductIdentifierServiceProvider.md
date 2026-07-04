---
type: FIBO Class
title: "unique product identifier service provider"
description: "organization designated by an external body of financial regulators to assign UPIs and operate a UPI reference data library"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider
tags: [DER, Release]
synonyms:
  - "UPI service provider"
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
  - {type: registers, target: "/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md", provenance: fibo}
---

organization designated by an external body of financial regulators to assign UPIs and operate a UPI reference data library

### Relationships
- is-a: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
- registers: [UniqueProductIdentifier](/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md)
