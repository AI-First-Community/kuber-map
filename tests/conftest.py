import os
import sys

# Make the etl/ and eval/ modules importable in tests without packaging.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "etl"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "eval"))

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
