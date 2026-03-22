import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from swap_nodes_in_pairs import SwapNodesInPairs


def test_swap_nodes_in_pairs():
    swap = SwapNodesInPairs()
    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(4)
    lst.next.next.next = Node(6)
    lst.next.next.next.next = Node(8)

    result = swap.swap_nodes_in_pairs(lst)

    assert result.value == 2
    assert result.next.value == 1
    assert result.next.next.value == 6
    assert result.next.next.next.value == 4
    assert result.next.next.next.next.value == 8
