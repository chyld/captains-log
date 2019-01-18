"""test queue."""
from src.queue import Queue


def test_create():
    """Test Constructor."""
    q = Queue()
    assert isinstance(q, Queue)
    assert len(q.data) == 0
