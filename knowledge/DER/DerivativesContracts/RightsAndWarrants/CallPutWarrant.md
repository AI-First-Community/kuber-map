---
type: FIBO Class
title: "call put warrant"
description: "warrant that either does not specify call or put features, or that explicitly includes both a call and put feature"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallPutWarrant
tags: [DER, Release]
detail: "The call and put code, 'B', in the CFI stands for 'Both', meaning such a warrant embodies characteristics of both a call and a put. This can appear in structured warrants or exotic warrants where payout may depend on movements in either direction (or give the holder a choice at certain triggers)."
synonyms:
  - "straddle warrant"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/RightsAndWarrants/PutWarrant.md", provenance: fibo}
---

warrant that either does not specify call or put features, or that explicitly includes both a call and put feature

### Relationships
- is-a: [CallWarrant](/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md)
- is-a: [PutWarrant](/DER/DerivativesContracts/RightsAndWarrants/PutWarrant.md)
