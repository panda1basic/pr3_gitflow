from typing import Dict

# Краткий набор курсов (можно обновить вручную)
RATES: Dict[str, float] = {
    'USD': 91.0,    # 1 доллар = 91 рубль
    'EUR': 98.0,    # 1 евро = 98 рублей
    'RUB': 1.0      # 1 рубль = 1 рубль :)
}

def convert(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Конвертация валюты.
    :param amount: Сумма
    :param from_currency: Исходная валюта (USD/EUR/RUB)
    :param to_currency: Целевая валюта (USD/EUR/RUB)
    :return: Сумма в целевой валюте
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in RATES or to_currency not in RATES:
        raise ValueError("Валюта не поддерживается.")
    rub_amount = amount * RATES[from_currency]
    return rub_amount / RATES[to_currency]

def main():
    print("=== Currency Converter ===")
    print("Доступные валюты:", ', '.join(RATES.keys()))
    try:
        amount = float(input("Введите сумму: "))
        from_cur = input("Из какой валюты (USD/EUR/RUB): ").strip()
        to_cur = input("В какую валюту (USD/EUR/RUB): ").strip()
        result = convert(amount, from_cur, to_cur)
        print(f"{amount:.2f} {from_cur.upper()} = {result:.2f} {to_cur.upper()}")
    except Exception as ex:
        print("Ошибка:", ex)

if __name__ == "__main__":
    main()
