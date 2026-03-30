from collections import deque
from .sort_stack import SortStack


def test_sort_stack():
    sort_stack = SortStack()

    stack = deque()
    stack.append(1)
    stack.append(5)
    stack.append(2)
    stack.append(4)
    sorted_stack = sort_stack.sort(stack)

    assert sorted_stack.pop() == 1
    assert sorted_stack.pop() == 2
    assert sorted_stack.pop() == 4
    assert sorted_stack.pop() == 5
