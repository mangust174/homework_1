from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("data,expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard Gold 1234567890123456", "MasterCard Gold 1234 56** **** 3456"),
    ("Счёт 1234567890", "Счёт **90"),
])
def test_mask_account_card(data, expected):
    """
    Тестирует маску для карточки и счёта пользователя.
    """
    assert mask_account_card(data) == expected


def test_get_date(date_data):
    """
    Проверяет корректность преобразования строки даты.
    Если переданная дата верна, проверяется её правильное преобразование.
    Если неверна, ожидается исключение ValueError.
    """
    if isinstance(date_data["valid"], tuple):
        date_str, expected_result = date_data["valid"]
        result = get_date(date_str)
        assert result == expected_result
    else:
        with pytest.raises(ValueError):
            get_date(date_data["invalid"])