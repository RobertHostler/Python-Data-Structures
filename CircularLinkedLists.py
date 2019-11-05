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
        self.tail = None

    def add_head(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            # does not need to traverse the whole list anymore
            current_node = self.head
            while current_node.next() != None:
                current_node = current_node.next()
            current_node.link(Node(value))

    def add_tail(self, value):
        new_tail = Node(value)
        if self.tail == None:
            self.tail = new_tail
            self.head.link(self.tail)
        else:
            self.tail.link(new_tail)

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

            for i in range(index - 1):
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
            for i in range(index):
                if current_node.next() == None:
                    print("Index out of bounds")
                    return None
                previous_node = current_node
                current_node = current_node.next()
            previous_node.link(current_node.next())

    def find(self, value):
        current_node = self.head
        i = 0
        while current_node != None:
            if current_node.get_value() == value:
                break
            else:
                current_node = current_node.next()
                i += 1
        if current_node == None:
            return -1
        else:
            return i

    def __str__(self):
        if self.head == None:
            return str(None)
        else:
            linked_string = "| "
            current_node = self.head
            while current_node != None:
                linked_string += str(current_node.get_value()) + " -> "
                current_node = current_node.next()
            linked_string += str(None) + " |"
            return linked_string