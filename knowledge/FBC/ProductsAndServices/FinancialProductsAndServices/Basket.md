---
type: FIBO Class
title: "basket"
description: "collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
tags: [FBC, Release]
detail: "A basket may be associated with a specific market sector, and may be delineated for the purposes of statistical analysis, such as for calculating CPI. According to the US Bureau of Labor Statistics (BLS), with respect to the CPI, a market basket is a package of goods and services that consumers purchase for day-to-day living. The weight of each item is based on the amount of expenditure reported by a sample of households. From a securities perspective, a basket is a collection of products or securities that are designated to mimic the performance of a market. For investors, the market basket is the principal idea behind index funds, which are essentially a broad sample of stocks, bonds or other securities in the market; this provides investors with a benchmark against which to compare their investment returns."
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: has-member, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent.md", provenance: fibo}
  - {type: has-selecting-party, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- has-member: [BasketConstituent](/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent.md)
- has-selecting-party: [Party](/CMNS/PartiesAndSituations/Party.md)
