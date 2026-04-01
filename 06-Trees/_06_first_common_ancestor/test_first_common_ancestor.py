from .first_common_ancestor import FirstCommonAncestor, Node


def test_first_common_ancestor():
    fca = FirstCommonAncestor()
    root = Node(4)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.left.left = Node(8)

    assert fca.first_common_ancestor(root, root.left.left.left, root.right).value == 4 # 8 y 7
    assert fca.first_common_ancestor(root, root.left.left, root.left.right).value == 5 # 1 y 3
    assert fca.first_common_ancestor(root, root, root.right) is None # 4 y 7
