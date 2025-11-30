import math
from src.decorators.decorators import handle_errors
from src.benchmarks import (
    generate_random_numbers_in_range,
    generate_uniquie_numbers_in_range,
)
from src.helpers import (
    run_all_scenarios_for_array,
    parse_lists_number,
    parse_list,
    merge_k_lists,
)


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


@handle_errors
def merge_lists_handler() -> None:
    list_number = parse_lists_number(
        input("Please, indicate number of lists to merge: ")
    )

    print(
        "Provide indicated lists. For each list provide numbers divided by space. "
        "\n Example: 1 5 190 49 7"
    )

    lists_to_sort: list[list[int]] = []
    for i in range(0, list_number):
        list_to_add = parse_list(input(f"List {i + 1}: "))
        lists_to_sort.append(sorted(list_to_add))

    sorted_array = merge_k_lists(lists_to_sort)
    print(f"Sorting completed! Sorted array: {sorted_array}.")
