from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.put(value)

        while not self.q1.empty():
            self.q2.put(self.q1.get())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return None

        return self.q1.get()

# Test case
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None
