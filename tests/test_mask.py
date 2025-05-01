from src.masks import get_mask_card_number, get_mask_account

from datetime import datetime

import pytest


@pytest.mark.parametrize("card_number,expected", valid_card_numbers())
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number,expected", valid_accounts())
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

def test_get_date(date_data):
    if isinstance(date_data["valid"], tuple):
        date_str, expected_result = date_data["valid"]
        result = get_date(date_str)
        assert result == expected_result
    else:
        with pytest.raises(ValueError):
            get_date(date_data["invalid"])