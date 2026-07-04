---
type: FIBO Class
title: "naked warrant"
description: "warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that does not hold as many securities as would be required if all the warrants are exercised"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/NakedWarrant
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/RightsAndWarrants/Warrant.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that does not hold as many securities as would be required if all the warrants are exercised

### Relationships
- is-a: [Warrant](/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)
- is-issued-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
