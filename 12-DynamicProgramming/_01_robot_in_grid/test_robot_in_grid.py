from robot_in_grid import Cell, RobotInGrid


def test_robot_in_grid():
    r = RobotInGrid()

    grid = [
        [True, True, True, True],
        [False, False, False, True],
        [True, True, False, True],
        [True, True, False, True],
    ]

    expected_path = [
        Cell(0, 0),
        Cell(0, 1),
        Cell(0, 2),
        Cell(0, 3),
        Cell(1, 3),
        Cell(2, 3),
        Cell(3, 3),
    ]
    cells = r.get_path(grid)
    assert cells == expected_path

    grid2 = [
        [True, True, True, True],
        [False, True, True, True],
        [True, True, False, False],
        [True, True, True, True],
    ]

    expected_path2 = [
        Cell(0, 0),
        Cell(0, 1),
        Cell(1, 1),
        Cell(2, 1),
        Cell(3, 1),
        Cell(3, 2),
        Cell(3, 3),
    ]
    cells2 = r.get_path(grid2)
    assert cells2 == expected_path2
