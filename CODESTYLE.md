
## Стандарты кодирования для проекта Currency Converter

1. Следовать PEP8.
2. Длина строки — не более 88 символов.
3. Отступы — 4 пробела.
4. Имена переменных и функций — snake_case.
5. Имена классов — CamelCase.
6. Типизация для всех функций.
7. Каждая функция и модуль — с docstring.
8. Импорт стандартных библиотек — выше сторонних.
9. Исключения — через try/except.
10. Код с примером:

```python
def convert(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Конвертация валюты.
    """
    pass
