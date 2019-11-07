class Stack:
    # This is a stack data structure implemented using
    # Python's built in List.

    def __init__(self, N):
        self.__N = N
        self.__pointer = 0
        self.__array = list(range(N))
        for i in range(N):
            self.__array[i] = None

    def len(self):
        return self.__N

    def __str__(self):
        return str(self.__array)

    def isEmpty(self):
        return self.__pointer == 0

    def isFull(self):
        return self.__pointer == self.__N

    def push(self, value):
        if self.__pointer == self.__N:
            print("Stack is full. Push operation not allowed.")
        elif self.__pointer > self.__N:
            print("How did the pointer even get here?")
        else:
            self.__array[self.__pointer] = value
            self.__pointer += 1

    def pop(self):
        if self.__pointer == 0:
            print("Stack is empty. Pop operation is not allowed.")
            return None
        elif self.__pointer < 0:
            print("How did the pointer even get here?")
            return None
        else:
            self.__pointer -= 1
            value = self.__array[self.__pointer]
            self.__array[self.__pointer] = None
            return value
        
    def peek(self):
        return self.__array[self.__pointer - 1]
