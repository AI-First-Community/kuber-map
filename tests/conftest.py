import os
import sys

# Make the etl/ modules importable in tests without packaging.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "etl"))

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
