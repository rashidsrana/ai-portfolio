import pytest
from python_dsa.queue_ds import Queue


def test_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2


def test_peek():
    q = Queue()
    q.enqueue(10)
    assert q.peek() == 10


def test_empty_dequeue():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
