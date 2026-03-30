from .house_robber import HouseRobber


def test_house_robber():
    h = HouseRobber()

    assert h.rob([1, 2, 3, 1]) == 4
    assert h.rob([2, 14, 8, 3, 4]) == 18
