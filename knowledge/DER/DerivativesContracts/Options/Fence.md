---
type: FIBO Class
title: "fence"
description: "option trading strategy that uses options to limit the range of possible returns on a financial instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Fence
tags: [DER, Release]
detail: "A fence consists of the following elements: - long position in a financial instrument (e.g., a share, index or currency) - long put (normally with a strike price close to or at the current spot price of the financial instrument) - short put (with a strike price lower than the bought put - e.g., 80% of the current spot price) - short call (with a strike price higher than the current spot price). The expiration dates of all the options are usually the same. The call strike is normally chosen in such a way that the sum total of the three option premiums is equal to zero. This investment strategy will ensure that the value of the investment at expiry will be between the strike price on the short call and the strike price on the long put. Thus, possible gains and losses (the value of the financial instrument minus the cost of acquiring it) are confined to a specified range. However, if the price of the financial instrument falls below the strike level of the sold put the investor will start participating in any further price declines of the financial instrument."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
---

option trading strategy that uses options to limit the range of possible returns on a financial instrument

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
