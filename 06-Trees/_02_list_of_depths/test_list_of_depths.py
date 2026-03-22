from list_of_depths import ListOfDepths, Node


def test_list_of_depths():
    list_of_depths = ListOfDepths()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    result = list_of_depths.list_of_depths(root)

    assert result[0][0].value == 4
    assert result[1][0].value == 2
    assert result[1][1].value == 7
    assert result[2][0].value == 1
    assert result[2][1].value == 3
    assert result[2][2].value == 6
    assert result[2][3].value == 9
