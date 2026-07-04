---
type: FIBO Class
title: "risk reversal"
description: "option trading strategy that consists of being short (selling) an out of the money put and being long (i.e., buying) an out of the money call, both with the same maturity"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/RiskReversal
tags: [DER, Release]
detail: "A risk reversal is a position which simulates profit and loss behavior of owning an underlying security; therefore, it is sometimes called a synthetic long. This is an investment strategy that amounts to both buying and selling out-of-money options simultaneously. In this strategy, the investor will first make a market hunch; if that hunch is bullish, he will want to go long. However, instead of going long on the stock, he will buy an out of the money call option, and simultaneously sell an out of the money put option. Presumably he will use the money from the sale of the put option to purchase the call option. Then as the stock goes up in price, the call option will be worth more, and the put option will be worth less."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

option trading strategy that consists of being short (selling) an out of the money put and being long (i.e., buying) an out of the money call, both with the same maturity

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
