---
type: FIBO Class
title: "principal protected note"
description: "structured finance that offers investors exposure to chosen underlying assets using various approaches and asymmetric pay-off profiles"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote
tags: [SEC, Release]
detail: "There are one or more reference entities underlying the product. Redemption is made at least in the amount of the conditional capital protection at maturity, provided that no credit event by the reference entity has occurred. Conditional capital protection only applies to the nominal amount and not to the purchase price. The general functioning of a capital guaranteed structured instrument is as follows: the notional amount is split into a zero bond, that will deliver the capital guarantee at maturity, and the difference between the zero bond's value (= present value of the guarantee level at maturity) and the notional amount is used for structuring the performance component with options which deliver the agreed pay-off profile of the structured instrument."
synonyms:
  - "capital protected note"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md", provenance: fibo}
---

structured finance that offers investors exposure to chosen underlying assets using various approaches and asymmetric pay-off profiles

### Relationships
- is-a: [CapitalProtectedProduct](/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md)
- is-a: [StructuredFinanceInstrument](/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)
