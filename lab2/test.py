import unittest
from logical_function import *


class MyTestCase(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("(!a->b)|(a&d)"), ['a', '!', 'b', '>', 'a', 'd', '&', '|'])

    def test_create_first_string(self):
        postfix_expression = infix_to_postfix("(!a->b)|(a&d)")
        self.assertEqual(create_first_string(postfix_expression),
                         'a b d !a !a->b a&d (!a->b)|(a&d) ')  # add assertion here

    def test_evaluate_expression(self):
        postfix_expression = infix_to_postfix("(!a->b)|(a&d)")
        self.assertEqual(evaluate_expression(postfix_expression, {'a': False, 'b': False, 'd': True}),
                         '0 0 1 1 0 0 0')

    def test_get_all_info(self):
        info = get_all_info("(a|b)&!c")
        self.assertEqual(info['index_form'], '65280 - 00101010')
        self.assertEqual(info['SDNF'], '(!a&b&!c)|(a&!b&!c)|(a&b&!c)')
        self.assertEqual(info['SKNF'], '(a|b|c)&(a|b|!c)&(a|!b|!c)&(!a|b|!c)&(!a|!b|!c)')
        self.assertEqual(info['numeric_SDNF'], '(2,4,6) &')
        self.assertEqual(info['numeric_SKNF'], '(0,1,3,5,7) |')


if __name__ == '__main__':
    unittest.main()
