"""Stack."""


class Stack:
    """Stack."""

    def __init__(self):
        """init."""
        self.data = []

    def is_empty(self):
        """is_empty."""
        return len(self.data) == 0

    def push(self, val):
        """push."""
        self.data.append(val)

    def pop(self):
        """pop."""
        if not self.is_empty():
            return self.data.pop()

    def peek(self):
        """peek."""
        if not self.is_empty():
            return self.data[-1]
