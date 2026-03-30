from .invert_binary_tree import InvertBinaryTree, Node


def test_invert_binary_tree():
    invert_binary_tree = InvertBinaryTree()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    new_root = invert_binary_tree.invert_tree(root)
    assert new_root.value == 4
    assert new_root.left.value == 7
    assert new_root.right.value == 2
    assert new_root.left.left.value == 9
    assert new_root.left.right.value == 6
    assert new_root.right.left.value == 3
    assert new_root.right.right.value == 1
