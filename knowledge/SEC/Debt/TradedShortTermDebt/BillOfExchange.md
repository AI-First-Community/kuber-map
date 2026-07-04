---
type: FIBO Class
title: "bill of exchange"
description: "short-term negotiable financial instrument consisting of an order in writing addressed by one person (the seller of goods) to another (the buyer), requiring the latter to pay a fixed amount of money on demand (a sight draft) or on a predetermined date (a time draft)"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BillOfExchange
tags: [SEC, Release]
detail: "A bill of exchange is a written agreement between two parties - the buyer and the seller - used primarily in international trade. The buyer or seller typically employs a bank to issue the bill of exchange due to the risks involved with international transactions. Bills of exchange can be transferred by endorsement, much like a check. They can also require the buyer to pay a third party - a bank - in the event that the buyer fails to make good on his agreement with the seller."
synonyms:
  - "bank draft"
  - "draft"
relations:
  - {type: is-a, target: "/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md", provenance: fibo}
  - {type: has-party-role, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md", provenance: fibo}
  - {type: has-party-role, target: "/SEC/Debt/TradedShortTermDebt/Drawee.md", provenance: fibo}
  - {type: has-party-role, target: "/SEC/Debt/TradedShortTermDebt/Drawer.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

short-term negotiable financial instrument consisting of an order in writing addressed by one person (the seller of goods) to another (the buyer), requiring the latter to pay a fixed amount of money on demand (a sight draft) or on a predetermined date (a time draft)

### Relationships
- is-a: [MoneyMarketInstrument](/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)
- has-party-role: [Payee](/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)
- has-party-role: [Drawee](/SEC/Debt/TradedShortTermDebt/Drawee.md)
- has-party-role: [Drawer](/SEC/Debt/TradedShortTermDebt/Drawer.md)
- is-issued-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
