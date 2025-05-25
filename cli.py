from currency_converter import convert

def main():
    """Запуск CLI."""
    print("=== Currency Converter CLI ===")
    print("Введите 'exit' или 'q' для выхода.\n")

    while True:
        # Ввод суммы или команды выхода
        user_input = input("Сумма (или exit): ").strip().lower()
        if user_input in ("exit", "q"):
            print("Выход из программы. До встречи!")
            break

        # Проверяем, что введено число
        try:
            amount = float(user_input)
        except ValueError:
            print("Неверный ввод. Введите число или 'exit' для выхода.\n")
            continue

        # Ввод валют
        src = input("Из (USD/EUR/RUB): ").strip().upper()
        dst = input("В (USD/EUR/RUB): ").strip().upper()

        # Выполняем конвертацию
        try:
            result = convert(amount, src, dst)
            print(f"Результат: {result:.2f} {dst}\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

if __name__ == "__main__":
    main()
