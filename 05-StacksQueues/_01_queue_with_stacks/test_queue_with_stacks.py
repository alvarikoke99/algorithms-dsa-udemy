import pytest
from .queue_with_stacks import QueueWithStacks


def test_queue_with_stacks():
    queue_with_stacks = QueueWithStacks()

    assert queue_with_stacks.size() == 0
    queue_with_stacks.add(1)
    queue_with_stacks.add(2)
    queue_with_stacks.add(3)
    assert queue_with_stacks.remove() == 1
    assert queue_with_stacks.peek() == 2
    assert queue_with_stacks.size() == 2
    queue_with_stacks.add(4)
    assert not queue_with_stacks.is_empty()
    assert queue_with_stacks.remove() == 2
    assert queue_with_stacks.remove() == 3
    assert queue_with_stacks.remove() == 4
    assert queue_with_stacks.is_empty()
