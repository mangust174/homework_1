""" фильтрация и сортировка по состоянию и дате """

from datetime import datetime
from typing import List, Dict

def filter_by_state(items: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """ вернуть новый список операций """
    return [item for item in items if item.get("state") == state]