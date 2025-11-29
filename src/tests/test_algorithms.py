from src.algorithms import merge_sort, insertion_sort

if __name__ == "__main__":
    assert insertion_sort([3, 7, 5, 1, 2]) == [1, 2, 3, 5, 7]
    assert insertion_sort([3, 7, -5, 1, 2]) == [-5, 1, 2, 3, 7]
    assert insertion_sort([3, 7, 3, 1, 2]) == [1, 2, 3, 3, 7]

    assert merge_sort([3, 7, 5, 1, 2]) == [1, 2, 3, 5, 7]
    assert merge_sort([3, 7, -5, 1, 2]) == [-5, 1, 2, 3, 7]
    assert merge_sort([3, 7, 3, 1, 2]) == [1, 2, 3, 3, 7]
