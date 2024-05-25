import unittest
from hash_table import *


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        table = HashTable(100)
        table.insert('яблоко', 10)
        table.insert('ананас', 100)

        self.assertEqual(table.search('яблоко'), 10)
        self.assertEqual(table.search('ананас'), 100)

        table.insert('яблоко', 111)
        self.assertEqual(table.search('яблоко'), 111)

        table.remove('что-то')

        table_2 = HashTable(1)
        table_2.insert('ананас', 100)
        table_2.insert('яблоко', 10)
        table_2.insert('апельсин', 500)

        self.assertEqual(table_2.search('яблоко'), 10)
        self.assertEqual(table_2.search('ананас'), 100)
        self.assertEqual(table_2.search('апельсин'), 500)

        table_2.remove('апельсин')
        table_2.remove('ананас')
        table_2.remove('яблоко')

        self.assertEqual(table_2.search('яблоко'), None)
        self.assertEqual(table_2.search('ананас'), None)
        self.assertEqual(table_2.search('апельсин'), None)


if __name__ == '__main__':
    unittest.main()
