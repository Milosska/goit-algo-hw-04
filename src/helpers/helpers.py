import timeit
import math
from typing import Callable
from src.decorators.decorators import handle_errors
from src.constants import Command
from src.benchmarks import (
    generate_random_numbers_in_range,
    generate_uniquie_numbers_in_range,
)

from src.algorithms import merge_sort, insertion_sort


@handle_errors
def parse_input(user_input: str) -> Command:
    if user_input is None:
        raise ValueError("Invalid command. Please, use one of the listed below.")

    normalized_input = user_input.strip().lower()
    command = Command(normalized_input)
    return command


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


@handle_errors
def compare_sorting_algorithms() -> None:
    print("Starting sorting algorithms comparison.")

    for pow in range(1, 4):
        elements_num = int(math.pow(10, pow))

        numbers_in_range = generate_random_numbers_in_range(elements_num)
        run_all_scenarios_for_array(numbers_in_range, "repetable")

        unique_numbers_in_range = generate_uniquie_numbers_in_range(elements_num)
        run_all_scenarios_for_array(unique_numbers_in_range, "unique")

    print("Comparison is finished succssfuly.")
