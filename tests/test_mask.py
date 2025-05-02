import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("8765432187654321876", "8765 43** **** 1876"),
    ],
)
def test_get_mask_card_number(raw, expected):
    assert get_mask_card_number(raw) == expected


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("40817810099910004312", "**4312"),
        ("1234", "**1234"),
        ("7", "**7"),
    ],
)
def test_get_mask_account(raw, expected):
    assert get_mask_account(raw) == expected
