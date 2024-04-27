from minimization import *


def example(string):
    expression = string
    print('\nРасчётный метод:')
    calculation_method_sdnf(expression)
    print('\nРасчётно-табличный метод:')
    table(expression)
    print('\nТабличный (Карно) метод:')
    karno_map(expression)


def example_sknf(string):
    expression = string
    print('\nРасчётный метод:')
    calculation_method_sknf(expression)
    print('\nРасчётно-табличный метод:')
    table(expression, False)
    print('\nТабличный (Карно) метод:')
    karno_map(expression, False)


while (True):
    choise = input()
    if choise == '1':
        example("(!a&b&c)|(a&!b&!c)|(a&!b&c)|(a&b&!c)|(a&b&c)")
    if choise == '2':
        example("(!a&!b&!c&d)|(!a&!b&c&d)|(!a&b&!c&d)|(!a&b&c&d)|(a&b&c&!d)|(a&b&c&d)|")
    if choise == '3':
        example(
            "(!a&!b&!c&d)|(!a&!b&c&d)|(!a&b&!c&!d)|(!a&b&!c&d)|(!a&b&c&!d)|(!a&b&c&d)|(a&!b&!c&!d)|(a&!b&!c&d)|(a&!b&c&!d)|(a&!b&c&d)|(a&b&!c&!d)|(a&b&!c&d)|(a&b&c&!d)|(a&b&c&d)")
    if choise == '4':
        example_sknf("(!a|b|c)&(a|!b|!c)&(a|!b|c)&(a|b|!c)&(a|b|c)")
    if choise == '5':
        example_sknf("(!a|!b|!c|d)&(!a|!b|c|d)&(!a|b|!c|d)&(!a|b|c|d)&(a|b|c|!d)&(a|b|c|d)")
    if choise == '6':
        break
