from SingleLinkedLists import LinkedList

class StackFromLL():
    # This is a stack data structure implemented using
    # a linked list rather than relying on built-in Lists.
    # It inserts new elements at the head of the linked
    # list and removes popped elements from the head to
    # simulate Last-In, First-Out behaviour.


    def __init__(self):
        self.__linked_list = LinkedList()

    def peek(self):
        return self.__linked_list.retrieve(0)

    def push(self, value):
        self.__linked_list.insert(0, value)

    def pop(self):
        value = self.__linked_list.retrieve(0)
        self.__linked_list.remove(0)
        return value

    def __str__(self):
        return self.__linked_list.__str__()