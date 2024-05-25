import unittest
from Matrix import *


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()
        self.word2 = "0101110011111111"
        self.word3 = "1101110011111110"
        self.word9 = "0100101001010101"

    def test_get_word(self):
        self.matrix.set_word(9, self.word9)
        self.assertEqual(self.word9, self.matrix.get_word(9))

    def test_get_address(self):
        self.matrix.set_address_column(9, self.word9)
        self.assertEqual(self.word9, self.matrix.get_address_column(9))

    def test_word_apply_logical_operations_to_each_bit(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        result = self.matrix.word_apply_logical_operations_to_each_bit(2, 3, 15, Operations.PIERCE_OPERATION)
        self.assertEqual("0010001100000000", result)

    def test_address_apply_logical_operations_to_each_bit(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(9, self.word9)
        result = self.matrix.address_apply_logical_operations_to_each_bit(2, 9, 15,
                                                                          Operations.IMPLICATION_FIRST_TO_SECOND)
        self.assertEqual("1111111111111111", result)

    def test_replace_s_via_sum_ab(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        self.matrix.set_word(9, self.word9)
        self.matrix.replace_s_via_sum_ab("010")
        result1 = "0101110011110101"
        self.assertIn(result1, self.matrix.get_word(2))

    def test_replace_s_via_sum_ab2(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        self.matrix.set_word(9, self.word9)
        self.matrix.replace_s_via_sum_ab("010")
        result2 = "0100101001000111"
        self.assertIn(result2, self.matrix.get_word(9))

    def test_find_in_range(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        self.matrix.set_word(9, self.word9)
        a = "0100101011010101"
        b = "1101110011111110"
        words_in_range = self.matrix.find_in_range(a, b)
        self.assertIn(self.word2, words_in_range)

    def test_find_in_range2(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        self.matrix.set_word(9, self.word9)
        a = "0100101011010101"
        b = "1101110011111110"
        words_in_range = self.matrix.find_in_range(a, b)
        self.assertIn(self.word3, words_in_range)

    def test_find_in_range3(self):
        self.matrix.set_word(2, self.word2)
        self.matrix.set_word(3, self.word3)
        self.matrix.set_word(9, self.word9)
        a = "0100101011010101"
        b = "1101110011111110"
        words_in_range = self.matrix.find_in_range(a, b)
        self.assertNotIn(self.word9, words_in_range)


if __name__ == '__main__':
    unittest.main()
