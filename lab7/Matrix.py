from enum import Enum


class Operations(Enum):
    DISJUNCTION = 1
    PIERCE_OPERATION = 2
    BANNING_THE_FIRST_ARG = 3
    IMPLICATION_FIRST_TO_SECOND = 4


class LogicalOperationsCalculator:
    @staticmethod
    def disjunction(value1, value2):
        return value1 or value2

    @staticmethod
    def pierce_operation(value1, value2):
        return not LogicalOperationsCalculator.disjunction(value1, value2)

    @staticmethod
    def banning_the_first_arg(value1, value2):
        return value1 and not value2

    @staticmethod
    def implication_first_to_second(value1, value2):
        return not value1 or value2


class Matrix:
    def __init__(self):
        self.size = 16
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def set_value(self, i, j, value):
        i_index = i % self.size
        j_index = j % self.size
        self.matrix[i_index][j_index] = value

    def get_value(self, i, j):
        i_index = i % self.size
        j_index = j % self.size
        return self.matrix[i_index][j_index]

    def set_word(self, position, word):
        for i in range(position, position + self.size):
            self.set_value(i, position, int(word[i - position]))

    def get_word(self, position):
        word = ''.join(str(self.get_value(i, position)) for i in range(position, position + self.size))
        return word

    def set_address_column(self, position, address):
        for i in range(position, self.size + position):
            self.set_value(i, i - position, int(address[i - position]))

    def get_address_column(self, position):
        address = ''.join(str(self.get_value(i, i - position)) for i in range(position, position + self.size))
        return address

    def print_matrix(self):
        for row in self.matrix:
            print('  '.join(map(str, row)))

    def address_apply_logical_operations_to_each_bit(self, position_address1, position_address2, result_position,
                                                     operation):
        address1 = self.get_address_column(position_address1)
        address2 = self.get_address_column(position_address2)
        result_address = self.apply_logical_operations_to_each_bit(address1, address2, operation)
        self.set_address_column(result_position, result_address)
        return result_address

    def word_apply_logical_operations_to_each_bit(self, position_word1, position_word2, result_position, operation):
        word1 = self.get_word(position_word1)
        word2 = self.get_word(position_word2)
        result_word = self.apply_logical_operations_to_each_bit(word1, word2, operation)
        self.set_word(result_position, result_word)
        return result_word

    def apply_logical_operations_to_each_bit(self, string1, string2, operation):
        result = []
        for i in range(len(string1)):
            value1 = int(string1[i]) > 0
            value2 = int(string2[i]) > 0
            if operation == Operations.BANNING_THE_FIRST_ARG:
                result_value = int(LogicalOperationsCalculator.banning_the_first_arg(value1, value2))
            elif operation == Operations.PIERCE_OPERATION:
                result_value = int(LogicalOperationsCalculator.pierce_operation(value1, value2))
            elif operation == Operations.IMPLICATION_FIRST_TO_SECOND:
                result_value = int(LogicalOperationsCalculator.implication_first_to_second(value1, value2))
            elif operation == Operations.DISJUNCTION:
                result_value = int(LogicalOperationsCalculator.disjunction(value1, value2))
            else:
                raise ValueError("Unknown logical operation")
            result.append(str(result_value))
        return ''.join(result)

    def replace_s_via_sum_ab(self, key):
        for i in range(self.size):
            if self.get_word(i)[:3] == key:
                word = self.get_word(i)
                a = int(word[3:7], 2)
                b = int(word[7:11], 2)
                sum_ab = a + b
                binary_sum = bin(sum_ab)[2:].zfill(5)
                result = word[:11] + binary_sum
                self.set_word(i, result)

    def find_g(self, g, a, s, l):
        return g or (not a and s and not l)

    def find_l(self, g, a, s, l):
        return l or (a and not s and not g)

    def find_in_range(self, min_val, max_val):
        if self.compare_s_via_a(max_val, min_val) == -1:
            return self.find_in_range(max_val, min_val)

        words = [self.get_word(i) for i in range(self.size)]
        temp_result = [word for word in words if self.compare_s_via_a(word, min_val) != -1]

        words_in_range = [word for word in temp_result if self.compare_s_via_a(word, max_val) != 1]
        return words_in_range

    def compare_s_via_a(self, s, a):
        g = l = False
        for ai, si in zip(a, s):
            ai = int(ai)
            si = int(si)
            g = self.find_g(g, ai, si, l)
            l = self.find_l(g, ai, si, l)
        if g and not l:
            return 1
        elif l and not g:
            return -1
        else:
            return 0
