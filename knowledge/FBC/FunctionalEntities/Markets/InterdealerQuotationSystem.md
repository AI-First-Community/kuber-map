---
type: FIBO Class
title: "interdealer quotation system"
description: "automated system for organizing and disseminating price quotes by brokers and dealer firms that facilitates electronic trading in securities"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/InterdealerQuotationSystem
tags: [FBC, Release]
detail: "An IQS ties the price quotations of a number of exchanges together into one platform. This allows investors to more easily access security price quotations that would otherwise need to be monitored on several separate exchanges. In the United States, an IQS is an automated interdealer quotation system of a national securities association registered pursuant to section 15A(a) of the Exchange Act (15 U.S.C. 78o-3(a))."
examples:
  - "The National Association of Securities Dealers Automatic Quotation (Nasdaq), Nasdaq SmallCap Market, and the Over-The-Counter Bulletin Board (OTCBB) exchange platforms are integrated into one IQS. By using this integrated system, investors have access to a wide range of securities, ranging from large blue-chip companies to smaller micro-caps."
synonyms:
  - "IQS"
  - "inter-dealer quotation system"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-IDQS.md", provenance: fibo}
---

automated system for organizing and disseminating price quotes by brokers and dealer firms that facilitates electronic trading in securities

### Relationships
- is-a: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
- is-classified-by: [MarketCategoryClassifier-IDQS](/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-IDQS.md)
