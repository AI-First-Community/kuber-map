---
type: FIBO Class
title: "protective collar"
description: "collar that consists of a covered call and protective put"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectiveCollar
tags: [DER, Release]
detail: "A protective collar consists of a long position in the underlying security, a put option purchased to hedge the downside risk on a stock, a call option written on the stock to finance the put purchase."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/Collar.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CoveredCall.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/ProtectivePut.md", provenance: fibo}
---

collar that consists of a covered call and protective put

### Relationships
- is-a: [Collar](/DER/DerivativesContracts/Options/Collar.md)
- comprises: [CoveredCall](/DER/DerivativesContracts/Options/CoveredCall.md)
- comprises: [ProtectivePut](/DER/DerivativesContracts/Options/ProtectivePut.md)
