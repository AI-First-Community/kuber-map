---
type: FIBO Class
title: "covered warrant"
description: "warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that holds as many securities as would be required if all the warrants are exercised"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant
tags: [DER, Release]
detail: "Covered warrants are very similar to options in that they can be created to allow holders to benefit from either rising prices or falling prices, by having both put and call warrants. They can also be created on a wide variety of underlying instruments, not just equities and they are fairly standardised and are mostly traded on exchanges. The main difference is that warrants tend to have longer maturity dates, typically measured in years instead of months (as with options), and are easier to access for individuals as they can be bought and sold in the same way as shares in the stock exchange. In contrast to traditional equity warrants, with covered warrants, no new issuance of common stock occurs if the warrant is exercised. The underlying shares of common stock are usually either owned by the issuer of the covered warrants or the issuer has a mechanism, such as owning equity warrants for the underlying shares, through which they can obtain the shares."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/RightsAndWarrants/Warrant.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that holds as many securities as would be required if all the warrants are exercised

### Relationships
- is-a: [Warrant](/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)
- is-issued-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
