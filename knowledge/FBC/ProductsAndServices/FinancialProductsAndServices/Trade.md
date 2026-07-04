---
type: FIBO Class
title: "trade"
description: "situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
tags: [FBC, Release]
detail: "The advent of money as a medium of exchange has allowed trade to be conducted in a manner that is much simpler and effective compared to earlier forms of trade, such as bartering. In financial markets, trading also can mean performing a transaction that involves the selling and purchasing of a security. The seller must deliver the commodity sold to the buyer; the buyer must pay the agreed purchase price, which could be in the form of other goods or services, on the agreed date. Trading activities typically include (a) regularly underwriting or dealing in securities; interest rate, foreign exchange rate, commodity, equity, and credit derivative contracts; other financial instruments; and other assets for resale, (b) acquiring or taking positions in such items principally for the purpose of selling in the near term or otherwise with the intent to resell in order to profit from short-term price movements, and (c) acquiring or taking positions in such items as an accommodation to customers or for other trading purposes. (Source: Instructions for Preparation of Consolidated Reports of Condition and Income (FFIEC 031 and 041), Schedule RC-D - Trading Assets and Liabilities, 2013."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-buyer, target: "/FND/ProductsAndServices/ProductsAndServices/Buyer.md", provenance: fibo}
  - {type: has-seller, target: "/FND/ProductsAndServices/ProductsAndServices/Seller.md", provenance: fibo}
  - {type: is-characterized-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md", provenance: fibo}
  - {type: is-embodied-in, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-facilitated-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Trader.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md", provenance: fibo}
---

situation that realizes an agreement between parties participating in a voluntary action of buying and selling goods and services

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-buyer: [Buyer](/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- has-seller: [Seller](/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- is-characterized-by: [TradeLifecycle](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- is-embodied-in: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-facilitated-by: [Trader](/FBC/ProductsAndServices/FinancialProductsAndServices/Trader.md)
- is-identified-by: [TradeIdentifier](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md)
