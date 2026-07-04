---
type: FIBO Class
title: "regulated commodity"
description: "commodity under the jurisdiction of the regulatory agency, such as the Commodities Futures Trading Commission (CFTF) in the United States, which includes any commodity traded in an organized contracts market"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegulatedCommodity
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Commodity.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-regulated-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
---

commodity under the jurisdiction of the regulatory agency, such as the Commodities Futures Trading Commission (CFTF) in the United States, which includes any commodity traded in an organized contracts market

### Relationships
- is-a: [Commodity](/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-regulated-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
