from src.masks import get_mask_card_number, get_mask_account

from datetime import datetime

import pytest


@pytest.fixture(scope="module")
def valid_cards():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("0000000000000000", "0000 00** **** 0000"),  # минимально возможный номер
        ("9999999999999999", "9999 99** **** 9999")  # максимально возможный номер
    ]

@pytest.fixture(scope="module")
def invalid_cards():
    return [
        "",                      # пустая строка
        "12345678901234",       # слишком короткая
        "12345678901234567",    # слишком длинная
        "abcde",                 # буквенный номер
        "123456789012abcc",     # смешанный номер
        None                     # None
    ]

@pytest.fixture(scope="module")
def valid_accounts():
    return [
        ("1234567890", "**90"),
        ("9876543210", "**10"),
        ("111122223333", "**33"),
        ("0000000000", "**00"),  # минимальный счёт
        ("9999999999", "**99")   # максимальный счёт
    ]

@pytest.fixture(scope="module")
def invalid_accounts():
    return [
        "",
        "123",
        "12345678901234567890",  # слишком длинный счёт
        "abcde",                  # буквенный счёт
        None                      # None
    ]

# ТЕСТЫ ДЛЯ КАРТ
@pytest.mark.parametrize("card_number,expected", valid_cards)
def test_get_mask_card_number_valid_cases(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number,expected", valid_accounts)
def test_get_mask_account_valid_cases(account_number, expected):
    assert get_mask_account(account_number) == expected

# ТЕСТЫ НА ОШИБКИ ДЛЯ НОМЕРОВ КАРТ
@pytest.mark.parametrize("invalid_card", invalid_cards)
def test_get_mask_card_number_invalid_cases(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)

# ТЕСТЫ НА ОШИБКИ ДЛЯ АККАУНТОВ
@pytest.mark.parametrize("invalid_account", invalid_accounts)
def test_get_mask_account_invalid_cases(invalid_account):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)