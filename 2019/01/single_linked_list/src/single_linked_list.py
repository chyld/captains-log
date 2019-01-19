from src.node import Node


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def prepend(self, val):
        if self.is_empty():
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val, self.head)
            self.head = node

    def __str__(self):
        if self.is_empty():
            return ""
        return self.traverse(self.head)

    def traverse(self, node):
        if not node.nxt:
            return node.val
        return f"{node.val} -> {self.traverse(node.nxt)}"

    def append(self, val):
        if self.is_empty():
            self.prepend(val)
        else:
            self.tail.nxt = Node(val)
            self.tail = self.tail.nxt
