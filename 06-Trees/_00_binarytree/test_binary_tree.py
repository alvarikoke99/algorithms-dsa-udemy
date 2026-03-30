"""
         1
     2       3
  4     5      6
7     8
"""
from .binary_tree import BinaryTreeTraversals, Node


def test_traversals(capsys):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(6)

    root.left.left.left = Node(7)

    root.left.right.left = Node(8)

    print("IN-ORDER TRAVERSAL: ", end="")
    BinaryTreeTraversals.in_order_traversal(root)
    print()

    print("PRE-ORDER TRAVERSAL: ", end="")
    BinaryTreeTraversals.pre_order_traversal(root)
    print()

    print("POST-ORDER TRAVERSAL: ", end="")
    BinaryTreeTraversals.post_order_traversal(root)
    print()

    captured = capsys.readouterr()
    assert "IN-ORDER TRAVERSAL:" in captured.out
    assert "PRE-ORDER TRAVERSAL:" in captured.out
    assert "POST-ORDER TRAVERSAL:" in captured.out
