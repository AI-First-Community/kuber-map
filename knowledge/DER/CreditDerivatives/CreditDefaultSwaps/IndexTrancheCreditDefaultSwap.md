---
type: FIBO Class
title: "index tranche credit default swap"
description: "credit default swap that references a synthetic collateralized debt obligation (CDO) based on a credit index where each tranche references a different segment of the loss distribution of the underlying index"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/IndexTrancheCreditDefaultSwap
tags: [DER, Release]
detail: "Each tranche has a different priority of claims on the principal and interest flows from the collateral pool, and is traditionally portioned into rising levels of seniority."
relations:
  - {type: is-a, target: "/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md", provenance: fibo}
---

credit default swap that references a synthetic collateralized debt obligation (CDO) based on a credit index where each tranche references a different segment of the loss distribution of the underlying index

### Relationships
- is-a: [MultiNameCreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md)
