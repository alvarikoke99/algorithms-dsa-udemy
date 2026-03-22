from bubble_sort import BubbleSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from selection_sort import SelectionSort

array = [8, 4, 0, 3, 6, 1, 7, 19, 12, 2]
expected_array = [0, 1, 2, 3, 4, 6, 7, 8, 12, 19]


def test_bubble_sort():
    array_cp = array.copy()
    BubbleSort.sort(array_cp)
    assert array_cp == expected_array


def test_selection_sort():
    array_cp = array.copy()
    SelectionSort.sort(array_cp)
    assert array_cp == expected_array


def test_merge_sort():
    array_cp = array.copy()
    MergeSort.sort(array_cp)
    assert array_cp == expected_array


def test_quick_sort():
    array_cp = array.copy()
    QuickSort.sort(array_cp)
    assert array_cp == expected_array
