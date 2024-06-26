# Личный финансовый кошелек

Это простое приложение для управления финансами. Оно позволяет добавлять, редактировать и просматривать записи о доходах и расходах.

## Установка

Чтобы запустить, выполните следующие шаги:

1. Склонируйте репозиторий:
```bash
git clone https://github.com/AStmav/cli_finances.git
```

3. Перейдите в каталог проекта:
```bash
cd cli_finances
```


3. Установить зависимости:
```bash
pip install -r requirements.txt
```
## Функционал

- **Добавление записей:** Вы можете добавлять новые записи о доходах и расходах, указывая дату, категорию, сумму и описание.
- **Редактирование записей:** Позволяет изменять существующие записи по их индексу, обновляя дату, категорию, сумму и описание.
- **Отображение текущего баланса:** Показывает общий доход, расход и текущий баланс.
- **Поиск записей:** Позволяет искать записи по категории, дате или сумме.

## Использование

1. **Добавление записи:** `python main.py add --date <дата> --category <категория> --amount <сумма> --description <описание>`
2. **Редактирование записи:** `python main.py edit --index <индекс> --date <дата> --category <категория> --amount <сумма> --description <описание>`
3. **Отображение текущего баланса:** `python main.py balance`
4. **Поиск записей:** `python main.py search --category <категория> --date <дата> --amount <сумма>`

## Примеры

- Добавить запись о доходе: `python main.py add --date 2024-04-15 --category доход --amount 5000 --description Зарплата`
- Редактировать запись: `python main.py edit --index 0 --date 2024-04-15 --category расход --amount 1500 --description Покупка продуктов`
- Отобразить текущий баланс: `python main.py balance`
- Поиск записей по категории: `python main.py search --category доход`
- Поиск записей по дате: `python main.py search --date 2024-04-15`
- Поиск записей по сумме: `python main.py search --amount 1500`


## Тестирование

Чтобы запустить файл test.py для тестирования приложения, следуйте этим шагам:

- Откройте терминал (или командную строку) и перейдите в каталог с вашим проектом. Затем выполните следующую команду:

```bash
python test.py
```
