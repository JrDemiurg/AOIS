class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    class TreeNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def hash_function(self, input_str):
        russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

        first_letter = input_str[0].lower()
        second_letter = input_str[1].lower()

        first_letter_index = russian_alphabet.index(first_letter)
        second_letter_index = russian_alphabet.index(second_letter)

        return (first_letter_index * 33 + second_letter_index) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = self.TreeNode(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.key > key:
                    if current.left is None:
                        current.left = new_node
                        return
                    current = current.left
                if current.key < key:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right

    def search(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            if current is not None and current.key > key:
                current = current.left
            if current is not None and current.key < key:
                current = current.right
        return None

    def remove(self, key):
        index = self.hash_function(key)
        root = self.table[index]
        if root is None:
            return None
        if root.left is None and root.right is None and root.key == key:
            self.table[index] = None
            return
        if root.left is None and root.right is not None and root.key == key:
            self.table[index] = root.right
        if root.left is not None and root.right is None and root.key == key:
            self.table[index] = root.left
        self.delete_node(root, key)

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_minimum(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        return root

    def find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
