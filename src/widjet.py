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





