import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from nth_node_to_last import NthNodeToLast


def test_nth_node_to_last():
    nth_node = NthNodeToLast()
    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(4)
    lst.next.next.next = Node(6)

    assert nth_node.nth_node_to_last(lst, 1).value == 6
    assert nth_node.nth_node_to_last(lst, 2).value == 4
    assert nth_node.nth_node_to_last(lst, 3).value == 2
    assert nth_node.nth_node_to_last(lst, 4).value == 1
    assert nth_node.nth_node_to_last(lst, 5) is None
