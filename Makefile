PY := ./.venv/bin/python
PIP := ./.venv/bin/pip
DOMAINS ?= FND LOAN FBC BE

.PHONY: setup fibo extract build curate pack eval validate test lint attribution check all clean

setup:
	python3 -m venv .venv
	$(PIP) install -q --disable-pip-version-check -e ".[dev]"
	@echo "setup complete"

fibo:
	./scripts/fetch_fibo.sh

extract:
	$(PY) etl/extract.py --domains $(DOMAINS) --out out/intermediate.json

build:
	$(PY) etl/to_okf.py --in out/intermediate.json --clusters $(DOMAINS) --bundle knowledge

# Regenerate the curated layer (grounded in out/intermediate.json), then rebuild the bundle
# so core: flags and bridges land in the OKF files. Run `make extract` (or `make all`) first.
curate:
	$(PY) etl/nominate_core.py --in out/intermediate.json --out curation/loan-origination.json
	$(PY) etl/bridges.py --in out/intermediate.json --bundle knowledge
	$(MAKE) build

pack:
	$(PY) etl/export_pack.py --use-case loan-origination

eval:
	$(PY) eval/harness.py --adapter offline

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
	rm -rf out knowledge/FND knowledge/LOAN knowledge/FBC knowledge/BE knowledge/CMNS knowledge/LCC __pycache__ etl/__pycache__
