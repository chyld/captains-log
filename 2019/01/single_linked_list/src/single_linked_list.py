from src.node import Node


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def prepend(self, val):
        self.size += 1
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
        return self._traverse(self.head)

    def _traverse(self, node):
        if not node.nxt:
            return node.val
        return f"{node.val} -> {self._traverse(node.nxt)}"

    def append(self, val):
        self.size += 1
        if self.is_empty():
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = Node(val)
            self.tail = self.tail.nxt

    def __len__(self):
        return self.size

    def reverse(self):
        sll = SingleLinkedList()
        if not self.is_empty():
            node = self.head
            while node:
                sll.prepend(node.val)
                node = node.nxt
        return sll
