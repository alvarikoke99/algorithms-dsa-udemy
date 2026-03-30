from collections import deque
from .sort_stack import SortStack


def test_sort_stack():
    sort_stack = SortStack()

    stack = deque()
    stack.appendleft(1)
    stack.appendleft(5)
    stack.appendleft(2)
    stack.appendleft(4)
    sorted_stack = sort_stack.sort(stack)

    assert sorted_stack.popleft() == 1
    assert sorted_stack.popleft() == 2
    assert sorted_stack.popleft() == 4
    assert sorted_stack.popleft() == 5
