from SingleLinkedLists import LinkedList

class QueueFromLL():
    # My simple implementation of a queue using a linked
    # list. Enqueues new elements at the tail of the
    # linked list, and dequeues/peeks elements at the
    # head. Needs to traverse the whole list to enqueue
    # new elements.


    def __init__(self):
        self.__linked_list = LinkedList()

    def peek(self):
        return self.__linked_list.retrieve(0)

    def enqueue(self, value):
        self.__linked_list.add(value)

    def dequeue(self):
        value = self.__linked_list.retrieve(0)
        self.__linked_list.remove(0)
        return value

    def __str__(self):
        return self.__linked_list.__str__()


def main():
    queue = QueueFromLL()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(9)
    queue.enqueue(16)
    queue.enqueue(25)
    print(queue)
    queue.enqueue(36)
    queue.enqueue(49)
    queue.enqueue(64)
    print(queue)
    print(queue.peek())
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue)


if __name__ == "__main__":
    main()