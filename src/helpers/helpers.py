import timeit
from typing import Callable

from src.algorithms import merge_sort, insertion_sort, merge


def measure_sort_time(
    results: dict[str, float], sort_func: Callable, array: list[int]
) -> None:
    # Insertion Sort
    measured_func = timeit.timeit(stmt=lambda: sort_func(array.copy()), number=1)
    results[sort_func.__name__] = measured_func


def compare_algorithms_for_array(array: list[int]) -> None:
    results: dict[str, float] = {}

    # Insertion Sort
    measure_sort_time(results, insertion_sort, array)

    # Merge Sort
    measure_sort_time(results, merge_sort, array)

    # Python Timsort
    measure_sort_time(results, sorted, array)

    for key, time in results.items():
        print(f" -- Array is sorted by {key} during {time} seconds.")


def run_all_scenarios_for_array(array: list[int], type: str) -> None:
    print(f"\n Sorting {type} random numbers array of {len(array)} length.")

    sorted_array = sorted(array)
    reversed_array = sorted_array[::-1]

    scenarios = [
        ("unsorted array (average case)", array),
        ("sorted array (best case)", sorted_array),
        ("reversely sorted array (worst case)", reversed_array),
    ]

    for label, arr in scenarios:
        print(f"\n Sorting {label}.")
        compare_algorithms_for_array(arr)


def merge_k_lists(lists_to_sort: list[list[int]], i=0) -> list[int]:
    print(f"Sorting lists: {lists_to_sort}")

    if len(lists_to_sort) == 1:
        return lists_to_sort[0]

    mid = len(lists_to_sort) // 2
    left = merge_k_lists(lists_to_sort[:mid])
    right = merge_k_lists(lists_to_sort[mid:])
    return merge(left, right)
