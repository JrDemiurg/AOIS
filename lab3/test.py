import unittest
from minimization import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        expression = "(!a&b&c)|(a&!b&!c)|(a&!b&c)|(a&b&!c)|(a&b&c)"
        self.assertEqual(calculation_method_sdnf(expression), "(b&c)|(a)")
        self.assertEqual(table(expression), "(b&c)|(a)")
        self.assertEqual(karno_map(expression), "(b&c)|(a)")

    def test_2(self):
        expression = "(!a&!b&!c&d)|(!a&!b&c&d)|(!a&b&!c&d)|(!a&b&c&d)|(a&b&c&!d)|(a&b&c&d)|"
        self.assertEqual(calculation_method_sdnf(expression), '(a&b&c)|(!a&d)')
        self.assertEqual(table(expression), '(!a&d)|(a&b&c)')
        self.assertEqual(karno_map(expression), '(a&b&c)|(!a&d)')

    def test_3(self):
        expression = "(!a&!b&!c&d)|(!a&!b&c&d)|(!a&b&!c&!d)|(!a&b&!c&d)|(!a&b&c&!d)|(!a&b&c&d)|(a&!b&!c&!d)|(a&!b&!c&d)|(a&!b&c&!d)|(a&!b&c&d)|(a&b&!c&!d)|(a&b&!c&d)|(a&b&c&!d)|(a&b&c&d)"
        self.assertEqual(calculation_method_sdnf(expression), '(d)|(b)|(a)')
        self.assertEqual(table(expression), '(d)|(b)|(a)')
        self.assertEqual(karno_map(expression), '(d)|(b)|(a)')

    def test_4(self):
        expression = "(!a|b|c)&(a|!b|!c)&(a|!b|c)&(a|b|!c)&(a|b|c)"
        self.assertEqual(calculation_method_sdnf(expression), '(b&c)|(a)')
        self.assertEqual(table(expression), '(b&c)|(a)')
        self.assertEqual(karno_map(expression), '(b&c)|(a)')

    def test_5(self):
        expression = "(!a|!b|!c|d)&(!a|!b|c|d)&(!a|b|!c|d)&(!a|b|c|d)&(a|b|c|!d)&(a|b|c|d)"
        self.assertEqual(calculation_method_sdnf(expression), '(a&b&c)|(!a&d)')
        self.assertEqual(table(expression), '(!a&d)|(a&b&c)')
        self.assertEqual(karno_map(expression), '(a&b&c)|(!a&d)')


if __name__ == '__main__':
    unittest.main()
