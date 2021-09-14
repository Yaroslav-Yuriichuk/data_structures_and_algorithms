class BST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None
            self.count = 1
            self.size = 1

    def __init__(self, key=lambda x: x):
        self.__root = None
        self.__key = key

    def __str(self, node):
        string = ""

        if node.left is not None:
            string += self.__str(node.left)

        string += (str(node.data) + ", ") * node.count

        if node.right is not None:
            string += self.__str(node.right)

        return string

    def __insert(self, node, data):
        if node is None:
            return BST.Node(data)

        if self.__key(data) == self.__key(node.data):
            node.count += 1
        elif self.__key(data) < self.__key(node.data):
            node.left = self.__insert(node.left, data)
        else:
            node.right = self.__insert(node.right, data)

        node.size = self.__size(node.left) + node.count + \
            self.__size(node.right)
        return node

    def __size(self, node):
        return 0 if node is None else node.size

    def __min(self, node):
        while node.left is not None:
            node = node.left

        return node

    def __max(self, node):
        while node.right is not None:
            node = node.right

        return node

    def __floor(self, node, key):
        if node is None:
            return None

        if self.__key(key) == self.__key(node.data):
            return node
        if self.__key(key) > self.__key(node.data):
            tmp = self.__floor(node.right, key)
            return tmp if tmp is not None else node
        return self.__floor(node.left, key)

    def __ceiling(self, node, key):
        if node is None:
            return None

        if self.__key(key) == self.__key(node.data):
            return node
        elif self.__key(key) < self.__key(node.data):
            tmp = self.__ceiling(node.left, key)
            return tmp if tmp is not None else node
        return self.__ceiling(node.right, key)

    def __rank(self, node, key):
        if node is None:
            return 0
        if self.__key(key) == self.__key(node.data):
            return self.__size(node.left)
        elif self.__key(key) < self.__key(node.data):
            return self.__rank(node.left, key)
        else:
            return self.__size(node.left) + node.count + self.__rank(node.right, key)

    def __delete_min(self, node, delete_all):
        if node.left is None and (delete_all or node.count == 1):
            node.size -= node.count
            return node.right
        elif node.left is None:
            node.count -= 1
            node.size -= 1
            return node

        node.left = self.__delete_min(node.left, delete_all)
        node.size = self.__size(node.left) + node.count + \
            self.__size(node.right)
        return node

    def __delete_max(self, node, delete_all):
        if node.right is None and (delete_all or node.count == 1):
            node.size -= node.count
            return node.left
        elif node.right is None:
            node.count -= 1
            node.size -= 1
            return node

        node.right = self.__delete_max(node.right, delete_all)
        node.size = self.__size(node.left) + node.count + \
            self.__size(node.right)
        return node

    def __delete(self, node, key, delete_all):
        if node is None:
            return None
        if self.__key(key) < self.__key(node.data):
            node.left = self.__delete(node.left, key, delete_all)
        elif self.__key(key) > self.__key(node.data):
            node.right = self.__delete(node.right, key, delete_all)
        else:
            if (not delete_all) and node.count > 1:
                node.count -= 1
                node.size -= 1
                return node

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            to_replace = self.__min(node.right)
            to_replace.right = self.__delete_min(node.right, True)
            to_replace.left = node.left
            node = to_replace

        node.size = self.__size(node.left) + node.count + \
            self.__size(node.right)
        return node

    def __str__(self):
        if self.__root is not None:
            return "{" + self.__str(self.__root)[:-2] + "}"
        return "{}"

    def __contains__(self, key):
        node = self.__root

        while node is not None:
            if self.__key(key) == self.__key(node.data):
                return True
            elif self.__key(key) < self.__key(node.data):
                node = node.left
            else:
                node = node.right
        return False

    def __inorder(self, node, items):
        if node is None:
            return
        self.__inorder(node.left, items)
        items.extend([node.data for _ in range(node.count)])
        self.__inorder(node.right, items)

    def insert(self, data):
        self.__root = self.__insert(self.__root, data)

    def min(self):
        if self.__root is not None:
            return self.__min(self.__root).data
        return None

    def max(self):
        if self.__root is not None:
            return self.__max(self.__root).data
        return None

    def floor(self, key):
        floor = self.__floor(self.__root, key)
        return floor.data if floor is not None else None

    def ceiling(self, key):
        ceiling = self.__ceiling(self.__root, key)
        return ceiling.data if ceiling is not None else None

    def rank(self, key):
        return self.__rank(self.__root, key)

    def count(self, key):
        node = self.__root

        while node is not None:
            if self.__key(key) == self.__key(node.data):
                return node.count
            elif self.__key(key) < self.__key(node.data):
                node = node.left
            else:
                node = node.right

        return 0

    def delete_min(self, delete_all=True):
        if self.__root is not None:
            self.__root = self.__delete_min(self.__root, delete_all)

    def delete_max(self, delete_all=True):
        if self.__root is not None:
            self.__root = self.__delete_max(self.__root, delete_all)

    def delete(self, key, delete_all=True):
        self.__root = self.__delete(self.__root, key, delete_all)

    def size(self):
        return self.__size(self.__root)

    def clear(self):
        self.__root = None

    def items(self):
        items = []
        self.__inorder(self.__root, items)
        return items
