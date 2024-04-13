def create_first_string(expression):
    stack_char = []
    text_output = ''

    for token in expression:
        if token.isalpha() and token not in text_output:
            text_output = text_output + token + ' '

    for token in expression:
        if token.isalpha():
            stack_char.append(token)
        elif token == '|':
            operand1_char = stack_char.pop()
            operand2_char = stack_char.pop()
            stack_char.append(f"({operand2_char}|{operand1_char})")
            text_output = text_output + f"{operand2_char}|{operand1_char} "
        elif token == '&':
            operand1_char = stack_char.pop()
            operand2_char = stack_char.pop()
            stack_char.append(f"({operand2_char}&{operand1_char})")
            text_output = text_output + f"{operand2_char}&{operand1_char} "
        elif token == '~':
            operand1_char = stack_char.pop()
            operand2_char = stack_char.pop()
            stack_char.append(f"({operand2_char}~{operand1_char})")
            text_output = text_output + f"{operand2_char}~{operand1_char} "
        elif token == '!':
            operand_char = stack_char.pop()
            stack_char.append(f"!{operand_char}")
            text_output = text_output + f"!{operand_char} "
        elif token == '>':
            operand1_char = stack_char.pop()
            operand2_char = stack_char.pop()
            stack_char.append(f"({operand2_char}->{operand1_char})")
            text_output = text_output + f"{operand2_char}->{operand1_char} "
    return text_output


def evaluate_expression(expression, variables: dict):
    stack = []
    text_output = ''
    text_output_char = ''

    for token in expression:
        if token.isalpha() and token not in text_output_char:
            text_output_char = text_output_char + token + ' '
            text_output = text_output + str(int(variables[token])) + ' '

    for token in expression:
        if token.isalpha():
            stack.append(variables[token])
        elif token == '|':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 or operand2
            stack.append(result)
            text_output = text_output + str(int(result)) + ' '
        elif token == '&':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 and operand2
            stack.append(result)
            text_output = text_output + str(int(result)) + ' '
        elif token == '~':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 == operand2
            stack.append(result)
            text_output = text_output + str(int(result)) + ' '
        elif token == '!':
            operand = stack.pop()
            result = not operand
            stack.append(result)
            text_output = text_output + str(int(result)) + ' '
        elif token == '>':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = (not operand1) or operand2
            stack.append(result)
            text_output = text_output + str(int(result)) + ' '
    text_output = text_output[:-1]
    return text_output


def infix_to_postfix(expression):
    expression = expression.replace('-', "")
    precedence = {'(': 0, '|': 1, '&': 1, '~': 1, '!': 2, '>': 1}
    output = []
    stack = []

    for token in expression:
        if token.isalpha():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def get_all_info(expression: str):
    postfix_expression = infix_to_postfix(expression)
    table = create_first_string(postfix_expression)

    SDNF = ''
    SKNF = ''
    numeric_SDNF = '('
    numeric_SKNF = '('
    index_form = ''
    variables = []
    binary = []
    for token in expression:
        if token.isalpha() and token not in variables:
            binary.append(False)
            variables.append(token)

    for a in range(2 ** len(binary)):
        result_dict = dict(zip(variables, binary))
        postfix_expression = infix_to_postfix(expression)
        result = evaluate_expression(postfix_expression, result_dict)
        table = table + f'\n{result}'

        flag = True
        for i in range(len(binary) - 1, -1, -1):
            if flag:
                if binary[i] == False:
                    binary[i] = True
                    flag = False
                else:
                    binary[i] = False

        if result[-1] == '1':
            index_form = index_form + '1'
            numeric_SDNF = numeric_SDNF + f'{a},'
            SDNF = SDNF + '('
            for item in result_dict:
                SDNF = SDNF + f'{item}&' if result_dict[item] == True else SDNF + f'!{item}&'
            SDNF = SDNF[:-1] + ')|'
        else:
            index_form = index_form + '0'
            numeric_SKNF = numeric_SKNF + f'{a},'
            SKNF = SKNF + '('
            for item in result_dict:
                SKNF = SKNF + f'{item}|' if result_dict[item] == False else SKNF + f'!{item}|'
            SKNF = SKNF[:-1] + ')&'

    index_form_num  = 0
    for i in range(len(index_form) - 1, -1, -1):
        index_form_num += 2**(15-i)

    index_form = str(index_form_num) + ' - ' + index_form
    SDNF = SDNF[:-1]
    SKNF = SKNF[:-1]
    numeric_SDNF = numeric_SDNF[:-1] + ') &'
    numeric_SKNF = numeric_SKNF[:-1] + ') |'

    result = {
        'table': table,
        'index_form': index_form,
        'SDNF': SDNF,
        'SKNF': SKNF,
        'numeric_SDNF': numeric_SDNF,
        'numeric_SKNF': numeric_SKNF
    }
    return result


expression = "(!a->b)|(a&d)"
get_all_info(expression)
