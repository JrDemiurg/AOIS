from hash_table import *

table = HashTable(100)
while True:
    print("1 - Добавить элемент")
    print("2 - Найти значение элемента")
    print("3 - Удалить элемент")
    choise = input("Выберите действие ")
    if choise == "1":
        key = input("Ключ ")
        value = input("Значение ")
        table.insert(key, value)
    if choise == "2":
        key = input("Ключ ")
        print(table.search(key))
    if choise == "3":
        key = input("Ключ ")
        table.remove(key)
