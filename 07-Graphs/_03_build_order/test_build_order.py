import pytest
from .build_order import BuildOrder


def test_build_order():
    build_order = BuildOrder()

    projects = ["a", "b", "c", "d"]
    dependencies = [["a", "b"], ["a", "c"], ["a", "d"], ["c", "b"], ["d", "b"], ["d", "c"]]

    result = build_order.build_order(projects, dependencies)
    assert result == ["a", "d", "c", "b"]

    cycle_dependencies = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "a"]]

    with pytest.raises(Exception):
        build_order.build_order(projects, cycle_dependencies)
