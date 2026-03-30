from .maximum_depth import MaximumDepth, Node


def test_max_depth():
    max_depth = MaximumDepth()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    assert max_depth.max_depth(root) == 3
    root.left.left.left = Node(8)
    assert max_depth.max_depth(root) == 4
