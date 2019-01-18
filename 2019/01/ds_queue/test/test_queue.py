"""test queue."""
from src.queue import Queue


def test_create():
    """Test Constructor."""
    q = Queue()
    assert isinstance(q, Queue)
    assert len(q.data) == 0


def test_empty():
    """Test is_empty."""
    q = Queue()
    assert q.is_empty()


def test_enqueue():
    """Test enqueue."""
    q = Queue()
    q.enqueue(3)
    assert not q.is_empty()


def test_peek():
    """Test peek."""
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    assert q.peek() == 3
    assert q.peek() == 3
    assert q.peek() == 3


def test_dequeue():
    """Test dequeue."""
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    assert q.dequeue() == 3
    assert q.dequeue() == 5
    assert q.dequeue() == 7
    assert q.dequeue() is None
