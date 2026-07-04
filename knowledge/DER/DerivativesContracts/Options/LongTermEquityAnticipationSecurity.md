---
type: FIBO Class
title: "long-term equity anticipation security"
description: "equity option that allows the holder to buy or sell shares of stock with expiration dates that are longer than one year, and typically up to three years from issue"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/LongTermEquityAnticipationSecurity
tags: [DER, Release]
detail: "By providing opportunities to control and manage risk or even to speculate, LEAPS are virtually identical to regular options. Expiration dates on LEAPs can range from nine months to three years, which is longer than the holding period for a traditional call or put option. Although they are not available on all stocks, LEAPS are available on most widely held issues."
synonyms:
  - "LEAP"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/EquityOption.md", provenance: fibo}
  - {type: has-contract-duration, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
---

equity option that allows the holder to buy or sell shares of stock with expiration dates that are longer than one year, and typically up to three years from issue

### Relationships
- is-a: [EquityOption](/DER/DerivativesContracts/Options/EquityOption.md)
- has-contract-duration: [Duration](/CMNS/DatesAndTimes/Duration.md)
