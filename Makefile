PY := ./.venv/bin/python
PIP := ./.venv/bin/pip
DOMAINS ?= FND LOAN

.PHONY: setup extract build validate test lint attribution check all clean

setup:
	python3 -m venv .venv
	$(PIP) install -q --disable-pip-version-check -e ".[dev]"
	@echo "setup complete"

extract:
	$(PY) etl/extract.py --domains $(DOMAINS) --out out/intermediate.json

build:
	$(PY) etl/to_okf.py --in out/intermediate.json --clusters $(DOMAINS) --bundle knowledge

validate:
	$(PY) etl/validate.py --bundle knowledge

test:
	$(PY) -m pytest

lint:
	$(PY) -m ruff check etl tests scripts

attribution:
	$(PY) scripts/check_no_attribution.py

check: lint test validate attribution
	@echo "quality gate: PASS"

all: extract build validate

clean:
	rm -rf out knowledge/FND knowledge/LOAN knowledge/CMNS knowledge/LCC __pycache__ etl/__pycache__
