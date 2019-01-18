from src.node import Node


def test_node():
    n1 = Node(3)
    assert n1.val == 3
    assert n1.nxt is None
    n2 = Node(5, Node(7))
    assert n2.val == 5
    assert n2.nxt is not None
