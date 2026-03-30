from .stack_min import StackMin


def test_stack_min():
    stack_min = StackMin()

    stack_min.push(3)
    stack_min.push(1)
    stack_min.push(2)

    assert stack_min.min() == 1
    stack_min.pop()
    assert stack_min.min() == 1
    stack_min.pop()
    assert stack_min.min() == 3
    stack_min.push(0)
    assert stack_min.min() == 0
