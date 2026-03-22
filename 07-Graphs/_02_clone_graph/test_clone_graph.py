from clone_graph import Node, CloneGraph


def test_clone_graph():
    clone_graph = CloneGraph()

    node1 = Node()
    node1.val = 1
    node2 = Node()
    node2.val = 2
    node3 = Node()
    node3.val = 3
    node4 = Node()
    node4.val = 4

    node1.neighbors = [node2, node3]
    node2.neighbors = [node3]
    node3.neighbors = [node4]
    node4.neighbors = [node2]

    cloned_node1 = clone_graph.clone_graph(node1)
    cloned_node2 = cloned_node1.neighbors[0]
    cloned_node3 = cloned_node1.neighbors[1]
    cloned_node4 = cloned_node3.neighbors[0]

    assert cloned_node1.val == 1
    assert node1 is not cloned_node1
    assert cloned_node2.val == 2
    assert node2 is not cloned_node2
    assert cloned_node3.val == 3
    assert node3 is not cloned_node3
    assert cloned_node4.val == 4
    assert node4 is not cloned_node4
