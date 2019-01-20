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
        return SingleLinkedList._traverse(self.head)

    @staticmethod
    def _traverse(node):
        if not node.nxt:
            return str(node.val)
        return f"{node.val} -> {SingleLinkedList._traverse(node.nxt)}"

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

    def find(self, val):
        if not self.is_empty():
            return SingleLinkedList._find(self.head, val)

    @staticmethod
    def _find(node, val):
        if node.val == val:
            return node
        elif not node.nxt:
            return None
        else:
            return SingleLinkedList._find(node.nxt, val)

    def delete(self, val):
        if self.is_empty():
            return

        if self.head.val == val:
            self._delete_head()
            return

        node = self.head
        while node.nxt:
            prev = node
            node = node.nxt
            if node.val == val:
                self._delete_body(prev)

    def _delete_head(self):
        self.head = self.head.nxt

    def _delete_body(self, prev):
        prev.nxt = prev.nxt.nxt
