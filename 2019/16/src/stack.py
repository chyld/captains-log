class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
