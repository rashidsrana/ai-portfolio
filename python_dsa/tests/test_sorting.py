from python_dsa.sorting import bubble_sort, quick_sort


def test_bubble_sort():
    arr = [5, 3, 8, 1]
    assert bubble_sort(arr.copy()) == [1, 3, 5, 8]


def test_quick_sort():
    arr = [10, -1, 2, 5]
    assert quick_sort(arr.copy()) == [-1, 2, 5, 10]
