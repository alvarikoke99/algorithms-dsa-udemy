from .graph import Graph, GraphNode, GraphNodeStatus, DepthFirstSearch, BreadthFirstSearch


def reset_nodes(graph: Graph) -> None:
    for node in graph.nodes.values():
        node.status = GraphNodeStatus.UNVISITED


def search_test(graph: Graph, target: str) -> bool:
    dfs = DepthFirstSearch.depth_first_search(graph, target)
    reset_nodes(graph)
    bfs = DepthFirstSearch.depth_first_search(graph, target)
    reset_nodes(graph)
    return dfs and bfs and dfs == bfs


def test_search():
    family = Graph()
    family.add_edge("daniel", "maria")
    family.add_edge("daniel", "pedro")
    family.add_edge("maria", "javier")
    family.add_edge("lucia", "javier")

    assert search_test(family, "daniel")
    assert search_test(family, "maria")
    assert search_test(family, "pedro")
    assert search_test(family, "javier")
    assert search_test(family, "lucia")

    assert not search_test(family, "juan")
