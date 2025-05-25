from typing import Dict

# Курсы на 25.05.2025
RATES: Dict[str, float] = {
    'USD': 79.753,   # 1 USD = 79.753 RUB
    'EUR': 91.299,  # 1 EUR = 91.299 RUB
    'RUB': 1.0      # 1 RUB = 1 RUB
}

def convert(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Конвертация валюты.
    :param amount: сумма
    :param from_currency: исходная валюта (USD/EUR/RUB)
    :param to_currency: целевая валюта (USD/EUR/RUB)
    :return: сумма в целевой валюте
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in RATES or to_currency not in RATES:
        raise ValueError("Валюта не поддерживается.")
    rub_amount = amount * RATES[from_currency]
    return rub_amount / RATES[to_currency]

def main():
    """
    Главная точка входа модуля.
    Просто выводит подсказку, что нужно запускать cli.py.
    """
    print("=== Currency Converter Module ===")
    print("Используйте cli.py для интерактивного запуска.")

if __name__ == "__main__":
    main()
