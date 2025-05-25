from currency_converter import convert

def run_converter():
    """Запустить цикл конвертации."""
    print("\n=== Конвертация валюты ===")
    while True:
        user_input = input("Введите сумму (или 'back' для меню): ").strip().lower()
        if user_input in ('back',):
            return

        try:
            amount = float(user_input)
        except ValueError:
            print("Неверный ввод. Введите число или 'back' для возврата в меню.")
            continue

        src = input("Из (USD/EUR/RUB): ").strip().upper()
        dst = input("В (USD/EUR/RUB): ").strip().upper()

        try:
            result = convert(amount, src, dst)
            print(f"Результат: {result:.2f} {dst}\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

def main():
    """Главное меню CLI."""
    while True:
        print("\n=== Currency Converter CLI ===")
        print("1. Конвертировать валюту")
        print("2. Завершить работу")
        choice = input("Выберите пункт (1–2): ").strip()

        if choice == '1':
            run_converter()
        elif choice == '2':
            print("Выход из программы. До встречи!")
            break
        else:
            print("Неверный выбор. Введите 1 или 2.")

if __name__ == "__main__":
    main()