from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция, принимающая информацию о карте или счете"""
    parts = data.rsplit(" ", 1)
    if len(parts) != 2:
        return data

    first_part, number_part = parts
    # Проверяем, является ли это счётом:
    if "счет" in first_part.lower():  # исправлено
        masked_number = get_mask_account(number_part)
        return f"{first_part} {masked_number}"
    else:
        # Иначе считаем, что это карта
        masked_number = get_mask_card_number(number_part)
        return f"{first_part} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Принимает дату в ISO-формате (например, "2024-03-11T02:26:18.671407")
    и возвращает дату в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
