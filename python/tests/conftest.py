import os, sys
# Ensure parent folder (python/) is visible to pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
