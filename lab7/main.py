from Matrix import *

matrix = Matrix()
word2 = "0101110011111111"
word3 = "1101110011111110"
# word4 = "1101110011111110"
# word5 = "1111100001110000"
matrix.set_word(2, word2)
matrix.set_word(3, word3)
matrix.set_word(6, word3)
matrix.set_word(7, word3)
# matrix.set_word(4, word5)
# matrix.set_word(0, word5)
print(matrix.get_word(2))
print(matrix.get_word(3))
# print(matrix.get_word(4))

# matrix.set_address_column(3, word4)
# print(matrix.get_address_column(3))
# matrix.word_apply_logical_operations_to_each_bit(2, 3, 15, LogicalOperations.DENIAL_OPERATION)
# print(matrix.get_word(15))
# matrix.replace_s_via_sum_ab('111')
# print(matrix.get_word(4))
# print(matrix.get_word(5))
matrix.print_matrix()
min1 = "0011111111111111"
max1 = "1111000000000001"
words = matrix.find_in_range(min1, max1)
print(words)
