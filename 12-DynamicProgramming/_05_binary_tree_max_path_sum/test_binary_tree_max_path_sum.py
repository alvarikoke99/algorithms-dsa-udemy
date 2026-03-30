from .binary_tree_max_path_sum import BinaryTreeMaxPathSum, TreeNode


def test_binary_tree_max_path_sum():
    sum_ = BinaryTreeMaxPathSum()

    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.left.left = TreeNode(-5)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(-1)
    assert sum_.max_path_sum(root1) == 6

    root2 = TreeNode(-12)
    root2.left = TreeNode(5)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(4)
    assert sum_.max_path_sum(root2) == 8
