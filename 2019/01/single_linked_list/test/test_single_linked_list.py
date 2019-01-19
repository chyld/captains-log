# test watcher
# chokidar "**/*.py" -c "clear && pytest -v -s"

from src.single_linked_list import SingleLinkedList


def test_create():
    sll = SingleLinkedList()
    assert isinstance(sll, SingleLinkedList)
    assert sll.head is None
    assert sll.tail is None


def test_prepend():
    sll = SingleLinkedList()
    sll.prepend(3)
    assert sll.head is sll.tail
    assert sll.head.val == 3
    assert sll.head.nxt is None
    sll.prepend(2)
    assert sll.head is not sll.tail
    assert sll.head.val == 2
    assert sll.head.nxt.val == 3
    assert sll.tail.val == 3
    assert sll.tail.nxt is None
    sll.prepend(1)
    assert str(sll) == "1 -> 2 -> 3"
