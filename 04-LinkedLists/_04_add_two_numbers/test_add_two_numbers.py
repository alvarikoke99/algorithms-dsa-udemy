import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from add_two_numbers import AddTwoNumbers


def test_add_two_numbers():
    add = AddTwoNumbers()
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(4)
    list1.next.next.next = Node(6)

    list2 = Node(5)
    list2.next = Node(2)
    list2.next.next = Node(8)

    result = add.add_two_numbers(list1, list2)

    assert result.value == 6
    assert result.next.value == 4
    assert result.next.next.value == 2
    assert result.next.next.next.value == 7

    list1.next.next.next = None
    result = add.add_two_numbers(list1, list2)

    assert result.value == 6
    assert result.next.value == 4
    assert result.next.next.value == 2
    assert result.next.next.next.value == 1
