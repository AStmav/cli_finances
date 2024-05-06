import argparse
import json
from datetime import datetime
from typing import Any, Dict, List, Optional

class Record:
    """Класс для хранения записей о финансах."""

    def __init__(self, date: str, category: str, amount: float, description: str) -> None:
        """Инициализация объекта Record."""
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

class FileManager:
    """Класс для управления файлами."""

    @staticmethod
    def create_file_if_not_exists(file_name: str) -> None:
        """Создает файл, если он не существует."""
        try:
            with open(file_name, 'x') as f:
                json.dump([], f)  # Используем пустой список для инициализации файла
        except FileExistsError:
            pass  # Файл уже существует

    @staticmethod
    def load_records(file_name: str) -> List[Dict[str, Any]]:
        """Загружает записи из файла."""
        FileManager.create_file_if_not_exists(file_name)
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_records(file_name: str, records: List[Dict[str, Any]]) -> None:
        """Сохраняет записи в файл."""
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False)

class Finances:
    """Класс для управления финансами."""

    def __init__(self, file_name: str) -> None:
        """Инициализация объекта Finances."""
        self.file_name = file_name
        self.records = FileManager.load_records(file_name)

    def add_record(self, date: str, category: str, amount: float, description: str) -> None:
        """Добавление новой записи."""
        record = Record(date, category, amount, description)
        self.records.append(record.__dict__)  # Добавляем новую запись в список как словарь
        FileManager.save_records(self.file_name, self.records)

    def edit_record(self, index: int, date: str, category: str, amount: float, description: str) -> bool:
        """Редактирование существующей записи."""
        if 0 <= index < len(self.records):
            self.records[index] = Record(date, category, amount, description).__dict__
            FileManager.save_records(self.file_name, self.records)
            return True
        return False

    def show_balance(self) -> None:
        """Вывод баланса."""
        income = sum(record['amount'] for record in self.records if record['category'] == 'доход')
        expenses = sum(record['amount'] for record in self.records if record['category'] == 'расход')
        balance = income - expenses
        print(f"Доход: {income} руб.")
        print(f"Расход: {expenses} руб.")
        print(f"Баланс: {balance} руб.")

    def search_records(self, category: Optional[str] = None, date: Optional[str] = None, amount: Optional[float] = None) -> None:
        """Поиск записей по категории, дате или сумме."""
        results = []
        for record in self.records:
            if (category is None or record['category'] == category) and \
               (date is None or record['date'] == date) and \
               (amount is None or record['amount'] == amount):
                results.append(record)
        if results:
            print("Найденные записи:")
            for result in results:
                print(result)
        else:
            print("Записи не найдены.")

def main() -> None:
    finances = Finances("finances.json")

    parser = argparse.ArgumentParser(description="Личный финансовый кошелек")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Добавить новую запись')
    add_parser.add_argument('--date', required=True, help='Дата (YYYY-MM-DD)')
    add_parser.add_argument('--category', choices=['доход', 'расход'], required=True, help='категория')
    add_parser.add_argument('--amount', type=float, required=True, help='Сумма')
    add_parser.add_argument('--description', required=True, help='Описание')
    add_parser.set_defaults(func=lambda args: finances.add_record(args.date, args.category, args.amount, args.description))

    edit_parser = subparsers.add_parser('edit', help='Редактировать существующую запись')
    edit_parser.add_argument('--index', type=int, required=True, help='Индекс записи для редактирования')
    edit_parser.add_argument('--date', required=True, help='Дата записи (YYYY-MM-DD)')
    edit_parser.add_argument('--category', choices=['доход', 'расход'], required=True, help='Категория записи')
    edit_parser.add_argument('--amount', type=float, required=True, help='Сумма записи')
    edit_parser.add_argument('--description', required=True, help='Описание записи')
    edit_parser.set_defaults(func=lambda args: finances.edit_record(args.index, args.date, args.category, args.amount, args.description))

    balance_parser = subparsers.add_parser('balance', help='Отобразить текущий баланс')
    balance_parser.set_defaults(func=lambda args: finances.show_balance())

    search_parser = subparsers.add_parser('search', help='Поиск записей по категории, дате или сумме')
    search_parser.add_argument('--category', help='Категория для поиска')
    search_parser.add_argument('--date', help='Дата для поиска (YYYY-MM-DD)')
    search_parser.add_argument('--amount', type=float, help='Сумма для поиска')
    search_parser.set_defaults(func=lambda args: finances.search_records(args.category, args.date, args.amount))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
