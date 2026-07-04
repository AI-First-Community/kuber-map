---
type: FIBO Class
title: "contract lifecycle"
description: "lifecycle of an agreement, including, but not limited to a credit agreement, financial instrument, or other formal contract, from initial stages through retirement"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycle
tags: [FBC, Release]
detail: "Certain business agreements, such as partnership agreements,may involve planning, drafting/review/revision, execution and management, renewal, and possibly sunsetting phases. Financial contracts, such as loans and other instruments have specific stages and events during the execution and management phase, i.e. from the effective date of the contract through maturity and redemption."
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/Lifecycle.md", provenance: fibo}
  - {type: defines, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md", provenance: fibo}
  - {type: has-stage, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md", provenance: fibo}
  - {type: is-lifecycle-of, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
---

lifecycle of an agreement, including, but not limited to a credit agreement, financial instrument, or other formal contract, from initial stages through retirement

### Relationships
- is-a: [Lifecycle](/FND/Arrangements/Lifecycles/Lifecycle.md)
- defines: [ContractLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)
- has-stage: [ContractLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)
- is-lifecycle-of: [Contract](/FND/Agreements/Contracts/Contract.md)
