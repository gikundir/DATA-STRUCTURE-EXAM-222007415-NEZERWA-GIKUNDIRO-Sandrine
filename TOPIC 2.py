class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return None
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = self.rear = -1
            return data
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return data

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Queue contents:", end=" ")
            if self.rear >= self.front:
                print(*self.queue[self.front : self.rear + 1])
            else:
                print(*self.queue[self.front :], *self.queue[: self.rear + 1])

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def display(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            print("Stack contents:",self.stack)




cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(50)
cq.enqueue(60)
cq.display()


stack = Stack()
stack.push(16)
stack.push(78)
stack.push(29)
stack.display()
print("Popped:", stack.pop())
stack.display()
