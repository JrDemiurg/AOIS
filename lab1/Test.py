import unittest
from binary_numbers import *


class MyTestCase(unittest.TestCase):
    def test_to_the_direct_code(self):
        self.assertEqual(to_the_direct_code(0), '0000000000000000')
        self.assertEqual(to_the_direct_code(10), '0000000000001010')
        self.assertEqual(to_the_direct_code(-10), '1000000000001010')
        self.assertEqual(to_the_direct_code(99), '0000000001100011')
        self.assertEqual(to_the_direct_code(-99), '1000000001100011')

    def test_to_the_reverse_code(self):
        self.assertEqual(to_the_reverse_code(0), '0000000000000000')
        self.assertEqual(to_the_reverse_code(10), '0000000000001010')
        self.assertEqual(to_the_reverse_code(-10), '1111111111110101')
        self.assertEqual(to_the_reverse_code(99), '0000000001100011')
        self.assertEqual(to_the_reverse_code(-99), '1111111110011100')

    def test_to_the_additional_code(self):
        self.assertEqual(to_the_additional_code(0), '0000000000000000')
        self.assertEqual(to_the_additional_code(10), '0000000000001010')
        self.assertEqual(to_the_additional_code(-10), '1111111111110110')
        self.assertEqual(to_the_additional_code(99), '0000000001100011')
        self.assertEqual(to_the_additional_code(-99), '1111111110011101')

    def test_direct_code_to_int(self):
        self.assertEqual(0, direct_code_to_int('0000000000000000'))
        self.assertEqual(10, direct_code_to_int('0000000000001010'))
        self.assertEqual(-10, direct_code_to_int('1000000000001010'))
        self.assertEqual(99, direct_code_to_int('0000000001100011'))
        self.assertEqual(-99, direct_code_to_int('1000000001100011'))

    def test_additional_code_to_int(self):
        self.assertEqual(0, additional_code_to_int('0000000000000000'))
        self.assertEqual(10, additional_code_to_int('0000000000001010'))
        self.assertEqual(-10, additional_code_to_int('1111111111110110'))
        self.assertEqual(99, additional_code_to_int('0000000001100011'))
        self.assertEqual(-99, additional_code_to_int('1111111110011101'))

    def test_sum_of_additional_code(self):
        self.assertEqual(0, sum_of_additional_code(-10, 10))
        self.assertEqual(129, sum_of_additional_code(0, 129))
        self.assertEqual(-5, sum_of_additional_code(16, -21))
        self.assertEqual(133, sum_of_additional_code(33, 100))
        self.assertEqual(128, sum_of_additional_code(64, 64))

    def test_subtracting(self):
        self.assertEqual(-20, subtracting(-10, 10))
        self.assertEqual(-129, subtracting(0, 129))
        self.assertEqual(37, subtracting(16, -21))
        self.assertEqual(-67, subtracting(33, 100))
        self.assertEqual(0, subtracting(64, 64))

    def test_multiplication(self):
        self.assertEqual(-100, multiplication(-10, 10))
        self.assertEqual(0, multiplication(0, 129))
        self.assertEqual(-336, multiplication(16, -21))
        self.assertEqual(3300, multiplication(33, 100))
        self.assertEqual(4096, multiplication(64, 64))

    def test_division(self):
        self.assertEqual(-1, division(-10, 10))
        self.assertEqual(0, division(0, 129))
        self.assertTrue(-0.7 > division(16, -21) > -0.8)
        self.assertTrue(0.3 < division(33, 100) < 0.34)
        self.assertEqual(1, division(64, 64))

    def test_sum_of_binary_float(self):
        self.assertEqual('01000001011010100000000000000000', sum_of_binary_float(12.5, 2.125))
        self.assertEqual('01000000010100000000000000000000', sum_of_binary_float(0, 3.25))
        self.assertEqual('01000001010011100000000000000000', sum_of_binary_float(0.625, 12.25))
        self.assertEqual('00111111001000000000000000000000', sum_of_binary_float(0.125, 0.5))
        self.assertEqual('01000001001001100000000000000000', sum_of_binary_float(0.375, 10))


if __name__ == '__main__':
    unittest.main()
