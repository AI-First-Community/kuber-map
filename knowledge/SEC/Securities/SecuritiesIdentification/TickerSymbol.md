---
type: FIBO Class
title: "ticker symbol"
description: "reassignable identifier of relatively short character string length that is unique within an exchange for a particular financial instrument or listing for that instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/TickerSymbol
tags: [SEC, Release]
detail: "Every listed security has at least one unique ticker symbol, facilitating the vast array of trade orders that flow through the financial markets every day. However, in some countries this relationship may be indirect, through the listing, rather than direct, as is the case in the United States. In the US, the relationship between a ticker symbol and the listed security is one-to-one. This is not, however, the case in Singapore, where there may be unique ticker symbols for the same security based on the lot size. Some well-known ticker symbols are commonly used by multiple exchanges for the same instrument, such as 'IBM', though exchanges attempt to coordinate to limit duplication. Ticker symbols are reusable, assigned to a given instrument by an exchange for some period of time."
relations:
  - {type: is-a, target: "/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier.md", provenance: fibo}
---

reassignable identifier of relatively short character string length that is unique within an exchange for a particular financial instrument or listing for that instrument

### Relationships
- is-a: [ReassignableIdentifier](/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier.md)
