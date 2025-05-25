# Проект Currency Converter

## Описание

Простой сервис для конвертации валют с двумя интерфейсами:

* **currency\_converter.py** — модуль с функцией `convert`
* **cli.py** — консольный интерфейс на основе `currency_converter`

Проект реализован в рамках практической работы №3 по методике GitFlow. Все изменения оформлены через GitHub Issues и Pull Requests.

## Структура репозитория

* `master` — основная ветка с готовыми релизами
* `develop` — ветка разработки
* `feature/linter-setup` — задача по настройке код-стандарта и линтера
* `feature/3-cli-interface` — задача по реализации CLI-интерфейса
* `release/v0.3` — релизная ветка
* **Теги:** `v0.1`, `v0.2`, `v0.3`

## Реализация задач (Issues)

### Issue #1: Разработка стандарта кодирования

* **Описание:** Добавлен `.editorconfig` и `CODESTYLE.md` с правилами кодирования.
* **Ветка:** `feature/linter-setup`
* **Коммиты:**

  * `Добавлен .editorconfig и CODESTYLE.md, closes #1`
* **Pull Request:** #1 → `feature/linter-setup` → `develop`
* **Ревью:** самопроверка (Approve)
* **Merge:** через GitHub PR, Issue закрылся при merge.

### Issue #2: Настройка статического анализатора и pre-commit hook

* **Описание:** Настроен `pylint` (`.pylintrc`) и создан pre-commit hook для проверки `currency_converter.py`.
* **Ветка:** `feature/linter-setup`
* **Коммиты:**

  * `Добавлены .pylintrc и currency_converter.py для настройки линтера, closes #2`
  * `Доработан currency_converter.py согласно замечаниям линтера, closes #2`
* **Pull Request:** #2 → `feature/linter-setup` → `develop`
* **Ревью:** самопроверка (Approve)
* **Merge:** через GitHub PR, Issue закрылся при merge.

### Issue #3: Реализовать CLI-интерфейс для конвертера

* **Описание:** Добавлен файл `cli.py` с консольным интерфейсом.
* **Ветка:** `feature/3-cli-interface`
* **Коммит:**

  * `feat: добавлен CLI-интерфейс для конвертера, closes #3`
* **Pull Request:** #3 → `feature/3-cli-interface` → `develop`
* **Ревью:** самопроверка (Approve)
* **Merge:** через GitHub PR, Issue закрылся при merge.

## Релиз (GitFlow)

1. Создана ветка `release/v0.3` от `develop`
2. Смержена в `master` с флагом `--no-ff` (`Merge release v0.3 into master`)
3. Создан аннотированный тег `v0.3`
4. Ветки `release/v0.3` удалена, изменения обратно влиты в `develop`

## Инструкции по запуску

1. **Клонировать репозиторий**

   ```bash
   git clone https://github.com/panda1basic/pr3_gitflow.git
   cd pr3_gitflow
   ```
2. **Запустить Python-скрипт**

   ```bash
   python currency_converter.py
   ```
3. **Запустить CLI**

   ```bash
   python cli.py
   ```

## Пример работы CLI

```
=== Currency Converter CLI ===
Сумма: 100
Из (USD/EUR/RUB): USD
В (USD/EUR/RUB): EUR
Результат: 92.86 EUR
```

## Контрольные вопросы

1. **Зачем нужен `.editorconfig`?**

   * Для унификации настроек редактора (отступы, кодировка, длина строки).
2. **Какие инструменты статического анализа использовались?**

   * `pylint`.
3. **Какие инструменты динамического анализа?**

   * Встроенная проверка ввода пользователем, обработка исключений.
4. **Какие практики код-ревью применялись?**

   * Pull Requests, self-approve, комментарии по качеству кода.

## Выводы

В рамках практики освоен процесс работы по GitFlow: создание веток, Pull Request, code review, release-ветка и тегирование. Настроены стандарты кодирования и статический анализ.

---

