import pytest
from python_dsa.linked_list import LinkedList


def test_insert_and_display():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    assert ll.display() == [10, 20, 30]


def test_delete():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.delete(20)
    assert ll.display() == [10, 30]


def test_search():
    ll = LinkedList()
    ll.insert(5)
    assert ll.search(5) is True
    assert ll.search(99) is False
