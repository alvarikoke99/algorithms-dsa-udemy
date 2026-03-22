import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from remove_dups import RemoveDups


def test_remove_dups():
    remove_dups = RemoveDups()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(1)

    remove_dups.remove_dups(head)

    assert head.value == 1
    assert head.next.value == 2
    assert head.next.next.value == 3
    assert head.next.next.next.value == 4
    assert head.next.next.next.next is None
