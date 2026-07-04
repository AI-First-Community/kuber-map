---
type: FIBO Class
title: "equity forward"
description: "forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures contract, or equity option at a specified future date at the price specified at the outset of the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A forward to buy 1,000 shares in six months at a set price."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/Forward.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: has-dividend-adjustment-period, target: "/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod.md", provenance: fibo}
  - {type: has-method-of-adjustment, target: "/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod.md", provenance: fibo}
---

forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures contract, or equity option at a specified future date at the price specified at the outset of the contract

### Relationships
- is-a: [Forward](/DER/DerivativesContracts/FuturesAndForwards/Forward.md)
- has-contractual-element: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- has-dividend-adjustment-period: [DividendAdjustmentPeriod](/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod.md)
- has-method-of-adjustment: [ForwardContractAdjustmentMethod](/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod.md)
