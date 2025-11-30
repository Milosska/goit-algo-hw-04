from src.algorithms import merge_sort, insertion_sort
from src.helpers import merge_k_lists

if __name__ == "__main__":
    assert insertion_sort([3, 7, 5, 1, 2]) == [1, 2, 3, 5, 7]
    assert insertion_sort([3, 7, -5, 1, 2]) == [-5, 1, 2, 3, 7]
    assert insertion_sort([3, 7, 3, 1, 2]) == [1, 2, 3, 3, 7]

    assert merge_sort([3, 7, 5, 1, 2]) == [1, 2, 3, 5, 7]
    assert merge_sort([3, 7, -5, 1, 2]) == [-5, 1, 2, 3, 7]
    assert merge_sort([3, 7, 3, 1, 2]) == [1, 2, 3, 3, 7]

    assert merge_k_lists([[1, 2, 7], [-33, 2, 8], [4, 6, 55]]) == [
        -33,
        1,
        2,
        2,
        4,
        6,
        7,
        8,
        55,
    ]
    assert merge_k_lists([[-5, 67, 176], [-339, -52, -8], [4, 55, 55, 57]]) == [
        -339,
        -52,
        -8,
        -5,
        4,
        55,
        55,
        57,
        67,
        176,
    ]
