class Queue:
    def __init__(self, n):
        self.__N = n
        self.__front_pointer = 0
        self.__back_pointer = 0
        self.__array = list(range(self.__N + 1))
        for i in range(len(self.__array)):
            self.__array[i] = None

    def len(self):
        return self.__N

    def __str__(self):
        return str(self.__array)

    def enqueue(self, value):
        if (self.__back_pointer + 1) % (self.len() + 1) == (self.__front_pointer % (self.len() + 1)):
            print("The Queue has run out of space")
        else:
            self.__array[self.__back_pointer] = value
            self.__back_pointer += 1
            self.__back_pointer = self.__back_pointer % (self.len() + 1)

    def dequeue(self):
        if self.__front_pointer == self.__back_pointer:
            print("The queue is empty.")
        else:
            value = self.__array[self.__front_pointer]
            self.__array[self.__front_pointer] = None
            self.__front_pointer += 1
            self.__front_pointer = self.__front_pointer % (self.len() + 1)
            return value