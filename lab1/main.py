from binary_numbers import *


def demonstrate_all_form():
    show_all_form(0)
    show_all_form(10)
    show_all_form(-10)
    show_all_form(99)
    show_all_form(-99)


def demonstrate_sum_of_additional_code():
    print('\nDemonstration of the sum:')
    sum_with_info(-10, 10)
    sum_with_info(0, 129)
    sum_with_info(16, -21)
    sum_with_info(33, 100)
    sum_with_info(64, 64)


def demonstrate_subtracting():
    print('\nDemonstration of the subtracting:')
    subtracting_with_info(-10, 10)
    subtracting_with_info(0, 129)
    subtracting_with_info(16, -21)
    subtracting_with_info(33, 100)
    subtracting_with_info(64, 64)


def demonstrate_multiplication():
    print('\nDemonstration of the multiplication:')
    multiplication_with_info(-10, 10)
    multiplication_with_info(0, 129)
    multiplication_with_info(16, -21)
    multiplication_with_info(33, 100)
    multiplication_with_info(64, 64)


def demonstrate_division():
    print('\nDemonstration of the division:')
    division_with_info(-10, 10)
    division_with_info(0, 129)
    division_with_info(16, -21)
    division_with_info(33, 100)
    division_with_info(64, 64)


def demonstrate_sum_of_binary_float():
    print('\nDemonstration of the sum of float:')
    sum_of_binary_float_with_info(12.5, 2.125)
    sum_of_binary_float_with_info(3.25, 0)
    sum_of_binary_float_with_info(0.625, 12.25)
    sum_of_binary_float_with_info(0.125, 0.5)
    sum_of_binary_float_with_info(0.375, 10)

while True:
    key: int = 7
    try:
        key: int = int(input())
    except ValueError:
        print("Invalid input")

    if key == 1:
        demonstrate_all_form()
    if key == 2:
        demonstrate_sum_of_additional_code()
    if key == 3:
        demonstrate_subtracting()
    if key == 4:
        demonstrate_multiplication()
    if key == 5:
        demonstrate_division()
    if key == 6:
        demonstrate_sum_of_binary_float()
    if key == 7:
        break
