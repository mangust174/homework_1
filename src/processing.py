from datetime import datetime
from typing import List, Dict

Operation = Dict[str, str]


def filter_by_state(operations: List[Operation], state: str) -> List[Operation]:
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Operation],
    *,
    reverse: bool = False
) -> List[Operation]:
    key_fn = lambda op: datetime.fromisoformat(op["date"])
    return sorted(operations, key=key_fn, reverse=reverse)
