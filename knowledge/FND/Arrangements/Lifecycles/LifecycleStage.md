---
type: FIBO Class
title: "lifecycle stage"
description: "phase in a lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
tags: [FND, Release]
examples:
  - "a research and development phase of a product lifecycle, the introduction phase in a marketing lifecycle, a growth stage in an economic lifecycle, or the origination phase in the lifecycle of a loan"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: comprises, target: "/FND/Arrangements/Lifecycles/LifecycleEvent.md", provenance: fibo}
  - {type: is-defined-in, target: "/FND/Arrangements/Lifecycles/Lifecycle.md", provenance: fibo}
  - {type: is-stage-of, target: "/FND/Arrangements/Lifecycles/Lifecycle.md", provenance: fibo}
---

phase in a lifecycle

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- comprises: [LifecycleEvent](/FND/Arrangements/Lifecycles/LifecycleEvent.md)
- is-defined-in: [Lifecycle](/FND/Arrangements/Lifecycles/Lifecycle.md)
- is-stage-of: [Lifecycle](/FND/Arrangements/Lifecycles/Lifecycle.md)
