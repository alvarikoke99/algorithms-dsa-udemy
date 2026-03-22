from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinaryTreeTraversals:
    @staticmethod
    def in_order_traversal(node: Optional[Node]) -> None:
        if node is not None:
            BinaryTreeTraversals.in_order_traversal(node.left)
            print(node.value, end=" ")
            BinaryTreeTraversals.in_order_traversal(node.right)

    @staticmethod
    def pre_order_traversal(node: Optional[Node]) -> None:
        if node is not None:
            print(node.value, end=" ")
            BinaryTreeTraversals.pre_order_traversal(node.left)
            BinaryTreeTraversals.pre_order_traversal(node.right)

    @staticmethod
    def post_order_traversal(node: Optional[Node]) -> None:
        if node is not None:
            BinaryTreeTraversals.post_order_traversal(node.left)
            BinaryTreeTraversals.post_order_traversal(node.right)
            print(node.value, end=" ")
