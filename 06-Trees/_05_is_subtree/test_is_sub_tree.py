from .is_sub_tree import IsSubTree, Node


def test_is_sub_tree():
    is_sub_tree = IsSubTree()
    first = Node(4)
    first.left = Node(5)
    first.right = Node(7)
    first.left.left = Node(1)
    first.left.right = Node(3)
    first.left.left.left = Node(8)

    second = Node(5)
    second.left = Node(1)
    second.right = Node(3)
    second.left.left = Node(8)
    assert is_sub_tree.is_subtree(first, second)

    second.right.right = Node(12)
    assert not is_sub_tree.is_subtree(first, second)
