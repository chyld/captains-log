from src.stack import Stack


def test_create():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s.data) == 0


def test_is_empty():
    s = Stack()
    assert s.is_empty()


def test_push():
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(7)
    assert len(s.data) == 3
    assert not s.is_empty()


def test_pop():
    s = Stack()
    s.push(3)
    assert s.pop() == 3


def test_peek():
    s = Stack()
    s.push(3)
    assert s.peek() == 3
