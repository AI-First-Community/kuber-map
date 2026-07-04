PY := ./.venv/bin/python
PIP := ./.venv/bin/pip
DOMAINS ?= FND LOAN FBC BE SEC DER IND MD BP CAE
CLUSTERS ?= $(DOMAINS) CMNS   # domains emitted in the bundle (+ Commons upper ontology)

.PHONY: setup fibo commons extract build curate pack contrib eval map validate test lint attribution check all clean

setup:
	python3 -m venv .venv
	$(PIP) install -q --disable-pip-version-check -e ".[dev]"
	@echo "setup complete"

fibo:
	./scripts/fetch_fibo.sh

commons:
	./scripts/fetch_commons.sh

extract:
	$(PY) etl/extract.py --domains $(DOMAINS) --out out/intermediate.json

build:
	$(PY) etl/to_okf.py --in out/intermediate.json --clusters $(CLUSTERS) --bundle knowledge

# Regenerate the curated layer (grounded in out/intermediate.json), then rebuild the bundle
# so core: flags and bridges land in the OKF files. Run `make extract` (or `make all`) first.
# Each use case = a spec under curation/usecases/.
curate:
	$(PY) etl/nominate_core.py --in out/intermediate.json --out curation/loan-origination.json
	$(PY) etl/nominate_core.py --in out/intermediate.json --spec curation/usecases/kyc.json --out curation/kyc.json
	$(PY) etl/nominate_core.py --in out/intermediate.json --spec curation/usecases/securities.json --out curation/securities.json
	$(PY) etl/nominate_core.py --in out/intermediate.json --spec curation/usecases/regulatory-reporting.json --out curation/regulatory-reporting.json
	$(PY) etl/bridges.py --in out/intermediate.json --bundle knowledge
	$(PY) etl/bridges.py --in out/intermediate.json --bundle knowledge --spec curation/usecases/kyc-bridges.json --out curation/kyc-bridges.json
	$(PY) etl/bridges.py --in out/intermediate.json --bundle knowledge --spec curation/usecases/securities-bridges.json --out curation/securities-bridges.json
	$(PY) etl/bridges.py --in out/intermediate.json --bundle knowledge --spec curation/usecases/regulatory-reporting-bridges.json --out curation/regulatory-reporting-bridges.json
	$(MAKE) build

pack:
	$(PY) etl/export_pack.py --use-case loan-origination
	$(PY) etl/export_pack.py --use-case kyc --core curation/kyc.json --bridges curation/kyc-bridges.json --out export/kyc
	$(PY) etl/export_pack.py --use-case securities --core curation/securities.json --bridges curation/securities-bridges.json --out export/securities
	$(PY) etl/export_pack.py --use-case regulatory-reporting --core curation/regulatory-reporting.json --bridges curation/regulatory-reporting-bridges.json --defs curation/regulatory-reporting-definitions.json --out export/regulatory-reporting

# Package the 15 curated cross-domain bridges as an EDM Council contribution proposal.
contrib:
	$(PY) etl/export_bridges.py

eval:
	$(PY) eval/harness.py --adapter offline

# knowledge/ OKF bundle + okf.config.js -> js/data.js for the Cytoscape map (needs node).
map:
	node scripts/okf.js build

validate:
	$(PY) etl/validate.py --bundle knowledge

test:
	$(PY) -m pytest

lint:
	$(PY) -m ruff check etl eval tests scripts

attribution:
	$(PY) scripts/check_no_attribution.py

check: lint test validate attribution
	@echo "quality gate: PASS"

all: extract build validate

clean:
	rm -rf out $(addprefix knowledge/,$(CLUSTERS)) knowledge/LCC __pycache__ etl/__pycache__
