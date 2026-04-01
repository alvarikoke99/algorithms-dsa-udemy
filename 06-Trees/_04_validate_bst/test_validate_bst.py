from .validate_bst import Node, ValidateBST


def test_validate_bst():
    validate_bst = ValidateBST()
    root = Node(4)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.left.left = Node(8)
    
    print(validate_bst.is_valid_bst(root))
    assert not validate_bst.is_valid_bst(root)

    root.left.value = 2
    root.left.left.left = None
    print(validate_bst.is_valid_bst(root))
    assert validate_bst.is_valid_bst(root)
