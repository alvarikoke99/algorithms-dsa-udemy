from reverse_nodes_k_group import ListNode, ReverseNodesKGroup


def test_reverse_nodes_k_group():
    reverse = ReverseNodesKGroup()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(6)
    node.next.next.next.next.next.next = ListNode(7)

    new_head = reverse.reverse_k_group(node, 4)

    assert new_head.val == 4
    assert new_head.next.val == 3
    assert new_head.next.next.val == 2
    assert new_head.next.next.next.val == 1
    assert new_head.next.next.next.next.val == 5
    assert new_head.next.next.next.next.next.val == 6
    assert new_head.next.next.next.next.next.next.val == 7
