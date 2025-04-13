from datetime import datetime


def mask_account_card(cart_number: str) -> str:
    """Функция принимает номер карты (строка) и возвращает её маску"""
    """проверяем на случай,если днина номера отличается"""
    if len(cart_namber) != 16:
        """если цифр больше маскируем по такому варианту"""
        return cart_namber[:4] + "****" + cart_namber[-4:]
        """если цифр 16"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """если номер короче"""
    if len(account_number) < 4:
        return "**" + account_number
    return "**" + account_number[-4:]


def mask_account_card(data: str) -> str:
    """функция принимающая информацию о карте или счете"""
    parts = data.split(' ', 1)
    if len(parts) != 2:
        return data

first_part, number_part = parts
    # Проверяем, является ли это счётом:
    if first_part.split().lower().startswith("счет"):
        masked_number = mask_account_number(number_part)
        return f"{first_part} {masked_number}"
    else:
        # Иначе считаем, что это карта
        masked_number = mask_card_number(number_part)
        return f"{first_part} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Принимает дату в ISO-формате (например, "2024-03-11T02:26:18.671407")
    и возвращает дату в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
