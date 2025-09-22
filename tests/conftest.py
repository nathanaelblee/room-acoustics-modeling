# filename: conftest.py
# author: Nate Lee
# description: Ensure project root is on sys.path so tests can import from src/.

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # .../room-acoustics-modeling
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))