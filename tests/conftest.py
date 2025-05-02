import pytest
from datetime import datetime, timedelta

@pytest.fixture(scope="module")
def sample_operations():
    base = datetime(2025, 5, 1)
    to_iso = lambda dt: dt.isoformat()

    return [
        {"state": "EXECUTED",  "date": to_iso(base - timedelta(days=2))},
        {"state": "CANCELED",  "date": to_iso(base - timedelta(days=1))},
        {"state": "PENDING",   "date": to_iso(base)},
        {"state": "EXECUTED",  "date": to_iso(base + timedelta(days=1))},
    ]