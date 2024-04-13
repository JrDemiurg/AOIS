from logical_function import *


def example_1():
    info = get_all_info("(a|b)&!c")
    print(info['table'])
    print(info['index_form'])
    print(info['SDNF'])
    print(info['SKNF'])
    print(info['numeric_SDNF'])
    print(info['numeric_SKNF'])


def example_2():
    info = get_all_info("(!a->b)|(c&d)")
    print(info['table'])
    print(info['index_form'])
    print(info['SDNF'])
    print(info['SKNF'])
    print(info['numeric_SDNF'])
    print(info['numeric_SKNF'])


def example_3():
    info = get_all_info("!((!a)&(b&(a|c)))")
    print(info['table'])
    print(info['index_form'])
    print(info['SDNF'])
    print(info['SKNF'])
    print(info['numeric_SDNF'])
    print(info['numeric_SKNF'])


def example_4():
    info = get_all_info("((!a~b)|(c&d))->e")
    print(info['table'])
    print(info['index_form'])
    print(info['SDNF'])
    print(info['SKNF'])
    print(info['numeric_SDNF'])
    print(info['numeric_SKNF'])
    print(info['numeric_SKNF'])


example_1()
example_2()
example_3()
example_4()
