---
type: FIBO Class
title: "cash flow"
description: "the movement of money from some source to some sink"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlow
tags: [FND, Provisional]
detail: "From the perspective of an individual investor, the transaction date is the day when the investor's order is executed in the market. However, the process doesn't end there. The value date, on the other hand, is when the transaction actually settles, meaning when the buyer receives the securities and the seller gets the money. This lag between the transaction and value dates is known as the settlement period, which can vary depending on the type of security involved. One of the primary concepts in value dating is the 'value date', which is the date on which the funds from a transaction are considered available for use. This date can be influenced by various factors, including the type of transaction, the currencies involved, and the policies of the financial institutions handling the transaction. For instance, in international transactions, the value date might be delayed due to the time required for currency conversion and cross-border fund transfers."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

the movement of money from some source to some sink

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
