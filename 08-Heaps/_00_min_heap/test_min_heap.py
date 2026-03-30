from .min_heap import MinHeap


def test_min_heap():
    min_heap = MinHeap(20)
    min_heap.insert(5)
    min_heap.insert(10)
    min_heap.insert(12)
    min_heap.print_heap()
    min_heap.insert(3)
    min_heap.print_heap()
    min_heap.insert(9)
    min_heap.insert(15)
    min_heap.insert(1)
    min_heap.print_heap()

    assert min_heap.extract_min() == 1
    assert min_heap.extract_min() == 3
    assert min_heap.extract_min() == 5
    assert min_heap.extract_min() == 9
    assert min_heap.extract_min() == 10
    assert min_heap.extract_min() == 12
    assert min_heap.extract_min() == 15
