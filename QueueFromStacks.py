from Stacks import Stack

class Queue2():
    def __init__(self, N):
        self.N = N
        self.stack1 = Stack(N)
        self.stack2 = Stack(N)

    def __str__(self):
        return str(self.stack1) + "\n" + str(self.stack2)

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def isFull(self):
        return self.stack1.isFull() and self.stack2.isFull()

    def enqueue(self, value):
        if self.isFull():
            print("The queue is full.")
        elif self.isEmpty():
            self.stack1.push(value)
        else:
            while not self.stack1.isEmpty():
                temporary = self.stack1.pop()
                self.stack2.push(temporary)

            self.stack1.push(value)

            while not self.stack2.isEmpty():
                temporary = self.stack2.pop()
                self.stack1.push(temporary)

    def dequeue(self):
        return self.stack1.pop()