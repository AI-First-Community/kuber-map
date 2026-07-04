---
type: FIBO Class
title: "credit card asset-backed security"
description: "asset-backed security based on credit card receivables"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAssetBackedSecurity
tags: [SEC, Release]
detail: "Credit card securitizations currently represent the primary funding vehicle for unsecured revolving consumer credit. Similar to mortgage and other asset securitizations, the financial institution that originates the credit card receivables sells a group of these receivables to a trust. The trust then creates and sells certificates backed by the credit card receivables to investors, which are predominately institutional investors. Very few credit card ABS are marketed to retail customers, primarily due to the complex nature of the transactions and the need to continually monitor various performance indices on the underlying receivables. The underlying credit card receivables generate income to support the interest payments on the certificates."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool.md", provenance: fibo}
---

asset-backed security based on credit card receivables

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- is-based-on: [CreditCardAccountPool](/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool.md)
