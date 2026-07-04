---
type: FIBO Class
title: "exchange-traded fund"
description: "investment fund whose fund units are traded on an exchange, much like stocks"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ExchangeTradedFund
tags: [SEC, Release]
core: true
detail: "An ETF holds assets such as stocks, commodities, or bonds, and trades close to its net asset value over the course of the trading day. Most ETFs track an index, such as a stock, bond, or commodity index."
examples:
  - "SPDR S&P 500 ETF (SPY), traded intraday on an exchange."
examples_provenance: curated
synonyms:
  - "ETF"
relations:
  - {type: is-a, target: "/SEC/Funds/Funds/OpenEndInvestment.md", provenance: fibo}
---

investment fund whose fund units are traded on an exchange, much like stocks

### Relationships
- is-a: [OpenEndInvestment](/SEC/Funds/Funds/OpenEndInvestment.md)
