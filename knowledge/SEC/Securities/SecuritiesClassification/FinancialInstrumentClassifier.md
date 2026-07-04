---
type: FIBO Class
title: "financial instrument classifier"
description: "classifier for a financial instrument based on its type and features"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
tags: [SEC, Release]
examples:
  - "Examples include equity instrument, debt instrument, option, future, etc. per the the ISO 10962 CFI (Classification of Financial Instruments) standard, as cash instruments or derivative instruments per the Financial Accounting Standards Board (FASB) and International Accounting Standards Board (IASB) accounting standards, and so forth."
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md", provenance: fibo}
---

classifier for a financial instrument based on its type and features

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- is-defined-in: [FinancialInstrumentClassificationScheme](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md)
