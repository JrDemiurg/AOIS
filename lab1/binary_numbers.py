BINARY_LENGTH: int = 16
BINARY_FRACTION_LENGTH: int = 5
MANTISSA_LENGTH: int = 23
EXPONENT_LENGTH: int = 8


def to_the_direct_code(num: int) -> str:
    result: str = ''
    minus: bool = False
    if num < 0:
        num = abs(num)
        minus = True
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    result = result.zfill(BINARY_LENGTH-1)
    if minus:
        result = '1' + result
    else:
        result = '0' + result
    return result


def to_the_reverse_code(num: int) -> str:
    result: str = to_the_direct_code(num)
    if num >= 0:
        return result

    lst = list(result)
    for i in range(1, BINARY_LENGTH):
        if lst[i] == '1':
            lst[i] = '0'
        else:
            lst[i] = '1'
    result = ''.join(lst)
    return result


def to_the_additional_code(num: int) -> str:
    if num >= 0:
        return to_the_direct_code(num)

    result: str = to_the_reverse_code(num)
    lst = list(result)
    flag: bool = True
    for i in range(BINARY_LENGTH - 1, 0, -1):
        if flag:
            if lst[i] == '0':
                lst[i] = '1'
                flag = False
            else:
                lst[i] = '0'
    result = ''.join(lst)
    return result


def show_all_form(num: int) -> None:
    print("Number:", num)
    print("Direct:    ", to_the_direct_code(num))
    print("Reverse:   ", to_the_reverse_code(num))
    print("Additional:", to_the_additional_code(num))


def direct_code_to_int(bin_num: str) -> int:
    lst = list(bin_num)
    result: int = 0
    if lst[0] == '0':
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result += 2 ** (BINARY_LENGTH - i - 1)
    else:
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result -= 2 ** (BINARY_LENGTH - i - 1)
    return result


def additional_code_to_int(bin_num: str) -> int:
    lst = list(bin_num)
    result: int = 0
    if lst[0] == '0':
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result += 2 ** (BINARY_LENGTH - i - 1)
    else:
        for i in range(1, BINARY_LENGTH):
            if lst[i] == '1':
                lst[i] = '0'
            else:
                lst[i] = '1'

        flag: bool = True
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if flag:
                if lst[i] == '0':
                    lst[i] = '1'
                    flag = False
                else:
                    lst[i] = '0'

        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result -= 2 ** (BINARY_LENGTH - i - 1)
    return result


def sum_with_info(num_1: int, num_2: int) -> int:
    print('\nFirst:')
    show_all_form(num_1)
    print('Second')
    show_all_form(num_2)
    result = sum_of_additional_code(num_1, num_2)
    print('Result:')
    show_all_form(result)
    return result


def sum_of_additional_code(num_1: int, num_2: int) -> int:
    value_1: str = to_the_additional_code(num_1)
    value_2: str = to_the_additional_code(num_2)

    lst_1 = list(value_1)
    lst_2 = list(value_2)

    result: str = ''
    flag: bool = False
    for i in range(len(value_1) - 1, -1, -1):
        if flag:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '1' + result
                flag = False
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '1' + result
        else:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '1' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '1' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '0' + result
                flag = True
    return additional_code_to_int(result)


def subtracting_with_info(num_1: int, num_2: int) -> int:
    print('\nFirst:')
    show_all_form(num_1)
    print('Second')
    show_all_form(num_2)
    result = subtracting(num_1, num_2)
    print('Result:')
    show_all_form(result)
    return result


def subtracting(num_1: int, num_2: int) -> int:
    return sum_of_additional_code(num_1, num_2*-1)


def multiplication_with_info(num_1: int, num_2: int) -> int:
    print('First:')
    show_all_form(num_1)
    print('Second')
    show_all_form(num_2)
    result = multiplication(num_1, num_2)
    print('Result:')
    show_all_form(result)
    return result


def multiplication(num_1: int, num_2: int) -> int:

    if num_1 == 0 or num_2 == 0:
        return 0

    value_1: str = to_the_direct_code(num_1)
    value_2: str = to_the_direct_code(num_2)

    last_one_index_value_1 = value_1.rfind('1')
    last_one_index_value_2 = value_2.rfind('1')

    zeros = value_1[last_one_index_value_1 + 1:] + value_2[last_one_index_value_2 + 1:]

    value_1 = value_1[:last_one_index_value_1 + 1]
    value_2 = value_2[:last_one_index_value_2 + 1]

    lst_1 = list(value_1)
    lst_2 = list(value_2)

    lst_1.pop(0)
    lst_2.pop(0)
    result = list('')

    for i in range(len(lst_2) - 1, -1, -1):
        if lst_2[i] == '0':
            lst_1.append('0')
            continue
        result = sum_for_multiplication(result, lst_1)
        lst_1.append('0')

    my_string = ''.join(result) + zeros
    if len(my_string) >= BINARY_LENGTH:
        my_string = my_string[-BINARY_LENGTH+1:]

    if num_1 * num_2 < 0:
        my_string = '1' + my_string
    else:
        my_string = '0' + my_string

    return direct_code_to_int(my_string)


def sum_for_multiplication(lst_1: list, lst_2: list) -> list:
    my_string1, my_string2 = ''.join(lst_1), ''.join(lst_2)
    my_string1, my_string2 = my_string1.zfill(len(my_string2)), my_string2.zfill(len(my_string1))
    lst_1, lst_2 = list(my_string1), list(my_string2)
    result: str = ''
    flag: bool = False
    for i in range(len(lst_2) - 1, -1, -1):
        if flag:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '1' + result
                flag = False
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '1' + result
        else:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '1' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '1' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '0' + result
                flag = True
    if flag:
        result = '1' + result
    return list(result)


def fixed_point_code_to_float(bin_num: str) -> float:
    lst = list(bin_num)
    result: float = 0
    if lst[0] == '0':
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result += 2 ** (BINARY_LENGTH - i - 1 - BINARY_FRACTION_LENGTH)
    else:
        for i in range(BINARY_LENGTH - 1, 0, -1):
            if lst[i] == '1':
                result -= 2 ** (BINARY_LENGTH - i - 1 - BINARY_FRACTION_LENGTH)
    return result


def division_with_info(num_1: int, num_2: int) -> float:
    print('First:')
    show_all_form(num_1)
    print('Second')
    show_all_form(num_2)
    result = division(num_1, num_2)
    print(result)
    return result


def division(num_1: int, num_2: int) -> float:
    if num_2 == 0:
        return None
    devinded = to_the_direct_code(abs(num_1))
    devisor = to_the_direct_code(abs(num_2))
    quontient_integer: str = ''.zfill(BINARY_LENGTH - BINARY_FRACTION_LENGTH - 1)
    quontient_fractional = ''.zfill(BINARY_FRACTION_LENGTH)

    while True:
        if compare_binary_numbers(devinded, devisor):
            devinded = to_the_direct_code(subtracting(direct_code_to_int(devinded), direct_code_to_int(devisor)))
            lst = list(quontient_integer)
            flag: bool = True
            for i in range(BINARY_LENGTH - BINARY_FRACTION_LENGTH - 2, -1, -1):
                if flag:
                    if lst[i] == '0':
                        lst[i] = '1'
                        flag = False
                    else:
                        lst[i] = '0'
            quontient_integer = ''.join(lst)
        else:
            break

    devinded = devinded + '0' * BINARY_FRACTION_LENGTH
    if len(devinded) > BINARY_LENGTH:
        devinded = devinded[-BINARY_LENGTH:]
    while True:
        if compare_binary_numbers(devinded, devisor):
            devinded = to_the_direct_code(subtracting(direct_code_to_int(devinded), direct_code_to_int(devisor)))
            lst = list(quontient_fractional)
            flag: bool = True
            for i in range(BINARY_FRACTION_LENGTH - 1, -1, -1):
                if flag:
                    if lst[i] == '0':
                        lst[i] = '1'
                        flag = False
                    else:
                        lst[i] = '0'
            quontient_fractional = ''.join(lst)
        else:
            break

    if num_1 * num_2 < 0:
        result = '1' + quontient_integer + quontient_fractional
    else:
        result = '0' + quontient_integer + quontient_fractional
    print('Result:\nDirect fixed-point code, fractional part length', BINARY_FRACTION_LENGTH, ':')
    print(result)
    return fixed_point_code_to_float(result)


def compare_binary_numbers(num_1: str, num_2: str) -> bool:
    num_1, num_2 = num_1.lstrip('0'), num_2.lstrip('0')
    num_1, num_2 = num_1.zfill(len(num_2)), num_2.zfill(len(num_1))
    lst_1, lst_2 = list(num_1), list(num_2)

    for i in range(0, len(num_1)):
        if lst_1[i] == '1' and lst_2[i] == '0':
            return True
        elif lst_1[i] == '1' and lst_2[i] == '1':
            continue
        elif lst_1[i] == '0' and lst_2[i] == '1':
            return False
    return True


def to_float_binary(num: float) -> str:
    if num < 0:
        sign = '1'
    else:
        sign = '0'

    whole: str = to_the_direct_code(int(abs(num)))
    fractional_float: float = abs(num) - int(abs(num))
    mantissa: str = ''

    for i in range(0, MANTISSA_LENGTH):
        fractional_float *= 2
        if fractional_float >= 1:
            fractional_float -= 1
            mantissa = mantissa + '1'
        else:
            mantissa = mantissa + '0'
    whole = whole.lstrip('0')
    if whole == '':
        exponent_int = 0
        for char in mantissa:
            if char == '1':
                break
            if char == '0':
                exponent_int -= 1
        exponent_int += 127 - 1
    else:
        exponent_int = len(whole) - 1 + 127
    exponent: str = ''
    while exponent_int > 0:
        exponent = str(exponent_int % 2) + exponent
        exponent_int //= 2
    exponent = exponent.zfill(EXPONENT_LENGTH)

    if whole == '':
        mantissa = mantissa.lstrip('0')
        mantissa = mantissa[1:]
    else:
        whole = whole[1:]
        mantissa = whole + mantissa
    mantissa = mantissa.ljust(MANTISSA_LENGTH, '0')
    mantissa = mantissa[:MANTISSA_LENGTH]
    return sign + exponent + mantissa


def float_binary_to_float(bin_num: str) -> float:
    sign = bin_num[0]
    exponent = bin_num[1:9]
    mantissa = bin_num[-23:]

    lst = list(exponent)
    exponent_int = 0
    for i in range(EXPONENT_LENGTH - 1, -1, -1):
        if lst[i] == '1':
            exponent_int += 2 ** (EXPONENT_LENGTH - i - 1)

    exponent_int = exponent_int - 127
    mantissa = '1' + mantissa
    whole_int: int = 0
    fractional_int: float = 0
    if exponent_int >= 0:
        whole = mantissa[:1 + exponent_int]
        fractional = mantissa[1 + exponent_int:]
        fractional = fractional.ljust(MANTISSA_LENGTH, '0')

        lst = list(whole)
        for i in range(len(whole) - 1, -1, -1):
            if lst[i] == '1':
                whole_int += 2 ** (len(whole) - 1 - i)
    else:
        fractional = '0' * abs(exponent_int + 1) + mantissa

    lst = list(fractional)
    for i in range(0, MANTISSA_LENGTH):
        if lst[i] == '1':
            fractional_int += 2 ** (-i - 1)
    result: float = whole_int + fractional_int
    if sign == '1':
        result *= -1
    return result


def sum_of_binary_float(num_1: float, num_2: float) -> str:
    value_1: str = to_float_binary(num_1)
    value_2: str = to_float_binary(num_2)
    exponent_1 = value_1[1:9]
    lst = list(exponent_1)
    exponent_1_int = 0
    for i in range(EXPONENT_LENGTH - 1, -1, -1):
        if lst[i] == '1':
            exponent_1_int += 2 ** (EXPONENT_LENGTH - i - 1)
    exponent_1_int = exponent_1_int - 127

    exponent_2 = value_2[1:9]
    lst = list(exponent_2)
    exponent_2_int = 0
    for i in range(EXPONENT_LENGTH - 1, -1, -1):
        if lst[i] == '1':
            exponent_2_int += 2 ** (EXPONENT_LENGTH - i - 1)
    exponent_2_int = exponent_2_int - 127
    mantissa_1 = value_1[-23:]
    mantissa_1 = '001' + mantissa_1

    mantissa_2 = value_2[-23:]
    mantissa_2 = '001' + mantissa_2

    exponent_diff = exponent_1_int - exponent_2_int
    if exponent_diff < 0:
        mantissa_1 = mantissa_1[0] + abs(exponent_diff) * '0' + mantissa_1[1:-abs(exponent_diff)]
    elif exponent_diff > 0:
        mantissa_2 = mantissa_2[0] + abs(exponent_diff) * '0' + mantissa_2[1:-abs(exponent_diff)]
    lst_1 = list(mantissa_1)
    lst_2 = list(mantissa_2)

    result: str = ''
    flag: bool = False
    for i in range(len(mantissa_1) - 1, -1, -1):
        if flag:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '1' + result
                flag = False
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '1' + result
        else:
            if lst_1[i] == '0' and lst_2[i] == '0':
                result = '0' + result
            elif lst_1[i] == '1' and lst_2[i] == '0':
                result = '1' + result
            elif lst_1[i] == '0' and lst_2[i] == '1':
                result = '1' + result
            elif lst_1[i] == '1' and lst_2[i] == '1':
                result = '0' + result
                flag = True

    exponent_max = max(exponent_1_int, exponent_2_int) + 127
    if result[1] == '1':
        exponent_max += 1
    exponent: str = ''
    while exponent_max > 0:
        exponent = str(exponent_max % 2) + exponent
        exponent_max //= 2
    exponent = exponent.zfill(EXPONENT_LENGTH)
    return '0' + exponent + result[3:]


def sum_of_binary_float_with_info(num_1: float, num_2: float) -> int:
    print('\n', num_1)
    print(to_float_binary(num_1))
    print(num_2)
    print(to_float_binary(num_2))
    print(float_binary_to_float(sum_of_binary_float(num_1, num_2)))
    print(sum_of_binary_float(num_1, num_2))
