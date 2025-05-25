from currency_converter import convert

def main():
    """Запуск CLI."""
    print("=== Currency Converter CLI ===")
    try:
        amount = float(input("Сумма: "))
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля.")
    except ValueError as e:
        print("Ошибка ввода:", e)
        return

    src = input("Из (USD/EUR/RUB): ").upper()
    dst = input("В (USD/EUR/RUB): ").upper()
    try:
        result = convert(amount, src, dst)
        print(f"Результат: {result:.2f} {dst}")
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
