# test watcher
# chokidar "**/*.py" -c "clear && pytest -v -s"

import pytest

from src.single_linked_list import SingleLinkedList


@pytest.fixture
def sll():
    sll = SingleLinkedList()
    sll.append(3)
    sll.append(5)
    sll.append(7)
    return sll


def test_create():
    sll = SingleLinkedList()
    assert isinstance(sll, SingleLinkedList)
    assert sll.head is None
    assert sll.tail is None


def test_prepend():
    sll = SingleLinkedList()
    sll.prepend(3)
    sll.prepend(2)
    sll.prepend(1)
    assert str(sll) == "1 -> 2 -> 3"


def test_append():
    sll = SingleLinkedList()
    sll.append(4)
    sll.append(5)
    sll.append(6)
    assert str(sll) == "4 -> 5 -> 6"


def test_reverse(sll):
    assert str(sll) == "3 -> 5 -> 7"
    sll = sll.reverse()
    assert str(sll) == "7 -> 5 -> 3"


def test_len(sll):
    assert len(sll) == 3


def test_find(sll):
    assert sll.find(2) is None
    assert sll.find(3).val == 3
