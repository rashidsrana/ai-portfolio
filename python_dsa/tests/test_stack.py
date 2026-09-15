import pytest
from python_dsa.stack import Stack


def test_push_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10


def test_peek():
    s = Stack()
    s.push(5)
    assert s.peek() == 5


def test_empty_pop():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
