class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value

    def link(self, new_node):
        self.__next = new_node

    def next(self):
        return self.__next

    def __str__(self):
        return str((self.__value, self.__next))


class LinkedList:
    def __init__(self):
        self.head = None

    def len(self):
        if self.head == None:
            return 0
        else:
            length = 1
            current_node = self.head
            while current_node.next():
                length += 1
                current_node = current_node.next()
            return length

    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next():
                current_node = current_node.next()
            current_node.link(Node(value))

    def insert(self, index, value):
        if self.head == None:
            self.add(value)
        if index < 0:
            print("Index out of bounds")
            return None
        elif index == 0:
            inserted_node = Node(value)
            next_node = self.head
            inserted_node.link(next_node)
            self.head = inserted_node
        else:
            current_node = self.head
            inserted_node = Node(value)
            for _ in range(index - 1):
                if current_node.next() == None:
                    print("Index out of bounds")
                    return None
                current_node = current_node.next()
            next_node = current_node.next()
            current_node.link(inserted_node)
            inserted_node.link(next_node)

    def remove(self, index):
        if index == 0:
            new_head = self.head.next()
            self.head = new_head
        else:
            current_node = self.head
            previous_node = None
            for _ in range(index):
                if current_node.next() == None:
                    print("Index out of bounds")
                    return None
                previous_node = current_node
                current_node = current_node.next()
            previous_node.link(current_node.next())

    def retrieve(self, index):
        if self.head == None:
            return None
        else:
            current_node = self.head
            for _ in range(index):
                if current_node.next() == None:
                    print("Index out of bounds")
                    return None
                current_node = current_node.next()
            return current_node.get_value()

    def find(self, value):
        current_node = self.head
        i = 0
        while current_node:
            if current_node.next() == None:
                print("The requested element was not found in this linked list")
                return None
            if current_node.get_value() == value:
                return i
            else:
                current_node = current_node.next()
                i += 1

    def __str__(self):
        if self.head == None:
            return str(None)
        else:
            linked_string = "| "
            current_node = self.head
            while current_node:
                linked_string += str(current_node.get_value()) + " -> "
                current_node = current_node.next()
            linked_string += str(None) + " |"
            return linked_string