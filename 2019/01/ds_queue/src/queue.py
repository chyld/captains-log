"""Queue."""


class Queue:
    """Queue."""

    def __init__(self):
        """init."""
        self.data = []

    def is_empty(self):
        """is_empty."""
        return len(self.data) == 0

    def enqueue(self, val):
        """enqueue."""
        self.data.append(val)

    def peek(self):
        """peek."""
        if len(self.data) > 0:
            return self.data[0]

    def dequeue(self):
        """dequeue."""
        if len(self.data) > 0:
            val = self.data[0]
            self.data = self.data[1:]
            return val
