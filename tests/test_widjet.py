import pytest
from src.widjet import mask_account_card, get_date


@pytest.mark.parametrize(
    "line,expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234567812345678",    "MasterCard 1234 56** **** 5678"),
        ("Счет 40817810099910004312",      "Счет **4312"),
        ("сЧеТ 1234",                      "сЧеТ **1234"),
        ("Something‑Else",                 "Something‑Else"),
    ],
)
def test_mask_account_card(line, expected):
    assert mask_account_card(line) == expected


@pytest.mark.parametrize(
    "iso,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59",        "31.12.1999"),
        ("2025-05-02",                 "02.05.2025"),
    ],
)
def test_get_date(iso, expected):
    assert get_date(iso) == expected