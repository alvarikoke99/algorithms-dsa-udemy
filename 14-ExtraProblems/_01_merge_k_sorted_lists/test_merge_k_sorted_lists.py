from merge_k_sorted_lists import Node, MergeKSortedLists


def test_merge_k_sorted_lists():
    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    l3 = Node(2)
    l3.next = Node(6)

    merged = MergeKSortedLists().merge_k_lists([l1, l2, l3])

    assert merged.value == 1
    assert merged.next.value == 1
    assert merged.next.next.value == 2
    assert merged.next.next.next.value == 3
    assert merged.next.next.next.next.value == 4
    assert merged.next.next.next.next.next.value == 4
    assert merged.next.next.next.next.next.next.value == 5
    assert merged.next.next.next.next.next.next.next.value == 6
