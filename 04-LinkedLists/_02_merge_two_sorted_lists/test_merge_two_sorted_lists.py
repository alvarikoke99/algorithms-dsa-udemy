from single_linked_list import Node
from .merge_two_sorted_lists import MergeTwoSortedLists


def test_merge_two_sorted_lists():
    merge = MergeTwoSortedLists()
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(4)
    list1.next.next.next = Node(6)

    list2 = Node(2)
    list2.next = Node(3)
    list2.next.next = Node(5)

    result = merge.merge_two_lists(list1, list2)
    assert result.value == 1
    assert result.next.value == 2
    assert result.next.next.value == 2
    assert result.next.next.next.value == 3
    assert result.next.next.next.next.value == 4
    assert result.next.next.next.next.next.value == 5
    assert result.next.next.next.next.next.next.value == 6
