"""фильтрация и сортировка по состоянию и дате"""

from datetime import datetime
from typing import Dict, List


def filter_by_state(items: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """вернуть новый список операций"""
    return [item for item in items if item.get("state") == state]


def sort_by_date(items: List[Dict], revers: bool = True) -> List[Dict]:
    """возвращаем новый список по ключу 'date'"""

    def _key(item: Dict):
        raw = item.get("date")
        if raw is None:
            return datetime.min
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return datetime.min

    return sorted(items, key=_key, reverse=reverse)