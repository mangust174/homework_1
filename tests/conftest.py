import pytest


@pytest.fixture(scope="module")
""" карточные номера """
def valid_card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]


@pytest.fixture(scope="module")
""" неверные номера """
def invalid_card_number():
    return ["123456789012345", "abcdef"]


@pytest.fixture(scope="module")
""" номера счетов """
def valid_accounts():
    return [
        ("1234567890", "**90"),
        ("9876543210", "**10"),
        ("111122223333", "**33"),
    ]


@pytest.fixture(scope="module")
""" неверные счета """
def invalid_accounts():
    return ["abcde", "123"]


@pytest.fixture(scope="module")
""" тест даты """
def date_data():
    return {
        "valid": ("2024-03-11T02:26:18.671407", "11.03.2024"), # дата
        "invalid": ("not-a-date", None), # неверная дата
    }
