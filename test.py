import unittest
from main import Finances

class TestFinances(unittest.TestCase):
    def setUp(self):
        self.finances = Finances("test_finances.json")
        self.finances.records = [
            {'date': '2024-04-01', 'category': 'доход', 'amount': 5000, 'description': 'Зарплата'},
            {'date': '2024-04-02', 'category': 'расход', 'amount': 1500, 'description': 'Продукты'},
            {'date': '2024-04-03', 'category': 'расход', 'amount': 200, 'description': 'Транспорт'},
        ]

    def test_add_record(self):
        initial_length = len(self.finances.records)
        self.finances.add_record('2024-04-04', 'доход', 3000, 'Продажа акций')
        self.assertEqual(len(self.finances.records), initial_length + 1)

    def test_edit_record(self):
        index = 1
        self.finances.edit_record(index, '2024-04-02', 'расход', 2000, 'Ресторан')
        edited_record = self.finances.records[index]
        self.assertEqual(edited_record['date'], '2024-04-02')
        self.assertEqual(edited_record['category'], 'расход')
        self.assertEqual(edited_record['amount'], 2000)
        self.assertEqual(edited_record['description'], 'Ресторан')

    def test_search_records(self):
        # Поиск по категории
        self.finances.search_records(category='доход')
        # Поиск по дате
        self.finances.search_records(date='2024-04-01')
        # Поиск по сумме
        self.finances.search_records(amount=1500)

if __name__ == '__main__':
    unittest.main()
