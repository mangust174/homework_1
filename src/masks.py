def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты (строка) и возвращает её маску"""
    # Здесь сразу считаем, что минимум 16 символов
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(number_account: str) -> str:
    """Функция принимает номер счёта (строка) и возвращает её маску"""
    # Показываем последние 4 символа, перед ними ставим две звездочки
    return f"**{number_account[-4:]}"

# --- Основная часть ---

card_number = input("введите номер карты: ")            # строка
number_account = input("введите номер счета: ")         # строка

print(get_mask_card_number(card_number))
print(get_mask_account(number_account))