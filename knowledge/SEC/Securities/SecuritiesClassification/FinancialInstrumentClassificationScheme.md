---
type: FIBO Class
title: "financial instrument classification scheme"
description: "classification scheme defining a set of classifiers for financial instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme
tags: [SEC, Release]
examples:
  - "the ISO 10962 Classification of Financial Instruments (CFI) classification scheme"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/ClassificationScheme.md", provenance: fibo}
  - {type: defines, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
---

classification scheme defining a set of classifiers for financial instruments

### Relationships
- is-a: [ClassificationScheme](/CMNS/Classifiers/ClassificationScheme.md)
- defines: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
