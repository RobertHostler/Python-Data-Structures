class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    def get_value(self):
        return self.__value

    def link(self, first_node, second_node):
        self.__previous = first_node
        self.__next = second_node

        first_node.__next = self
        second_node.__previous = self

    def next(self):
        return self.__next

    def __str__(self):
        return str((self.__value, self.__next))