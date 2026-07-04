---
type: FIBO Class
title: "packaged financial product"
description: "financial product that acts as a container for at least one financial instrument, including other financial products, and whose value is derived from, or based on a reference asset, market measure, or investment strategy"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PackagedFinancialProduct
tags: [FBC, Release]
detail: "Certain properties of the instruments, such as their term, interest rate, eligibility of the client, etc., may be set as a part of the product specification. Some of these are intrinsic but variable properties of the instrument, for example the exact interest rate, whereas others are extrinsic, such as client eligibility. Product offerings have prices, which may build in various fees, that are components of the cost of carry on a trader's books. Reference assets and market measures may include single equity or debt securities, indexes, commodities, interest rates and/or foreign currencies, as well as baskets of these reference assets or market measures. Like other well-known market instruments such as convertible bonds, many structured products are hybrid securities. Structured products typically have two components - a debt instrument and a derivative, which is often an option. The debt instrument, in some instances, may pay interest at a specified rate and interval. The derivative component establishes payment at maturity, which may give the issuer the right to buy from you, or sell you, the referenced security or securities at a predetermined price. For example, structured products may combine characteristics of debt and equity or of debt and commodities. SEC Rule 434 defines structured securities as 'securities whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows'."
synonyms:
  - "market-linked investment"
  - "structured product"
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog.md", provenance: fibo}
---

financial product that acts as a container for at least one financial instrument, including other financial products, and whose value is derived from, or based on a reference asset, market measure, or investment strategy

### Relationships
- is-a: [FinancialProduct](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- is-a: [ContractualProduct](/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md)
- is-included-in: [FinancialProductCatalog](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog.md)
