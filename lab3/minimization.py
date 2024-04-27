from logical_function import *

gray_encoding = {
    0: [False, False, False, False],
    1: [False, False, False, True],
    2: [False, False, True, True],
    3: [False, False, True, False],
    4: [False, True, True, False],
    5: [False, True, True, True],
    6: [False, True, False, True],
    7: [False, True, False, False]
}


def expression_to_array(expression):
    variables = sorted(set(char for char in expression if char.isalpha()))
    result = []
    sign = False
    for char in expression:
        if char.isalpha():
            if sign:
                result.append(f"!{char}")
                sign = False
            else:
                result.append(f"{char}")
        sign = True if char == '!' else sign
    return tuple(tuple(result[i:i + len(variables)]) for i in range(0, len(result), len(variables)))


def find_matching_elements(arr1, arr2):
    if len(arr1) != len(arr2):
        return None

    matching_elements = []
    different_elements = []

    for i in range(len(arr1)):
        if arr1[i] in arr2:
            matching_elements.append(arr1[i])
        else:
            different_elements.append(arr1[i])
        if arr2[i] not in arr1:
            different_elements.append(arr2[i])

    if len(different_elements) == 2:
        if different_elements[0] == '!' + different_elements[1]:
            return matching_elements
        elif different_elements[1] == '!' + different_elements[0]:
            return matching_elements

    return None


def merge_arrays(arr, is_sdnf=True, flag=True):
    result = []
    result.extend(arr)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            part = find_matching_elements(arr[i], arr[j])
            if part is not None:
                result.append(part)

    for exclude_array in result:
        result = [x for x in result if not all(item in x for item in exclude_array)]
        result.append(exclude_array)
    if result == arr:
        return result
    else:
        if flag:
            if is_sdnf:
                print('|'.join('({})'.format('&'.join(subarray)) for subarray in result))
            else:
                print('&'.join('({})'.format('|'.join(subarray)) for subarray in result))
        return merge_arrays(result, is_sdnf, flag)


def calculation_method_sdnf(string: str):
    arr = expression_to_array(string)
    print('Исходное:')
    print('|'.join('({})'.format('&'.join(subarray)) for subarray in arr))
    print("Склеивание:")
    new_arr = merge_arrays(arr)

    str_new_arr = '|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr)

    variables = []
    binary = []
    for token in str_new_arr:
        if token.isalpha() and token not in variables:
            binary.append(False)
            variables.append(token)

    index = 0
    while index < len(new_arr):

        temp_arr = new_arr.copy()
        chosen_elem = temp_arr[index]
        temp_arr.remove(temp_arr[index])
        str_temp_arr = '|'.join('({})'.format('&'.join(subarray)) for subarray in temp_arr)
        counter = 0

        for a in range(2 ** len(binary)):
            result_dict = dict(zip(variables, binary))

            for element in chosen_elem:
                result_dict[element] = True

            postfix_expression = infix_to_postfix(str_temp_arr)
            result = evaluate_expression(postfix_expression, result_dict)[-1]

            flag = True
            for i in range(len(binary) - 1, -1, -1):
                if flag:
                    if binary[i] == False:
                        binary[i] = True
                        flag = False
                    else:
                        binary[i] = False
            if result == '1':
                counter += 1
        if counter == 2 ** len(binary):
            new_arr.remove(chosen_elem)
            index -= 1
        index += 1
    print('После проверки:')
    print('|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr))
    return '|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr)


def calculation_method_sknf(string: str):
    arr = expression_to_array(string)
    print('Исходное:')
    print('&'.join('({})'.format('|'.join(subarray)) for subarray in arr))
    print("Склеивание:")
    new_arr = merge_arrays(arr, False)

    str_new_arr = '&'.join('({})'.format('|'.join(subarray)) for subarray in new_arr)

    variables = []
    binary = []
    for token in str_new_arr:
        if token.isalpha() and token not in variables:
            binary.append(False)
            variables.append(token)

    index = 0
    while index < len(new_arr):

        temp_arr = new_arr.copy()
        chosen_elem = temp_arr[index]
        temp_arr.remove(temp_arr[index])
        str_temp_arr = '&'.join('({})'.format('|'.join(subarray)) for subarray in temp_arr)
        counter = 0
        for a in range(2 ** len(binary)):
            result_dict = dict(zip(variables, binary))

            for element in chosen_elem:
                result_dict[element] = False
            postfix_expression = infix_to_postfix(str_temp_arr)
            result = evaluate_expression(postfix_expression, result_dict)[-1]

            flag = True
            for i in range(len(binary) - 1, -1, -1):
                if flag:
                    if binary[i] == False:
                        binary[i] = True
                        flag = False
                    else:
                        binary[i] = False
            if result == '0':
                counter += 1
        if counter == 2 ** len(binary):
            new_arr.remove(chosen_elem)
            index -= 1
        index += 1
    print('После проверки:')
    print('&'.join('({})'.format('|'.join(subarray)) for subarray in new_arr))
    return '&'.join('({})'.format('|'.join(subarray)) for subarray in new_arr)


def table(string, is_sdnf=True):
    arr1 = expression_to_array(string)
    print('Исходное:')
    if is_sdnf:
        print('|'.join('({})'.format('&'.join(subarray)) for subarray in arr1))
    else:
        print('&'.join('({})'.format('|'.join(subarray)) for subarray in arr1))
    print("Склеивание:")
    arr2 = merge_arrays(arr1) if is_sdnf else merge_arrays(arr1, False)

    char_number = 97
    first_line = '  '
    for i in arr1:
        print(chr(char_number) + f' - {i}')
        first_line = first_line + chr(char_number)
        char_number += 1

    char_number = 65
    my_dict = {}
    for i in arr2:
        print(chr(char_number) + f' - {i}')
        my_dict[chr(char_number)] = i
        char_number += 1
    print(first_line)

    table_arr = []
    arr_number = 0
    char_number = 65
    for i in arr2:
        string = chr(char_number) + ' '
        char_number += 1
        table_arr.append([])
        for j in arr1:
            if all(item in j for item in i):
                string = string + '1'
                table_arr[arr_number].append(1)
            else:
                string = string + '0'
                table_arr[arr_number].append(0)
        arr_number += 1
        print(string)

    rows = len(table_arr)
    columns = len(table_arr[0])
    result = []

    for j in range(columns):
        column = [table_arr[i][j] for i in range(rows)]
        if column.count(1) == 1:
            row_index = column.index(1)
            letter = chr(row_index + ord('A'))
            if my_dict[letter] not in result:
                result.append(my_dict[letter])
    print('Результат:')
    if is_sdnf:
        print('|'.join('({})'.format('&'.join(subarray)) for subarray in result))
        res = '|'.join('({})'.format('&'.join(subarray)) for subarray in result)
    else:
        print('&'.join('({})'.format('|'.join(subarray)) for subarray in result))
        res = '&'.join('({})'.format('|'.join(subarray)) for subarray in result)
    return res


def find_rectangles(grid):
    rows = len(grid)
    columns = len(grid[0])
    rectangles = []

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '1':
                rectangle = []
                new_column = column
                new_row = row
                while new_column < columns * 2 - 1 and grid[row][
                    new_column if new_column < columns else new_column - columns] != '0':
                    rectangle.append((row, new_column if new_column < columns else new_column - columns))
                    if (len(rectangle) & (len(rectangle) - 1)) == 0 and tuple(rectangle) not in rectangles:
                        rectangles.append(tuple(rectangle))
                    new_column += 1
                rectangle = []
                while new_row < rows * 2 - 1 and grid[new_row if new_row < rows else new_row - rows][column] != '0':
                    rectangle.append((new_row if new_row < rows else new_row - rows, column))
                    if (len(rectangle) & (len(rectangle) - 1)) == 0 and tuple(rectangle) not in rectangles:
                        rectangles.append(tuple(rectangle))
                    new_row += 1
    print('')
    return rectangles


def karno_map(string: str, is_sdnf: bool = True):
    arr = expression_to_array(string)

    str_new_arr = '|'.join('({})'.format('&'.join(subarray)) for subarray in arr) if is_sdnf else '&'.join(
        '({})'.format('|'.join(subarray)) for subarray in arr)
    print(str_new_arr)
    variables = []
    binary = []
    for token in str_new_arr:
        if token.isalpha() and token not in variables:
            binary.append(False)
            variables.append(token)

    horizontal = variables[len(variables) // 2:]
    vertical = variables[:len(variables) // 2:]
    horizontal_bin = binary[len(binary) // 2:]
    vertical_bin = binary[:len(binary) // 2:]
    map_karno = [[0] * (2 ** len(horizontal)) for _ in range(2 ** len(vertical_bin))]

    hor_dict = {}
    ver_dict = {}
    counter_ver = 0
    postfix_expression = infix_to_postfix(str_new_arr)
    for ver in range(2 ** len(vertical_bin)):
        ver_dict[ver] = [tuple(vertical_bin)]
        counter_hor = 0
        for hor in range(2 ** len(horizontal)):
            horizontal_bin = gray_encoding[counter_hor][-len(horizontal):]
            vertical_bin = gray_encoding[counter_ver][-len(vertical):]
            counter_hor += 1
            result_dict = dict(zip(horizontal, horizontal_bin))
            result_dict.update(dict(zip(vertical, vertical_bin)))
            hor_dict[hor] = [tuple(horizontal_bin)]
            map_karno[ver][hor] = evaluate_expression(postfix_expression, result_dict)[-1]

        counter_ver += 1

    for x in map_karno:
        print(x)

    result = []
    rectangles = find_rectangles(map_karno)
    count_2 = 0
    for x in rectangles:
        if len(x) == 1:
            result.append([])
            for y in ver_dict[x[0][0]]:
                count = 0
                for i in y:
                    if not y[count]:
                        result[len(result) - 1].append(f'!{vertical[count]}')
                    else:
                        result[len(result) - 1].append(f'{vertical[count]}')
                    count += 1
            for z in hor_dict[x[0][1]]:
                count = 0
                for i in z:
                    if not z[count]:
                        result[count_2].append(f'!{horizontal[count]}')
                    else:
                        result[count_2].append(f'{horizontal[count]}')
                    count += 1
            count_2 += 1
    new_arr = merge_arrays(arr, True, False) if is_sdnf else merge_arrays(arr, False, False)

    str_new_arr = '|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr) if is_sdnf else '&'.join(
        '({})'.format('|'.join(subarray)) for subarray in new_arr)

    variables = []
    binary = []
    for token in str_new_arr:
        if token.isalpha() and token not in variables:
            binary.append(False)
            variables.append(token)

    index = 0
    while index < len(new_arr):

        temp_arr = new_arr.copy()
        chosen_elem = temp_arr[index]
        temp_arr.remove(temp_arr[index])
        str_temp_arr = '|'.join('({})'.format('&'.join(subarray)) for subarray in temp_arr) if is_sdnf else '&'.join(
            '({})'.format('|'.join(subarray)) for subarray in temp_arr)
        counter = 0
        for a in range(2 ** len(binary)):
            result_dict = dict(zip(variables, binary))

            for element in chosen_elem:
                result_dict[element] = True if is_sdnf else False
            postfix_expression = infix_to_postfix(str_temp_arr)
            result = evaluate_expression(postfix_expression, result_dict)[-1]
            flag = True
            for i in range(len(binary) - 1, -1, -1):
                if flag:
                    if binary[i] == False:
                        binary[i] = True
                        flag = False
                    else:
                        binary[i] = False
            if result == '1' and is_sdnf:
                counter += 1
            elif result == '0' and not is_sdnf:

                counter += 1
        if counter == 2 ** len(binary):
            new_arr.remove(chosen_elem)
            index -= 1
        index += 1

    print('|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr) if is_sdnf else '&'.join(
        '({})'.format('|'.join(subarray)) for subarray in new_arr))
    return '|'.join('({})'.format('&'.join(subarray)) for subarray in new_arr) if is_sdnf else '&'.join(
        '({})'.format('|'.join(subarray)) for subarray in new_arr)
