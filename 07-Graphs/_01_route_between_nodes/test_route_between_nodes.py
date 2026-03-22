from route_between_nodes import Graph, GraphNode, GraphNodeStatus, RouteBetweenNodes


def clear(graph: Graph) -> None:
    for n in graph.nodes.values():
        n.status = GraphNodeStatus.UNVISITED


def test_route_between_nodes():
    route_between_nodes = RouteBetweenNodes()

    graph = Graph()

    node0 = graph.get_or_create_node("0")
    node1 = graph.get_or_create_node("1")
    node3 = graph.get_or_create_node("3")
    node4 = graph.get_or_create_node("4")
    node6 = graph.get_or_create_node("6")

    graph.add_edge("0", "1")
    graph.add_edge("1", "2")
    graph.add_edge("2", "0")
    graph.add_edge("2", "3")
    graph.add_edge("3", "2")
    graph.add_edge("4", "6")
    graph.add_edge("5", "4")
    graph.add_edge("6", "5")

    assert route_between_nodes.is_route_between(graph, node0, node3)
    clear(graph)
    assert route_between_nodes.is_route_between(graph, node3, node0)
    clear(graph)
    assert route_between_nodes.is_route_between(graph, node6, node4)
    clear(graph)
    assert route_between_nodes.is_route_between(graph, node1, node0)
    clear(graph)
    assert not route_between_nodes.is_route_between(graph, node0, node4)
    clear(graph)

    graph2 = Graph()
    graph2.add_edge("4", "1")
    graph2.add_edge("4", "3")
    graph2.add_edge("3", "2")
    graph2.add_edge("2", "1")

    node0 = graph2.get_or_create_node("0")
    node1 = graph2.get_or_create_node("1")
    node2 = graph2.get_or_create_node("2")
    node3 = graph2.get_or_create_node("3")
    node4 = graph2.get_or_create_node("4")

    assert not route_between_nodes.is_route_between(graph2, node2, node4)
    clear(graph2)
    assert route_between_nodes.is_route_between(graph2, node3, node1)
    clear(graph2)
    assert not route_between_nodes.is_route_between(graph2, node0, node1)
    clear(graph2)
    assert route_between_nodes.is_route_between(graph2, node0, node0)
    clear(graph2)
